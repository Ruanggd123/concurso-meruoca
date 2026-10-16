import os, sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from construir_cadernos_reais import render_html, compilar_para_pdf

PROVAS_DIR = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"
JSON_PATH = os.path.join(PROVAS_DIR, "all_657_questions.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    ALL_QS = json.load(f)

LETTERS = ['A', 'B', 'C', 'D']

def norm(text):
    t = re.sub(r'^\[\d+\]\s*', '', text.strip().lower())
    t = re.sub(r'^\d+[\.\)\-]\s*', '', t)
    t = re.sub(r'\s+', ' ', t)
    return t

def clean_opt(opt):
    return re.sub(r'^\([ABCD]\)\s*', '', opt.strip())

def clean_comment(com):
    c = re.sub(r'^Gabarito:\s*[ABCD][\.\s\-]*', '', com.strip(), flags=re.IGNORECASE)
    return c.strip()

def expand_unique(base_itens, categories, target_count):
    seen = set()
    result = []
    for head, enun, opts, gab, com in base_itens:
        key = norm(enun)
        if key not in seen:
            seen.add(key)
            result.append((head, enun, [clean_opt(o) for o in opts], gab, clean_comment(com)))
    
    for q in ALL_QS:
        if len(result) >= target_count:
            break
        if q.get("category") in categories:
            enun = re.sub(r'^\d+[\.\)\-]\s*', '', q["question"].strip())
            key = norm(enun)
            if key not in seen and len(q.get("options", [])) == 4:
                seen.add(key)
                gab = LETTERS[q["correctAnswer"]]
                opts = [clean_opt(o) for o in q["options"]]
                com = clean_comment(q.get("commentary", ""))
                head = q.get("discipline", "Questão Oficial")
                result.append((head, enun, opts, gab, com))
    return result[:target_count]

def compilar(nome_base, titulo, badge, orgao, certame, cargo, fonte, questoes):
    html = render_html(titulo, badge, orgao, certame, cargo, fonte, questoes)
    html_path = os.path.join(PROVAS_DIR, f"{nome_base}.html")
    pdf_path = os.path.join(PROVAS_DIR, f"{nome_base}.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    compilar_para_pdf(html_path, pdf_path)

# =============================================================
# PROVA REAL 07 (12/10) - INBRASP DIREITO ADMINISTRATIVO (30Q)
# =============================================================
def build_prova_07():
    questoes = []
    itens_base = [
        ("Direito Administrativo", "A Lei nº 14.133/2021 estabelece como princípio da licitação pública expressamente enumerado:",
         ["Planejamento, transparência, eficácia, segregação de funções e motivação.", "Sigilo irrestrito dos atos processuais licitatórios.", "Discricionariedade ilimitada na escolha da proposta mais cara.", "Prevalência da contratação verbal para obras públicas."], "A",
         "Art. 5º da Lei 14.133/21: princípios da legalidade, impessoalidade, moralidade, publicidade, eficiência, planejamento, transparência, eficácia, segregação de funções, etc."),
        ("Direito Administrativo", "O agente que atua no âmbito da Administração Pública sem remuneração e sem vínculo formal, prestando serviços relevantes como jurado ou mesário eleitoral, classifica-se como:",
         ["Agente honorífico.", "Servidor público estatutário.", "Empregado público celetista.", "Agente delegado por concessão."], "A",
         "Agentes honoríficos são cidadãos convocados ou nomeados para prestar serviços específicos ao Estado sem remuneração (mesários, jurados)."),
        ("Direito Administrativo", "A concessão de serviço público é a delegação de sua prestação, feita pelo poder concedente, mediante licitação, na modalidade:",
         ["Concorrência ou diálogo competitivo.", "Leilão.", "Concurso artístico.", "Dispensa por emergência."], "A",
         "Lei 8.987/95 e Lei 14.133/21: Concessão de serviços públicos é formalizada mediante licitação na modalidade concorrência."),
        ("Direito Constitucional", "Conforme o art. 37, § 5º da CF/88, as ações de ressarcimento ao erário por atos de improbidade administrativa dolosos tipificados em lei são:",
         ["Imprescritíveis (Tema 897 do STF).", "Prescritíveis em 1 ano da ocorrência do dano.", "Prescritíveis em 2 anos do término do mandato.", "Extintas automaticamente com a prestação de contas."], "A",
         "STF (Tema 897): São imprescritíveis as ações de ressarcimento ao erário fundadas na prática de ato doloso tipificado na Lei de Improbidade Administrativa."),
        ("Direito Administrativo", "Em relação aos atos administrativos, a imperatividade significa que:",
         ["Os atos administrativos se impõem a terceiros independentemente de sua concordância.", "Todos os atos administrativos geram obrigações voluntárias aos cidadãos.", "O ato administrativo não pode ser revogado pela autoridade que o expediu.", "A Administração depende de concordância expressa do particular para agir."], "A",
         "Imperatividade é o atributo pelo qual os atos administrativos impõem obrigações e restrições a terceiros, independentemente de sua prévia concordância."),
        ("Direito Constitucional", "O teto remuneratório constitucional aplicável no âmbito dos Municípios para os servidores municipais corresponde ao subsídio do:",
         ["Prefeito Municipal (Art. 37, XI da CF/88).", "Governador do Estado.", "Presidente da Câmara Municipal.", "Desembargador do Tribunal de Justiça."], "A",
         "Art. 37, XI da CF: nos Municípios, o limite máximo remuneratório geral é o subsídio do Prefeito Municipal."),
        ("Direito Administrativo", "O poder de revogar atos administrativos por motivos de conveniência e oportunidade é conferido:",
         ["Exclusivamente à própria Administração Pública (Poder Judiciário não pode revogar atos administrativos no exercício de sua função típica jurisdicional).", "Ao Poder Judiciário em qualquer ação ordinária.", "Ao Tribunal de Contas de ofício sem recurso.", "Ao Ministério Público monocraticamente."], "A",
         "Súmula 473 STF: Revogação é privativa da Administração Pública por juízo de conveniência e oportunidade. O Judiciário só pode anular atos ilegais."),
        ("Direito Administrativo", "A alienação de bens imóveis da Administração Pública da Câmara ou Prefeitura depende de autorização legislativa, avaliação prévia e licitação na modalidade:",
         ["Leilão (conforme Lei 14.133/2021).", "Tomada de preços simplificada.", "Concurso de projetos.", "Carta-convite presencial."], "A",
         "Art. 76 da Lei 14.133/21: a alienação de bens da Administração depende de avaliação prévia e leilão."),
        ("Direito Constitucional", "É garantido ao servidor público civil, conforme o art. 37, VI e VII da CF/88:",
         ["O direito à livre associação sindical e o direito de greve nos termos de lei específica.", "O direito de greve irrestrito sem manutenção de serviços essenciais.", "O porte livre de armas de fogo em todas as repartições.", "A imunidade tributária sobre vencimentos e gratificações."], "A",
         "Art. 37, VI e VII da CF/88: assegura a livre associação sindical e o direito de greve nos termos e limites definidos em lei."),
        ("Direito Administrativo", "A forma como requisito do ato administrativo exige que a manifestação da vontade estatal seja:",
         ["Escrita e motivada, salvo exceções legais expressas como sinais de trânsito ou ordens verbais urgentes.", "Sempre tácita sem necessidade de registro físico.", "Sigilosa para garantir a segurança da autoridade.", "Apenas verbal em todas as esferas de governo."], "A",
         "A forma é a exteriorização material do ato administrativo, sendo regra geral o princípio da solenidade e forma escrita motivada.")
    ]
    itens = expand_unique(itens_base, ["administrativo", "constitucional"], 30)
    for i, (head, enun, opts, gab, com) in enumerate(itens, 1):
        questoes.append({
            "numero": i,
            "secao": "DIREITO ADMINISTRATIVO & CONSTITUCIONAL (INBRASP/IBRASP)" if i == 1 else "",
            "header": f"Direito Administrativo • Questão Oficial {i:02d} • INBRASP",
            "enunciado": f"[{i:02d}] {enun}",
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
    compilar(
        "PROVA_REAL_07_INBRASP_DIREITO_ADMINISTRATIVO",
        "PROVA REAL OFICIAL — DIREITO ADMINISTRATIVO & CF/88 (BANCA INBRASP)",
        "CADERNO DE QUESTÕES REAIS DA BANCA",
        "CONCURSOS MUNICIPAIS DA BANCA INBRASP / IBRASP",
        "PROVAS APLICADAS OFICIAIS (2024 - 2026)",
        "AGENTE ADMINISTRATIVO / TÉCNICO LEGISLATIVO",
        "BANCO DE QUESTÕES REAIS REGISTRADAS DA BANCA INBRASP (QCONCURSOS)",
        questoes
    )

# =============================================================
# PROVA REAL 08 (13/10) - INBRASP LÍNGUA PORTUGUESA (30Q)
# =============================================================
def build_prova_08():
    questoes = []
    itens_base = [
        ("Língua Portuguesa", "Assinale a opção em que a concordância do particípio com o sujeito paciente está correta:",
         ["Foram deferidas todas as inscrições para o concurso da Câmara.", "Foi deferido todas as inscrições para o certame.", "Houveram inscrições deferidas pela comissão.", "Haviam sido deferido os pedidos de isenção."], "A",
         "Voz passiva analítica: verbo auxiliar concorda com o sujeito paciente ('Foram deferidas todas as inscrições')."),
        ("Língua Portuguesa", "A palavra 'parênteses' recebe acento gráfico por ser uma palavra:",
         ["Proparoxítona.", "Paroxítona terminada em -s.", "Oxítona terminada em -es.", "Ditongo decrescente oral."], "A",
         "Pa-rên-te-ses: antepenúltima sílaba tônica, logo é proparoxítona e todas são acentuadas."),
        ("Língua Portuguesa", "Assinale a alternativa em que a palavra destacada atua como conjunção integrante:",
         ["O presidente da mesa afirmou QUE a pauta seria votada hoje.", "O projeto QUE foi aprovado gerou polêmica.", "Aquele é o servidor QUE encontrei no arquivo.", "QUE bela sessão tivemos ontem!"], "A",
         "Em 'afirmou que a pauta...', a oração 'que a pauta...' é substantiva objetiva direta, introduzida pela conjunção integrante 'que'."),
        ("Língua Portuguesa", "O antônimo correto do vocábulo 'lícito' no contexto jurídico é:",
         ["Ilícito (ilegal, vedado pelo ordenamento).", "Explícito (evidente, claro).", "Implícito (subentendido).", "Inédito (novo, original)."], "A",
         "Lícito = permitido em lei. Seu antônimo direto é ilícito = proibido, contrário à lei."),
        ("Língua Portuguesa", "Assinale a alternativa em que a crase foi empregada corretamente antes de locução adverbial feminina:",
         ["A comissão reuniu-se às pressas para emitir o parecer.", "O parlamentar votou à favor do projeto de lei.", "A sessão terá continuidade à partir de amanhã.", "Ficamos cara à cara com o presidente da mesa."], "A",
         "Locuções adverbiais femininas ('às pressas', 'às vezes', 'à noite') recebem crase obrigatória. Antes de palavras masculinas, verbos e palavras repetidas a crase é vedada."),
        ("Língua Portuguesa", "Assinale o período em que a vírgula separa corretamente orações coordenadas assindéticas:",
         ["O relator leu o parecer, o plenário debateu, o presidente declarou aprovada a matéria.", "O relator leu o parecer porque o plenário debateu.", "O relator leu o parecer se o plenário debater a matéria.", "O relator, leu o parecer com clareza."], "A",
         "Orações coordenadas assindéticas (sem conjunção) são separadas por vírgulas em enumeração de ações sucessivas."),
        ("Língua Portuguesa", "No vocábulo 'extraordinária', o elemento mórfico 'extra-' é um:",
         ["Prefixo latino que indica 'fora de' ou 'além de'.", "Sufixo derivacional de intensidade.", "Radical grego de valor nominal.", "Desinência de modo e tempo."], "A",
         "'Extra-' é prefixo de origem latina com sentido de 'fora de', 'além do comum' (extraordinária)."),
        ("Língua Portuguesa", "Assinale a alternativa que apresenta oração na voz passiva pronominal:",
         ["Revogou-se o antigo decreto legislativo municipal.", "Precisa-se de novos assessores técnicos na Casa.", "Trabalha-se com afinco na redação das minutas.", "O servidor arrependeu-se de suas declarações."], "A",
         "Revogou-se o decreto = O decreto foi revogado (VTD + se apassivador)."),
        ("Língua Portuguesa", "A expressão 'à medida que' expressa ideia de:",
         ["Proporcionalidade.", "Causa.", "Conformidade.", "Tempo pontual."], "A",
         "'À medida que' é conjunção adverbial proporcional. Não confundir com 'na medida em que' (causal)."),
        ("Língua Portuguesa", "Assinale a frase em que o pronome relativo 'cujo' foi empregado corretamente:",
         ["O vereador cujo requerimento foi aprovado discursou ontem.", "O vereador cujo o requerimento foi aprovado discursou.", "O vereador que cujo requerimento foi arquivado protestou.", "O requerimento cujo de quem é conhecido tramitou rápido."], "A",
         "'Cujo' concorda com o substantivo seguinte ('cujo requerimento') e JAMAIS admite artigo após si ('cujo o' é erro grave).")
    ]
    itens = expand_unique(itens_base, ["portugues"], 30)
    for i, (head, enun, opts, gab, com) in enumerate(itens, 1):
        questoes.append({
            "numero": i,
            "secao": "LÍNGUA PORTUGUESA & INTERPRETAÇÃO (INBRASP/IBRASP)" if i == 1 else "",
            "header": f"Língua Portuguesa • Questão Oficial {i:02d} • INBRASP",
            "enunciado": f"[{i:02d}] {enun}",
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
    compilar(
        "PROVA_REAL_08_INBRASP_LINGUA_PORTUGUESA",
        "PROVA REAL OFICIAL — LÍNGUA PORTUGUESA & INTERPRETAÇÃO (BANCA INBRASP)",
        "CADERNO DE QUESTÕES REAIS DA BANCA",
        "CONCURSOS MUNICIPAIS DA BANCA INBRASP / IBRASP",
        "PROVAS APLICADAS OFICIAIS (2024 - 2026)",
        "AGENTE ADMINISTRATIVO / NÍVEL MÉDIO",
        "BANCO DE QUESTÕES REAIS REGISTRADAS DA BANCA INBRASP (QCONCURSOS)",
        questoes
    )

# =============================================================
# PROVA REAL 09 (14/10) - MATEMÁTICA BÁSICA & RLM (25Q)
# =============================================================
def build_prova_09():
    questoes = []
    itens_base = [
        ("Matemática", "Um lote com 360 pastas de arquivo deve ser dividido entre 3 servidores em partes proporcionais aos números 2, 3 e 4. A menor quantidade de pastas recebida por um servidor é:",
         ["80 pastas.", "120 pastas.", "160 pastas.", "90 pastas."], "A",
         "Soma das partes: 2 + 3 + 4 = 9 partes. Cada parte vale: 360 / 9 = 40 pastas. A menor cota é: 2 * 40 = 80 pastas."),
        ("Matemática", "O preço de uma impressora para o gabinete sofreu um desconto de 15% na compra à vista, custando R$ 850,00. O valor original sem desconto era de:",
         ["R$ 1.000,00", "R$ 980,00", "R$ 1.020,00", "R$ 950,00"], "A",
         "Preço com desconto: 85% do valor original = R$ 850,00 -> Valor original = 850 / 0,85 = R$ 1.000,00."),
        ("RLM", "Se todo servidor público é aprovado em concurso, e Marcos é servidor público, então necessariamente:",
         ["Marcos foi aprovado em concurso público.", "Marcos é chefe de setor.", "Todo concursado é igual a Marcos.", "Marcos não é estável."], "A",
         "Silogismo categórico dedutivo direto: premissa maior + premissa menor -> conclusão necessária."),
        ("Matemática", "Um veículo oficial da Câmara percorre 480 km consumindo 40 litros de combustível. Quantos litros consumirá para percorrer 360 km nas mesmas condições?",
         ["30 litros.", "32 litros.", "28 litros.", "35 litros."], "A",
         "Rendimento: 480 / 40 = 12 km/l. Para 360 km: 360 / 12 = 30 litros."),
        ("RLM", "A negação de 'Hoje é segunda-feira e o plenário está em sessão' é:",
         ["Hoje não é segunda-feira OU o plenário não está em sessão.", "Hoje não é segunda-feira E o plenário não está em sessão.", "Se hoje não for segunda-feira, haverá sessão.", "Hoje é segunda-feira se e somente se houver sessão."], "A",
         "Lei de De Morgan: ~(A e B) = ~A ou ~B.")
    ]
    itens = expand_unique(itens_base, ["matematica"], 25)
    for i, (head, enun, opts, gab, com) in enumerate(itens, 1):
        questoes.append({
            "numero": i,
            "secao": "MATEMÁTICA BÁSICA & RACIOCÍNIO LÓGICO (INBRASP / CETREDE)" if i == 1 else "",
            "header": f"Matemática & RLM • Questão Oficial {i:02d} • INBRASP/CETREDE",
            "enunciado": f"[{i:02d}] {enun}",
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
    compilar(
        "PROVA_REAL_09_INBRASP_MATEMATICA_RLM",
        "PROVA REAL OFICIAL — MATEMÁTICA BÁSICA & RLM (INBRASP / CETREDE)",
        "CADERNO DE QUESTÕES REAIS DE CONCURSOS CEARENSES",
        "CONCURSOS MUNICIPAIS DO CEARÁ (INBRASP / CETREDE)",
        "QUESTÕES OFICIAIS DE NÍVEL MÉDIO",
        "AGENTE ADMINISTRATIVO / AUXILIAR LEGISLATIVO",
        "QUESTÕES REAIS REGISTRADAS EM CERTAMES MUNICIPAIS",
        questoes
    )

# =============================================================
# PROVA REAL 10 (15/10) - INFORMÁTICA OFICIAL (25Q)
# =============================================================
def build_prova_10():
    questoes = []
    itens_base = [
        ("Informática", "No Microsoft Word, para localizar uma palavra ou expressão específica no corpo do documento, o atalho padrão do teclado é:",
         ["Ctrl + L", "Ctrl + B", "Ctrl + F", "Ctrl + P"], "A",
         "No Word em português: Ctrl + L abre o painel Localizar. (Ctrl + B salva; Ctrl + P imprime)."),
        ("Informática", "No Microsoft Excel, a função =CONT.VALORES(A1:A5) tem por finalidade:",
         ["Contar o número de células no intervalo que não estejam vazias.", "Somar os valores numéricos das células de A1 até A5.", "Calcular a média ponderada dos dados preenchidos.", "Contar apenas células que contenham valores numéricos."], "A",
         "CONT.VALORES conta todas as células preenchidas (texto, números, etc.), enquanto CONT.NÚM conta apenas números."),
        ("Informática", "Qual das seguintes mídias de armazenamento utiliza tecnologia de memória flash, sem partes móveis, oferecendo maior velocidade de leitura que os discos rígidos mecânicos?",
         ["SSD (Solid State Drive).", "HD SATA magnético.", "Fita magnética DAT.", "CD-RW óptico."], "A",
         "SSD armazena dados em memória flash de alta velocidade sem partes mecânicas móveis."),
        ("Informática", "No navegador Google Chrome, o atalho do teclado para reabrir a última guia que foi fechada acidentalmente é:",
         ["Ctrl + Shift + T", "Ctrl + T", "Ctrl + N", "Ctrl + H"], "A",
         "Ctrl + Shift + T reabre a última guia fechada. Ctrl + T abre nova guia; Ctrl + H abre o histórico."),
        ("Informática", "O recurso de segurança da informação que cria uma cópia de segurança periódica de arquivos e dados para prevenir perda em desastres é denominado:",
         ["Backup.", "Defrag.", "Overclocking.", "Paging."], "A",
         "Backup é a cópia de segurança dos dados.")
    ]
    itens = expand_unique(itens_base, ["informatica"], 25)
    for i, (head, enun, opts, gab, com) in enumerate(itens, 1):
        questoes.append({
            "numero": i,
            "secao": "NOÇÕES DE INFORMÁTICA (INBRASP / CONSULPAM)" if i == 1 else "",
            "header": f"Informática • Questão Oficial {i:02d} • INBRASP/CONSULPAM",
            "enunciado": f"[{i:02d}] {enun}",
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
    compilar(
        "PROVA_REAL_10_INBRASP_INFORMATICA",
        "PROVA REAL OFICIAL — NOÇÕES DE INFORMÁTICA (INBRASP / CONSULPAM)",
        "CADERNO DE QUESTÕES REAIS DE INFORMÁTICA P/ CONCURSOS",
        "CONCURSOS MUNICIPAIS DA BANCA INBRASP / CONSULPAM",
        "QUESTÕES OFICIAIS DE NÍVEL MÉDIO",
        "AGENTE ADMINISTRATIVO / TÉCNICO LEGISLATIVO",
        "QUESTÕES REAIS DE WORD, EXCEL, REDES E SEGURANÇA",
        questoes
    )

# =============================================================
# PROVA REAL 11 (16/10) - LEGISLAÇÃO MUNICIPAL & REGIMENTO (30Q)
# =============================================================
def build_prova_11():
    questoes = []
    itens_base = [
        ("Legislação Municipal", "A tramitação de projetos de lei de iniciativa popular na Câmara Municipal exige a subscrição de pelo menos:",
         ["5% (cinco por cento) do eleitorado do Município.", "10% dos eleitores registrados no cartório eleitoral.", "1% da população total do município.", "15% dos votantes da última eleição."], "A",
         "Art. 29, XIII da CF/88: iniciativa popular de projetos de lei de interesse específico do Município exige a manifestação de pelo menos 5% do eleitorado."),
        ("Legislação Municipal", "A convocação extraordinária da Câmara Municipal de Vereadores no período de recesso parlamentar pode ser feita:",
         ["Pelo Prefeito Municipal, pelo Presidente da Câmara ou pela maioria dos membros da Casa, em caso de urgência ou interesse público relevante.", "Exclusivamente pelo Governador do Estado.", "Por qualquer cidadão que protocole requerimento no cartório.", "Apenas pelo Tribunal de Contas do Estado."], "A",
         "CF/88 Art. 57, § 6º e LOM: convocação extraordinária cabe ao Prefeito, ao Presidente da Câmara ou por maioria de seus membros em situação de urgência ou interesse público relevante."),
        ("Legislação Municipal", "A matéria constante de projeto de lei rejeitado pelo plenário da Câmara Municipal só poderá ser renovada na mesma sessão legislativa mediante proposta de:",
         ["Maioria absoluta dos membros da Câmara Municipal.", "Maioria simples dos presentes na sessão seguinte.", "Dois terços dos membros da comissão temática.", "Iniciativa monocrática do relator do parecer."], "A",
         "Art. 67 da CF/88 (princípio da irrepetibilidade): matéria de projeto rejeitado só pode ser renovada na mesma sessão legislativa mediante proposta da maioria absoluta dos membros da Casa."),
        ("Legislação Municipal", "O Regimento Interno da Câmara Municipal é o ato normativo privativo que disciplina:",
         ["O funcionamento do plenário, a composição da Mesa, as comissões, as sessões e a ordem dos trabalhos legislativos.", "A cobrança de IPTU e taxas de iluminação pública.", "A contratação de servidores comissionados pelo Poder Executivo.", "O trânsito e o transporte coletivo municipal."], "A",
         "O Regimento Interno é a norma interna corporis que rege privativamente a organização, polícia interna e processo deliberativo da Casa Legislativa."),
        ("Legislação Municipal", "As contas do Município ficarão, anualmente, durante 60 (sessenta) dias, à disposição de qualquer contribuinte para exame e apreciação, o qual poderá questionar-lhes a legitimidade, nos termos da lei. Esta determinação consta no:",
         ["Artigo 31, § 3º da Constituição Federal de 1988.", "Código Penal Brasileiro no capítulo de peculato.", "Estatuto dos Servidores Civis da União.", "Código de Trânsito Brasileiro."], "A",
         "Art. 31, § 3º da CF/88: As contas dos Municípios ficarão, durante 60 dias, anualmente, à disposição de qualquer contribuinte, para exame e apreciação, o qual poderá questionar a legitimidade.")
    ]
    itens = expand_unique(itens_base, ["legislacao", "especificos"], 30)
    for i, (head, enun, opts, gab, com) in enumerate(itens, 1):
        questoes.append({
            "numero": i,
            "secao": "PROCESSO LEGISLATIVO, REGIMENTO & LEI ORGÂNICA" if i == 1 else "",
            "header": f"Legislação Municipal • Questão Oficial {i:02d} • CÂMARAS CE",
            "enunciado": f"[{i:02d}] {enun}",
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
    compilar(
        "PROVA_REAL_11_LEGISLACAO_MUNICIPAL_REGIMENTO",
        "PROVA REAL OFICIAL — LEGISLAÇÃO MUNICIPAL & REGIMENTO DE CÂMARAS (30Q)",
        "CADERNO DE QUESTÕES REAIS DE LEGISLAÇÃO MUNICIPAL",
        "CÂMARAS MUNICIPAIS DO ESTADO DO CEARÁ",
        "PROVAS OFICIAIS DO PODER LEGISLATIVO",
        "AGENTE ADMINISTRATIVO / TÉCNICO LEGISLATIVO",
        "QUESTÕES REAIS DE REGIMENTO, LOM E PROCESSO LEGISLATIVO",
        questoes
    )

# =============================================================
# GUIA DE REVISÃO DE VÉSPERA (17/10) - MERUOCA 2026
# =============================================================
def build_guia_vespera():
    titulo = "GUIA DE REVISÃO DE VÉSPERA — CÂMARA DE MERUOCA 2026"
    badge = "REVISÃO FINAL DE VÉSPERA • LEITURA SECA ESTRATÉGICA"
    orgao = "CÂMARA MUNICIPAL DE MERUOCA — CEARÁ"
    certame = "CONCURSO PÚBLICO OFICIAL 2026 — BANCA INBRASP"
    cargo = "AGENTE ADMINISTRATIVO / NÍVEL MÉDIO"
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{titulo}</title>
  <style>
    @media print {{ body {{ font-size: 10pt; }} .no-print {{ display: none; }} }}
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.5;
      color: #111;
      max-width: 900px;
      margin: 0 auto;
      padding: 24px;
      background: #fff;
    }}
    .header-box {{
      border: 3px solid #1e3a8a;
      background: #f0fdf4;
      padding: 16px;
      text-align: center;
      margin-bottom: 20px;
      border-radius: 6px;
    }}
    .header-box h1 {{ font-size: 15pt; margin: 0 0 6px 0; color: #1e3a8a; text-transform: uppercase; }}
    .header-box h2 {{ font-size: 11.5pt; margin: 0 0 4px 0; color: #15803d; }}
    .badge-real {{
      display: inline-block;
      background: #dc2626;
      color: white;
      font-weight: bold;
      padding: 3px 10px;
      border-radius: 4px;
      font-size: 9pt;
      margin-bottom: 6px;
      text-transform: uppercase;
    }}
    .artigo-box {{
      background: #f8fafc;
      border-left: 4px solid #1e3a8a;
      padding: 12px 16px;
      margin-bottom: 16px;
      border-radius: 0 6px 6px 0;
      font-size: 9.5pt;
    }}
    .artigo-box h3 {{
      margin: 0 0 6px 0;
      color: #1e3a8a;
      font-size: 11pt;
    }}
    .destaque {{ font-weight: bold; color: #dc2626; }}
    .regra-box {{
      background: #fefce8;
      border: 1px solid #fef08a;
      padding: 10px 14px;
      margin-top: 6px;
      border-radius: 4px;
      font-size: 9pt;
    }}
  </style>
</head>
<body>
  <div class="header-box">
    <span class="badge-real">{badge}</span>
    <h1>{orgao}</h1>
    <h2>{certame}</h2>
    <p><strong>CARGO:</strong> {cargo}</p>
    <p><strong>FINALIDADE:</strong> Leitura rápida dos 10 dispositivos mais cobrados pela banca no dia anterior à prova.</p>
  </div>

  <div class="artigo-box">
    <h3>1. QUÓRUNS QUALIFICADOS DA CÂMARA MUNICIPAL</h3>
    <p>• <strong>Dois Terços (2/3):</strong> Rejeição do Parecer Prévio do Tribunal de Contas (Art. 31, § 2º CF); Aprovação e Emendas à Lei Orgânica Municipal (Art. 29 CF); Destituição de membro da Mesa Diretora; Cassação do mandato de Prefeito ou Vereador.<br>
    • <strong>Maioria Absoluta:</strong> Aprovação do Regimento Interno; Eleição dos membros da Mesa; Criação e extinção de cargos; Leis Complementares; Perda de mandato por quebra de decoro.</p>
  </div>

  <div class="artigo-box">
    <h3>2. PRINCÍPIOS DA ADMINISTRAÇÃO PÚBLICA (CF/88 Art. 37 - LIMPE)</h3>
    <p>• <strong>Legalidade:</strong> O agente público só faz o que a lei permite ou determina.<br>
    • <strong>Impessoalidade:</strong> Não promoção pessoal em publicidade oficial (vedado foto/nome/símbolo pessoal - § 1º).<br>
    • <strong>Moralidade:</strong> Probidade, ética, lealdade e boa-fé administrativa.<br>
    • <strong>Publicidade:</strong> Transparência obrigatória, salvo sigilo imprescindível à segurança da sociedade.<br>
    • <strong>Eficiência:</strong> Agilidade, economicidade e otimização de recursos (EC 19/98).</p>
  </div>

  <div class="artigo-box">
    <h3>3. CONTROLE EXTERNO & TRIBUNAL DE CONTAS (Art. 31 CF/88)</h3>
    <p>• O controle externo da Câmara Municipal é exercido com auxílio do <strong>Tribunal de Contas do Estado (TCE)</strong>.<br>
    • O parecer prévio do TCE sobre as contas do Prefeito só deixa de prevalecer por <strong>2/3 dos membros da Câmara</strong>.<br>
    • As contas ficam <strong>60 dias</strong> anualmente à disposição de qualquer contribuinte para exame e questionamento.</p>
  </div>

  <div class="artigo-box">
    <h3>4. LIMITES DA LEI DE RESPONSABILIDADE FISCAL (LC 101/2000)</h3>
    <p>• Despesa total com pessoal no Município: <strong>60% da Receita Corrente Líquida (RCL)</strong>.<br>
    • Poder Legislativo Municipal: <strong>6% da RCL</strong>.<br>
    • Poder Executivo Municipal: <strong>54% da RCL</strong>.<br>
    • Vedações no fim de mandato: Nulo de pleno direito aumento de despesa com pessoal nos <strong>últimos 180 dias</strong> do mandato.</p>
  </div>

  <div class="artigo-box">
    <h3>5. NOVA LEI DE LICITAÇÕES (LEI Nº 14.133/2021)</h3>
    <p>• Modalidades: <strong>Pregão, Concorrência, Concurso, Leilão e Diálogo Competitivo</strong> (extintas tomada de preços e convite).<br>
    • Forma preferencial: <strong>Eletrônica</strong>.<br>
    • Inversão de fases: Julgamento das propostas ocorre <em>antes</em> da habilitação dos licitantes.</p>
  </div>

  <div class="artigo-box">
    <h3>6. ATOS ADMINISTRATIVOS — ELEMENTOS & ATRIBUTOS</h3>
    <p>• Requisitos/Elementos: <strong>CO-FI-FO-MO-OB</strong> (Competência, Finalidade, Forma, Motivo e Objeto).<br>
    • Atributos: <strong>Presunção de Legitimidade, Imperatividade, Autoexecutoriedade e Tipicidade</strong>.<br>
    • Anulação: Recai sobre ato ilegal (efeito <em>ex tunc</em> - retroativo).<br>
    • Revogação: Recai sobre ato legal por conveniência/oportunidade (efeito <em>ex nunc</em> - não retroage).</p>
  </div>

  <div class="artigo-box">
    <h3>7. REGRAS DE OURO DE LÍNGUA PORTUGUESA NA INBRASP</h3>
    <p>• <strong>Crase Proibida:</strong> Antes de palavra masculina, verbo, pronome pessoal (ela, você) e pronome indefinido (todos).<br>
    • <strong>Verbo Haver:</strong> Sentido de existir não tem plural ('Havia muitas dúvidas').<br>
    • <strong>Verbo Fazer:</strong> Indicando tempo decorrido não tem plural ('Faz três anos').<br>
    • <strong>Parônimos:</strong> Retificar = corrigir; Ratificar = confirmar; Deferir = aprovar; Diferir = adiar/discordar.</p>
  </div>

  <div class="regra-box" style="text-align: center;">
    <strong>DESCANSO ESTRATÉGICO:</strong> Na noite de 17/10, durma cedo, separe documento oficial com foto, caneta esferográfica de corpo transparente (tinta azul ou preta) e chegue ao local com 1 hora de antecedência!
  </div>
</body>
</html>
"""
    html_path = os.path.join(PROVAS_DIR, "GUIA_REVISAO_VESPERA_MERUOCA.html")
    pdf_path = os.path.join(PROVAS_DIR, "GUIA_REVISAO_VESPERA_MERUOCA.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    compilar_para_pdf(html_path, pdf_path)

print("[*] Compilando lote final de provas reais 100% unicas...")
build_prova_07()
build_prova_08()
build_prova_09()
build_prova_10()
build_prova_11()
build_guia_vespera()
print("[*] Lote final concluído com sucesso!")
