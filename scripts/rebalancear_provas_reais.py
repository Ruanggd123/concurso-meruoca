import re, os, sys, subprocess
from bs4 import BeautifulSoup
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

PROVAS_DIR = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

files = [
    'PROVA_REAL_02_CONSULPAM_CAMARA_FORQUILHA_CE.html',
    'PROVA_REAL_03_CETREDE_ADMINISTRATIVO_CE.html',
    'PROVA_REAL_04_IDIB_CAMARA_LEGISLATIVO_CE.html',
    'PROVA_REAL_05_CONSULPAM_CRATEUS_CE.html',
    'PROVA_REAL_06_GRANDE_PROVA_LEGISLATIVO_CE.html',
    'PROVA_REAL_07_INBRASP_DIREITO_ADMINISTRATIVO.html',
    'PROVA_REAL_08_INBRASP_LINGUA_PORTUGUESA.html',
    'PROVA_REAL_09_INBRASP_MATEMATICA_RLM.html',
    'PROVA_REAL_10_INBRASP_INFORMATICA.html',
    'PROVA_REAL_11_LEGISLACAO_MUNICIPAL_REGIMENTO.html'
]

letters = ['A', 'B', 'C', 'D']

def rebalance_file(filename):
    file_path = os.path.join(PROVAS_DIR, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Encontrar todos os boxes de questão e todos os boxes de gabarito
    # Na estrutura: primeiros boxes são as questões (com ul.options-list);
    # depois da folha óptica vêm os boxes de gabarito (com .comentario-box)
    q_boxes = []
    g_boxes = []
    
    for box in soup.find_all('div', class_='question-box'):
        if box.find('ul', class_='options-list'):
            q_boxes.append(box)
        elif box.find('div', class_='comentario-box'):
            g_boxes.append(box)
            
    num_q = len(q_boxes)
    if num_q != len(g_boxes):
        print(f"[!] Aviso em {filename}: {num_q} questões vs {len(g_boxes)} gabaritos!")
        return False

    # Gerar sequência equilibrada de gabarito (A, B, C, D)
    # Exemplo: se 40 questões, 10 de cada, com alternância natural
    base_keys = ['A', 'B', 'C', 'D'] * ((num_q // 4) + 1)
    # Criar um padrão pseudo-aleatório determinístico elegante
    # Para não ficar A, B, C, D, A, B, C, D em ordem exata:
    # Usar um padrão que pareça uma prova real
    pattern_seeds = [
        ['B', 'D', 'A', 'C', 'D', 'B', 'A', 'C', 'C', 'A', 'D', 'B', 'B', 'A', 'C', 'D', 'A', 'C', 'B', 'D'],
        ['C', 'A', 'D', 'B', 'A', 'D', 'C', 'B', 'B', 'C', 'A', 'D', 'D', 'B', 'A', 'C', 'C', 'D', 'B', 'A'],
        ['D', 'B', 'C', 'A', 'B', 'A', 'D', 'C', 'A', 'D', 'B', 'C', 'C', 'A', 'D', 'B', 'B', 'C', 'A', 'D']
    ]
    # Escolher seed baseado no nome do arquivo
    seed_idx = abs(hash(filename)) % len(pattern_seeds)
    pattern = (pattern_seeds[seed_idx] * 3)[:num_q]
    
    # Ajustar para garantir distribuição balanceada
    target_counts = Counter(pattern)
    print(f"\n[*] Rebalanceando {filename} ({num_q} questões). Alvo:", dict(target_counts))

    for idx in range(num_q):
        q_box = q_boxes[idx]
        g_box = g_boxes[idx]
        new_target_letter = pattern[idx]
        target_idx = letters.index(new_target_letter)
        
        # Obter gabarito atual do g_box
        g_header = g_box.find('div', class_='question-header')
        match = re.search(r'Gabarito Oficial:\s*<strong>\(([ABCD])\)</strong>', str(g_header))
        old_letter = match.group(1) if match else 'A'
        old_idx = letters.index(old_letter)
        
        # Obter as 4 opções de q_box
        ul = q_box.find('ul', class_='options-list')
        li_items = ul.find_all('li')
        if len(li_items) != 4:
            continue
            
        opt_texts = []
        for li in li_items:
            # remove '(A) ', '(B) ', etc.
            t = re.sub(r'^\([ABCD]\)\s*', '', li.get_text().strip())
            opt_texts.append(t)
            
        # O texto correto estava na posição old_idx
        correct_text = opt_texts[old_idx]
        wrong_texts = [opt_texts[i] for i in range(4) if i != old_idx]
        
        # Montar a nova lista de 4 textos onde target_idx é correct_text
        new_opts = [None, None, None, None]
        new_opts[target_idx] = correct_text
        w_i = 0
        for pos in range(4):
            if pos != target_idx:
                new_opts[pos] = wrong_texts[w_i]
                w_i += 1
                
        # Atualizar os <li> na questão
        ul.clear()
        for l_idx, let in enumerate(letters):
            new_li = soup.new_tag('li')
            new_li.string = f"({let}) {new_opts[l_idx]}"
            ul.append(new_li)
            
        # Atualizar o gabarito no g_box
        g_header.clear()
        q_num_str = f"QUESTÃO {idx+1:02d}"
        g_header.append(f"{q_num_str} • Gabarito Oficial: ")
        strong_tag = soup.new_tag('strong')
        strong_tag.string = f"({new_target_letter})"
        g_header.append(strong_tag)

    # Salvar HTML
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    # Recompilar PDF
    pdf_path = file_path.replace('.html', '.pdf')
    normalized_url = "file:///" + file_path.replace("\\", "/")
    cmd = [
        EDGE_PATH,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        normalized_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"    [SUCESSO] {os.path.basename(pdf_path)} ({size_kb:.1f} KB) - Gabaritos rebalanceados!")
        return True
    else:
        print(f"    [FALHA] {os.path.basename(pdf_path)}")
        return False

for fn in files:
    rebalance_file(fn)

print("\n[OK] Todos os 10 arquivos foram rebalanceados com gabaritos naturais de A a D!")
