import json

QUESTOES_S3_D4 = [
  {
  "id": 491,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Contratacao Direta: Dispensa vs Inexigibilidade (Arts. 74-75)",
  "question": "Quanto à contratação direta na Lei nº 14.133/2021, a diferença essencial entre dispensa e inexigibilidade de licitação é que:",
  "options": [
    "Na dispensa a competição é viável, mas a lei autoriza não licitar (rol taxativo); na inexigibilidade a competição é inviável (rol exemplificativo).",
    "Na dispensa a competição é inviável e na inexigibilidade a competição é viável, invertendo a lógica da licitação.",
    "Ambas dispensam qualquer processo formal, bastando ordem verbal do prefeito para contratar.",
    "A dispensa exige sempre licitação prévia e a inexigibilidade é vedada aos municípios."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Arts. 74 e 75 da Lei 14.133/21. Dispensa (Art. 75): competir seria possível, mas a lei DISPENSA por conveniência (rol TAXATIVO, ex: pequeno valor, emergência). Inexigibilidade (Art. 74): competir é INVIÁVEL (fornecedor exclusivo, artista consagrado) — rol EXEMPLIFICATIVO. Pegadinha INBRASP nº 1 do tema."
},
  {
  "id": 492,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Dispensa por Valor (Art. 75, I e II)",
  "question": "A dispensa de licitação em razão do pequeno valor (Art. 75, I e II da Lei nº 14.133/2021, valores atualizados por decreto federal) aplica-se a:",
  "options": [
    "Qualquer compra milionária, desde que o prefeito declare urgência verbal.",
    "Obras e serviços de engenharia até o limite superior e outros serviços e compras até o limite inferior, vedado o fracionamento para enquadrar a despesa.",
    "Obras acima de R$ 10 milhões e serviços contínuos de qualquer valor.",
    "Apenas à compra de café e material de limpeza, independentemente do valor."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 75, I (obras/engenharia/manutenção de veículos: teto maior) e II (outros serviços e compras: teto menor), atualizados anualmente por decreto. É VEDADO o fracionamento de despesa para fugir da licitação (soma-se o gasto anual do objeto). Números exatos mudam por decreto; a banca cobra a lógica dos dois patamares."
},
  {
  "id": 493,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Inexigibilidade: Hipoteses (Art. 74)",
  "question": "São hipóteses de inexigibilidade de licitação previstas no Art. 74 da Lei nº 14.133/2021:",
  "options": [
    "Compra de bens comuns de prateleira e contratação de obra padrão por menor preço.",
    "Serviços de limpeza com dezenas de empresas aptas e fornecimento de papel A4.",
    "Fornecedor exclusivo, profissional do setor artístico consagrado e serviços técnicos especializados de natureza predominantemente intelectual.",
    "Locação de imóvel qualquer sem avaliação prévia e sem justificativa."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 74, I a V da Lei 14.133/21: I - fornecedor exclusivo (atestado); II - artista consagrado pela crítica ou público; III - serviços técnicos intelectuais (estudos, pareceres, projetos) com notória especialização; IV - objetos que devam ser contratados por credenciamento; V - aquisição/locação de imóvel com características específicas (com avaliação e justificativa). Bens comuns = pregão, jamais inexigibilidade."
},
  {
  "id": 494,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Processo da Contratacao Direta (Art. 72)",
  "question": "O processo de contratação direta (dispensa ou inexigibilidade) exige, nos termos do Art. 72 da Lei nº 14.133/2021:",
  "options": [
    "Apenas um telefonema para a empresa amiga e pagamento adiantado sem recibo.",
    "Somente a nota de empenho, dispensados parecer, pesquisa de preços e publicidade.",
    "Autorização verbal do vereador presidente, sem qualquer documento escrito.",
    "Documento de formalização da demanda, estimativa de despesa com pesquisa de preços, parecer jurídico e técnico, demonstração de compatibilidade orçamentária e autorização da autoridade competente, tudo divulgado no PNCP."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 72 da Lei 14.133/21. Contratação direta NÃO é contratação informal: exige DFD, ETP quando cabível, TR, pesquisa de preços (Art. 23), parecer jurídico, razão da escolha do contratado, justificativa do preço e autorização — com divulgação no PNCP. Pegadinha: 'direta' dispensa a COMPETIÇÃO, não o PROCESSO."
},
  {
  "id": 495,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Dispensa Emergencial (Art. 75, VIII)",
  "question": "A dispensa emergencial do Art. 75, VIII da Lei nº 14.133/2021 (emergência ou calamidade pública) caracteriza-se por:",
  "options": [
    "Ser cabível apenas para os bens e serviços necessários ao atendimento da emergência, com contratação pelo prazo máximo de 1 ano, vedada a prorrogação e a recontratação da mesma empresa no período seguinte.",
    "Permitir qualquer contratação pelo prazo de 10 anos, inclusive obras não relacionadas à emergência.",
    "Dispensar a comprovação da emergência, bastando a alegação genérica de pressa.",
    "Autorizar a contratação de empresa punida com inidoneidade sem qualquer restrição."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 75, VIII da Lei 14.133/21. Emergência real (não fabricada pela desídia do gestor): só o necessário, contrato de até 1 ANO, sem prorrogação, vedada recontratação da mesma empresa. A emergência deve ser demonstrada; a culpa do gestor pela falta de planejamento não gera emergência lícita (entendimento do TCU)."
},
  {
  "id": 496,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Formalizacao do Contrato (Arts. 89-95)",
  "question": "Sobre a formalização dos contratos administrativos na Lei nº 14.133/2021, é correto afirmar que:",
  "options": [
    "Todo contrato pode ser verbal, inclusive obras de grande vulto, sem qualquer registro.",
    "A regra é o termo de contrato escrito, admitindo-se instrumento hábil substituto (carta-contrato, nota de empenho, autorização de compra) nas compras com entrega imediata e integral sem obrigações futuras.",
    "É vedado qualquer substituto do termo de contrato, mesmo para compras à vista de pequeno valor.",
    "O contrato verbal é a regra e o escrito é exceção para valores acima de R$ 1 bilhão."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Arts. 89 a 95 da Lei 14.133/21. Regra: termo escrito. Exceção: instrumento hábil (empenho, carta-contrato) em compras de entrega imediata/integral sem obrigação futura (ex: material de expediente à vista) e nos limites da dispensa por valor. Contrato verbal só em pequenas compras de pronto pagamento (Art. 95, §2º) e mesmo assim com justificativa."
},
  {
  "id": 497,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Clausulas Necessarias (Art. 92)",
  "question": "O Art. 92 da Lei nº 14.133/2021 estabelece as cláusulas necessárias do contrato administrativo. Entre elas NÃO se inclui:",
  "options": [
    "O objeto e seus elementos característicos, com quantitativos e especificações.",
    "O preço, as condições de pagamento, os critérios de reajuste e a dotação orçamentária.",
    "A preferência pessoal do gestor pelo contratado e a dispensa de definir o objeto com precisão.",
    "Os prazos de execução e vigência, o modelo de gestão, os casos de extinção e as penalidades."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 92 da Lei 14.133/21 (rol com ~20 incisos): objeto detalhado, preço e pagamento, reajuste, prazos, crédito orçamentário, garantias, direitos/deveres, fiscalização, penalidades, extinção, foro. A opção A descreve vícios (pessoalidade e objeto impreciso), jamais cláusula válida — é a clássica questão de 'EXCETO' da banca."
},
  {
  "id": 498,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Vigencia dos Contratos Continuos (Arts. 105-107)",
  "question": "Quanto à duração dos contratos de serviços e fornecimentos contínuos na Lei nº 14.133/2021, assinale a opção correta:",
  "options": [
    "São sempre de 30 dias improrrogáveis, devendo licitar todo mês.",
    "Podem durar 99 anos desde o início, sem qualquer limite ou justificativa.",
    "A prorrogação é automática e independe de previsão no edital ou de vantagem para a Administração.",
    "Podem ter vigência inicial de até 5 anos, prorrogável sucessivamente até o máximo de 10 anos, desde que atestada a vantajosidade e prevista a prorrogação no edital."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Arts. 105 a 107 da Lei 14.133/21. Contratos por escopo seguem o cronograma; contínuos (limpeza, vigilância): até 5 anos + prorrogações até 10. Exceções com prazos próprios: aluguel de equipamentos/programas e operação continuada de sistemas estruturantes. Prorrogação exige previsão, interesse público e preço vantajoso."
},
  {
  "id": 499,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Alteracao Unilateral: Limites (Art. 125)",
  "question": "Nas alterações unilaterais do contrato pela Administração (Art. 125 da Lei nº 14.133/2021), os acréscimos ou supressões ficam limitados a:",
  "options": [
    "25% do valor inicial atualizado, em regra, e 50% no caso particular de reforma de edifício ou de equipamento.",
    "100% em qualquer caso, sem limite, a critério do fiscal do contrato.",
    "10% para acréscimos e 90% para supressões, sem distinção de objeto.",
    "Não há limite algum, podendo o contrato dobrar de valor por decisão unilateral."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 125 da Lei 14.133/21 (mesma lógica da Lei 8.666/93, Art. 65). Regra: até 25% para mais ou para menos. Exceção: até 50% em reforma de edifício ou equipamento. Supressões ACIMA do limite dependem de acordo (consensual). Ultrapassar unilateralmente gera nulidade do excesso."
},
  {
  "id": 500,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Reajuste, Repactuacao e Reequilibrio (Arts. 124-136)",
  "question": "Sobre a manutenção do equilíbrio econômico-financeiro do contrato (Arts. 124 a 136 da Lei nº 14.133/2021), é correto afirmar que:",
  "options": [
    "As três figuras são sinônimas e podem ser usadas livremente a qualquer tempo, sem previsão contratual.",
    "O reajuste repõe a inflação por índice previsto (após 1 ano); a repactuação é própria de serviços com mão de obra dedicada (planilha de custos); o reequilíbrio cobre fato imprevisível ou de consequências incalculáveis.",
    "O reequilíbrio é vedado e o contratado assume todo prejuízo, mesmo em caso fortuito.",
    "O reajuste dispensa interregno mínimo e pode ser mensal por decisão do contratado."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Arts. 124-136 da Lei 14.133/21. Reajuste em sentido estrito: índice (IPCA etc.), após 12 meses do orçamento. Repactuação: demonstração analítica de custos (terceirização com dedicação exclusiva). Revisão/reequilíbrio: álea extraordinária (fato do príncipe, caso fortuito, força maior). Mnemônico: índice = reajuste; planilha = repactuação; imprevisível = reequilíbrio."
},
  {
  "id": 501,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Fiscalizacao e Recebimento (Arts. 117 e 140)",
  "question": "Na execução contratual (Arts. 117 e 140 da Lei nº 14.133/2021), o recebimento do objeto ocorre em duas etapas:",
  "options": [
    "Verbal e definitivo, sem qualquer verificação, bastando a palavra do contratado.",
    "Somente definitivo após 10 anos do término da obra, sem etapa provisória.",
    "Provisório (verificação sumária pelo fiscal, em até 15 dias do comunicado, salvo prazo diverso) e definitivo (verificação da qualidade e quantidade, por servidor ou comissão designada).",
    "Automático na assinatura do contrato, antes mesmo da execução do objeto."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 140 da Lei 14.133/21. Recebimento provisório: conferência rápida (fiscal). Definitivo: aceite após testes/verificações (servidor ou comissão). Em obras/serviços de engenharia o definitivo exige comissão. O recebimento definitivo NÃO exclui a responsabilidade civil (solidez e segurança — Art. 140, §6º c/c Código Civil)."
},
  {
  "id": 502,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Pagamento e Ordem Cronologica (Art. 141)",
  "question": "O Art. 141 da Lei nº 14.133/2021 determina que os pagamentos observem a ordem cronológica de exigibilidade por fonte de recursos. A quebra dessa ordem:",
  "options": [
    "É livre e pode ocorrer por simpatia do tesoureiro, sem qualquer justificativa.",
    "É obrigatória todo mês, pagando-se primeiro as empresas de amigos do gestor.",
    "Dispensa qualquer publicidade, podendo ser decidida oralmente.",
    "Somente é admitida mediante justificativa da autoridade competente, devidamente publicada, em casos de grave perturbação da ordem, emergência ou calamidade."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 141 da Lei 14.133/21 (regra da fila de pagamentos por fonte). Quebra só com justificativa formal e pública: risco de paralisação de serviço essencial, emergência, calamidade. Pagamento fora da ordem sem motivo configura improbidade/irregularidade grave apontada pelos Tribunais de Contas."
},
  {
  "id": 503,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Garantias Contratuais (Arts. 96-102)",
  "question": "Sobre as garantias de execução contratual (Arts. 96 a 102 da Lei nº 14.133/2021), assinale a opção correta:",
  "options": [
    "O edital pode exigir garantia nas modalidades caução em dinheiro, seguro-garantia ou fiança bancária, limitada a 5% do valor inicial (até 10% mediante justificativa em obras de grande vulto).",
    "A garantia é sempre de 50% do contrato e só admite depósito em ouro.",
    "O contratado escolhe livremente não apresentar garantia, mesmo quando exigida no edital.",
    "O seguro-garantia cobre apenas o primeiro dia de obra e depois se extingue sozinho."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Arts. 96-102 da Lei 14.133/21. Modalidades à escolha do contratado: caução (dinheiro/títulos), seguro-garantia, fiança bancária (e título de capitalização foi incluído). Teto: 5%, até 10% com justificativa técnica em obras/serviços de grande vulto. Há ainda o seguro-garantia com cláusula de retomada (step in) em grandes obras."
},
  {
  "id": 504,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Matriz de Riscos (Art. 22)",
  "question": "A matriz de riscos prevista no Art. 22 da Lei nº 14.133/2021 consiste em:",
  "options": [
    "Documento secreto que esconde os riscos da obra do Tribunal de Contas.",
    "Cláusula contratual que define a repartição objetiva de riscos entre contratante e contratado (ex: variação cambial, atraso de licenças), vedada a alocação de risco de caso fortuito ao contratado sem contrapartida.",
    "Planilha de apostas sobre qual empresa vai falir primeiro durante a execução.",
    "Lista de servidores que serão punidos se a obra atrasar, independentemente de culpa."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 22 da Lei 14.133/21. A matriz distribui riscos previsíveis (quem arca com cada evento) e integra o cálculo do equilíbrio econômico-financeiro: risco alocado ao contratado já está no preço (sem reequilíbrio por ele). Obrigatória em obras e serviços de engenharia de grande vulto."
},
  {
  "id": 505,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Infracoes Administrativas (Art. 155)",
  "question": "O Art. 155 da Lei nº 14.133/2021 tipifica as infrações do licitante/contratado. Configura infração administrativa, entre outras condutas:",
  "options": [
    "Entregar o objeto antes do prazo com qualidade superior à exigida.",
    "Apresentar proposta com desconto maior que o dos concorrentes.",
    "Dar causa à inexecução parcial ou total do contrato, apresentar documentação falsa, fraudar a licitação e comportar-se de modo inidôneo.",
    "Comparecer pontualmente à sessão e assinar a ata de registro de preços."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 155, I a XII da Lei 14.133/21: inexecução parcial/total, retardamento, documentação falsa, fraude, inidoneidade, conluio. Cumprir bem e pontualmente jamais é infração — as demais opções descrevem conduta exemplar ou competitiva lícita."
},
  {
  "id": 506,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Penalidades: Especies e Prazos (Art. 156)",
  "question": "As sanções aplicáveis ao responsável por infração (Art. 156 da Lei nº 14.133/2021) e seus alcances temporais são:",
  "options": [
    "Prisão perpétua do sócio e confisco de todos os bens da família.",
    "Apenas advertência verbal, sem qualquer outra consequência em qualquer caso.",
    "Multa única de R$ 1,00 simbólica para todas as infrações graves.",
    "Advertência, multa, impedimento de licitar e contratar (até 3 anos, no ente sancionador) e declaração de inidoneidade (3 a 6 anos, em todos os entes)."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 156 da Lei 14.133/21. Escada: advertência (só inexecução parcial leve) → multa (mora/inexecução, cumulável) → impedimento (até 3 anos, no âmbito do ente: ex: só no Município de Meruoca) → inidoneidade (3 a 6 anos, em TODOS os entes, para fraudes e crimes). Mnemônico de alcance: Impedimento = local; Inidoneidade = nacional."
},
  {
  "id": 507,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Reabilitacao do Punido (Art. 163)",
  "question": "A reabilitação do licitante punido com impedimento ou inidoneidade (Art. 163 da Lei nº 14.133/2021) exige cumulativamente:",
  "options": [
    "Reparação integral do dano, pagamento da multa, transcurso do prazo mínimo de 1 ano (impedimento) ou 3 anos (inidoneidade), cumprimento das condições e análise jurídica prévia.",
    "Apenas um pedido de desculpas por escrito ao prefeito, sem reparar nada.",
    "O decurso de 30 dias e a promessa verbal de não repetir.",
    "Sentença judicial transitada em julgado absolvendo em qualquer outro processo."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 163 da Lei 14.133/21. Reabilitação NÃO é perdão automático: exige reparar o dano + pagar multa + esperar prazo mínimo (1 ano impedimento / 3 anos inidoneidade) + cumprir condições impostas + parecer jurídico. Só então o nome sai do CEIS/CNEP."
},
  {
  "id": 508,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Extincao do Contrato: Hipoteses (Art. 137)",
  "question": "Constituem motivos para extinção do contrato administrativo (Art. 137 da Lei nº 14.133/2021):",
  "options": [
    "O simples desejo do contratado de receber mais, sem qualquer inadimplemento.",
    "Descumprimento ou cumprimento irregular das obrigações, atraso injustificado na execução, subcontratação vedada e razões de interesse público devidamente justificadas.",
    "A troca de prefeito, por si só, sem motivação relacionada ao contrato.",
    "O fato de outra empresa oferecer preço menor após a assinatura do contrato."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 137 da Lei 14.133/21 (rol com ~9 incisos): inadimplemento, mora, alteração social que prejudique, caso fortuito/força maior, interesse público (com indenização do contratado de boa-fé). Troca de governo NÃO extingue contrato (princípio da continuidade e impessoalidade)."
},
  {
  "id": 509,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Subcontratacao (Art. 122)",
  "question": "Quanto à subcontratação de partes do objeto (Art. 122 da Lei nº 14.133/2021), é correto afirmar que:",
  "options": [
    "É sempre livre e total, podendo o vencedor repassar 100% do contrato a terceiros sem avisar.",
    "É proibida em qualquer hipótese, mesmo parcial e prevista em edital.",
    "Somente é admitida se prevista no edital e no contrato, até o limite autorizado, vedada a subcontratação total e da parcela de maior relevância técnica.",
    "Dispensa qualquer responsabilidade do contratado original, que some após repassar."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 122 da Lei 14.133/21. Subcontratação parcial e autorizada: exige previsão, limite e avaliação técnica; vedada a integral e a do 'coração' técnico do objeto. O contratado original continua INTEGRALMENTE responsável pela execução (não há novação)."
},
  {
  "id": 510,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Nulidade do Contrato (Arts. 147-150)",
  "question": "Declarada a nulidade do contrato administrativo (Arts. 147 a 150 da Lei nº 14.133/2021), a consequência quanto aos efeitos já produzidos é que:",
  "options": [
    "O contratado perde tudo, mesmo de boa-fé, e ainda deve demolir o que construiu sem indenização.",
    "A nulidade nunca retroage e o contrato nulo continua válido para sempre.",
    "Os efeitos do contrato nulo são convertidos automaticamente em doação ao particular.",
    "A nulidade opera retroativamente, mas a Administração deve indenizar o contratado de boa-fé pelo que executou e pelo prejuízo da desmobilização, apurando-se a responsabilidade de quem deu causa."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Arts. 147-150 da Lei 14.133/21. Nulidade ex tunc (retroage), mas com indenização ao contratado de BOA-FÉ (o que executou + desmobilização + diferença de preço), sem prejuízo de apurar quem causou a nulidade (servidor/responsável responde). Vedado enriquecimento ilícito da Administração."
},
  {
  "id": 511,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Verbo Haver Impessoal",
  "question": "Assinale a frase em que a concordância do verbo HAVER está em estrita conformidade com a norma-padrão:",
  "options": [
    "Havia muitas divergências entre os parlamentares durante a votação do veto.",
    "Haviam muitos requerimentos sobre a mesa da presidência ontem.",
    "Houveram intensos debates acerca da lei orçamentária na sessão.",
    "Hão muitas vagas para o cargo de técnico legislativo em Meruoca."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. HAVER com sentido de EXISTIR é impessoal: fica na 3ª pessoa do singular (Havia = existiam seriam... não!). 'Muitas divergências' é objeto direto, não sujeito. Em B, C e D o verbo foi indevidamente ao plural. Macete: troque por EXISTIR — se 'existir' iria ao plural, o 'haver' continua singular."
},
  {
  "id": 512,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Verbo Fazer (Tempo e Clima)",
  "question": "Assinale a alternativa em que o verbo FAZER está corretamente flexionado segundo a norma culta:",
  "options": [
    "Fazem dez anos que o regimento interno da Câmara não é atualizado.",
    "Faz dez anos que o regimento interno da Câmara não é atualizado.",
    "Fizeram dias quentes em Meruoca durante todo o verão passado.",
    "Hão de fazer dois meses que a obra foi inaugurada."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. FAZER indicando tempo decorrido ou clima é impessoal (singular): 'Faz dez anos', 'Fez calor ontem'. Em B o verbo foi ao plural indevidamente; em C o correto seria 'Fez dias quentes' (ou 'Fizeram-se' em outra construção); em D há erro duplo. Macete: tempo e clima com FAZER nunca têm sujeito — singular sempre."
},
  {
  "id": 513,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Sujeito Partitivo",
  "question": "Com sujeito partitivo (expressões como 'a maioria', 'a maior parte', 'parte de' seguidas de especificador no plural), a norma-padrão admite:",
  "options": [
    "Exclusivamente o plural, sendo erro grave usar o singular em qualquer caso.",
    "Exclusivamente o singular, sendo proibida a concordância com o especificador plural.",
    "Dupla concordância: o verbo pode ir ao singular (com o núcleo partitivo) ou ao plural (com o especificador) — 'A maioria dos vereadores aprovou/aprovaram o veto'.",
    "A flexão no dual, inexistente em português, com desinência própria."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Sujeito partitivo admite concordância SINGULAR (núcleo: 'A maioria... aprovou') ou PLURAL (atrativa com o especificador: '...aprovaram'). As duas estão certas — a banca INBRASP cobra exatamente essa faculdade. Atenção: se o partitivo vier com artigo definido + especificador, o plural é preferível, mas o singular continua válido."
},
  {
  "id": 514,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Expressoes Percentuais",
  "question": "Quanto à concordância com expressões percentuais seguidas de especificador, a norma-padrão estabelece que:",
  "options": [
    "O verbo fica sempre no singular, mesmo com percentual plural e especificador plural.",
    "O verbo fica sempre no plural, mesmo com '1%' e especificador singular.",
    "Percentuais exigem verbo no futuro do pretérito em qualquer contexto.",
    "O verbo concorda com o número percentual ou, facultativamente, com o especificador — '10% da turma faltou/faltaram à sessão'."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Com percentuais + especificador há dupla possibilidade: concordância gramatical com o número ('10%... faltou') ou atrativa com o especificador ('...faltaram'). Com número no singular ('1% da turma'), o singular é obrigatório se não houver especificador plural divergente. A banca testa a faculdade, não a obrigação."
},
  {
  "id": 515,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia com SE: Apassivadora vs Indice",
  "question": "Assinale a frase com concordância rigorosamente correta quanto ao emprego da partícula SE:",
  "options": [
    "Aprovaram-se as diretrizes orçamentárias prioritárias para o próximo exercício.",
    "Precisam-se de novos servidores para o arquivo da Câmara Municipal.",
    "Vende-se processos antigos arquivados na secretaria municipal.",
    "Aluga-se salas comerciais no centro de Meruoca."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Em A, 'aprovar' é VTD + SE apassivador: 'as diretrizes' é sujeito paciente → plural ('foram aprovadas'). Em B, 'precisar' é VTI: o SE é índice de indeterminação e o verbo deve ficar no SINGULAR ('Precisa-se') — o plural 'Precisam-se' está errado. Em C e D, VTD + SE apassivador exigem plural ('Vendem-se processos', 'Alugam-se salas'). Macete SE: teste 'foram + particípio' — deu certo, concorda; não deu, singular."
},
  {
  "id": 516,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Sujeito Composto",
  "question": "Assinale a alternativa em que a concordância com sujeito composto está correta:",
  "options": [
    "O Presidente e o Relator da Comissão assinou o parecer técnico.",
    "O Presidente e o Relator da Comissão assinaram o parecer técnico.",
    "Vereadores e prefeito faltou à sessão solene de ontem.",
    "As atas e o relatório foi arquivado pela secretaria."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Sujeito composto ANTES do verbo → plural obrigatório ('assinaram'). As demais quebram a regra: B e C com singular, D com singular para dois núcleos. Exceção (núcleos sinônimos ou gradação) não se aplica aqui. Macete: dois sujeitos antes do verbo, verbo no plural sem choro."
},
  {
  "id": 517,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia Nominal: Anexo, Obrigado, Mesmo, Só",
  "question": "Assinale a frase em que a concordância nominal está correta:",
  "options": [
    "Seguem anexo as planilhas de gastos do gabinete da presidência.",
    "Muito obrigado — disse a vereadora ao receber a homenagem.",
    "Seguem anexas as planilhas de gastos do gabinete da presidência.",
    "Eles mesmos redigiu a ata da sessão extraordinária."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. 'Anexo' como adjetivo varia ('anexas as planilhas'); invariável só como advérbio ('em anexo'). 'Obrigado' varia com quem fala ('obrigada' disse a vereadora → C errada). 'Mesmo' como reforço varia ('eles mesmos redigiram' → D errada duplamente). Macete: anexo/obrigado/mesmo/só se comportam como adjetivos — combinam com o nome."
},
  {
  "id": 518,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Um e Outro, Nem Um Nem Outro",
  "question": "Quanto às expressões 'um e outro' e 'nem um nem outro', a norma-padrão determina que:",
  "options": [
    "Ambas exigem sempre o plural, sem exceção.",
    "Ambas exigem sempre o singular, sem exceção.",
    "O verbo fica no infinitivo impessoal em todos os casos.",
    "Com 'um e outro' o verbo vai ao singular ou ao plural ('Um e outro vereador faltou/faltaram'); com 'nem um nem outro' a regra geral é o singular ('Nem um nem outro compareceu')."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. 'Um e outro' = soma com ideia de reciprocidade/exclusão alternada → singular ou plural (facultativo). 'Nem um nem outro' = negação dos dois → singular (regra geral; plural só com ideia enfática de adição, raro em prova). A banca cobra a diferença entre as duas expressões."
},
  {
  "id": 519,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Sujeito Oracional",
  "question": "Quando o sujeito é uma oração (sujeito oracional), o verbo da oração principal fica:",
  "options": [
    "Na 3ª pessoa do singular — 'Falta aprovar dois projetos polêmicos antes do recesso'.",
    "No plural, concordando com o numeral dentro da oração sujeito.",
    "No infinitivo, sem flexão de pessoa.",
    "Na 1ª pessoa do plural, por deferência ao leitor."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Sujeito oracional ('aprovar dois projetos...') não tem número definido → verbo no singular ('Falta aprovar...', 'Convém analisar os vetos', 'Importa concluir as atas'). Pegadinha: o plural dentro da oração ('dois projetos') NÃO puxa o verbo. Macete: substitua a oração por ISSO — 'ISSO falta' (singular)."
},
  {
  "id": 520,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: É Proibido / São Necessários",
  "question": "Assinale a frase em que a concordância com as expressões 'é proibido', 'é necessário' e similares está correta:",
  "options": [
    "É proibida entrada de estranhos no plenário durante a votação.",
    "É proibido entrada de estranhos no plenário durante a votação.",
    "São necessário a assinatura dos dois secretários no autógrafo.",
    "É necessários paciência e diálogo na condução dos trabalhos."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Sem artigo antes do substantivo, a expressão fica INVARIÁVEL ('É proibido entrada', 'É necessário assinatura'). Com artigo, varia ('É proibida A entrada', 'São necessárias AS assinaturas'). Em B falta o artigo para variar; C e D invertem a regra. Macete: sem artigo, trava tudo no singular masculino."
}
]

print(f"[OK] Total de questões S3/D4 geradas: {len(QUESTOES_S3_D4)}")
