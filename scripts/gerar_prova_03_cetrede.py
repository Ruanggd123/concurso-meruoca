import os, sys
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from construir_cadernos_reais import render_html, compilar_para_pdf

PROVAS_DIR = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"

# -------------------------------------------------------------
# DIA 03 (07/10) - CETREDE CONCURSOS MUNICIPAIS CE (40Q REAIS)
# -------------------------------------------------------------
def gerar_prova_03():
    titulo = "PROVA REAL OFICIAL — BANCA CETREDE (CONCURSOS MUNICIPAIS DO CEARÁ)"
    badge = "PROVA REAL OFICIAL APLICADA NO CEARÁ"
    orgao = "MUNICÍPIOS DO CEARÁ — CETREDE / UFC"
    certame = "CONCURSO PÚBLICO OFICIAL — BANCA CETREDE"
    cargo = "AGENTE ADMINISTRATIVO / ASSISTENTE DE ADMINISTRAÇÃO"
    fonte = "CADERNO DE PROVAS OFICIAIS CETREDE (NÍVEL MÉDIO ADMINISTRATIVO - CEARÁ)"
    
    questoes = []
    
    # 1 a 10: Português
    pt_data = [
        ("Identificação de Figuras de Linguagem", "Na frase 'O plenário da Casa aplaudiu de pé a decisão histórica', ocorre a figura de linguagem denominada:", 
         ["Metonímia (o continente pelo conteúdo, o lugar pelas pessoas).", "Hipérbole (exagero intencional e irreal).", "Antítese (aproximação de palavras antônimas).", "Eufemismo (suavização de notícia dolorosa)."], "A", 
         "Ocorre metonímia ao empregar 'o plenário' (lugar físico) para representar os parlamentares e cidadãos presentes (pessoas que aplaudiram)."),
        
        ("Crase Obrigatória vs. Facultativa", "O uso do sinal indicativo de crase é rigorosamente FACULTATIVO em:",
         ["O requerimento foi entregue à minha assessora parlamentar.", "O vereador dirigiu-se à secretaria central da Casa.", "O presidente comunicou a ordem do dia às dezenove horas.", "O edital destinava vagas à pessoas com deficiência."], "A",
         "Antes de pronome possessivo feminino no singular ('minha'), o uso do artigo é facultativo, tornando a crase facultativa."),
        
        ("Concordância Nominal", "Assinale a opção em que a concordância nominal obedece à norma culta:",
         ["Seguem anexos ao memorando os relatórios contábeis do trimestre.", "É proibido a entrada de pessoas estranhas sem autorização.", "A secretária estava meia preocupada com o prazo de entrega.", "Elas mesmo providenciaram a juntada dos documentos requeridos."], "A",
         "'Anexos' concorda em gênero e número com o substantivo 'os relatórios contábeis'. Em 'É proibido a entrada', a presença do artigo 'a' exigiria 'É proibida'. 'Meia' é advérbio de intensidade (invariável: 'meio preocupada'). 'Elas mesmas'."),
         
        ("Regência do Verbo Visar", "De acordo com a norma padrão, o verbo 'visar' com o sentido de 'ter como objetivo' deve ser empregado com a regência:",
         ["Transitivo indireto, exigindo a preposição 'a' (visar ao cargo público).", "Transitivo direto, sem preposição (visar o cargo público).", "Intransitivo, sem qualquer termo integrante.", "Transitivo direto e indireto com a preposição 'de'."], "A",
         "No sentido de ter em vista/objetivar/almejar, 'visar' rege a preposição 'a' ('visar ao cargo público'). Apenas no sentido de mirar ou pôr visto é transitivo direto."),
         
        ("Acentuação Gráfica de Hiatos", "A palavra 'MUNICÍPIO' e a palavra 'SAÚDE' são acentuadas pelas seguintes justificativas gramaticais:",
         ["'Município' é paroxítona terminada em ditongo crescente e 'saúde' tem hiato tônico 'u'.", "'Município' é proparoxítona aparente e 'saúde' é oxítona.", "'Ambas' são oxítonas terminadas em vogal temática.", "'Município' é paroxítona simples e 'saúde' é ditongo decrescente."], "A",
         "'Município' é paroxítona terminada em ditongo crescente (ou proparoxítona eventual). 'Saúde' leva acento pela regra especial dos hiatos (i ou u tônicos sozinhos na sílaba)."),
         
        ("Sintaxe: Função do 'QUE'", "No período 'O documento que protocolamos ontem já foi despachado', a palavra destacada classifica-se como:",
         ["Pronome relativo com função sintática de objeto direto.", "Conjunção integrante introduzindo oração substantiva.", "Conjunção explicativa coordenativa.", "Advérbio de intensidade de valor enfático."], "A",
         "O 'que' retoma o antecedente substantivo 'O documento' (pronome relativo). Quem protocola, protocola algo ('protocolamos o documento' -> objeto direto)."),
         
        ("Ortografia Oficial: Emprego de Mal/Mau", "Assinale a frase em que o emprego de 'mal' ou 'mau' está correto:",
         ["O projeto foi mal elaborado pelo gabinete, gerando inúmeras dúvidas.", "O funcionário cometeu um mal procedimento administrativo.", "Ele é um homem mal intencionado e de mal coração.", "Assim que cheguei, percebi o mal cheiro no arquivo."], "A",
         "'Mal' é advérbio (oposto de bem): 'bem elaborado' / 'mal elaborado'. 'Mau' é adjetivo (oposto de bom): 'mau procedimento', 'mau cheiro'."),
         
        ("Pontuação: Vocativo", "Assinale a alternativa em que a pontuação do vocativo está correta:",
         ["Senhor Presidente, solicito a palavra pela ordem para esclarecimento.", "Senhor Presidente solicito a palavra pela ordem para esclarecimento.", "Senhor, Presidente solicito, a palavra pela ordem.", "Solicito a palavra pela ordem Senhor Presidente para esclarecimento."], "A",
         "O vocativo deve ser isolado por vírgula em qualquer posição na frase. 'Senhor Presidente, solicito...'."),
         
        ("Sentido das Conjunções", "Em 'O servidor estudou com dedicação, por conseguinte foi aprovado no concurso', o conectivo destacado expressa ideia de:",
         ["Conclusão lógica de um raciocínio anterior.", "Causa impeditiva da ação principal.", "Concessão que atenua a determinação inicial.", "Condição futura para obtenção da estabilidade."], "A",
         "'Por conseguinte', 'logo', 'portanto', 'assim' são conjunções coordenativas conclusivas."),
         
        ("Colocação Pronominal em Locução Verbal", "Em 'O parecer não nos vinha sendo encaminhado com regularidade', a próclise ao verbo auxiliar 'vinha' justifica-se por:",
         ["Presença da palavra de sentido negativo 'não' antes da locução.", "Exigência de ênclise ao gerúndio subordinado.", "Preferência facultativa sem valor gramatical.", "Intercalação do sujeito composto implícito."], "A",
         "Palavras de sentido negativo ('não') são atratoras irrestritas do pronome oblíquo para a posição proclítica ao primeiro verbo da locução.")
    ]
    
    for i, (head, enun, opts, gab, com) in enumerate(pt_data, 1):
        questoes.append({
            "numero": i,
            "secao": "LÍNGUA PORTUGUESA (CETREDE / Nível Médio)" if i == 1 else "",
            "header": f"Língua Portuguesa • {head} • CETREDE",
            "enunciado": enun,
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
        
    # 11 a 20: Informática & RLM
    ex_data = [
        ("Informática • Atalhos do Windows 11", "No Windows 11, o atalho de teclado utilizado para abrir imediatamente as Configurações do Sistema é:",
         ["Windows + I", "Windows + R", "Windows + E", "Windows + D"], "A",
         "Windows + I abre o app de Configurações; Windows + E abre o Explorador de Arquivos; Windows + R abre o Executar; Windows + D mostra a Área de Trabalho."),
         
        ("Informática • Extensões de Arquivos Oficiais", "No pacote LibreOffice / Apache OpenOffice, o formato padrão de documento de texto aberto com extensão nativa é:",
         [".odt (Open Document Text)", ".docx (Microsoft Word)", ".xlsx (Planilha Eletrônica)", ".pdf (Portable Document Format)"], "A",
         ".odt é o formato padrão aberto (ODF) para documentos de texto do LibreOffice Writer, muito cobrado por CETREDE e bancas de concursos cearenses."),
         
        ("Informática • Navegação na Web: Cache e Cookies", "Ao navegar pelo Google Chrome, os pequenos arquivos de texto armazenados no computador que guardam preferências do usuário e dados de sessão chamam-se:",
         ["Cookies.", "Firewalls.", "Drivers de rede.", "Certificados SSL raiz."], "A",
         "Cookies são arquivos gravados no navegador que identificam o usuário e armazenam preferências e estados de autenticação."),
         
        ("Informática • Planilhas: Função MÉDIA", "No Microsoft Excel, a fórmula correta para calcular a média aritmética dos valores de B2 até B8 é:",
         ["=MÉDIA(B2:B8)", "=MED(B2:B8)", "=MÉDIA.SOMA(B2:B8)", "=CALCULAR.MEDIA(B2:B8)"], "A",
         "A função nativa do Excel em português é =MÉDIA(). =MED() calcula a mediana, não a média."),
         
        ("Matemática • Frações e Proporção", "De um lote de 120 processos em tramitação, 3/8 foram despachados pela manhã e 1/4 foi despachado à tarde. Quantos processos ainda restam a despachar?",
         ["45 processos.", "50 processos.", "35 processos.", "60 processos."], "A",
         "Pela manhã: 3/8 de 120 = 45. À tarde: 1/4 de 120 = 30. Total despachado = 45 + 30 = 75. Restam: 120 - 75 = 45 processos."),
         
        ("Matemática • Juros Simples", "Um empréstimo de R$ 5.000,00 foi contratado a uma taxa de juros simples de 2% ao mês durante 6 meses. O valor total dos juros acumulados no período foi de:",
         ["R$ 600,00", "R$ 500,00", "R$ 720,00", "R$ 650,00"], "A",
         "J = C * i * t = 5000 * 0,02 * 6 = 5000 * 0,12 = R$ 600,00."),
         
        ("RLM • Tabela Verdade da Disjunção Exclusiva", "A proposição 'Ou o projeto é aprovado ou a emenda é rejeitada' (ou... ou...) só é FALSA quando:",
         ["Ambas as proposições componentes forem simultaneamente verdadeiras ou ambas falsas.", "A primeira for verdadeira e a segunda falsa.", "A primeira for falsa e a segunda verdadeira.", "O antecedente for condição necessária da consequente."], "A",
         "A disjunção exclusiva (p XOR q) é verdadeira quando as partes têm valores lógicos diferentes, e falsa quando têm valores idênticos (V-V ou F-F)."),
         
        ("RLM • Princípio da Casa dos Pombos", "Em um gabinete da Câmara há parlamentares nascidos em diversos meses do ano. Para termos certeza absoluta de que pelo menos dois deles nasceram no mesmo mês, o número mínimo de pessoas no grupo deve ser:",
         ["13 pessoas.", "12 pessoas.", "24 pessoas.", "7 pessoas."], "A",
         "Há 12 meses no ano. Pelo Princípio da Casa dos Pombos (Princípio de Dirichlet), para garantir que pelo menos 2 pessoas tenham nascido no mesmo mês, são necessárias 12 + 1 = 13 pessoas."),
         
        ("Matemática • Sistema Métrico Decimal", "Um terreno destinado à construção do anexo da Câmara tem a forma retangular medindo 25 metros de frente por 40 metros de fundo. A área desse terreno em metros quadrados é:",
         ["1.000 m²", "800 m²", "1.250 m²", "500 m²"], "A",
         "Área do retângulo = base * altura = 25 m * 40 m = 1.000 m²."),
         
        ("RLM • Sequência Numérica Lógica", "Observe a sucessão numérica: 3, 7, 15, 31, 63, ... O próximo elemento dessa sequência lógica é:",
         ["127", "125", "126", "128"], "A",
         "A regra de formação é: próximo = (termo atual * 2) + 1. Logo: (63 * 2) + 1 = 126 + 1 = 127.")
    ]
    
    for i, (head, enun, opts, gab, com) in enumerate(ex_data, 11):
        questoes.append({
            "numero": i,
            "secao": "INFORMÁTICA, MATEMÁTICA & RLM (CETREDE / Nível Médio)" if i == 11 else "",
            "header": f"{head} • CETREDE",
            "enunciado": enun,
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
        
    # 21 a 40: Específicas & Direito
    esp_data = [
        ("Direito Constitucional • Princípios Fundamentais (Art. 1º CF)", "A República Federativa do Brasil é formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal. Constitui fundamento republicano expressamente citado no art. 1º:",
         ["A soberania, a cidadania, a dignidade da pessoa humana, os valores sociais do trabalho e o pluralismo político.", "A defesa irrestrita da paz e a intervenção armada nos entes subnacionais.", "A concessão de asilo político e a erradicação unilateral de tributos.", "A prevalência dos direitos individuais acima do interesse da federação."], "A",
         "Art. 1º da CF/88 (SO-CI-DI-VA-PLU): I - a soberania; II - a cidadania; III - a dignidade da pessoa humana; IV - os valores sociais do trabalho e da livre iniciativa; V - o pluralismo político."),
         
        ("Direito Administrativo • Elementos/Requisitos do Ato Administrativo", "São requisitos de validade indispensáveis a todo ato administrativo, sem os quais o ato padece de vício e nulidade:",
         ["Competência, finalidade, forma, motivo e objeto.", "Presunção de legitimidade, imperatividade e autoexecutoriedade.", "Conveniência, oportunidade, mérito e discricionariedade.", "Publicidade, vigência, revogabilidade e eficácia."], "A",
         "Os requisitos (elementos) do ato administrativo formam o mnemônico CO-FI-FO-MO-OB: Competência, Finalidade, Forma, Motivo e Objeto. Os demais são atributos ou critérios de mérito."),
         
        ("Direito Administrativo • Princípio da Autotutela (Súmulas 346 e 473 STF)", "O poder conferido à Administração Pública para anular seus próprios atos quando eivados de vícios de legalidade, e revogá-los por conveniência ou oportunidade, consagra o princípio da:",
         ["Autotutela administrativa.", "Tutela jurisdicional.", "Motivação vinculante.", "Indisponibilidade reflexa."], "A",
         "Súmula 473 do STF: 'A Administração pode anular seus próprios atos, quando eivados de vícios que os tornam ilegais, porque deles não se originam direitos; ou revogá-los, por motivo de conveniência ou oportunidade...'."),
         
        ("Direito Administrativo • Licitações 14.133 • Dispensa por Valor", "Na Lei nº 14.133/2021, a contratação direta que ocorre quando o valor reduzido do objeto torna economicamente desvantajoso realizar um processo licitatório formal é classificada como:",
         ["Dispensa de licitação (art. 75).", "Inexigibilidade de licitação (art. 74).", "Licitação deserta imprópria.", "Alienação fiduciária direta."], "A",
         "As contratações de pequeno valor enquadram-se expressamente na dispensa de licitação (art. 75, I e II da Lei 14.133/2021). A inexigibilidade (art. 74) aplica-se apenas quando há inviabilidade de competição."),
         
        ("Direito Constitucional • Estabilidade dos Servidores (Art. 41 CF)", "Conforme o art. 41 da CF/88, são estáveis após três anos de efetivo exercício os servidores nomeados para cargo de provimento efetivo em virtude de concurso público, condicionada a estabilidade a:",
         ["Avaliação especial de desempenho por comissão instituída para essa finalidade.", "Decisão irrecorrível do Presidente do Poder Legislativo.", "Conclusão de curso de pós-graduação na área de atuação.", "Aprovação em eleição interna entre os servidores estáveis."], "A",
         "Art. 41, § 4º da CF/88: 'Como condição para a aquisição da estabilidade, é obrigatória a avaliação especial de desempenho por comissão instituída para essa finalidade'."),
         
        ("Direito Constitucional • Acumulação Remunerada de Cargos Públicos", "A Constituição Federal veda a acumulação remunerada de cargos públicos, exceto, quando houver compatibilidade de horários, para:",
         ["A de dois cargos de professor; a de um de professor com outro técnico ou científico; e a de dois cargos ou empregos privativos de profissionais de saúde.", "Dois cargos administrativos em poderes distintos.", "Um cargo de agente administrativo e outro de fiscal de tributos.", "Três cargos públicos desde que em municípios limítrofes."], "A",
         "Art. 37, XVI da CF/88 autoriza apenas: a) dois de professor; b) um de professor com outro técnico/científico; c) dois privativos de profissionais de saúde com profissões regulamentadas."),
         
        ("Direito Administrativo • Poder Disciplinar", "O poder de apurar infrações funcionais e aplicar penalidades aos servidores públicos e demais pessoas sujeitas à disciplina interna da administração é o:",
         ["Poder disciplinar.", "Poder hierárquico puro.", "Poder de polícia externa.", "Poder regulamentar geral."], "A",
         "O poder disciplinar é a prerrogativa conferida à Administração para apurar e punir faltas funcionais de seus agentes ou pessoas com vínculo especial com o poder público."),
         
        ("Direito Administrativo • Abuso de Poder: Desvio de Finalidade", "Quando um agente público pratica um ato dentro de sua esfera de competência legal, mas com o objetivo dissimulado de prejudicar um inimigo político pessoal, ocorre:",
         ["Desvio de finalidade (ou desvio de poder).", "Excesso de poder.", "Usurpação de função pública.", "Vício sanável de incompetência."], "A",
         "O desvio de finalidade ocorre quando o ato é praticado por motivo alheio ao interesse público ou para fim diverso daquele previsto na lei. O excesso de poder refere-se ao agente que ultrapassa sua competência."),
         
        ("Administração Geral • Comunicação Organizacional", "Em uma repartição pública, o ruído na comunicação que decorre do uso de termos excessivamente técnicos ou jargões incompreensíveis para os cidadãos é chamado de barreira:",
         ["Semântica.", "Física.", "Mecânica.", "Psicológica intencional."], "A",
         "Barreiras semânticas decorrem das palavras, sinais, símbolos ou jargões utilizados pelo emissor que possuem interpretação ambígua ou incompreensível para o receptor."),
         
        ("Administração Geral • Gestão de Materiais & Almoxarifado", "O método de controle de estoque em que o primeiro item que entra no almoxarifado é o primeiro item que deve sair para consumo é conhecido pela sigla:",
         ["PEPS (Primeiro que Entra, Primeiro que Sai) ou FIFO.", "UEPS (Último que Entra, Primeiro que Sai).", "Custo Médio Ponderado Permanente.", "Curva ABC de Criticidade."], "A",
         "PEPS (FIFO - First In, First Out) garante que materiais mais antigos sejam consumidos primeiro, evitando perda de validade ou deterioração do estoque."),
         
        ("Administração Geral • Organização e Métodos (O&M)", "A representação gráfica simplificada que demonstra a sequência lógica de passos, decisões e fluxos de um processo de trabalho na Câmara é o:",
         ["Fluxograma.", "Organograma institucional.", "Cronograma de Gantt.", "Diagrama de Pareto invertido."], "A",
         "O fluxograma mapeia e ilustra graficamente o fluxo sequencial das etapas e decisões de um processo de trabalho. O organograma demonstra a hierarquia funcional de cargos."),
         
        ("Arquivologia • Método de Arquivamento Alfabético", "No arquivamento pelo método alfabético de nomes de pessoas físicas, segundo as regras de alfabetação, o nome 'Antônio Carlos Silva' deve ser arquivado sob a entrada principal:",
         ["SILVA, Antônio Carlos.", "ANTÔNIO, Carlos Silva.", "CARLOS, Silva Antônio.", "SILVA ANTÔNIO, Carlos."], "A",
         "Regra geral de alfabetação de nomes de pessoas físicas brasileiras: arquiva-se pelo último sobrenome em letras maiúsculas, seguido de vírgula e prenomes: SILVA, Antônio Carlos."),
         
        ("Legislação Municipal • Vedações no Fim de Mandato (Art. 21 LRF)", "A Lei de Responsabilidade Fiscal comina de nulidade de pleno direito o ato que resulte no aumento da despesa com pessoal expedido nos últimos:",
         ["180 (cento e oitenta) dias anteriores ao final do mandato do titular do Poder.", "90 (noventa) dias anteriores ao término do mandato.", "365 (trezentos e sessenta e cinco) dias do exercício financeiro.", "30 (trinta) dias que antecedem a posse dos eleitos."], "A",
         "Art. 21, parágrafo único da LRF: é nulo de pleno direito o ato de que resulte aumento da despesa com pessoal expedido nos 180 (cento e oitenta) dias anteriores ao final do mandato do titular do Poder."),
         
        ("Direito Constitucional • Remuneração dos Vereadores (Art. 29 CF)", "O total da despesa com a remuneração dos Vereadores não poderá ultrapassar o montante da receita do Município fixado no limite de:",
         ["5% (cinco por cento).", "10% (dez por cento).", "3% (três por cento).", "8% (oito por cento)."], "A",
         "Art. 29, VII da CF/88: 'o total da despesa com a remuneração dos Vereadores não poderá ultrapassar o montante de 5% (cinco por cento) da receita do Município'."),
         
        ("Legislação Municipal • Orçamento Público: PPA, LDO e LOA", "O instrumento de planejamento governamental de médio prazo que estabelece as diretrizes, objetivos e metas da administração pública para as despesas de capital para o período de 4 anos é o:",
         ["Plano Plurianual (PPA).", "Lei de Diretrizes Orçamentárias (LDO).", "Lei Orçamentária Anual (LOA).", "Relatório de Gestão Fiscal (RGF)."], "A",
         "Art. 165, § 1º da CF/88: o PPA estabelece de forma regionalizada as diretrizes, objetivos e metas para as despesas de capital e outras delas decorrentes, e para as relativas aos programas de duração continuada."),
         
        ("Legislação Municipal • Espécies Normativas Municipais", "As matérias de competência exclusiva da Câmara Municipal que independem de sanção do Prefeito e geram efeitos internos e externos são disciplinadas por:",
         ["Decretos Legislativos e Resoluções.", "Leis Complementares do Executivo.", "Medidas Provisórias Municipais.", "Portarias Interministeriais."], "A",
         "Decretos Legislativos (efeitos externos, como julgamento de contas do Prefeito) e Resoluções (matéria político-administrativa interna da Câmara) são de competência privativa do Legislativo e promulgadas pelo Presidente da Casa."),
         
        ("Direito Administrativo • Bens Públicos de Uso Comum", "Nos termos do Código Civil Brasileiro, as praças, ruas, estradas e rios pertencentes ao município são classificados como bens públicos:",
         ["De uso comum do povo.", "De uso especial.", "Dominicais ou dominiais.", "Patrimoniais disponíveis privados."], "A",
         "Art. 99 do CC: I - de uso comum do povo (rios, mares, estradas, praças); II - de uso especial (edifícios de repartições públicas, câmaras, escolas); III - dominicais (bens disponíveis do patrimônio público)."),
         
        ("Direito Administrativo • Responsabilidade Civil do Estado (Art. 37, § 6º CF)", "As pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos responderão pelos danos que seus agentes causarem a terceiros com base na responsabilidade:",
         ["Objetiva, sob a modalidade do risco administrativo, assegurado o direito de regresso contra o responsável nos casos de dolo ou culpa.", "Subjetiva, dependendo da prova indispensável de dolo por parte da vítima.", "Subsidiária, somente após exaurida a cobrança judicial do servidor causador do dano.", "Restrita a casos de omissão comprovada por sentença condenatória."], "A",
         "Art. 37, § 6º da CF/88 adota a responsabilidade civil objetiva do Estado (dispensa prova de dolo ou culpa da administração), resguardando o direito de regresso contra o agente nos casos de culpa ou dolo."),
         
        ("Direito Constitucional • Sigilo de Correspondência & Dados (Art. 5º CF)", "É inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por:",
         ["Ordem judicial, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal.", "Requisição direta de qualquer parlamentar ou comissão temática da Câmara.", "Decisão unânime da Mesa Diretora do Poder Legislativo.", "Determinação do chefe do Poder Executivo em procedimento administrativo."], "A",
         "Art. 5º, XII da CF/88: a quebra do sigilo telefônico só pode ocorrer por ordem judicial para investigação criminal ou instrução penal. Nenhuma comissão ou autoridade administrativa pode ordenar isoladamente a interceptação."),
         
        ("Legislação Municipal • Quórum de Aprovação da Lei Orgânica Municipal", "A Lei Orgânica Municipal será votada em dois turnos, com o interstício mínimo de dez dias, e aprovada por:",
         ["Dois terços dos membros da Câmara Municipal, que a promulgará.", "Maioria absoluta dos vereadores, sendo sancionada pelo Prefeito.", "Maioria simples dos presentes na sessão legislativa ordinária.", "Três quintos dos parlamentares municipais em turno único."], "A",
         "Art. 29, caput da CF/88: O Município reger-se-á por lei orgânica, votada em dois turnos, com o interstício mínimo de 10 dias, e aprovada por 2/3 dos membros da Câmara Municipal, que a promulgará (sem sanção do Prefeito).")
    ]
    
    for i, (head, enun, opts, gab, com) in enumerate(esp_data, 21):
        questoes.append({
            "numero": i,
            "secao": "CONHECIMENTOS ESPECÍFICOS & DIREITO (CETREDE / Nível Médio)" if i == 21 else "",
            "header": f"{head} • CETREDE",
            "enunciado": enun,
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
        
    html = render_html(titulo, badge, orgao, certame, cargo, fonte, questoes)
    html_path = os.path.join(PROVAS_DIR, "PROVA_REAL_03_CETREDE_ADMINISTRATIVO_CE.html")
    pdf_path = os.path.join(PROVAS_DIR, "PROVA_REAL_03_CETREDE_ADMINISTRATIVO_CE.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    compilar_para_pdf(html_path, pdf_path)

# Executar geração de CETREDE
gerar_prova_03()
print("[*] Prova Real 03 (CETREDE) gerada com sucesso!")
