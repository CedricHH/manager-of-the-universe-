import sys
import os

# Add current directory to path so we can import RR_uploader
sys.path.append(os.getcwd())

import RR_uploader

test_file = r"g:\Meine Ablage\EBOOKS\Der Manager des Universums\Story\Chapters-HTML\Chapter_01_Dead_Capital.html"

print(f"Testing parsing on: {test_file}")
try:
    title, content = RR_uploader.read_file(test_file)
    print(f"EXTRACTED TITLE: {title}")
    print(f"CONTENT LENGTH: {len(content)}")
    print("CONTENT START (first 100 chars):")
    print(content[:100])
    print("-" * 20)
    
    if "<h1>" in content:
        print("FAIL: h1 tag still present in content body.")
    else:
        print("PASS: h1 tag removed from content body.")
        
    if title == "Chapter 1: Dead Capital":
        print("PASS: Title extracted correctly.")
    else:
        print(f"FAIL: Title mismatch. Got '{title}'")

except Exception as e:
    print(f"ERROR: {e}")
