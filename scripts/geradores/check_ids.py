import re

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect line by line
for i, line in enumerate(text.splitlines()):
    if 'id: 60' in line or '"id": 60' in line or 'id: 61' in line or '"id": 61' in line or 'id: 100' in line or '"id": 100' in line:
        print(f"Line {i+1}: {line.strip()[:60]}")
