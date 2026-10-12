import re, json

with open('provas/PROVA_OFICIAL_SIMULADO_01_INBRASP.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extrair questões do HTML do Simulado 1
# Cada questão tem:
# <div class="question-box">
#   <div class="question-title">QUESTÃO 01 (Língua Portuguesa)</div>
#   <p>...</p>
#   <ul class="options-list">
#     <li>(A) ...</li>
#     <li>(B) ...</li>
#     <li>(C) ...</li>
#     <li>(D) ...</li>
#   </ul>
# </div>

pattern = re.compile(
    r'<div class="question-box">\s*<div class="question-title">QUEST[ÃA]O\s+(\d+)\s*\(([^)]+)\)</div>\s*<p>([\s\S]*?)</p>\s*<ul class="options-list">\s*<li>\(A\)\s*([\s\S]*?)</li>\s*<li>\(B\)\s*([\s\S]*?)</li>\s*<li>\(C\)\s*([\s\S]*?)</li>\s*<li>\(D\)\s*([\s\S]*?)</li>\s*</ul>\s*</div>',
    re.IGNORECASE
)

matches = pattern.findall(html)
print(f"Total de questões extraídas do Simulado 1: {len(matches)}")

# Gabarito oficial do simulado
gabarito_map = {
    1: ('A', 'Morfossintaxe - Oração subordinada adverbial temporal.'),
    2: ('C', 'Crase antes de palavra feminina sem artigo definido.'),
    3: ('A', 'Concordância verbal com partícula apassivadora "se".'),
    4: ('D', 'Regência verbal do verbo assistir no sentido de ver/presenciar.'),
    5: ('B', 'Gênero textual Editorial - institucional do jornal, sem assinatura.'),
    6: ('C', 'Ofício - comunicação formal da administração pública.'),
    7: ('C', 'Função Conotativa/Apelativa - foco no leitor, verbos no imperativo.'),
    8: ('A', 'Divulgação científica - transmitir conhecimento ao leigo.'),
    9: ('B', 'Artigo de opinião - texto argumentativo e assinado.'),
    10: ('B', 'Crônica - cotidiano em tom leve e reflexivo.'),
    11: ('A', 'Caracteres proibidos no Windows: \\ / : * ? " < > |.'),
    12: ('C', 'Win + L - atalho de bloqueio rápido da sessão do Windows.'),
    13: ('B', '/etc - pasta de arquivos de configuração globais do Linux.'),
    14: ('B', 'Memória RAM é primária e volátil.'),
    15: ('A', 'Regra 3-2-1 de Backup (3 cópias, 2 mídias, 1 fora/nuvem).'),
    16: ('B', 'Conjuntos: 60 + 50 - 20 = 90 servidores. 100 - 90 = 10 servidores.'),
    17: ('B', 'Razão e proporção: 3x + 5x = 40 -> 8x = 40 -> x = 5. Manhã: 3 * 5 = 15.'),
    18: ('B', 'Porcentagem: 50.000 + 15% = R$ 57.500,00.'),
    19: ('C', 'Regra de três inversa: 3 téc * 4h = X * 2h -> X = 6 técnicos.'),
    20: ('A', 'Negação do condicional (P -> Q): P ^ ~Q (Mané).'),
    21: ('C', 'Art. 5º, XI CF/88 - Casa como asilo inviolável durante o dia.'),
    22: ('C', 'Crimes inafiançáveis e imprescritíveis: Racismo e Ação de grupos armados.'),
    23: ('B', 'Tráfico de drogas é inafiançável e insuscetível de graça ou anistia.'),
    24: ('D', 'Lei 12.016/09, Art. 23 - Prazo decadencial de 120 dias para Mandado de Segurança.'),
    25: ('C', 'Art. 5º, XXXVIII, "d" - Competência do Tribunal do Júri para crimes dolosos contra a vida.'),
    26: ('A', 'Mnemônico LIMPE - Art. 37, caput da CF/88.'),
    27: ('B', 'Art. 37, § 1º CF/88 - Princípio da impessoalidade na publicidade institucional.'),
    28: ('C', 'Autotutela - Súmulas 346 e 473 do STF.'),
    29: ('B', 'Desconcentração - distribuição interna de competências criando órgãos.'),
    30: ('A', 'Art. 37, XIX - Autarquia criada diretamente por lei específica.'),
    31: ('A', 'Sociedade de Economia Mista sob forma obrigatória de S/A.'),
    32: ('D', 'Lei 14.133/2021 extinguiu as modalidades Convite e Tomada de Preços.'),
    33: ('B', 'Inexigibilidade de licitação por inviabilidade de competição (Art. 74).'),
    34: ('B', 'Lei Orgânica de Meruoca - Prazo de veto do prefeito: 15 dias úteis.'),
    35: ('C', 'Quórum qualificado de 2/3 da Câmara de Meruoca para rejeitar parecer do TCE.'),
    36: ('B', 'Funções típicas do Poder Legislativo: legislar e fiscalizar.'),
    37: ('B', 'LC 95/98 - Artigos são numerados com ordinais até o 9º e cardinais a partir do 10.'),
    38: ('B', 'LRF - LC 101/00 - Limite total de despesa com pessoal da Câmara: 6% da RCL.'),
    39: ('B', 'Lei 14.230/2021 - Exigência de dolo específico para configuração de improbidade.'),
    40: ('C', 'LAI - Lei 12.527/11 - Prazo padrão de resposta: até 20 dias, prorrogável por 10 dias.')
}

letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

QUESTOES_DIA6 = []
for m in matches:
    num = int(m[0])
    disc = m[1].strip()
    enunciado = re.sub(r'<[^>]+>', '', m[2]).strip()
    optA = re.sub(r'<[^>]+>', '', m[3]).strip()
    optB = re.sub(r'<[^>]+>', '', m[4]).strip()
    optC = re.sub(r'<[^>]+>', '', m[5]).strip()
    optD = re.sub(r'<[^>]+>', '', m[6]).strip()

    gab_letter, com = gabarito_map.get(num, ('A', 'Gabarito Oficial INBRASP'))
    correct_idx = letter_to_idx.get(gab_letter, 0)

    # mapear categoria
    cat = "portugues"
    if "Informática" in disc: cat = "informatica"
    elif "Matemática" in disc or "Lógica" in disc: cat = "matematica"
    elif "Constitucional" in disc: cat = "constitucional"
    elif "Administrativo" in disc: cat = "administrativo"
    elif "Específicos" in disc or "Legislativo" in disc: cat = "legislacao"

    QUESTOES_DIA6.append({
        "id": 140 + num, # IDs 141 a 180
        "simuladoQNum": num,
        "category": cat,
        "day": "dia6",
        "discipline": disc,
        "topic": f"Simulado Oficial 01 • Questão {num}",
        "question": f"[Simulado 01 - Q{num:02d}] {enunciado}",
        "options": [optA, optB, optC, optD],
        "correctAnswer": correct_idx,
        "commentary": f"Gabarito Oficial: {gab_letter}. {com}"
    })

print(f"[OK] Total de questões do Simulado 1 estruturadas: {len(QUESTOES_DIA6)}")
with open('questoes_dia6_simulado1.json', 'w', encoding='utf-8') as f:
    json.dump(QUESTOES_DIA6, f, ensure_ascii=False, indent=2)
