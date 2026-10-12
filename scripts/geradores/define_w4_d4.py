import json

W4_D4_QUESTIONS = [
  {
    "id": 631,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Conceito e Apuração da Receita Corrente Líquida (RCL)",
    "question": "Para fins de aplicação dos limites fiscais estabelecidos pela LRF, a Receita Corrente Líquida (RCL) municipal é apurada computando-se:",
    "options": [
      "As receitas auferidas no mês de referência somadas às dos onze meses imediatamente anteriores.",
      "As receitas totais de capital arrecadadas no exercício financeiro encerrado no ano anterior.",
      "O somatório das receitas correntes previstas pelo Executivo para os próximos dois exercícios.",
      "A arrecadação líquida obtida exclusivamente no último trimestre do ano civil de apuração."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 2º, IV, 'a' da LRF: a Receita Corrente Líquida é apurada 'somando-se as [receitas] recebidas no mês em referência e nos onze anteriores, excluídas as duplicidades'."
  },
  {
    "id": 632,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Limite Global de Despesa com Pessoal nos Municípios (Art. 19, III)",
    "question": "A despesa total com pessoal, em cada período de apuração e em cada ente da Federação, não poderá exceder os percentuais da RCL. No Município, o limite global é de:",
    "options": [
      "50% (cinquenta por cento) da Receita Corrente Líquida para todos os poderes somados.",
      "60% (sessenta por cento) da Receita Corrente Líquida para o conjunto do município.",
      "70% (setenta por cento) da Receita Corrente Líquida incluídas as despesas de capital.",
      "40% (quarenta por cento) da Receita Corrente Líquida apurada nos últimos seis meses."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 19, III da LRF: nos Municípios, a despesa total com pessoal não poderá exceder a 60% (sessenta por cento) da Receita Corrente Líquida."
  },
  {
    "id": 633,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Repartição dos Limites de Pessoal na Esfera Municipal (Art. 20, III)",
    "question": "Na repartição dos limites globais de despesa com pessoal no âmbito municipal, a LRF estabelece de maneira expressa que caberá, respectivamente, ao Legislativo e ao Executivo:",
    "options": [
      "10% para o Poder Legislativo municipal e 50% para a administração do Poder Executivo.",
      "6% para o Poder Legislativo (Câmara) e 54% para o Poder Executivo (Prefeitura local).",
      "8% para a Câmara de Vereadores do município e 52% para os órgãos da Prefeitura.",
      "5% para o Poder Legislativo da cidade e 55% para os quadros gerais do Poder Executivo."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 20, III da LRF: no âmbito municipal, o limite de 60% reparte-se em: a) 6% para o Legislativo (incluído o Tribunal de Contas do Município, se houver); b) 54% para o Executivo."
  },
  {
    "id": 634,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Limite Prudencial de Despesa com Pessoal (Art. 22, parágrafo único)",
    "question": "Se a despesa total com pessoal do Poder Legislativo municipal ultrapassar 95% do seu limite legal máximo (limite prudencial), é vedado à Câmara Municipal:",
    "options": [
      "Conceder qualquer vantagem, aumento, reajuste ou adequação de remuneração a servidores.",
      "Pagar os proventos regulares de aposentadorias e pensões concedidas em períodos anteriores.",
      "Contratar fornecedores de bens essenciais para os serviços de limpeza e conservação predial.",
      "Promover a realização de sessões plenárias ordinárias convocadas pelo presidente da Casa."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 22, parágrafo único, I da LRF: ao atingir 95% do limite (limite prudencial), é vedada a concessão de vantagem, aumento, reajuste ou adequação de remuneração a qualquer título."
  },
  {
    "id": 635,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Limite de Alerta do Tribunal de Contas (Art. 59, § 1º, II)",
    "question": "O Tribunal de Contas competente alertará os poderes municipais quando o montante da despesa total com pessoal ultrapassar determinado percentual do limite máximo, que corresponde a:",
    "options": [
      "80% (oitenta por cento) do limite legal estabelecido para a despesa total com pessoal.",
      "85% (oitenta e cinco por cento) do teto máximo admitido para o encargo remuneratório.",
      "90% (noventa por cento) do limite estabelecido na LRF para o respectivo poder público.",
      "95% (noventa e cinco por cento) do teto máximo de comprometimento orçamentário anual."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 59, § 1º, II da LRF: os Tribunais de Contas alertarão os Poderes quando constatarem que o montante da despesa total com pessoal ultrapassou 90% (noventa por cento) do limite."
  },
  {
    "id": 636,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Vedação de Aumento de Despesa com Pessoal no Fim do Mandato (Art. 21)",
    "question": "Conforme a Lei de Responsabilidade Fiscal, é nulo de pleno direito o ato que resulte em aumento da despesa com pessoal expedido nos:",
    "options": [
      "Trinta dias que antecederem o término do mandato do titular do respectivo Poder.",
      "Sessenta dias finais do exercício orçamentário e financeiro do ente federativo.",
      "Cento e oitenta dias anteriores ao final do mandato do titular de Poder ou órgão.",
      "Noventa dias antecedentes à data da eleição municipal ordinária da respectiva comarca."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 21, parágrafo único da LRF: 'Também é nulo de pleno direito o ato de que resulte aumento da despesa com pessoal [...] expedido nos 180 (cento e oitenta) dias anteriores ao final do mandato do titular do respectivo Poder ou órgão'."
  },
  {
    "id": 637,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Restos a Pagar e Disponibilidade de Caixa no Final do Mandato (Art. 42)",
    "question": "O Art. 42 da LRF proíbe o titular de Poder contrair obrigação de despesa que não possa ser cumprida integralmente dentro dele, ou que tenha parcelas para o ano seguinte sem caixa, nos últimos:",
    "options": [
      "Dois quadrimestres do seu mandato eletivo à frente da administração pública.",
      "Três meses do encerramento oficial do primeiro semestre de seu governo municipal.",
      "Cento e vinte dias antecedentes à homologação final das contas pelo plenário.",
      "Dois meses que antecedem a posse regular dos vereadores eleitos no certame."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 42 da LRF: 'É vedado ao titular de Poder ou órgão [...] nos últimos dois quadrimestres do seu mandato, contrair obrigação de despesa que não possa ser cumprida integralmente dentro dele, ou que tenha parcelas a serem pagas no exercício seguinte sem que haja suficiente disponibilidade de caixa'."
  },
  {
    "id": 638,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Relatório de Gestão Fiscal (RGF - Arts. 54 e 55)",
    "question": "A respeito do Relatório de Gestão Fiscal (RGF) exigido pela Lei Complementar nº 101/2000, é correto afirmar que:",
    "options": [
      "É emitido exclusivamente pelo Poder Executivo, sendo a Câmara dispensada de produzi-lo.",
      "Deve ser emitido ao final de cada quadrimestre pelos chefes dos Poderes, inclusive da Câmara.",
      "Tem publicação exigida apenas anualmente após o parecer técnico do Tribunal de Contas.",
      "Contém unicamente o demonstrativo das despesas com obras e compras de equipamentos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Arts. 54 e 55 da LRF: ao final de cada quadrimestre será emitido pelos titulares dos Poderes e órgãos (inclusive Presidente da Câmara) o Relatório de Gestão Fiscal (RGF)."
  },
  {
    "id": 639,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Relatório Resumido da Execução Orçamentária (RREO - Arts. 52 e 53)",
    "question": "O Relatório Resumido da Execução Orçamentária (RREO), instrumento essencial de transparência da gestão fiscal, é elaborado pelo Poder Executivo com periodicidade:",
    "options": [
      "Mensal, devendo ser publicado até o quinto dia útil de cada mês subsequente.",
      "Bimestral, devendo ser publicado em até trinta dias após o encerramento do bimestre.",
      "Semestral, devendo ser enviado à Câmara de Vereadores até o final de dezembro.",
      "Trimestral, devendo coincidir com as reuniões da comissão de orçamento da Casa."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 52 da LRF: o Relatório Resumido da Execução Orçamentária (RREO) abrange todos os Poderes e é publicado pelo Poder Executivo até trinta dias após o encerramento de cada bimestre."
  },
  {
    "id": 640,
    "category": "especificos",
    "day": "w4_d4",
    "discipline": "LRF — Lei Complementar nº 101/2000",
    "topic": "Instrumentos de Transparência da Gestão Fiscal (Art. 48)",
    "question": "A transparência da gestão fiscal, nos termos do Art. 48 da LRF, é assegurada mediante incentivo à participação popular e realização de audiências públicas, bem como pela liberação ao pleno conhecimento público:",
    "options": [
      "Apenas mediante requerimento formal fundamentado por escrito protocolado na ouvidoria.",
      "Em tempo real, de informações pormenorizadas sobre a execução orçamentária e financeira.",
      "Somente após decorridos cinco anos do término regular da legislatura correspondente.",
      "Exclusivamente por meio de afixação em mural físico restrito ao saguão da prefeitura."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 48, II da LRF: liberação ao pleno conhecimento e acompanhamento da sociedade, em tempo real, de informações pormenorizadas sobre a execução orçamentária e financeira, em meios eletrônicos de acesso público."
  },
  {
    "id": 641,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal: Próclise com Palavras Negativas",
    "question": "Na frase 'Os servidores não se manifestaram sobre a decisão da mesa diretora', a posição proclítica do pronome oblíquo átono 'se' justifica-se gramaticalmente pela presença de:",
    "options": [
      "Palavra de sentido negativo atuando como fator gramatical atrativo obrigatório.",
      "Conjunção coordenativa explicativa posicionada no início do período oracional.",
      "Pronome demonstrativo neutro exercendo função sintática de sujeito do predicado.",
      "Advérbio de modo intercalado entre o núcleo do sujeito e o verbo principal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Palavras de sentido negativo (não, nunca, jamais, nada, ninguém) são fatores de atração obrigatória da próclise na norma-padrão ('não se manifestaram')."
  },
  {
    "id": 642,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal: Próclise com Pronomes Relativos",
    "question": "Assinale a alternativa em que a colocação pronominal proclítica decorre obrigatoriamente da presença de um pronome relativo na oração:",
    "options": [
      "Aqui se discutem com frequência os projetos prioritários da Câmara de Meruoca.",
      "O relatório que me entregaram continha apontamentos sobre a gestão de pessoal.",
      "Talvez se encontrem novas alternativas para equilibrar as contas deste ano.",
      "Alguém lhe informou sobre o prazo final de apresentação das emendas na Casa."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O pronome relativo 'que' ('O relatório que me entregaram') atrai obrigatoriamente o pronome oblíquo 'me' para a posição proclítica (antes do verbo)."
  },
  {
    "id": 643,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal: Próclise com Conjunções Subordinativas",
    "question": "A próclise é obrigatória em orações iniciadas por conjunções subordinativas. Assinale a frase que exemplifica corretamente essa regra gramatical:",
    "options": [
      "Os vereadores reuniram-se logo cedo para apreciar o veto parcial do prefeito.",
      "Embora se esforçassem muito, os técnicos não concluíram o parecer a tempo.",
      "Entreguem-me todos os comprovantes de despesas até o fim do expediente hoje.",
      "Dir-se-ia que a sessão legislativa transcorreria sem debates acalorados hoje."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A conjunção subordinativa concessiva 'Embora' atrai obrigatoriamente o pronome oblíquo para a posição proclítica: 'Embora se esforçassem'."
  },
  {
    "id": 644,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal: Próclise com Pronomes Indefinidos",
    "question": "Assinale a frase em que o pronome oblíquo átono foi posicionado em próclise por força da atração exercida por um pronome indefinido:",
    "options": [
      "Ninguém nos avisou acerca do adiamento da votação do projeto de resolução.",
      "Quando me consultaram formalmente, emiti parecer favorável à tramitação da lei.",
      "Fizeram-se presentes todos os membros da comissão permanente de finanças.",
      "Far-se-á a divulgação dos resultados em diário oficial na data aprazada."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O pronome indefinido 'Ninguém' (que também tem sentido negativo) atrai obrigatoriamente a próclise: 'Ninguém nos avisou'."
  },
  {
    "id": 645,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal: Vedação de Próclise no Início de Período",
    "question": "De acordo com a norma-padrão da Língua Portuguesa, é vedado iniciar período oracional com pronome oblíquo átono. A frase redigida em estrita conformidade com essa regra é:",
    "options": [
      "Me informaram ontem sobre a reabertura do prazo para impugnação do edital.",
      "Te ajudarei na consolidação dos demonstrativos do relatório quadrimestral.",
      "Apresentaram-se pontualmente todos os candidatos convocados para o certame.",
      "Se espera que o plenário vote as matérias regimentais na sessão ordinária."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Na norma-padrão culta (muito cobrada pela INBRASP), não se inicia frase com pronome oblíquo átono. Logo, 'Apresentaram-se' é a forma correta; frases como 'Me informaram' ou 'Se espera' são condenadas gramaticalmente."
  },
  {
    "id": 646,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal: Mesóclise com Verbos no Futuro",
    "question": "A mesóclise é o emprego do pronome intercalado no meio do verbo. Seu uso ocorre legitimamente quando o verbo está conjugado no futuro e não há fator atrativo, como em:",
    "options": [
      "Convidar-me-ão para a solenidade oficial de posse dos novos servidores.",
      "Não calar-me-ei diante das supostas irregularidades apontadas na pasta.",
      "Que Deus ajude-nos na condução harmoniosa dos trabalhos da comissão local.",
      "Todos calaram-se no instante exato em que o presidente iniciou os votos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'Convidar-me-ão' (futuro do presente do indicativo sem palavra atrativa) exige mesóclise. Na alternativa B, o 'Não' atrai próclise ('Não me calarei')."
  },
  {
    "id": 647,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal em Locução Verbal com Particípio",
    "question": "Nas locuções verbais cujo verbo principal encontra-se flexionado no particípio, o pronome oblíquo átono nunca poderá vir colocado:",
    "options": [
      "Após o verbo auxiliar, ainda que sem hífen e sem palavra atrativa antecedente.",
      "Antes do verbo auxiliar, quando houver palavra de sentido negativo no início.",
      "Depois do verbo principal no particípio, sendo essa posição terminantemente proibida.",
      "Ligado por hífen ao verbo auxiliar que estiver conjugado no tempo presente."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Regra fundamental da gramática normativa: NUNCA se coloca pronome oblíquo após particípio (ex: 'tinham avisado-me' é erro crasso; o correto é 'tinham-me avisado' ou 'tinham me avisado')."
  },
  {
    "id": 648,
    "category": "gerais",
    "day": "w4_d4",
    "discipline": "Língua Portuguesa",
    "topic": "Colocação Pronominal em Locução Verbal com Infinitivo",
    "question": "Em locuções verbais formadas por verbo auxiliar seguido de verbo principal no infinitivo, quando NÃO houver palavra atrativa na oração, é gramaticalmente correto:",
    "options": [
      "Posicionar o pronome oblíquo ligado por hífen ao infinitivo ou ao verbo auxiliar.",
      "Empregar o pronome exclusivamente no início da oração antes do sujeito simples.",
      "Omitir obrigatoriamente o pronome oblíquo para evitar vício de redundância.",
      "Intercalar o pronome átono com hífen no interior da raiz do verbo infinitivo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Com infinitivo sem palavra atrativa, o pronome pode ficar em ênclise ao auxiliar ou em ênclise ao infinitivo (ex: 'Quero-lhe dizer' ou 'Quero dizer-lhe'). Ambas as formas são plenamente corretas."
  }
]

print(f"Total w4_d4 preparadas: {len(W4_D4_QUESTIONS)}")
for q in W4_D4_QUESTIONS:
    lens = [len(o) for o in q["options"]]
    cor = q["correctAnswer"]
    max_l = max(lens)
    min_l = min(lens)
    ratio = max_l / min_l
    cor_l = lens[cor]
    print(f"Q{q['id']}: Cor={chr(65+cor)} | Lens={lens} | Ratio={ratio:.2f} | CorLen={cor_l} (Max={max_l})")
