import re

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

weeks = re.findall(r'weekNumber:\s*(\d+),\s*title:\s*["\']([^"\']+)["\'],\s*focus:\s*["\']([^"\']+)["\']', text)
for w in weeks:
    print(f"Semana {w[0]}: {w[1]} | Foco: {w[2]}")

print("\n--- DETALHAMENTO DE CADA DIA ---")
days = re.findall(r'id:\s*["\'](w\d+_d\d+)["\'],\s*dayLabel:\s*["\']([^"\']+)["\'],\s*date:\s*["\']([^"\']+)["\']', text)
blocks = re.findall(r'subject:\s*["\']([^"\']+)["\']', text)
print(f"Total de dias estruturados: {len(days)}")
print(f"Total de blocos de estudo: {len(blocks)}")

# Mostrar matérias por semana
for w_num in range(1, 8):
    w_match = re.search(rf'weekNumber:\s*{w_num}.*?(?=weekNumber:\s*{w_num+1}|$)', text, re.DOTALL)
    if w_match:
        w_text = w_match.group(0)
        subjects = re.findall(r'subject:\s*["\']([^"\']+)["\']', w_text)
        print(f"\n[Semana {w_num}] ({len(subjects)} blocos):")
        for s in set(subjects):
            print(f"  - {s}")
