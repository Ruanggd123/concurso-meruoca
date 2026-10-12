import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Vamos contar as questões e validar cada uma via regex/parse
start = content.find('const QUIZ_QUESTIONS_DATA = [')
end = content.find('// =========================================================================\n// CRONOGRAMA COMPLETO')
quiz_code = content[start:end]

# Extrair blocos de questões
question_blocks = re.findall(r'\{\s*id:\s*(\d+),[\s\S]*?commentary:\s*[\'"`]([\s\S]*?)[\'"`]\s*\}', quiz_code)

print(f"Total de blocos de questão identificados: {len(question_blocks)}")

# Vamos checar cada id de 1 a 100
found_ids = [int(m[0]) for m in question_blocks]
print(f"IDs encontrados: {min(found_ids)} até {max(found_ids)} (Total: {len(found_ids)})")

missing = [i for i in range(1, 101) if i not in found_ids]
if missing:
    print(f"IDs faltando: {missing}")
else:
    print("✅ Todos os IDs de 1 a 100 estão presentes!")

# Checar opções (cada questão deve ter 4 opções)
option_matches = re.findall(r'options:\s*\[([\s\S]*?)\]', quiz_code)
print(f"Total de arrays de opções: {len(option_matches)}")
bad_options = []
for idx, opt_str in enumerate(option_matches):
    # contar strings dentro do array
    opts = re.findall(r'["\']([\s\S]*?)["\']\s*(?:,|$)', opt_str)
    if len(opts) != 4:
        bad_options.append((idx+1, len(opts)))

if bad_options:
    print(f"❌ Questões com número incorreto de opções: {bad_options}")
else:
    print("✅ Todas as 100 questões possuem rigorosamente 4 alternativas (A, B, C, D)!")

# Checar gabaritos
ans_matches = re.findall(r'correctAnswer:\s*(\d+)', quiz_code)
print(f"Total de gabaritos encontrados: {len(ans_matches)}")
invalid_ans = [val for val in ans_matches if int(val) not in [0, 1, 2, 3]]
if invalid_ans:
    print(f"❌ Gabaritos inválidos: {invalid_ans}")
else:
    print("✅ Todos os gabaritos são válidos (0 a 3, correspondendo a A, B, C, D)!")
