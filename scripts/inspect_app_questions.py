with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m_start = text.find('const QUIZ_QUESTIONS_DATA = [')
m_end = text.find('\n];\n', m_start)
if m_end == -1:
    m_end = text.find('];', m_start)

sub = text[m_start:m_end+2]
ids = re.findall(r'"id":\s*(\d+)', sub)
cats = re.findall(r'"category":\s*"([^"]+)"', sub)
discs = re.findall(r'"discipline":\s*"([^"]+)"', sub)

from collections import Counter
print('Total IDs:', len(ids), 'Max ID:', max([int(x) for x in ids]) if ids else 0)
print('Categories:', Counter(cats))
print('Disciplines:', Counter(discs))
