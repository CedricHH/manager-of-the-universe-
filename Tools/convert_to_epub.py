#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EPUB Converter for RESONANZ Series
===================================
Converts a Markdown manuscript to EPUB format with cover, metadata, and chapters.

Usage:
    python convert_to_epub.py [--teaser TEASER_FILE] [--title TITLE] [--output OUTPUT_FILE]

Example:
    python convert_to_epub.py --teaser "Story/Prequel/Teaser.md" --title "RESONANZ: Der nächste Zyklus"
"""

import os
import re
import argparse
import markdown
from ebooklib import epub

# ============================================================================
# CONFIGURATION - Adjust these defaults for your project
# ============================================================================

DEFAULT_CONFIG = {
    'base_path': r"G:\Meine Ablage\EBOOKS\Der Manager des Universums",
    'input_file': "Manager_of_Universe_Arc1_Manuscript.md",
    'cover_file': "Concept/Cover_V3_Final.png",
    'output_file': "Manager_of_Universe_Arc1.epub",
    'teaser_file': "Story/Teaser.md",  # Relative to base_path
    
    # Book Metadata
    'book_title': 'The Manager of the Universe: Arc 1',
    'book_author': 'First Spring',
    'book_author_address': '',  # Can be left empty
    'book_language': 'en',
    'book_id': 'id-manager-universe-arc1',
}


# ============================================================================
# FUNCTIONS
# ============================================================================

def load_teaser(teaser_path):
    """Load teaser/summary from a Markdown file."""
    if os.path.exists(teaser_path):
        with open(teaser_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Remove markdown headers and formatting for plain text description
        # Keep only the paragraph content
        lines = content.split('\n')
        description_lines = []
        for line in lines:
            stripped = line.strip()
            # Skip headers, horizontal rules, and empty lines at the start
            if stripped.startswith('#') or stripped == '---' or stripped.startswith('**Tagline'):
                continue
            if stripped:
                description_lines.append(stripped)
        return '\n\n'.join(description_lines)
    else:
        print(f"Warning: Teaser file not found at {teaser_path}")
        return "Keine Beschreibung verfügbar."


def convert_to_epub(config):
    """Main conversion function."""
    base_path = config['base_path']
    input_file = os.path.join(base_path, config['input_file'])
    cover_file = os.path.join(base_path, config['cover_file'])
    output_file = os.path.join(base_path, config['output_file'])
    teaser_file = os.path.join(base_path, config['teaser_file'])

    # Load description from teaser file
    book_description = load_teaser(teaser_file)

    # Book Metadata Setup
    book = epub.EpubBook()
    book.set_identifier(config['book_id'])
    book.set_title(config['book_title'])
    book.set_language(config['book_language'])
    book.add_author(config['book_author'])
    book.add_metadata('DC', 'description', book_description)

    # 1. Add Cover
    if os.path.exists(cover_file):
        with open(cover_file, 'rb') as f:
            book.set_cover("cover.png", f.read())
        print("Cover added.")
    else:
        print("Warning: Cover file not found.")

    # 2. Read Manuscript
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3. Pre-process content
    content = re.sub(r'!\[Cover\]\(Cover\.png\)', '', content)
    content = re.sub(r'\\newpage', '', content)
    content = re.sub(r'<div.*?></div>', '', content)

    # 4. Split into chapters - Updated to recognize "# Chapter" pattern
    parts = re.split(r'\n(?=# Chapter \d+)', content)

    chapters = []
    
    # Process Preamble (Title page)
    preamble = parts[0]
    if preamble.strip():
        c0 = epub.EpubHtml(title='Title Page', file_name='title.xhtml', lang='en')
        c0.content = markdown.markdown(preamble)
        book.add_item(c0)
        chapters.append(c0)

    # Add Description Page - visible in the book
    description_html = book_description.replace('\n\n', '</p><p>').replace('\n', '<br/>')
    description_content = f"""
    <h1>Description</h1>
    <p><em>{description_html}</em></p>
    """
    c_desc = epub.EpubHtml(title='Description', file_name='description.xhtml', lang='en')
    c_desc.content = description_content
    book.add_item(c_desc)
    chapters.append(c_desc)

    # Add Impressum Page (if author address is provided)
    if config['book_author_address']:
        address_html = config['book_author_address'].replace('\n', '<br/>')
        impressum_content = f"""
        <h1>Credits</h1>
        <p><strong>Author:</strong><br/>
        {config['book_author']}<br/>
        {address_html}</p>
        <p>Manuscript - Version: {datetime.now().strftime('%Y-%m-%d')}</p>
        """
        c_impr = epub.EpubHtml(title='Credits', file_name='credits.xhtml', lang='en')
        c_impr.content = impressum_content
        book.add_item(c_impr)
        chapters.append(c_impr)

    # Process Chapters
    for i, part in enumerate(parts[1:], 1):
        if not part.strip():
            continue
            
        lines = part.strip().split('\n')
        title_line = lines[0].replace('#', '').strip()
        
        c = epub.EpubHtml(title=title_line, file_name=f'chap_{i:03d}.xhtml', lang='en')
        html_content = markdown.markdown(part)
        c.content = html_content
        
        book.add_item(c)
        chapters.append(c)
        print(f"Added chapter: {title_line}")

    # 5. Table of Contents
    book.toc = tuple(chapters)

    # 6. Navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # 7. CSS
    style = 'body { font-family: Times, serif; }'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # 8. Spine
    book.spine = ['nav'] + chapters

    # 9. Write EPUB
    epub.write_epub(output_file, book, {})
    print(f"EPUB created successfully at: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown manuscript to EPUB')
    parser.add_argument('--teaser', help='Path to teaser/summary file (relative to base_path)')
    parser.add_argument('--title', help='Book title')
    parser.add_argument('--input', help='Input manuscript file (relative to base_path)')
    parser.add_argument('--output', help='Output EPUB file (relative to base_path)')
    parser.add_argument('--cover', help='Cover image file (relative to base_path)')
    
    args = parser.parse_args()
    
    # Start with defaults
    config = DEFAULT_CONFIG.copy()
    
    # Override with command line arguments if provided
    if args.teaser:
        config['teaser_file'] = args.teaser
    if args.title:
        config['book_title'] = args.title
    if args.input:
        config['input_file'] = args.input
    if args.output:
        config['output_file'] = args.output
    if args.cover:
        config['cover_file'] = args.cover
    
    convert_to_epub(config)


if __name__ == "__main__":
    main()
