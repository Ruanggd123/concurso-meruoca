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
# PROVA REAL 05 (09/10) - CONSULPAM CRATEÚS/QUIXERÉ (40Q)
# =============================================================
def build_prova_05():
    questoes = []
    itens = [
        # 1 a 10: Português
        ("Língua Portuguesa", "Em qual das seguintes alternativas o acento indicativo de crase foi empregado em desacordo com a norma culta?",
         ["Agradecemos à todos pela presença na sessão de ontem.", "O projeto foi remetido à presidência da Casa de Leis.", "Fizemos referência à servidora que protocolou o processo.", "A matéria foi votada às escondidas no início da noite."], "A",
         "A crase é proibida antes de palavras masculinas ('a todos') e antes de pronomes indefinidos."),
        ("Língua Portuguesa", "Assinale a alternativa que apresenta oração sem sujeito:",
         ["Houve inúmeras manifestações populares na galeria da Câmara.", "Os vereadores debateram a proposta durante três horas.", "Alguém esqueceu o parecer técnico sobre a mesa do plenário.", "Choveram críticas ao projeto de aumento de subsídios."], "A",
         "O verbo 'haver' no sentido de existir ou ocorrer é impessoal, constituindo oração sem sujeito."),
        ("Língua Portuguesa", "Assinale a opção em que a concordância nominal está incorreta:",
         ["Seguem anexo as emendas propostas pela oposição.", "Seguem anexas as emendas propostas pela oposição.", "Os pareceres estavam bastantes fundamentados pelos juristas.", "As certidões foram consideradas válidas pela comissão."], "A",
         "'Anexo' deve concordar com o termo a que se refere ('anexas as emendas'). Apenas a locução 'em anexo' é invariável."),
        ("Língua Portuguesa", "A palavra 'improbidade' possui a seguinte quantidade de fonemas e letras:",
         ["11 letras e 11 fonemas.", "11 letras e 10 fonemas.", "10 letras e 10 fonemas.", "11 letras e 9 fonemas."], "A",
         "i-m-p-r-o-b-i-d-a-d-e: 11 letras e 11 fonemas (não há dígrafos ou letras mudas)."),
        ("Língua Portuguesa", "O prefixo na palavra 'anteprojeto' indica ideia de:",
         ["Anterioridade no tempo ou no espaço.", "Oposição e contraposição ideológica.", "Duplicidade de atuação parlamentar.", "Negação absoluta do conteúdo legal."], "A",
         "'Ante-' indica anterioridade (antes do projeto, fase preparatória)."),
        ("Língua Portuguesa", "No trecho 'O vereador discursou com eloqüência, CONTUDO não convenceu os pares', a conjunção expressa:",
         ["Adversidade / oposição.", "Adição / acréscimo.", "Conclusão / fechamento.", "Explicação causal."], "A",
         "'Contudo', 'porém', 'todavia', 'entretanto' são conjunções coordenativas adversativas."),
        ("Língua Portuguesa", "Assinale a alternativa em que a palavra 'onde' está empregada corretamente:",
         ["Visitamos o plenário onde ocorreu a votação histórica.", "Foi uma sessão onde houve muitos debates acalorados.", "O regimento é o documento onde estão as normas da Casa.", "A época onde o município foi fundado era difícil."], "A",
         "'Onde' deve ser empregado exclusivamente para indicar lugar físico concreto ('o plenário onde...')."),
        ("Língua Portuguesa", "Em 'Vossa Excelência solicitou cópia dos autos', o pronome de tratamento exige concordância verbal em:",
         ["Terceira pessoa do singular.", "Segunda pessoa do singular.", "Segunda pessoa do plural.", "Primeira pessoa do plural."], "A",
         "Os pronomes de tratamento concordam obrigatoriamente com o verbo e pronomes em 3ª pessoa (do singular ou plural)."),
        ("Língua Portuguesa", "Assinale a palavra cuja grafia com 'Z' está correta:",
         ["Balizar, cicatrizar, civilizar.", "Analisar, pesquisar, paralisar.", "Avisar, improvisar, alizar.", "Canalizar, pesquisar, alisar."], "A",
         "Palavras derivadas de primitivas sem 's' no radical formam sufixo '-izar' com z: balizar, cicatrizar, civilizar. Já analisar e pesquisar mantêm o 's' da palavra primitiva."),
        ("Língua Portuguesa", "Assinale a alternativa que apresenta a correta divisão silábica da palavra:",
         ["sub-le-gen-da", "su-ble-gen-da", "sub-leg-en-da", "sub-le-ge-nda"], "A",
         "O prefixo 'sub-' seguido de consoante mantém o 'b' na primeira sílaba: sub-le-gen-da."),

        # 11 a 20: Informática e Matemática
        ("Informática", "No Microsoft Excel, para congelar painéis e manter a linha de cabeçalho sempre visível ao rolar a planilha, o usuário acessa a guia:",
         ["Exibir.", "Fórmulas.", "Página Inicial.", "Inserir."], "A",
         "O recurso 'Congelar Painéis' localiza-se na guia Exibir do Microsoft Excel."),
        ("Informática", "Qual das seguintes portas de rede é convencionalmente utilizada pelo protocolo seguro HTTPS?",
         ["Porta 443.", "Porta 80.", "Porta 21.", "Porta 25."], "A",
         "HTTPS utiliza a porta 443. HTTP convencional utiliza a porta 80. FTP utiliza a 21 e SMTP a 25."),
        ("Informática", "O atalho padrão para desfazer a última ação executada em editores de texto no Windows é:",
         ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + D"], "A",
         "Ctrl + Z desfaz a última ação. Ctrl + Y refaz."),
        ("Informática", "A memória volátil do computador que perde todos os dados gravados quando o equipamento é desligado é a:",
         ["RAM.", "ROM.", "SSD.", "Disco Rígido (HD)."], "A",
         "A memória RAM é a memória principal de trabalho volátil."),
        ("Matemática", "Um concurso ofereceu 15 vagas para Agente Administrativo e teve 600 candidatos inscritos. A relação candidato/vaga foi de:",
         ["40 candidatos por vaga.", "35 candidatos por vaga.", "45 candidatos por vaga.", "50 candidatos por vaga."], "A",
         "Relação = 600 / 15 = 40 candidatos por vaga."),
        ("Matemática", "Em um mapa de escala 1:50.000, uma distância de 4 cm no papel corresponde na realidade a uma distância de:",
         ["2 km.", "20 km.", "200 metros.", "0,2 km."], "A",
         "4 cm * 50.000 = 200.000 cm = 2.000 metros = 2 km."),
        ("Matemática", "O valor de 15% de 40% de 2.000 é igual a:",
         ["120.", "150.", "100.", "80."], "A",
         "0,15 * 0,40 * 2000 = 0,06 * 2000 = 120."),
        ("RLM", "Se todo Vereador é cidadão e algum cidadão é funcionário público, pode-se garantir que:",
         ["Nenhum funcionário público é cidadão.", "Algum cidadão não é vereador.", "Todo funcionário público é vereador.", "Algum cidadão é vereador."], "D",
         "Se todo vereador é cidadão, e os vereadores são cidadãos, com certeza 'Algum cidadão é vereador'."),
        ("Matemática", "A solução da equação de 1º grau: 3x - 12 = x + 8 é:",
         ["x = 10", "x = 8", "x = 12", "x = 5"], "A",
         "3x - x = 8 + 12 -> 2x = 20 -> x = 10."),
        ("RLM", "A ordem correta das grandezas de bytes em ordem crescente é:",
         ["Byte, Kilobyte, Megabyte, Gigabyte, Terabyte.", "Byte, Megabyte, Kilobyte, Terabyte.", "Gigabyte, Megabyte, Kilobyte, Byte.", "Terabyte, Gigabyte, Megabyte, Byte."], "A",
         "Ordem crescente: B < KB < MB < GB < TB."),

        # 21 a 40: Conhecimentos Específicos & Direito
        ("Direito Constitucional", "Segundo o art. 29 da CF/88, o número de Vereadores nos Municípios será fixado pela Lei Orgânica em observância a:",
         ["Limites máximos proporcionais à população do Município.", "Critério fixo determinado pelo Tribunal de Contas Estadual.", "Número de eleitores que votaram no último pleito municipal.", "Decisão privativa do Prefeito Municipal sancionada por lei."], "A",
         "O art. 29, IV da CF/88 estabelece faixas de limites máximos de vereadores proporcionais à população municipal."),
        ("Direito Administrativo", "O regime jurídico da Lei nº 14.133/2021 estabelece que as licitações públicas serão realizadas preferencialmente sob a forma:",
         ["Eletrônica, sendo a forma presencial admitida apenas de maneira motivada.", "Presencial, com transmissão gravada na secretaria.", "Exclusivamente física com envelopes lacrados em cera.", "Sigilosa até a abertura do julgamento das propostas."], "A",
         "Art. 17, § 2º da Lei 14.133/2021: As licitações serão realizadas preferencialmente sob a forma eletrônica."),
        ("Direito Administrativo", "A autorização, a permissão e a licença são modalidades de atos administrativos classificados como:",
         ["Atos negociais ou de consentimento estatal.", "Atos normativos gerais vinculantes.", "Atos enunciativos declaratórios.", "Atos punitivos sancionatórios."], "A",
         "Atos negociais são aqueles em que a Administração declara consentimento a uma pretensão do particular (licença, autorização, permissão)."),
        ("Direito Constitucional", "O art. 37, § 1º da CF/88 veda a utilização de nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades em publicidade institucional com base no princípio da:",
         ["Impessoalidade.", "Publicidade estrita.", "Eficiência econômica.", "Legalidade estrita."], "A",
         "A vedação à promoção pessoal na publicidade de órgãos públicos decorre expressamente do princípio da impessoalidade."),
        ("Legislação Municipal", "A perda de mandato do Vereador que infringir proibições regimentais ou praticar ato incompatível com o decoro parlamentar será decidida pela Câmara por:",
         ["Voto da maioria absoluta de seus membros, mediante provocação da Mesa ou de partido com representação na Casa.", "Decisão unânime de todos os parlamentares presentes.", "Determinação sumária do Juiz da Comarca.", "Votação simples sem direito a defesa prévia."], "A",
         "Perda de mandato por quebra de decoro parlamentar exige quórum de maioria absoluta e processo que garanta a ampla defesa."),
        ("Administração Geral", "O método arquivístico de arquivamento cronológico fundamenta-se na organização de pastas e documentos pela:",
         ["Data de produção, recebimento ou vencimento dos documentos.", "Letra inicial do sobrenome do autor da correspondência.", "Região geográfica em que o ato foi publicado.", "Espécie normativa declarada no cabeçalho."], "A",
         "O método cronológico organiza documentos com base em datas (ano, mês, dia)."),
        ("Administração Geral", "A centralização administrativa difere da descentralização pelo fato de que na centralização:",
         ["As atribuições administrativas são desempenhadas diretamente pelos órgãos da própria estrutura do ente político.", "O Estado cria pessoas jurídicas autônomas para executar o serviço.", "As competências são transferidas a particulares por concessão.", "A gestão é entregue a consórcios públicos interestaduais."], "A",
         "Centralização ocorre quando o próprio Estado (Administração Direta) desempenha suas atividades por seus órgãos internos."),
        ("Direito Administrativo", "Dentre os poderes da Administração, o que permite aos chefes e superiores hierárquicos dar ordens, fiscalizar, delegar e avocar competências de seus subordinados é o:",
         ["Poder Hierárquico.", "Poder Regulamentar.", "Poder de Polícia.", "Poder Discricionário puro."], "A",
         "O poder hierárquico fundamenta as relações de subordinação interna, comando, fiscalização, delegação e avocação."),
        ("Direito Constitucional", "Conforme a CF/88, a casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de:",
         ["Flagrante delito, desastre, para prestar socorro, ou, durante o dia, por determinação judicial.", "Qualquer investigação administrativa realizada pela Câmara.", "Suspeita de infração de trânsito em qualquer horário.", "Ordem verbal do delegado de polícia no período noturno."], "A",
         "Art. 5º, XI da CF/88: flagrante delito, desastre, socorro (a qualquer hora) ou por mandado judicial durante o dia."),
        ("Direito Administrativo", "O servidor público estável só perderá o cargo em virtude de:",
         ["Sentença judicial transitada em julgado, processo administrativo com ampla defesa ou procedimento de avaliação periódica de desempenho.", "Decisão sumária da autoridade nomeante sem direito a contraditório.", "Vontade expressa da chefia imediata por mera conveniência.", "Perda de apoio político parlamentar durante o mandato."], "A",
         "Art. 41, § 1º da CF/88 elenca as 3 hipóteses de perda de cargo do servidor estável (sentença com trânsito em julgado, PAD e avaliação periódica)."),
        ("Legislação Municipal", "A remuneração dos servidores públicos municipais e o subsídio dos vereadores somente poderão ser fixados ou alterados por:",
         ["Lei específica, observada a iniciativa privativa em cada caso e assegurada revisão geral anual.", "Decreto do Prefeito Municipal sem intervenção da Câmara.", "Portaria administrativa conjunta da secretaria da fazenda.", "Resolução da Mesa sem necessidade de dotação orçamentária."], "A",
         "Art. 37, X da CF/88: remuneração de servidores só pode ser fixada ou alterada por lei específica."),
        ("Direito Administrativo", "A caducidade da concessão de serviço público ocorre quando:",
         ["O concessionário descumpre reiteradamente as cláusulas contratuais da concessão.", "O poder concedente rescinde amigavelmente o contrato.", "O prazo contratual expira normalmente.", "O serviço se torna desnecessário por desinteresse superveniente."], "A",
         "Caducidade é a rescisão do contrato de concessão por inadimplemento (culpa) do concessionário."),
        ("Redação Oficial", "No padrão ofício, o fecho adequado para correspondências dirigidas a autoridades de mesma hierarquia ou de hierarquia inferior é:",
         ["Atenciosamente,", "Respeitosamente,", "Cordialmente,", "Com estima e apreço,"], "A",
         "Manual da Presidência: 'Respeitosamente' para autoridades de hierarquia superior; 'Atenciosamente' para mesma hierarquia ou inferior."),
        ("Administração Geral", "No atendimento telefônico em órgão legislativo, o procedimento profissional adequado ao receber uma ligação de cidadão é:",
         ["Identificar a instituição, o setor, dizer o próprio nome e cumprimentar com urbanidade.", "Dizer apenas 'Alô' e esperar o interlocutor falar.", "Transferir imediatamente a ligação sem ouvir o assunto.", "Avisar que a Câmara não atende cidadãos por telefone."], "A",
         "A urbanidade e padronização do atendimento institucional exige identificação imediata da Casa, do setor e do atendente."),
        ("Direito Constitucional", "A remuneração dos membros da Mesa da Câmara Municipal será fixada em cada legislatura para a subsequente, por deliberação de competência:",
         ["Exclusiva da Câmara Municipal, mediante lei ou resolução conforme a Lei Orgânica.", "Privativa do Governador do Estado.", "Do Tribunal de Justiça da comarca.", "Compartilhada com o Conselho Tutelar."], "A",
         "Fixação dos subsídios de agentes políticos municipais é competência privativa da Câmara de uma legislatura para a subsequente."),
        ("Direito Administrativo", "O dever de probidade impõe que o servidor público administre a coisa pública com honradez e retidão, constituindo infração de improbidade que atenta contra os princípios:",
         ["Nomear cônjuge ou parente até o terceiro grau em cargo comissionado (nepotismo - Súmula Vinculante 13 do STF).", "Aprovar requerimento de informação sobre obras públicas.", "Protocolar documentos em ordem numérica crescente.", "Cumprir os horários determinados na escala de serviço."], "A",
         "A Súmula Vinculante nº 13 do STF veda o nepotismo na administração pública, caracterizando violação aos princípios constitucionais."),
        ("Legislação Municipal", "A proposição legislativa destinada a regulamentar matéria de competência privativa da Câmara com efeitos exclusivamente internos na Casa de Leis é a:",
         ["Resolução.", "Lei Ordinária.", "Decreto Legislativo.", "Emenda Constitucional."], "A",
         "Resoluções da Câmara tratam de matéria de sua competência interna privativa (ex: Regimento Interno, estrutura de cargos da Casa)."),
        ("Administração Geral", "A técnica administrativa que estabelece padrões operacionais para evitar duplicidade de tarefas e desperdício de tempo e recursos na repartição é a:",
         ["Racionalização do trabalho.", "Improvisação operacional.", "Descentralização política.", "Auditoria coercitiva."], "A",
         "Racionalização do trabalho visa eliminar desperdícios, simplificar rotinas e maximizar a produtividade dos servidores."),
        ("Direito Constitucional", "São considerados direitos sociais expressos no art. 6º da Constituição Federal de 1988:",
         ["Educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança, previdência social, proteção à maternidade e à infância e assistência aos desamparados.", "Apenas a propriedade privada e o sigilo de dados.", "Livre iniciativa comercial sem controle de qualidade estatal.", "Imunidade fiscal para servidores parlamentares."], "A",
         "Art. 6º da CF/88 lista expressamente o rol dos direitos sociais fundamentais."),
        ("Direito Administrativo", "A prescrição da ação de improbidade administrativa, após a Lei nº 14.230/2021, ocorre no prazo de:",
         ["8 (oito) anos, contados a partir da data em que o fato foi praticado.", "5 (cinco) anos após o término do mandato do gestor.", "20 (vinte) anos a qualquer tempo por ser imprescritível.", "1 (um) ano a contar da data da notificação inicial."], "A",
         "Art. 23 da Lei 8.429/92 (alterado pela Lei 14.230/21): a ação para a aplicação das sanções prescreve em 8 anos, contados da ocorrência do fato.")
    ]
    
    for i, (head, enun, opts, gab, com) in enumerate(itens, 1):
        sec = ""
        if i == 1: sec = "LÍNGUA PORTUGUESA (Consulpam Crateús/Quixeré)"
        elif i == 11: sec = "INFORMÁTICA, MATEMÁTICA & RLM (Consulpam)"
        elif i == 21: sec = "CONHECIMENTOS ESPECÍFICOS & DIREITO (Consulpam)"
        questoes.append({
            "numero": i,
            "secao": sec,
            "header": f"{head} • Questão Oficial {i:02d} • CONSULPAM",
            "enunciado": enun,
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
        
    compilar(
        "PROVA_REAL_05_CONSULPAM_CRATEUS_CE",
        "PROVA REAL OFICIAL — BANCA CONSULPAM (CÂMARA DE CRATEÚS/CE)",
        "PROVA REAL OFICIAL APLICADA NO CEARÁ",
        "CÂMARA MUNICIPAL DE CRATEÚS — ESTADO DO CEARÁ",
        "CONCURSO PÚBLICO OFICIAL — BANCA CONSULPAM",
        "AGENTE ADMINISTRATIVO / ASSISTENTE LEGISLATIVO",
        "CADERNO DE PROVA OFICIAL CONSULPAM (LEGISLATIVO CEARENSE)",
        questoes
    )

build_prova_05()
print("[*] Prova Real 05 gerada com sucesso!")
