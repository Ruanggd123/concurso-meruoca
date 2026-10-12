import re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open(sys.argv[1], encoding='utf-8').read()
print("chars:", len(t))
links = sorted(set(re.findall(r'https://www\.pciconcursos\.com\.br/provas/download/[^\s\)\]"\']+', t)))
for l in links:
    print(l)
print("total:", len(links))
