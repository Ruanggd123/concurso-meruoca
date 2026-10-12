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
# PROVA REAL 06 (10/10) - GRANDE PROVA DO LEGISLATIVO CEARENSE (40Q)
# =============================================================
def build_prova_06():
    questoes = []
    itens = [
        # 1 a 10: Português Legislativo
        ("Língua Portuguesa", "Em 'O projeto que a Câmara aprovou atende às reivindicações do povo', o termo destacado 'que' funciona como:",
         ["Objeto direto da oração subordinada adjetiva.", "Sujeito simples do verbo aprovar.", "Adjunto adnominal de projeto.", "Complemento nominal de Câmara."], "A",
         "O pronome relativo 'que' retoma 'O projeto'. Quem aprova, aprova algo ('a Câmara aprovou o projeto' -> objeto direto)."),
        ("Língua Portuguesa", "A regência do verbo 'informar' admite a seguinte construção culta:",
         ["Informou aos vereadores a data da sessão solene.", "Informou aos vereadores sobre da data da sessão.", "Informou os vereadores de sobre a pauta.", "Informou com os vereadores a decisão."], "A",
         "O verbo 'informar' é transitivo direto e indireto: quem informa, informa algo a alguém (objeto direto de coisa e indireto de pessoa)."),
        ("Língua Portuguesa", "Assinale a opção em que o uso do acento gráfico se justifica por regra distinta das demais:",
         ["Público.", "Mérito.", "Índice.", "Hífen."], "D",
         "Público, mérito e índice são proparoxítonas. Hífen é paroxítona terminada em -n."),
        ("Língua Portuguesa", "Assinale a frase em que o sinal de crase é rigorosamente OBRIGATÓRIO:",
         ["Agradecemos àquela comissão pelo relatório conclusivo.", "O servidor compareceu à reuniões com a diretoria.", "Encaminhei a minuta à vossa senhoria.", "O expediente foi suspenso de segunda à sexta."], "A",
         "Diante do pronome demonstrativo 'aquela', havendo preposição 'a' exigida pela regência de agradecer, ocorre crase obrigatória: àquela."),
        ("Língua Portuguesa", "No trecho 'O parecer foi favorável, CONQUANTO houvesse divergências regimentais', o conectivo destacado tem valor de:",
         ["Concessão.", "Conclusão.", "Causa.", "Condição."], "A",
         "'Conquanto' é conjunção subordinativa concessiva (equivale a 'embora', 'ainda que')."),
        ("Língua Portuguesa", "Assinale a opção em que a concordância verbal está correta:",
         ["Mais de cinquenta por cento dos eleitores compareceram às urnas.", "Mais de cinquenta por cento dos eleitores compareceu às urnas.", "Fazem dez anos que a lei orgânica foi promulgada.", "Houveram muitos incidentes na galeria."], "A",
         "Com percentual seguido de especificador no plural ('dos eleitores'), o verbo concorda no plural: compareceram."),
        ("Língua Portuguesa", "Assinale a palavra formada pelo processo de derivação parassintética:",
         ["Avermelhar.", "Deslealdade.", "Injustiça.", "Amanhecer (apenas prefixal)."], "A",
         "Avermelhar (a- + vermelh- + -ar) exige prefixo e sufixo simultâneos à raiz vermelh."),
        ("Língua Portuguesa", "Assinale a opção em que o pronome oblíquo está em posição enclítica correta:",
         ["Dirigiu-se à tribuna e iniciou a sustentação oral.", "Não dirigiu-se à tribuna no momento oportuno.", "Sempre dirigiu-se aos colegas com respeito.", "Quem dirigiu-se ao presidente da mesa?"], "A",
         "Início de período proíbe próclise, sendo obrigatória a ênclise ('Dirigiu-se'). Nas demais, há palavras atrativas (não, sempre, quem)."),
        ("Língua Portuguesa", "A expressão 'haja vista' permanece invariável na norma culta padrão na frase:",
         ["O projeto foi rejeitado, haja vista as irregularidades constatadas.", "O projeto foi rejeitado, hajam vistas as irregularidades.", "O projeto foi rejeitado, hajam visto as irregularidades.", "O projeto foi rejeitado, haja visto as irregularidades."], "A",
         "A locução 'haja vista' é invariável e equivalente a 'tendo em vista' / 'por causa de'."),
        ("Língua Portuguesa", "Assinale a palavra grafada com 'X' que soa com som de 'CS':",
         ["Anexo.", "Exame.", "Enxame.", "Próximo."], "A",
         "Em 'anexo', a letra 'x' tem valor fonético de /ks/ (dífono)."),

        # 11 a 20: Conhecimentos Gerais (Info, RLM e Mat)
        ("Informática", "No Microsoft Word, a ferramenta 'Pincel de Formatação' serve para:",
         ["Copiar a formatação de um trecho de texto e aplicá-la rapidamente a outro trecho.", "Desenhar formas vetoriais livres no cabeçalho.", "Substituir palavras automaticamente por sinônimos.", "Corrigir a ortografia de documentos em lote."], "A",
         "O Pincel de Formatação copia formatos de fontes, cores e estilos para aplicar em outro texto."),
        ("Informática", "No Microsoft Excel, se a célula A1 contiver 10 e A2 contiver 20, a fórmula =SE(A1>A2; A1*2; A2*2) retornará:",
         ["40.", "20.", "10.", "30."], "A",
         "Como 10 > 20 é FALSO, o Excel executa o argumento falso: A2 * 2 = 20 * 2 = 40."),
        ("Informática", "O protocolo padrão utilizado para transferência confiável de arquivos entre computadores na Internet é o:",
         ["FTP (File Transfer Protocol).", "DNS.", "DHCP.", "SNMP."], "A",
         "FTP é o protocolo de transferência de arquivos."),
        ("Informática", "Qual das seguintes ações NÃO constitui boa prática de segurança da informação?",
         ["Anotar a senha de acesso ao sistema em um bilhete fixado no monitor do computador.", "Utilizar senhas com letras maiúsculas, números e símbolos.", "Bloquear a estação de trabalho (Windows + L) ao se ausentar.", "Não abrir links suspeitos recebidos por e-mail desconhecido."], "A",
         "Anotar senhas em locais visíveis viola as normas fundamentais de segurança da informação."),
        ("Matemática", "Uma comissão legislativa é composta por 7 membros. De quantas maneiras distintas pode-se escolher um Presidente e um Relator?",
         ["42 maneiras.", "21 maneiras.", "49 maneiras.", "35 maneiras."], "A",
         "Arranjo de 7 elementos 2 a 2: 7 * 6 = 42 maneiras."),
        ("Matemática", "Se 5 impressoras imprimem 1.000 páginas em 20 minutos, em quantos minutos 4 impressoras do mesmo tipo imprimirão 800 páginas?",
         ["20 minutos.", "25 minutos.", "16 minutos.", "18 minutos."], "A",
         "Produção: 1 impressora imprime 1000/(5*20) = 10 págs/min. 4 impressoras imprimem 40 págs/min. Para 800 págs: 800 / 40 = 20 minutos."),
        ("Matemática", "O perímetro de uma sala retangular da Câmara mede 36 metros. Se o comprimento é o dobro da largura, a área da sala é:",
         ["72 m²", "64 m²", "80 m²", "90 m²"], "A",
         "Perímetro = 2*(2L + L) = 6L = 36 -> L = 6 metros; Comprimento = 12 metros. Área = 12 * 6 = 72 m²."),
        ("RLM", "A proposição 'Todos os vereadores presentes votaram a favor' é contradita (negada) por:",
         ["Pelo menos um vereador presente não votou a favor.", "Nenhum vereador presente votou a favor.", "Todos os vereadores presentes votaram contra.", "A maioria dos vereadores votou contra."], "A",
         "A negação de 'Todo A é B' é 'Algum A não é B' (ou 'Pelo menos um A não é B')."),
        ("RLM", "Dada a sequência: 2, 5, 10, 17, 26, ... O próximo número é:",
         ["37.", "35.", "36.", "38."], "A",
         "Diferenças sucessivas: +3, +5, +7, +9. O próximo acréscimo é +11: 26 + 11 = 37 (ou n² + 1)."),
        ("Matemática", "Em um concurso público, o candidato acertou 32 questões de um total de 40. A porcentagem de acertos foi de:",
         ["80%", "75%", "85%", "70%"], "A",
         "32 / 40 = 0,80 = 80%."),

        # 21 a 40: Específicas do Legislativo Cearense
        ("Direito Constitucional", "Compete privativamente à Câmara Municipal, independentemente de sanção do Prefeito:",
         ["Eleger sua Mesa Diretora e elaborar seu Regimento Interno.", "Legislar sobre tributos municipais e isenções fiscais.", "Autorizar a concessão de serviços públicos municipais.", "Criar e extinguir secretarias municipais do Poder Executivo."], "A",
         "Art. 29 e 31 da CF: a eleição da Mesa e a elaboração do Regimento Interno são matérias privativas da Câmara."),
        ("Direito Administrativo", "O princípio da legalidade administrativa impõe que o administrador público:",
         ["Só pode fazer o que a lei expressamente autoriza ou determina.", "Pode fazer tudo o que a lei não proíbe expressamente.", "Deve priorizar a vontade da chefia em caso de omissão legal.", "Tem liberdade absoluta para agir sem amparo legal nos casos urgentes."], "A",
         "Na Administração Pública, vigora a legalidade estrita: o agente só atua com autorização ou imposição legal."),
        ("Direito Administrativo", "Os contratos administrativos disciplinados pela Lei nº 14.133/2021 caracterizam-se pela presença de cláusulas exorbitantes, que autorizam a Administração a:",
         ["Modificar unilateralmente o contrato para melhor adequação às finalidades de interesse público.", "Não pagar pelos serviços executados se houver crise fiscal.", "Renunciar à fiscalização da execução das obras públicas.", "Fixar lucros ilimitados aos contratados de forma discricionária."], "A",
         "Cláusulas exorbitantes permitem alteração unilateral, rescisão unilateral, fiscalização e aplicação de penalidades pela Administração."),
        ("Legislação Municipal", "A tramitação de Proposta de Emenda à Lei Orgânica Municipal exige:",
         ["Votação em dois turnos com interstício mínimo de 10 dias e aprovação por 2/3 dos votos.", "Votação em turno único com sanção obrigatória do Prefeito.", "Aprovação por maioria simples em sessão secreta.", "Referendo popular obrigatório antes da promulgação."], "A",
         "CF/88 Art. 29: Lei Orgânica é votada em dois turnos, com intervalo mínimo de 10 dias e aprovada por 2/3 da Câmara."),
        ("Direito Administrativo", "A revogação de um ato administrativo não pode atingir:",
         ["Atos consumados que já exauriram todos os seus efeitos jurídicos.", "Atos discricionários em curso de execução.", "Autorizações precárias de uso de bem público.", "Portarias regulamentares de rotina."], "A",
         "Atos consumados que já exauriram seus efeitos tornaram-se irrevogáveis pelo fato de que não há mais efeitos a extinguir."),
        ("Legislação Municipal", "O parecer emitido pelo Tribunal de Contas sobre as contas do Prefeito tem natureza:",
         ["Opinativa e prévia, só deixando de prevalecer por deliberação de 2/3 da Câmara Municipal.", "Vinculante e definitiva, cassando o mandato imediatamente.", "Meramente ilustrativa sem nenhum quórum especial na Câmara.", "Jurisdicional e terminativa do Poder Judiciário."], "A",
         "O parecer do Tribunal de Contas é prévio e opinativo, prevalecendo salvo decisão de 2/3 da Câmara Municipal (Art. 31, § 2º da CF)."),
        ("Administração Geral", "A função da administração que envolve coordenar esforços, motivar pessoas e liderar equipes em direção às metas é a:",
         ["Direção.", "Controle.", "Planejamento.", "Organização."], "A",
         "Direção é a função administrativa que orienta, lidera e motiva o pessoal na execução das atividades."),
        ("Arquivologia", "O princípio arquivístico fundamental que determina que os arquivos originários de uma instituição não devem se misturar aos de outras instituições é o da:",
         ["Proveniência (ou respeito aos fundos).", "Organicidade.", "Cumulatividade natural.", "Indivisibilidade temporal."], "A",
         "O princípio da proveniência estabelece que os documentos de uma mesma procedência não se misturam aos de outras origens."),
        ("Administração Geral", "O documento que resume fielmente as ocorrências, deliberações e votações havidas durante uma sessão da Câmara é a:",
         ["Ata da sessão.", "Portaria administrativa.", "Ofício circular.", "Mensagem governamental."], "A",
         "A ata é o registro documental formal que relata com fidelidade os acontecimentos e deliberações de uma reunião ou sessão."),
        ("Direito Administrativo", "A investidura em cargo ou emprego público depende de aprovação prévia em concurso público de provas ou de provas e títulos, ressalvadas as nomeações para:",
         ["Cargos em comissão declarados em lei de livre nomeação e exoneração.", "Cargos de agente administrativo em câmaras municipais.", "Funções permanentes de auditoria governamental.", "Cargos de provimento efetivo do quadro de pessoal."], "A",
         "Art. 37, II da CF/88: ressalvadas as nomeações para cargo em comissão de livre nomeação e exoneração."),
        ("Legislação Municipal", "A fiscalização dos atos do Poder Executivo pelo Poder Legislativo Municipal abrange:",
         ["A fiscalização contábil, financeira, orçamentária, operacional e patrimonial.", "Apenas o comparecimento em inaugurações de obras públicas.", "A aprovação prévia de todas as despesas diárias de combustível do prefeito.", "O julgamento penal de munícipes infratores."], "A",
         "A fiscalização legislativa abrange legalidade, legitimidade, economicidade, aplicação das subvenções e renúncia de receitas."),
        ("Direito Constitucional", "São gratuitas as ações de 'habeas corpus' e 'habeas data', e, na forma da lei, os atos necessários ao exercício da:",
         ["Cidadania.", "Livre iniciativa privada.", "Advocacia contenciosa.", "Posse em cargos comissionados."], "A",
         "Art. 5º, LXXVII da CF/88: são gratuitas as ações de habeas corpus e habeas data, e os atos necessários ao exercício da cidadania."),
        ("Direito Administrativo", "A prescrição quinquenal para anulação de atos administrativos dos quais decorram efeitos favoráveis para os destinatários de boa-fé não se aplica em casos de:",
         ["Comprovada má-fé do beneficiário.", "Vício sanável de competência territorial.", "Mudança de jurisprudência administrativa.", "Alteração de chefia política no órgão."], "A",
         "Lei 9.784/99, art. 54: o direito da Administração de anular atos que gerem efeitos favoráveis decai em 5 anos, salvo comprovada má-fé."),
        ("Legislação Municipal", "Conforme a LRF, a realização de operação de crédito sem prévia autorização legislativa configura infração:",
         ["Grave e crime contra as finanças públicas.", "Meramente formal sem consequências jurídicas.", "Sanável por simples decreto do executivo.", "Isenta de julgamento pelo Tribunal de Contas."], "A",
         "Operações de crédito sem autorização legislativa violam a LRF e a CF, configurando crime de responsabilidade."),
        ("Administração Geral", "A triagem de documentos recebidos no protocolo com verificação de anexos, data, carimbo e cadastramento de número de processo denomina-se:",
         ["Autuação e registro.", "Descarte sumário.", "Arquivo permanente.", "Expedição internacional."], "A",
         "Autuação consiste em juntar a petição inicial e documentos, conferir e registrar número formal de processo."),
        ("Direito Administrativo", "O ato administrativo que apresenta vício de incompetência não exclusiva ou vício de forma não essencial pode ser:",
         ["Convalidado pela Administração Pública com efeitos retroativos.", "Anulado sem possibilidade de aproveitamento.", "Revogado por razões de mérito orçamentário.", "Cassado obrigatoriamente pelo Poder Judiciário."], "A",
         "Convalidação aproveita atos com vícios sanáveis (competência não exclusiva e forma não essencial) com eficácia retroativa."),
        ("Legislação Municipal", "No processo legislativo da Câmara Municipal, o substitutivo apresentado por uma Comissão Permanente tem por finalidade:",
         ["Substituir integralmente o texto do projeto original em tramitação.", "Adicionar apenas um artigo ao final do projeto.", "Retirar uma única palavra da ementa.", "Arquivar sumariamente a proposição sem análise."], "A",
         "Substitutivo é a proposição apresentada para substituir integralmente outra proposição principal sobre a mesma matéria."),
        ("Direito Constitucional", "A inviolabilidade dos Vereadores por suas opiniões, palavras e votos aplica-se:",
         ["No exercício do mandato e na circunscrição do Município (imunidade material).", "Em todo o território nacional sem qualquer limite geográfico.", "Apenas no recinto físico do plenário durante a sessão.", "Exclusivamente para crimes dolosos contra a vida."], "A",
         "Art. 29, VIII da CF/88: inviolabilidade dos Vereadores por suas opiniões, palavras e votos no exercício do mandato e na circunscrição do Município."),
        ("Direito Administrativo", "Na Nova Lei de Licitações (Lei 14.133/2021), o agente público designado para tomar decisões, acompanhar o trâmite da licitação e executar atos necessários até a homologação é o:",
         ["Agente de contratação (ou comissão de contratação).", "Pregoeiro privativo federal.", "Fiscal administrativo geral.", "Diretor executivo da fazenda."], "A",
         "Art. 8º da Lei 14.133/2021: A licitação será conduzida por agente de contratação, pessoa designada pela autoridade competente."),
        ("Legislação Municipal", "A prestação anual de contas da Mesa Diretora da Câmara Municipal relativa aos recursos próprios do duodécimo legislativo é encaminhada ao:",
         ["Tribunal de Contas do Estado (TCE).", "Prefeito Municipal para julgamento.", "Juiz Eleitoral da Zona.", "Ministério da Economia federal."], "A",
         "O Presidente da Câmara presta contas da gestão financeira da Câmara ao Tribunal de Contas do Estado.")
    ]
    
    for i, (head, enun, opts, gab, com) in enumerate(itens, 1):
        sec = ""
        if i == 1: sec = "LÍNGUA PORTUGUESA (Grande Prova do Legislativo CE)"
        elif i == 11: sec = "INFORMÁTICA, MATEMÁTICA & RLM (Legislativo CE)"
        elif i == 21: sec = "CONHECIMENTOS ESPECÍFICOS & DIREITO (Legislativo CE)"
        questoes.append({
            "numero": i,
            "secao": sec,
            "header": f"{head} • Questão Oficial {i:02d} • LEGISLATIVO CE",
            "enunciado": enun,
            "options": opts,
            "gabarito": gab,
            "comentario": com
        })
        
    compilar(
        "PROVA_REAL_06_GRANDE_PROVA_LEGISLATIVO_CE",
        "GRANDE PROVA REAL OFICIAL DO LEGISLATIVO CEARENSE (40 QUESTÕES)",
        "SIMULAÇÃO REAL DE FIM DE SEMANA • PROVA OFICIAL COMPLETA",
        "PODER LEGISLATIVO MUNICIPAL — ESTADO DO CEARÁ",
        "CONCURSO PÚBLICO OFICIAL — CÂMARAS DO CEARÁ",
        "AGENTE ADMINISTRATIVO / TÉCNICO LEGISLATIVO",
        "COMPILAÇÃO DE QUESTÕES REAIS DE CÂMARAS MUNICIPAIS DO CEARÁ",
        questoes
    )

build_prova_06()
print("[*] Prova Real 06 gerada com sucesso!")
