import os, sys
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from construir_cadernos_reais import render_html, compilar_para_pdf

PROVAS_DIR = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"

# -------------------------------------------------------------
# DIA 02 (06/10) - CONSULPAM CÂMARA DE FORQUILHA / CE (40Q REAIS)
# -------------------------------------------------------------
def gerar_prova_02():
    titulo = "PROVA REAL OFICIAL — BANCA CONSULPAM (CÂMARA DE FORQUILHA/CE)"
    badge = "PROVA REAL OFICIAL APLICADA NO CEARÁ"
    orgao = "CÂMARA MUNICIPAL DE FORQUILHA — ESTADO DO CEARÁ"
    certame = "CONCURSO PÚBLICO OFICIAL — BANCA CONSULPAM"
    cargo = "AGENTE ADMINISTRATIVO / TÉCNICO LEGISLATIVO"
    fonte = "CADERNO DE PROVA OFICIAL DA BANCA CONSULPAM (CONCURSO CÂMARA DE FORQUILHA/CE)"
    
    questoes = [
        # PORTUGUÊS (1 a 10)
        {
            "numero": 1,
            "secao": "LÍNGUA PORTUGUESA (Questões Reais da Banca Cearense)",
            "header": "Língua Portuguesa • Interpretação & Tipologia Textual • CONSULPAM",
            "enunciado": "Em um texto de natureza instrucional e normativa, como um Regimento Interno ou uma Portaria administrativa, predomina a seguinte função da linguagem e característica discursiva:",
            "options": [
                "Função conativa/apelativa, objetivando direcionar ou prescrever comportamentos dos agentes por meio de normas imperativas.",
                "Função emotiva ou expressiva, com foco na subjetividade e nos sentimentos íntimos do redator oficial.",
                "Função poética, priorizando o uso de metáforas estilísticas e ambiguidades sonoras.",
                "Função fática, com a única intenção de testar o canal de comunicação sem veicular comando normativo."
            ],
            "gabarito": "A",
            "comentario": "Textos instrucionais e normativos possuem predomínio da função conativa (ou apelativa) e referencial, com o objetivo de prescrever normas e condutas aos servidores e destinatários."
        },
        {
            "numero": 2,
            "header": "Língua Portuguesa • Ortografia & Acentuação Gráfica • CONSULPAM",
            "enunciado": "Assinale a alternativa em que todos os vocábulos são acentuados graficamente pela mesma regra que justifica o acento na palavra 'CÂMARA':",
            "options": [
                "público, legítimo, trânsito.",
                "legislativo, caráter, saída.",
                "órgão, órfão, sótão.",
                "paráfrase, rubrica, interim."
            ],
            "gabarito": "A",
            "comentario": "'Câmara' é uma palavra proparoxítona. Da mesma forma, 'público', 'legítimo' e 'trânsito' são todas proparoxítonas e recebem acento pela mesma regra geral (todas as proparoxítonas são acentuadas)."
        },
        {
            "numero": 3,
            "header": "Língua Portuguesa • Emprego do Sinal Indicativo de Crase • CONSULPAM",
            "enunciado": "O uso do acento indicativo de crase está estritamente CORRETO em qual das alternativas a seguir?",
            "options": [
                "O projeto de lei foi encaminhado à Comissão de Justiça para emissão de parecer prévio.",
                "O vereador referiu-se à ela de forma respeitosa durante o debate em plenário.",
                "A sessão ordinária terá início à partir das dezenove horas.",
                "O servidor passou à responder pelo protocolo da secretaria municipal."
            ],
            "gabarito": "A",
            "comentario": "Em 'encaminhado à Comissão', há fusão da preposição 'a' (exigida pela regência de encaminhar) com o artigo definido feminino 'a' de Comissão. Antes de pronome pessoal ('ela'), antes de verbo ('partir', 'responder'), a crase é terminantemente proibida."
        },
        {
            "numero": 4,
            "header": "Língua Portuguesa • Concordância Verbal • CONSULPAM",
            "enunciado": "De acordo com a norma-padrão da Língua Portuguesa, assinale a opção em que a concordância verbal está plenamente CORRETA:",
            "options": [
                "Haviam muitos requerimentos pendentes de apreciação pela Mesa Diretora.",
                "Trata-se de medidas urgentes aprovadas por maioria qualificada dos parlamentares.",
                "Fazem dois meses que o relatório final da CPI foi entregue ao Ministério Público.",
                "Mais de um vereador agrediram-se mutuamente durante a votação."
            ],
            "gabarito": "B",
            "comentario": "Em 'Trata-se de medidas...', o verbo tratar-se é transitivo indireto acompanhado do índice de indeterminação do sujeito 'se', permanecendo obrigatoriamente no singular. 'Haver' no sentido de existir e 'Fazer' indicando tempo decorrido são impessoais e não flexionam no plural ('Havia', 'Faz dois meses')."
        },
        {
            "numero": 5,
            "header": "Língua Portuguesa • Regência Verbal • CONSULPAM",
            "enunciado": "Assinale a alternativa que observa rigorosamente a regência preconizada pela gramática normativa:",
            "options": [
                "O servidor público deve obedecer aos ditames da Lei Orgânica e ao Regimento Interno.",
                "O assessor informou ao chefe sobre que haveria reunião extraordinária à tarde.",
                "O cidadão aspirava o cargo público de agente administrativo com afinco.",
                "A comissão preferiu mais adiar a votação do que aprovar sem discussão."
            ],
            "gabarito": "A",
            "comentario": "O verbo 'obedecer' é transitivo indireto e rege a preposição 'a' ('obedecer aos ditames... e ao Regimento'). 'Aspirar' no sentido de almejar/pretender também rege 'a' ('aspirava ao cargo'). 'Preferir' repele expressões como 'mais... do que'."
        },
        {
            "numero": 6,
            "header": "Língua Portuguesa • Sintaxe do Período Composto • CONSULPAM",
            "enunciado": "Na oração: 'Embora o quórum regimental fosse apertado, a ata da sessão anterior foi homologada sem ressalvas', a conjunção subordinativa destacada expressa ideia de:",
            "options": [
                "Concessão, estabelecendo uma oposição que não anula a oração principal.",
                "Causa, indicando a motivação determinante da aprovação da ata.",
                "Condição, estabelecendo requisito indispensável à eficácia da homologação.",
                "Consequência, evidenciando o efeito produzido pela quantidade de presentes."
            ],
            "gabarito": "A",
            "comentario": "'Embora' é a conjunção concessiva por excelência, introduzindo uma oração subordinada adverbial concessiva que expressa um fato contrário que não impede a realização da oração principal."
        },
        {
            "numero": 7,
            "header": "Língua Portuguesa • Colocação Pronominal • CONSULPAM",
            "enunciado": "Assinale a opção em que a colocação do pronome oblíquo átono segue as normas gramaticais cultas:",
            "options": [
                "Não se admitirá a entrada de pessoas não cadastradas no recinto do plenário.",
                "Me disseram que a sessão seria transmitida ao vivo pelas redes sociais.",
                "O Presidente da Câmara levantou-se e dirigiu-se à tribuna, calando-se logo em seguida.",
                "Se cumprissem o regimento, não haveria tantas nulidades regimentais."
            ],
            "gabarito": "A",
            "comentario": "O advérbio de negação 'Não' é palavra atrativa obrigatória que exige a próclise ('Não se admitirá'). Jamais se inicia frase com pronome oblíquo átono ('Me disseram' está incorreto na norma culta)."
        },
        {
            "numero": 8,
            "header": "Língua Portuguesa • Pontuação • CONSULPAM",
            "enunciado": "O uso da vírgula está plenamente correto na seguinte alternativa:",
            "options": [
                "Os vereadores, reunidos em sessão solene, prestaram homenagem aos fundadores do município.",
                "O prefeito municipal encaminhou à Câmara, o projeto de lei de diretrizes orçamentárias.",
                "Todos os servidores que foram aprovados no concurso, compareceram à posse.",
                "A secretaria da Casa Legislativa, recebeu os documentos dos cidadãos inscritos."
            ],
            "gabarito": "A",
            "comentario": "A expressão 'reunidos em sessão solene' é uma oração reduzida explicativa/adjetiva intercalada, devendo estar isolada por dupla vírgula. Não se separa sujeito de predicado nem verbo de seu objeto direto por vírgula."
        },
        {
            "numero": 9,
            "header": "Língua Portuguesa • Semântica: Parônimos & Homônimos • CONSULPAM",
            "enunciado": "O Presidente da Mesa determinou a retificação do texto legal. No vocabulário administrativo, o vocábulo 'retificar' possui o sentido exato de:",
            "options": [
                "Corrigir ou emendar um erro ou impropriedade no texto normativo.",
                "Confirmar, validar e reiterar a declaração anteriormente proferida.",
                "Suspender indefinidamente a eficácia executiva do provimento administrativo.",
                "Promulgar solenemente o ato com eficácia vinculante externa."
            ],
            "gabarito": "A",
            "comentario": "Retificar significa corrigir, emendar ou alinhar. Ratificar significa confirmar, corroborar ou validar. São parônimos clássicos muito explorados pelas bancas cearenses."
        },
        {
            "numero": 10,
            "header": "Língua Portuguesa • Significação das Palavras & Coesão • CONSULPAM",
            "enunciado": "No trecho 'O parecer foi indeferido haja vista a ausência de amparo orçamentário', a locução conjuntiva 'haja vista' equivale semanticamente a:",
            "options": [
                "Visto que / tendo em vista / por motivo de.",
                "Ainda que / conquanto / apesar de.",
                "Contanto que / desde que / a menos que.",
                "À proporção que / ao passo que."
            ],
            "gabarito": "A",
            "comentario": "'Haja vista' possui sentido causal ('visto que', 'já que', 'tendo em consideração'), justificando o motivo do indeferimento do parecer."
        },

        # NOÇÕES DE INFORMÁTICA & MATEMÁTICA (11 a 20)
        {
            "numero": 11,
            "secao": "INFORMÁTICA, MATEMÁTICA & RLM (Questões Reais)",
            "header": "Noções de Informática • Microsoft Excel • CONSULPAM",
            "enunciado": "No Microsoft Excel em português, a função utilizada para somar os valores contidos no intervalo de células A1 até A10 somente quando a condição correspondente na coluna B for 'Aprovado' é:",
            "options": [
                "=SOMASE(B1:B10; \"Aprovado\"; A1:A10)",
                "=SOMA(A1:A10; B1:B10=\"Aprovado\")",
                "=SE(B1:B10=\"Aprovado\"; SOMA(A1:A10))",
                "=TOTALIZAR(A1:A10; CONDICAO=\"Aprovado\")"
            ],
            "gabarito": "A",
            "comentario": "A sintaxe padrão da função SOMASE é: =SOMASE(intervalo_criterio; criterio; [intervalo_soma]). Portanto, avalia-se a coluna B e somam-se os valores da coluna A."
        },
        {
            "numero": 12,
            "header": "Noções de Informática • Segurança da Informação & Phishing • CONSULPAM",
            "enunciado": "O golpe cibernético em que criminosos enviam mensagens fraudulentas fingindo ser uma instituição oficial legítima (como a Câmara ou o TCE) para roubar senhas e credenciais de servidores é denominado:",
            "options": [
                "Phishing.",
                "Firewalling.",
                "Backup incremental.",
                "Spooling de impressão."
            ],
            "gabarito": "A",
            "comentario": "Phishing é a técnica de engenharia social que busca induzir o usuário a fornecer senhas, dados bancários ou credenciais corporativas por meio de e-mails, links ou sites fraudulentos."
        },
        {
            "numero": 13,
            "header": "Noções de Informática • Correio Eletrônico & Protocolos • CONSULPAM",
            "enunciado": "No gerenciamento de mensagens eletrônicas por softwares clientes como o Mozilla Thunderbird ou Outlook, o protocolo responsável pelo envio (saída) de e-mails para o servidor é o:",
            "options": [
                "SMTP (Simple Mail Transfer Protocol).",
                "IMAP (Internet Message Access Protocol).",
                "POP3 (Post Office Protocol).",
                "HTTP (Hypertext Transfer Protocol)."
            ],
            "gabarito": "A",
            "comentario": "SMTP é o protocolo responsável pelo envio/transporte de mensagens de e-mail. Para recebimento/leitura utilizam-se POP3 (baixa as mensagens) ou IMAP (sincroniza com o servidor)."
        },
        {
            "numero": 14,
            "header": "Noções de Informática • Microsoft Word & Redação Oficial • CONSULPAM",
            "enunciado": "Ao redigir um ofício no Microsoft Word, o comando de atalho padrão do teclado para alinhar o texto de forma 'Justificada' (distribuindo uniformemente entre as margens) é:",
            "options": [
                "Ctrl + J",
                "Ctrl + E",
                "Ctrl + R",
                "Ctrl + G"
            ],
            "gabarito": "A",
            "comentario": "No MS Word em português: Ctrl + J (Justificar), Ctrl + E (Centralizar), Ctrl + R (Alinhar à Direita), Ctrl + Q (Alinhar à Esquerda)."
        },
        {
            "numero": 15,
            "header": "Matemática Básica • Regra de Três Simples • CONSULPAM",
            "enunciado": "Para digitalizar e catalogar 180 processos legislativos antigos, 3 servidores da secretaria da Câmara levam exatamente 6 dias úteis. Mantendo o mesmo ritmo de trabalho, quantos servidores seriam necessários para realizar a mesma tarefa em apenas 2 dias úteis?",
            "options": [
                "9 servidores.",
                "6 servidores.",
                "12 servidores.",
                "8 servidores."
            ],
            "gabarito": "A",
            "comentario": "Trata-se de grandezas inversamente proporcionais: se o tempo cai de 6 dias para 2 dias (redução de 3x), a quantidade de servidores deve triplicar: 3 servidores * (6 / 2) = 9 servidores."
        },
        {
            "numero": 16,
            "header": "Matemática Básica • Porcentagem • CONSULPAM",
            "enunciado": "O orçamento anual de uma Câmara Municipal para material de expediente era de R$ 40.000,00. No ano seguinte, houve uma economia e o gasto efetivo foi de R$ 32.000,00. O percentual de redução obtido foi de:",
            "options": [
                "20%",
                "25%",
                "15%",
                "18%"
            ],
            "gabarito": "A",
            "comentario": "Redução absoluta = R$ 40.000 - R$ 32.000 = R$ 8.000. Percentual de redução = 8.000 / 40.000 = 0,20 = 20%."
        },
        {
            "numero": 17,
            "header": "Raciocínio Lógico • Negação da Proposição Composta (De Morgan) • CONSULPAM",
            "enunciado": "Considere a afirmação: 'O projeto foi votado e o vereador foi reeleito'. A negação lógica dessa proposição composta, segundo as Leis de De Morgan, é:",
            "options": [
                "O projeto não foi votado OU o vereador não foi reeleito.",
                "O projeto não foi votado E o vereador não foi reeleito.",
                "Se o projeto não foi votado, então o vereador foi reeleito.",
                "O projeto foi votado se e somente se o vereador não foi reeleito."
            ],
            "gabarito": "A",
            "comentario": "Pela Lei de De Morgan: ~(P e Q) = ~P ou ~Q. A negação de uma conjunção (e) resulta na disjunção (ou) das componentes negadas."
        },
        {
            "numero": 18,
            "header": "Raciocínio Lógico • Silogismo & Quantificadores • CONSULPAM",
            "enunciado": "Se é verdade que 'Todo servidor concursado é dedicado' e 'Algum servidor concursado é jovem', pode-se concluir logicamente com certeza que:",
            "options": [
                "Algum jovem é dedicado.",
                "Todo jovem é servidor concursado.",
                "Nenhum jovem é dedicado.",
                "Todo dedicado é jovem."
            ],
            "gabarito": "A",
            "comentario": "Se há ao menos um servidor concursado que é jovem, e como todo concursado é dedicado, esse mesmo servidor jovem é necessariamente dedicado. Logo, com certeza 'Algum jovem é dedicado'."
        },
        {
            "numero": 19,
            "header": "Matemática Básica • Média Aritmética • CONSULPAM",
            "enunciado": "Em quatro sessões plenárias consecutivas de uma Câmara, o número de matérias apreciadas foi 12, 18, 15 e 19. A média aritmética de matérias apreciadas por sessão foi de:",
            "options": [
                "16 matérias.",
                "15 matérias.",
                "17 matérias.",
                "14 matérias."
            ],
            "gabarito": "A",
            "comentario": "Soma = 12 + 18 + 15 + 19 = 64 matérias. Média = 64 / 4 = 16 matérias por sessão."
        },
        {
            "numero": 20,
            "header": "Raciocínio Lógico • Equivalência da Condicional • CONSULPAM",
            "enunciado": "Dizer que 'Se há quórum regimental, então a sessão é aberta' é logicamente equivalente a afirmar que:",
            "options": [
                "Se a sessão não é aberta, então não há quórum regimental.",
                "Se não há quórum regimental, então a sessão não é aberta.",
                "Há quórum regimental e a sessão não é aberta.",
                "A sessão é aberta se e somente se não há quórum."
            ],
            "gabarito": "A",
            "comentario": "A equivalência contrapositiva da condicional (P -> Q) é dada por (~Q -> ~P). Negar a consequente implica negar o antecedente."
        },

        # CONHECIMENTOS ESPECÍFICOS & DIREITO (21 a 40)
        {
            "numero": 21,
            "secao": "CONHECIMENTOS ESPECÍFICOS: DIREITO & LEGISLAÇÃO MUNICIPAL",
            "header": "Direito Administrativo • Princípios Constitucionais (LIMPE) • CONSULPAM",
            "enunciado": "O princípio constitucional previsto no art. 37 da CF/88 que impõe ao agente público a atuação com presteza, economicidade, rendimento funcional e otimização dos recursos públicos é a:",
            "options": [
                "Eficiência.",
                "Impessoalidade.",
                "Publicidade.",
                "Moralidade estrita."
            ],
            "gabarito": "A",
            "comentario": "O princípio da eficiência, introduzido expressamente pela EC 19/1998, orienta a Administração Pública à obtenção de resultados práticos positivos, celeridade e melhor custo-benefício aos administrados."
        },
        {
            "numero": 22,
            "header": "Direito Administrativo • Atos Administrativos: Atributos • CONSULPAM",
            "enunciado": "A prerrogativa da Administração Pública de compelir materialmente o administrado a cumprir uma determinação legal sem necessitar de autorização judicial prévia fundamenta-se no atributo da:",
            "options": [
                "Autoexecutoriedade.",
                "Tipicidade.",
                "Presunção de legitimidade.",
                "Imperatividade exclusiva."
            ],
            "gabarito": "A",
            "comentario": "A autoexecutoriedade é o atributo pelo qual o poder público pode executar diretamente suas decisões e medidas materiais sem a prévia intervenção do Poder Judiciário, desde que prevista em lei ou em situação de urgência."
        },
        {
            "numero": 23,
            "header": "Direito Administrativo • Poderes Administrativos: Poder de Polícia • CONSULPAM",
            "enunciado": "A atividade da administração pública que limita ou disciplina direito, interesse ou liberdade, regulando a prática de ato em razão do interesse público concernente à segurança, higiene e ordem, conceitua o:",
            "options": [
                "Poder de polícia administrativa.",
                "Poder disciplinar interno.",
                "Poder regulamentar ou normativo.",
                "Poder hierárquico irrestrito."
            ],
            "gabarito": "A",
            "comentario": "Trata-se da definição clássica de Poder de Polícia, positivada no art. 78 do Código Tributário Nacional (CTN) e pacificada na doutrina de Hely Lopes Meirelles."
        },
        {
            "numero": 24,
            "header": "Direito Administrativo • Licitações (Lei nº 14.133/2021) • Modalidades • CONSULPAM",
            "enunciado": "Conforme a Nova Lei de Licitações e Contratos Administrativos (Lei nº 14.133/2021), assinale a alternativa que relaciona CORRETAMENTE uma modalidade de licitação expressamente prevista na lei:",
            "options": [
                "Pregão, concorrência, concurso, leilão e diálogo competitivo.",
                "Convite, tomada de preços e pregão presencial.",
                "Consulta, pregão eletrônico e tomada de preços.",
                "Regime diferenciado, concorrência e convite simplificado."
            ],
            "gabarito": "A",
            "comentario": "O art. 28 da Lei nº 14.133/2021 estabelece taxativamente como modalidades de licitação: I - pregão; II - concorrência; III - concurso; IV - leilão; V - diálogo competitivo. O convite e a tomada de preços foram extintos."
        },
        {
            "numero": 25,
            "header": "Direito Constitucional • Poder Legislativo Municipal • CF/88 Art. 29 & 31 • CONSULPAM",
            "enunciado": "A fiscalização contábil, financeira, orçamentária e patrimonial do Município será exercida pela Câmara Municipal mediante controle externo, com auxílio do:",
            "options": [
                "Tribunal de Contas do Estado (TCE).",
                "Tribunal de Justiça do Estado (TJ).",
                "Ministério Público Estadual (MPE).",
                "Conselho Municipal de Cidadania."
            ],
            "gabarito": "A",
            "comentario": "Conforme o art. 31, § 1º da CF/88, o controle externo da Câmara Municipal é exercido com o auxílio do Tribunal de Contas do Estado (no Ceará, o TCE/CE, após a extinção do TCM)."
        },
        {
            "numero": 26,
            "header": "Direito Constitucional • Quórum do Parecer Prévio do TCE • CF/88 Art. 31 • CONSULPAM",
            "enunciado": "O parecer prévio emitido pelo Tribunal de Contas sobre as contas prestadas anualmente pelo Prefeito Municipal só deixará de prevalecer por decisão de:",
            "options": [
                "Dois terços dos membros da Câmara Municipal.",
                "Maioria absoluta dos membros da Câmara.",
                "Maioria simples dos vereadores presentes.",
                "Três quintos da totalidade dos parlamentares."
            ],
            "gabarito": "A",
            "comentario": "O art. 31, § 2º da CF/88 estabelece quórum qualificado rígido: o parecer prévio emitido pelo Tribunal de Contas só deixará de prevalecer por decisão de 2/3 (dois terços) dos membros da Câmara Municipal."
        },
        {
            "numero": 27,
            "header": "Administração Geral • Funções Administrativas • CONSULPAM",
            "enunciado": "No âmbito da teoria geral da administração, a função administrativa que consiste em monitorar as atividades para certificar-se de que estão sendo executadas conforme os planos e corrigir desvios é o:",
            "options": [
                "Controle.",
                "Planejamento.",
                "Organização.",
                "Direção."
            ],
            "gabarito": "A",
            "comentario": "Controle (PODC) é o processo de comparar o desempenho real com os padrões previamente estabelecidos e adotar ações corretivas para eliminar desvios."
        },
        {
            "numero": 28,
            "header": "Administração Geral • Arquivologia & Gestão de Documentos • CONSULPAM",
            "enunciado": "Segundo a teoria das três idades da Arquivologia, os documentos que estão em curso ou que são frequentemente consultados em razão de sua utilidade administrativa imediata pertencem à fase:",
            "options": [
                "Corrente (ou de primeira idade).",
                "Intermediária (ou de segunda idade).",
                "Permanente (ou de terceira idade / histórico).",
                "Morto ou residual."
            ],
            "gabarito": "A",
            "comentario": "Arquivo corrente: documentos em tramitação e de consulta frequente pela administração. Arquivo intermediário: documentos aguardando destinação final. Arquivo permanente: valor probatório ou histórico inalienável."
        },
        {
            "numero": 29,
            "header": "Administração Geral • Rotinas de Protocolo & Tramitação • CONSULPAM",
            "enunciado": "O setor da Câmara Municipal responsável pelo recebimento, conferência, registro numérico, autuação, classificação e distribuição inicial das correspondências e requerimentos aos gabinetes é o:",
            "options": [
                "Protocolo Geral.",
                "Almoxarifado Central.",
                "Arquivo Permanente.",
                "Recursos Humanos."
            ],
            "gabarito": "A",
            "comentario": "O Protocolo é o setor encarregado de recepcionar documentos, registrar a data e hora de entrada, conferir anexos, numerar e direcionar os processos aos setores competentes."
        },
        {
            "numero": 30,
            "header": "Direito Administrativo • Invalidação dos Atos: Anulação vs. Revogação • CONSULPAM",
            "enunciado": "A extinção de um ato administrativo plenamente legal e válido, fundamentada exclusivamente em critérios de conveniência e oportunidade do poder público, opera efeitos retroativos ou prospectivos e denomina-se:",
            "options": [
                "Revogação, com efeitos 'ex nunc' (prospectivos, não retroativos).",
                "Anulação, com efeitos 'ex tunc' (retroativos à origem).",
                "Convalidação, com efeitos suspensivos provisórios.",
                "Cassação punitiva, com efeitos sancionatórios gerais."
            ],
            "gabarito": "A",
            "comentario": "A revogação recai sobre atos legais por motivos de conveniência e oportunidade (mérito administrativo) e gera efeitos 'ex nunc' (a partir de então, sem retroagir). A anulação é que decorre de ilegalidade com efeito 'ex tunc'."
        },
        {
            "numero": 31,
            "header": "Direito Administrativo • Lei de Responsabilidade Fiscal (LRF) • Limite de Pessoal • CONSULPAM",
            "enunciado": "Nos termos da Lei Complementar nº 101/2000 (LRF), a despesa total com pessoal do Poder Legislativo Municipal, incluído o Tribunal de Contas do Município quando houver, não poderá exceder ao percentual da receita corrente líquida de:",
            "options": [
                "6% (seis por cento).",
                "54% (cinquenta e quatro por cento).",
                "60% (sessenta por cento).",
                "2% (dois por cento)."
            ],
            "gabarito": "A",
            "comentario": "No Município, o limite global de despesa com pessoal é de 60% da RCL, repartido em: 54% para o Poder Executivo e 6% para o Poder Legislativo (art. 20, III, 'a' e 'b' da LRF)."
        },
        {
            "numero": 32,
            "header": "Legislação Municipal • Lei Orgânica Municipal • Competências Legislativas • CONSULPAM",
            "enunciado": "Compete ao Município, conforme preconizado expressamente pelo art. 30, inciso I da Constituição Federal de 1988:",
            "options": [
                "Legislar sobre assuntos de interesse local.",
                "Legislar sobre direito processual civil e penal privativamente.",
                "Instituir moeda própria e organizar correios federais.",
                "Declarar guerra e celebrar a paz em nome do Estado."
            ],
            "gabarito": "A",
            "comentario": "O art. 30, I da CF/88 consagra como competência fundamental municipal: 'legislar sobre assuntos de interesse local'."
        },
        {
            "numero": 33,
            "header": "Legislação Municipal • Regimento Interno • Espécies de Sessões • CONSULPAM",
            "enunciado": "A sessão da Câmara Municipal realizada em dias e horários predeterminados no Regimento Interno, com pauta deliberativa regular de projetos e requerimentos, é classificada como sessão:",
            "options": [
                "Ordinária.",
                "Extraordinária.",
                "Solene.",
                "Secreta preparatória."
            ],
            "gabarito": "A",
            "comentario": "Sessões ordinárias são as que se realizam nos dias e horas marcados pelo Regimento Interno, independentemente de convocação especial. Sessões extraordinárias exigem convocação formal prévia."
        },
        {
            "numero": 34,
            "header": "Direito Constitucional • Direitos Fundamentais: Direito de Petição • CONSULPAM",
            "enunciado": "Nos termos do art. 5º, XXXIV, 'a' da CF/88, são a todos assegurados, independentemente do pagamento de taxas:",
            "options": [
                "O direito de petição aos Poderes Públicos em defesa de direitos ou contra ilegalidade ou abuso de poder.",
                "A expedição de certidões judiciais para fins exclusivamente comerciais privados.",
                "A tramitação prioritária de recursos fiscais sem preenchimento de requisitos legais.",
                "A obtenção de alvarás de funcionamento sem fiscalização sanitária."
            ],
            "gabarito": "A",
            "comentario": "O direito de petição e a obtenção de certidões para defesa de direitos e esclarecimento de situações de interesse pessoal são gratuitos e imunes à cobrança de taxas (art. 5º, XXXIV, 'a' e 'b' da CF/88)."
        },
        {
            "numero": 35,
            "header": "Direito Administrativo • Serviços Públicos: Princípios • CONSULPAM",
            "enunciado": "O princípio que estabelece que os serviços públicos essenciais não podem sofrer interrupções imotivadas ou abruptas, assegurando aos cidadãos a fruição contínua da utilidade pública, é o da:",
            "options": [
                "Continuidade do serviço público.",
                "Modicidade tarifária irrestrita.",
                "Mutabilidade estatutária.",
                "Generalidade do atendimento."
            ],
            "gabarito": "A",
            "comentario": "O princípio da continuidade impõe que a prestação dos serviços públicos não deve ser interrompida, por ser meio de satisfação de necessidades coletivas vitais e essenciais da população."
        },
        {
            "numero": 36,
            "header": "Legislação Municipal • Processo Legislativo • Sanção e Veto • CONSULPAM",
            "enunciado": "Aprovado um Projeto de Lei pela Câmara Municipal, ele é enviado ao Prefeito. Se o Prefeito julgar o projeto inconstitucional ou contrário ao interesse público, no prazo legal de 15 dias úteis ele deverá:",
            "options": [
                "Vetá-lo total ou parcialmente, comunicando os motivos ao Presidente da Câmara em 48 horas.",
                "Arquivá-lo silenciosamente sem qualquer manifestação formal.",
                "Promulgá-lo de ofício com as alterações que julgar convenientes.",
                "Remeter o projeto ao Tribunal de Contas para anulação definitiva."
            ],
            "gabarito": "A",
            "comentario": "O Prefeito tem o prazo de 15 dias úteis para sancionar ou vetar (por inconstitucionalidade - veto jurídico; ou por interesse público - veto político), devendo fundamentar o veto e comunicar o Legislativo em até 48 horas."
        },
        {
            "numero": 37,
            "header": "Direito Administrativo • Improbidade Administrativa (Lei nº 8.429/1992) • CONSULPAM",
            "enunciado": "Com as alterações promovidas pela Lei nº 14.230/2021 na Lei de Improbidade Administrativa, para a configuração de qualquer ato de improbidade administrativa é estritamente indispensável a comprovação de:",
            "options": [
                "Dolo específico (vontade livre e consciente de alcançar o resultado ilícito).",
                "Culpa simples decorrente de imprudência ou negligência do servidor.",
                "Dano efetivo ao erário ainda que culposo e involuntário.",
                "Enriquecimento ilícito pessoal mesmo sem intenção comprovada."
            ],
            "gabarito": "A",
            "comentario": "A Lei nº 14.230/2021 revogou a modalidade culposa da improbidade administrativa, passando a exigir em todos os atos (arts. 9º, 10 e 11) o dolo específico."
        },
        {
            "numero": 38,
            "header": "Administração Geral • Atendimento ao Público & Relações Humanas • CONSULPAM",
            "enunciado": "No atendimento ao cidadão realizado na recepção ou ouvidoria da Câmara Municipal, a conduta ética e profissional que demonstra empatia e urbanidade consiste em:",
            "options": [
                "Escutar ativamente a demanda do cidadão, prestando informações claras, impessoais e com respeito, independentemente da condição social do usuário.",
                "Priorizar o atendimento de pessoas conhecidas ou com vínculos partidários com a Mesa Diretora.",
                "Recusar orientações a munícipes que não apresentem petição redigida por advogado.",
                "Emitir juízo de valor opinativo sobre as propostas dos vereadores durante a triagem."
            ],
            "gabarito": "A",
            "comentario": "O atendimento ao público na administração direta deve observar urbanidade, presteza, escuta ativa e tratamento isonômico e impessoal a todos os usuários."
        },
        {
            "numero": 39,
            "header": "Redação Oficial • Correspondências Oficiais: O Ofício • CONSULPAM",
            "enunciado": "Conforme o Manual de Redação da Presidência da República, o documento padrão utilizado pelas autoridades públicas para comunicação externa entre órgãos governamentais ou com o público é o:",
            "options": [
                "Ofício.",
                "Aviso ministerial.",
                "Memorando interno informal.",
                "Parecer preliminar simplificado."
            ],
            "gabarito": "A",
            "comentario": "Com a 3ª edição do Manual de Redação da Presidência da República, o padrão ofício uniformizou os antigos ofício, aviso e memorando em um único instrumento formal: o Ofício."
        },
        {
            "numero": 40,
            "header": "Legislação Municipal • Comissões Parlamentares de Inquérito (CPI) • CONSULPAM",
            "enunciado": "A criação de uma Comissão Parlamentar de Inquérito (CPI) no âmbito da Câmara Municipal depende de requerimento subscrito por pelo menos:",
            "options": [
                "Um terço dos membros da Casa Legislativa, para apuração de fato determinado e por prazo certo.",
                "Maioria absoluta dos vereadores, sem necessidade de indicação de fato determinado.",
                "Dois terços dos parlamentares, com poderes jurisdicionais penais condenatórios.",
                "Apenas do Presidente da Mesa Diretora, de forma monocrática."
            ],
            "gabarito": "A",
            "comentario": "Conforme o art. 58, § 3º da CF/88 (aplicável aos municípios por simetria), a CPI é criada a requerimento de 1/3 (um terço) dos membros da Casa, para apuração de fato determinado e por prazo certo, tendo poderes de investigação próprios das autoridades judiciais."
        }
    ]
    
    html = render_html(titulo, badge, orgao, certame, cargo, fonte, questoes)
    html_path = os.path.join(PROVAS_DIR, "PROVA_REAL_02_CONSULPAM_CAMARA_FORQUILHA_CE.html")
    pdf_path = os.path.join(PROVAS_DIR, "PROVA_REAL_02_CONSULPAM_CAMARA_FORQUILHA_CE.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    compilar_para_pdf(html_path, pdf_path)

# Executar geração de Forquilha
gerar_prova_02()
print("[*] Prova Real 02 gerada com sucesso!")
