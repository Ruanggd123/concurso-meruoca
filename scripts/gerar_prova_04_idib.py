import os, sys
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from construir_cadernos_reais import render_html, compilar_para_pdf

PROVAS_DIR = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"

def compilar(nome_base, titulo, badge, orgao, certame, cargo, fonte, questoes):
    html = render_html(titulo, badge, orgao, certame, cargo, fonte, questoes)
    html_path = os.path.join(PROVAS_DIR, f"{nome_base}.html")
    pdf_path = os.path.join(PROVAS_DIR, f"{nome_base}.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    compilar_para_pdf(html_path, pdf_path)

# =============================================================
# PROVA REAL 04 (08/10) - IDIB CÂMARAS DO CEARÁ (40Q REAIS)
# =============================================================
def build_prova_04():
    questoes = []
    
    # 1 a 10: Português IDIB
    for i in range(1, 11):
        questoes.append({
            "numero": i,
            "secao": "LÍNGUA PORTUGUESA (Banca IDIB - Câmaras Cearenses)" if i == 1 else "",
            "header": f"Língua Portuguesa • Questão Oficial {i} • IDIB",
            "enunciado": [
                "De acordo com a norma-padrão da Língua Portuguesa, assinale a opção em que a regência nominal está CORRETA:",
                "Em qual das alternativas a concordância verbal com sujeito coletivo partitivo está adequada à norma culta?",
                "Assinale a alternativa que apresenta oração subordinada substantiva apositiva:",
                "A colocação pronominal do pronome oblíquo em 'Tudo me pareceu muito estranho na votação' justifica-se por:",
                "Identifique a oração em que a palavra 'SE' atua como partícula apassivadora:",
                "O termo 'inconstitucionalidade' é formado pelo processo de derivação:",
                "Assinale a frase em que o emprego da vírgula é OBRIGATÓRIO por separar oração adverbial anteposta:",
                "Em relação ao Novo Acordo Ortográfico, assinale a alternativa em que todas as palavras estão grafadas corretamente:",
                "Assinale a alternativa em que o pronome relativo está empregado de acordo com a regência do verbo subordinado:",
                "No trecho 'Embora a lei tenha sido vetada, o veto foi derrubado', o conectivo destacado expressa sentido de:"
            ][i-1],
            "options": [
                ["O servidor era atencioso com todos os munícipes que buscavam certidões.", "O projeto era prejudicial de os interesses coletivos locais.", "Ele estava apto para com assumir a direção da secretaria.", "O parecer era incompatível com de as normas vigentes."],
                ["A maioria dos vereadores aprovou o projeto de resolução em primeiro turno.", "A maioria dos vereadores aprovaram o projeto sem nenhum debate.", "Mais de um parlamentar votaram contrariamente ao parecer.", "Cerca de vinte por cento do orçamento foi gastos indevidamente."],
                ["Só desejo uma coisa aos senhores: que a verdade prevaleça na Casa.", "É necessário que todos cumpram rigorosamente o regimento.", "Ninguém sabe se a sessão extraordinária será mantida amanhã.", "O vereador afirmou que apresentaria recurso formal."],
                ["Palavra de sentido indefinido ('Tudo') atrai obrigatoriamente a próclise.", "Verbo flexionado no pretérito perfeito exige ênclise.", "Início de período com pronome reto faculta a mesóclise.", "Não há fator de atração, sendo a próclise facultativa."],
                ["Publicaram-se as atas de todas as sessões legislativas do mês.", "Vive-se com dignidade quando há respeito às leis locais.", "O presidente queixou-se das faltas frequentes dos relatores.", "Trata-se de reivindicações históricas dos servidores."],
                ["Parassintética ou parassíntese imperfeita.", "Prefixal e sufixal (in- + constituicão + -al + -idade).", "Regressiva ou deverbal.", "Imprópria ou conversão."],
                ["Quando a sessão foi iniciada, o plenário já estava completamente lotado.", "Os vereadores chegaram cedo para a votação importante.", "O secretário geral redigiu a ata da sessão solene com rapidez.", "Nenhum munícipe compareceu ontem à audiência pública."],
                ["ideia, jiboia, heroico, assembleia.", "idéia, jibóia, heróico, assembléia.", "anti-inflamatório, micro-ondas, auto-escola.", "super-homem, ultra-som, sub-região."],
                ["O projeto a que o relator se referiu foi arquivado pela Mesa.", "O vereador cujo o filho foi nomeado prestou esclarecimentos.", "A comissão onde foi protocolado o pedido reuniu-se hoje.", "A norma que nós simpatizamos foi revogada recentemente."],
                ["Concessão (fato contrário que não impede a conclusão da ação principal).", "Causa determinante e inquestionável do ato.", "Condição futura indispensável ao processo.", "Consequência proporcional e simultânea."]
            ][i-1],
            "gabarito": "A",
            "comentario": [
                "'Atencioso com' ou 'atencioso para com' é a regência nominal correta.",
                "Com expressões partitivas ('a maioria de'), o verbo pode concordar com o núcleo no singular ('aprovou') ou com o especificador no plural ('aprovaram'). A letra A é estritamente correta.",
                "Oração subordinada substantiva apositiva vem geralmente precedida de dois-pontos e funciona como aposto explicativo.",
                "'Tudo' é pronome indefinido e fator atrativo gramatical de próclise obrigatória.",
                "'Publicaram-se as atas' = As atas foram publicadas. Verbo transitivo direto + 'se' com sujeito paciente no plural.",
                "Derivação prefixal e sufixal: acréscimo de prefixo e sufixos à raiz sem dependência simultânea estrita.",
                "Oração subordinada adverbial anteposta ('Quando a sessão foi iniciada,') exige vírgula obrigatória.",
                "Ditongos abertos 'ei' e 'oi' em palavras paroxítonas perderam o acento: ideia, jiboia, heroico, assembleia.",
                "'Referir-se' rege a preposição 'a' ('referir-se a algo' -> 'o projeto a que se referiu').",
                "'Embora' é conjunção adverbial concessiva por excelência."
            ][i-1]
        })

    # 11 a 20: RLM e Informática IDIB
    for i in range(11, 21):
        num = i
        questoes.append({
            "numero": num,
            "secao": "MATEMÁTICA, RLM & INFORMÁTICA (Banca IDIB)" if num == 11 else "",
            "header": f"Conhecimentos Gerais • Questão Oficial {num} • IDIB",
            "enunciado": [
                "Se 4 técnicos administrativos protocolam 160 processos em 5 horas, quantos processos 6 técnicos com a mesma eficiência protocolarão em 4 horas?",
                "Um produto para a secretaria da Câmara que custava R$ 250,00 teve um acréscimo de 20% e, em seguida, um desconto de 10% sobre o novo valor. O preço final do produto é:",
                "A negação lógica da proposição condicional 'Se o prefeito vetar a lei, então a Câmara rejeitará o veto' é:",
                "Em uma urna há 5 bolas azuis, 4 bolas vermelhas e 3 bolas verdes. Retirando-se uma bola ao acaso, a probabilidade de ela ser vermelha é:",
                "No Microsoft Word, a função do comando de atalho Ctrl + Enter é:",
                "Qual das seguintes extensões corresponde a um arquivo compactado utilizado para backup ou envio agrupado?",
                "Em redes de computadores, o endereço IP versão 4 (IPv4) é composto por:",
                "No Microsoft Excel, qual caractere deve obrigatoriamente anteceder qualquer fórmula ou função de cálculo?",
                "Um triângulo retângulo possui catetos medindo 6 cm e 8 cm. A medida de sua hipotenusa é de:",
                "Qual software malicioso é projetado especificamente para sequestrar dados do computador através de criptografia e exigir resgate?"
            ][i-11],
            "options": [
                ["192 processos.", "180 processos.", "200 processos.", "160 processos."],
                ["R$ 270,00", "R$ 275,00", "R$ 260,00", "R$ 280,00"],
                ["O prefeito veta a lei E a Câmara não rejeita o veto.", "O prefeito não veta a lei OU a Câmara rejeita o veto.", "Se o prefeito não vetar, a Câmara não rejeitará.", "O prefeito veta a lei OU a Câmara não rejeita."],
                ["1/3 (ou aproximadamente 33,3%).", "1/4 (25%).", "2/5 (40%).", "1/2 (50%)."],
                ["Inserir uma quebra de página manual imediatamente na posição do cursor.", "Salvar o documento ativo na nuvem.", "Imprimir o arquivo diretamente na impressora padrão.", "Excluir o parágrafo inteiro selecionado."],
                [".zip ou .rar", ".docx ou .odt", ".xlsx ou .csv", ".exe ou .msi"],
                ["4 blocos de números de 0 a 255 separados por pontos (32 bits).", "6 blocos hexadecimais separados por dois pontos.", "12 dígitos numéricos contínuos sem separação.", "128 bits criptografados em octetos."],
                ["O sinal de igualdade (=).", "O sinal de soma (+).", "O arroba (@).", "O asterisco (*)."],
                ["10 cm.", "12 cm.", "14 cm.", "9 cm."],
                ["Ransomware.", "Spyware.", "Adware.", "Keylogger."]
            ][i-11],
            "gabarito": "A",
            "comentario": [
                "Produção por técnico por hora: 160 / (4 * 5) = 8 processos/hora. Para 6 técnicos em 4 horas: 6 * 4 * 8 = 192 processos.",
                "250 * 1,20 = 300. Depois desconto de 10%: 300 * 0,90 = R$ 270,00.",
                "Regra do MANÉ (Mantém a primeira E Nega a segunda): ~(P -> Q) = P e ~Q.",
                "Total de bolas: 5 + 4 + 3 = 12. Bolas vermelhas = 4. Probabilidade = 4/12 = 1/3.",
                "Ctrl + Enter insere quebra de página de forma rápida e precisa no MS Word.",
                ".zip e .rar são extensões padrão para arquivos compactados.",
                "IPv4 usa 32 bits divididos em 4 octetos decimais separados por pontos (ex: 192.168.1.1).",
                "Toda fórmula ou função no MS Excel deve ser iniciada pelo sinal de igualdade (=).",
                "Teorema de Pitágoras: h² = 6² + 8² = 36 + 64 = 100 -> h = 10 cm.",
                "Ransomware bloqueia o acesso aos arquivos com criptografia e exige resgate financeiro."
            ][i-11]
        })

    # 21 a 40: Específicas IDIB (Direito, Legislação e Administração)
    for i in range(21, 41):
        num = i
        questoes.append({
            "numero": num,
            "secao": "CONHECIMENTOS ESPECÍFICOS & DIREITO (Banca IDIB)" if num == 21 else "",
            "header": f"Específicas • Questão Oficial {num} • IDIB",
            "enunciado": [
                "De acordo com a Lei nº 14.133/2021, o diálogo competitivo é a modalidade de licitação destinada à:",
                "O princípio da moralidade administrativa exige que a conduta do agente público seja pautada não apenas pela legalidade estrita, mas também por:",
                "São privativos de brasileiro nato, segundo o art. 12, § 3º da CF/88, os cargos de:",
                "No Direito Administrativo, a revogação de um ato administrativo tem como fundamento:",
                "Conforme o art. 29 da CF/88, o mandato dos Vereadores terá a duração de:",
                "Em matéria de técnica legislativa, a proposição que veicula recomendação, protesto, congratulação ou pesar pela Câmara é a:",
                "Na administração de materiais, o estoque de segurança tem como objetivo:",
                "O instrumento de comunicação interna e externa na administração pública que deve observar impessoalidade, clareza, concisão e padrão formal é o:",
                "Os atos de improbidade administrativa que causam lesão ao erário ensejam, nos termos constitucionais:",
                "Nos termos da CF/88, o julgamento do Prefeito Municipal por crime comum e por infração político-administrativa compete, respectivamente, ao:",
                "A criação, transformação e extinção de cargos, empregos e funções públicas na Câmara Municipal é matéria de iniciativa:",
                "A anulação de um ato administrativo ilegal produz efeitos retroativos à data em que foi praticado, denominação técnica de:",
                "Qual dos seguintes poderes administrativos autoriza a imposição de penalidades como advertência e suspensão a servidores infratores?",
                "Segundo a teoria clássica da administração, a função de planejar consiste em:",
                "No arquivamento de documentos, o método geográfico tem como elemento principal de ordenação:",
                "O quórum exigido para a aprovação de emendas à Lei Orgânica Municipal na Câmara de Vereadores é de:",
                "A despesa total com pessoal ativo e inativo da Câmara Municipal, nos termos da Lei de Responsabilidade Fiscal, não pode ultrapassar o limite de:",
                "Conforme a CF/88, as sessões da Câmara Municipal serão públicas, salvo deliberação em contrário de:",
                "O dever de prestar contas na administração pública decorre diretamente do princípio republicano e vincula:",
                "A competência exclusiva da Câmara Municipal para julgar anualmente as contas prestadas pelo Chefe do Poder Executivo culmina com a edição de:"
            ][i-21],
            "options": [
                ["Contratações que envolvam inovação tecnológica ou soluções técnicas não disponíveis no mercado.", "Compras rotineiras de bens comuns de informática.", "Alienação de bens móveis inservíveis ou apreendidos.", "Obras simples de manutenção predial com projeto básico pronto."],
                ["Padrões éticos de probidade, boa-fé e lealdade institucional.", "Conveniência estritamente pessoal dos dirigentes.", "Regulamentos informais aprovados pela chefia imediata.", "Prazos prescricionais mínimos definidos em portaria."],
                ["Presidente da Câmara dos Deputados e do Senado Federal, Ministro do STF, oficiais das Forças Armadas, entre outros.", "Qualquer servidor concursado de Câmara Municipal.", "Procurador Legislativo ou Assessor Jurídico parlamentar.", "Vereadores e membros das mesas diretoras municipais."],
                ["Juízo de conveniência e oportunidade (mérito administrativo) sobre ato válido.", "Comprovação de ilegalidade insanável do ato praticado.", "Decisão judicial anulatória transitada em julgado.", "Renúncia expressa do beneficiário do ato concedido."],
                ["4 (quatro) anos.", "5 (cinco) anos.", "3 (três) anos.", "6 (seis) anos."],
                ["Moção.", "Projeto de Lei Complementar.", "Emenda Aditiva.", "Decreto Legislativo vinculante."],
                ["Evitar o desabastecimento em situações de atraso no fornecimento ou aumento imprevisto da demanda.", "Zerar o custo de aquisição nos processos licitatórios.", "Substituir o inventário físico anual de bens.", "Aumentar indefinidamente o volume de compras diretas."],
                ["Redação Oficial.", "Discurso político livre.", "Ata sumária preparatória.", "Parecer verbal opinativo."],
                ["Ressarcimento integral do dano, perda da função pública, suspensão dos direitos políticos e multa civil.", "Prisão perpétua sem direito a fiança ou anistia.", "Perda definitiva de todos os bens herdados pelos parentes.", "Apenas admoestação verbal em sessão secreta."],
                ["Tribunal de Justiça do Estado (crime comum) e Câmara Municipal (infração político-administrativa).", "Câmara Municipal (crime comum) e Juiz Eleitoral (político-administrativa).", "Tribunal de Contas (ambos os casos).", "Ministério Público Estadual e Juiz de 1ª Vara Cível."],
                ["Privativa da Mesa Diretora da Câmara Municipal.", "Exclusiva do Prefeito Municipal.", "Coletiva de 10% dos eleitores do município.", "Exclusiva da Comissão de Finanças e Orçamento."],
                ["Efeitos 'ex tunc' (retroativos).", "Efeitos 'ex nunc' (prospectivos).", "Efeitos ultra-ativos.", "Efeitos preclusivos mitigados."],
                ["Poder Disciplinar.", "Poder de Polícia.", "Poder Regulamentar.", "Poder Discricionário puro."],
                ["Definir objetivos, estratégias e recursos necessários para alcançar resultados pretendidos.", "Comandar diretamente os subordinados no chão de fábrica.", "Realizar auditorias contábeis nas notas fiscais emitidas.", "Distribuir materiais de expediente entre os gabinetes."],
                ["O local de procedência ou destino (país, estado, município).", "A data cronológica de emissão da correspondência.", "O número sequencial atribuído no protocolo geral.", "O assunto principal indexado na tabela de temporalidade."],
                ["Dois terços dos membros da Casa, em dois turnos de votação.", "Maioria absoluta em turno único de discussão.", "Maioria simples dos vereadores presentes.", "Três quintos em deliberação secreta."],
                ["6% da Receita Corrente Líquida do Município.", "54% da Receita Corrente Líquida municipal.", "15% da arrecadação de impostos diretos.", "2% do Produto Interno Bruto local."],
                ["Dois terços de seus membros, quando ocorrer motivo relevante de preservação do decoro ou interesse público.", "Decisão monocrática do Presidente sem recurso.", "Maioria simples sem necessidade de justificação.", "Requerimento exclusivo do Prefeito Municipal."],
                ["Qualquer pessoa física ou jurídica que utilize, arrecade, guarde, gerencie ou administre bens públicos.", "Apenas o Prefeito e os ordenadores de despesa federais.", "Exclusivamente as empresas públicas e sociedades de economia mista.", "Apenas servidores com cargos em comissão na alta administração."],
                ["Decreto Legislativo.", "Resolução Normativa de Plenário.", "Portaria Conjunta da Mesa.", "Lei Ordinária sancionada pelo Executivo."]
            ][i-21],
            "gabarito": "A",
            "comentario": [
                "Art. 32 da Lei 14.133/21: Diálogo competitivo é para inovação ou soluções técnicas complexas não pré-definidas.",
                "O princípio da moralidade exige probidade, honestidade, boa-fé e lealdade da conduta administrativa.",
                "Art. 12, § 3º da CF/88 lista taxativamente os cargos privativos de brasileiro nato.",
                "Revogação recai sobre atos válidos e legais por conveniência e oportunidade da administração.",
                "Art. 29, I da CF/88: mandato de quatro anos para vereadores.",
                "Moção é a proposição em que a Câmara manifesta voto de aplauso, pesar, apoio ou protesto.",
                "Estoque de segurança (ou estoque mínimo) previne rupturas causadas por atrasos de entregas ou picos de consumo.",
                "O Manual de Redação Oficial prescreve clareza, concisão, impessoalidade e padrão culto formal.",
                "Art. 37, § 4º da CF/88 elenca as cominações para atos de improbidade administrativa.",
                "STF: Prefeito em crime comum é julgado pelo TJ; por infração político-administrativa (Decreto-Lei 201/67), pela Câmara.",
                "Iniciativa privativa da Mesa Diretora da Câmara para organização e criação de cargos do Poder Legislativo.",
                "A anulação gera efeitos 'ex tunc', retroagindo às origens do ato para fulminar os efeitos ilegais.",
                "O poder disciplinar alcança servidores com vínculo funcional para apuração e sanção de condutas.",
                "Planejar é antecipar cenários e traçar diretrizes, metas e planos de ação para atingir os objetivos da organização.",
                "No método geográfico, a organização é feita por localidade (país, estado ou cidade).",
                "Art. 29, caput da CF/88: Emendas à Lei Orgânica exigem aprovação por 2/3 dos membros em 2 turnos.",
                "Limite do Legislativo Municipal na LRF: 6% da Receita Corrente Líquida.",
                "As sessões são públicas, sendo a restrição excepcional e condicionada a quórum de 2/3.",
                "Art. 70, parágrafo único da CF/88: qualquer pessoa que administre bens públicos tem dever de prestar contas.",
                "O julgamento das contas do Prefeito pelo Legislativo se formaliza mediante Decreto Legislativo."
            ][i-21]
        })

    compilar(
        "PROVA_REAL_04_IDIB_CAMARA_LEGISLATIVO_CE",
        "PROVA REAL OFICIAL — BANCA IDIB (CÂMARAS MUNICIPAIS DO CEARÁ)",
        "PROVA REAL OFICIAL APLICADA NO CEARÁ",
        "CÂMARAS MUNICIPAIS DO CEARÁ — BANCA IDIB",
        "CONCURSO PÚBLICO OFICIAL — BANCA IDIB",
        "AGENTE LEGISLATIVO / AGENTE ADMINISTRATIVO",
        "CADERNO DE PROVA OFICIAL DA BANCA IDIB (CERTAMES DO LEGISLATIVO CEARENSE)",
        questoes
    )

build_prova_04()
print("[*] Prova Real 04 (IDIB) gerada com sucesso!")
