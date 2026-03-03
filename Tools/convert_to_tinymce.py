#!/usr/bin/env python3
"""
Markdown to TinyMCE HTML Converter
Converts chapter Markdown files to TinyMCE-ready HTML while preserving:
- ARMI system messages (blockquotes)
- German special characters
- All formatting (headers, bold, italic)
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional

try:
    import markdown
    from markdown.extensions import fenced_code, tables
except ImportError:
    print("Error: 'markdown' package not found.")
    print("Install it with: pip install markdown")
    sys.exit(1)


class TinyMCEConverter:
    """Converts Markdown to TinyMCE-compatible HTML"""
    
    def __init__(self):
        self.md = markdown.Markdown(
            extensions=['fenced_code', 'tables', 'nl2br'],
            output_format='html'
        )
    
    def convert_file(self, input_path: Path, output_path: Optional[Path] = None) -> Path:
        """
        Convert a single Markdown file to TinyMCE HTML
        
        Args:
            input_path: Path to input .md file
            output_path: Optional path to output .html file
            
        Returns:
            Path to created HTML file
        """
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Read Markdown content
        content = input_path.read_text(encoding='utf-8')
        
        # Preprocess: Remove YAML frontmatter if present
        content = self._remove_frontmatter(content)
        
        # Preprocess: Remove word count footer
        content = self._remove_footer(content)
        
        # Convert Markdown to HTML
        html = self.md.convert(content)
        
        # Reset markdown instance for next conversion
        self.md.reset()
        
        # Post-process HTML for TinyMCE
        html = self._post_process_html(html)
        
        # Determine output path
        if output_path is None:
            output_dir = input_path.parent.parent / "Chapters-HTML"
            output_dir.mkdir(exist_ok=True)
            output_path = output_dir / input_path.with_suffix('.html').name
        
        # Write HTML file
        output_path.write_text(html, encoding='utf-8')
        
        return output_path
    
    def _remove_frontmatter(self, content: str) -> str:
        """Remove YAML frontmatter if present"""
        if content.startswith('---'):
            # Find second --- and remove everything before it
            parts = content.split('---', 2)
            if len(parts) >= 3:
                return parts[2].lstrip()
        return content
    
    def _remove_footer(self, content: str) -> str:
        """Remove word count footer and trailing metadata"""
        # Remove lines like: **Word Count**: ~1,620
        content = re.sub(r'\*\*Word Count\*\*:.*', '', content)
        
        # Remove lines like: **Next Chapter**: [...]
        content = re.sub(r'\*\*Next Chapter\*\*:.*', '', content)
        
        # Remove multiple trailing newlines
        content = content.rstrip() + '\n'
        
        return content
    
    def _post_process_html(self, html: str) -> str:
        """Post-process HTML for TinyMCE compatibility"""
        # Convert <hr> to <hr />
        html = html.replace('<hr>', '<hr />')
        
        # Convert <br> to <br />
        html = html.replace('<br>', '<br />')
        
        # Add CSS class to blockquotes for ARMI messages
        # Detect ARMI blockquotes by looking for [ARMI in the content
        html = self._style_armi_blockquotes(html)
        
        # Clean up excessive newlines
        html = re.sub(r'\n{3,}', '\n\n', html)
        
        return html.strip()
    
    def _style_armi_blockquotes(self, html: str) -> str:
        """Add styling hints to ARMI system message blockquotes"""
        # This is a simple approach - add a class if blockquote contains [ARMI
        # TinyMCE users can then style these with CSS
        
        def replace_armi_blockquote(match):
            blockquote_content = match.group(1)
            if '[ARMI' in blockquote_content or 'ARMI' in blockquote_content:
                return f'<blockquote class="armi-system-message">\n{blockquote_content}\n</blockquote>'
            return match.group(0)
        
        html = re.sub(
            r'<blockquote>(.*?)</blockquote>',
            replace_armi_blockquote,
            html,
            flags=re.DOTALL
        )
        
        return html


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Convert Markdown chapters to TinyMCE-ready HTML'
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='Input Markdown file or directory'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Convert all chapters in Story/Chapters/'
    )
    parser.add_argument(
        '--range',
        '-r',
        help='Chapter range to convert (e.g., "1-10")'
    )
    parser.add_argument(
        '--output',
        '-o',
        help='Output directory (default: Story/Chapters-HTML/)'
    )
    
    args = parser.parse_args()
    
    # Determine project root (where Tools/ directory is located)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    converter = TinyMCEConverter()
    
    if args.all or args.range:
        # Convert chapters
        chapters_dir = project_root / "Story" / "Chapters"
        if not chapters_dir.exists():
            print(f"Error: Chapters directory not found: {chapters_dir}")
            sys.exit(1)
        
        markdown_files = sorted(chapters_dir.glob("Chapter_*.md"))
        
        if not markdown_files:
            print(f"No chapter files found in {chapters_dir}")
            sys.exit(1)
        
        # Filter by range if specified
        if args.range:
            try:
                start, end = map(int, args.range.split('-'))
                filtered_files = []
                for md_file in markdown_files:
                    # Extract chapter number from filename
                    match = re.search(r'Chapter_(\d+)', md_file.name)
                    if match:
                        chapter_num = int(match.group(1))
                        if start <= chapter_num <= end:
                            filtered_files.append(md_file)
                markdown_files = sorted(filtered_files, key=lambda f: int(re.search(r'Chapter_(\d+)', f.name).group(1)))
            except ValueError:
                print(f"Error: Invalid range format. Use 'start-end' (e.g., '1-10')")
                sys.exit(1)
        
        print(f"Found {len(markdown_files)} chapter files")
        converted_count = 0
        
        for md_file in markdown_files:
            try:
                output_path = converter.convert_file(md_file)
                print(f"[OK] {md_file.name} -> {output_path.name}")
                converted_count += 1
            except Exception as e:
                print(f"[FAIL] {md_file.name}: {e}")
        
        print(f"\nConverted {converted_count}/{len(markdown_files)} files")
        
    elif args.input:
        # Convert single file
        input_path = Path(args.input)
        
        if not input_path.is_absolute():
            # Try relative to current directory first
            if input_path.exists():
                pass
            # Try relative to project root
            elif (project_root / input_path).exists():
                input_path = project_root / input_path
            else:
                print(f"Error: File not found: {input_path}")
                sys.exit(1)
        
        try:
            output_path = converter.convert_file(input_path)
            print(f"[OK] Converted: {output_path}")
        except Exception as e:
            print(f"[ERROR] Error: {e}")
            sys.exit(1)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
