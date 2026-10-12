import json

QUESTOES_S2_D1 = [
  # =========================================================================
  # DIREITO CONSTITUCIONAL: ORGANIZAÇÃO DO ESTADO (CF/88 ARTS. 18 A 31)
  # QUESTÕES 181 A 200 (20 QUESTÕES)
  # =========================================================================
  {
    "id": 181,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Forma de Estado & Autonomia Federativa (Art. 18)",
    "question": "Conforme o Art. 18 da Constituição Federal de 1988, a organização político-administrativa da República Federativa do Brasil compreende a União, os Estados, o Distrito Federal e os Municípios. A respeito dessa estrutura, é correto afirmar que:",
    "options": [
      "Todos são entes autônomos, nos termos da Constituição, sendo vedada qualquer tentativa de secessão ou dissolução do pacto federativo.",
      "A União é soberana e os demais entes federativos não possuem autonomia administrativa ou orçamentária.",
      "Os Municípios subordinam-se administrativamente aos Estados-membros, dependendo de autorização da Assembleia Legislativa para criar seus órgãos.",
      "O Distrito Federal pode ser dividido em Municípios autônomos por lei distrital aprovada por maioria simples."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 18, caput da CF/88: 'A organização político-administrativa da República Federativa do Brasil compreende a União, os Estados, o Distrito Federal e os Municípios, todos autônomos, nos termos desta Constituição'. A República Federativa do Brasil possui SOBERANIA (no plano internacional); os entes federados (União, Estados, DF e Municípios) possuem AUTONOMIA (política, administrativa e financeira). É vedada a secessão (pacto federativo indissolúvel)."
  },
  {
    "id": 182,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Criação, Incorporação e Fusão de Municípios (Art. 18, § 4º)",
    "question": "A criação, a incorporação, a fusão e o desmembramento de Municípios, consoante o Art. 18, § 4º da CF/88 (redação da EC nº 15/96), far-se-ão por:",
    "options": [
      "Lei estadual, dentro do período determinado por lei complementar federal, e dependerão de consulta prévia, mediante plebiscito, às populações dos Municípios envolvidos, após divulgação dos Estudos de Viabilidade Municipal.",
      "Decreto legislativo da Câmara Municipal, homologado pelo Prefeito e pelo Governador do Estado.",
      "Lei complementar municipal, independentemente de plebiscito, desde que aprovada por dois terços dos vereadores.",
      "Portaria do Ministério da Justiça, mediante referendo das populações dos distritos afetados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 18, § 4º da CF/88: Quatro requisitos cumulativos: 1. Lei Complementar Federal (fixando o período); 2. Estudos de Viabilidade Municipal (apresentados e publicados); 3. Plebiscito prévio às populações de TODOS os municípios envolvidos; 4. Lei Estadual ordinária criando/desmembrando o município."
  },
  {
    "id": 183,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Vedações Federativas (Art. 19)",
    "question": "O Art. 19 da Constituição Federal estabelece proibições expressas impostas à União, aos Estados, ao Distrito Federal e aos Municípios. Assinale a conduta expressamente VEDADA a todos esses entes:",
    "options": [
      "Criar distinções entre brasileiros ou preferências entre si.",
      "Manter relações de colaboração de interesse público com cultos religiosos ou igrejas na forma da lei.",
      "Instituir tributos municipais para a manutenção dos serviços de interesse local.",
      "Celebrar convênios de assistência mútua com órgãos de segurança pública."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 19 da CF/88 estabelece 3 vedações absolutas a todos os entes: I - Estabelecer cultos religiosos ou igrejas, subvencioná-los ou embaraçar-lhes o funcionamento (ressalvada colaboração de interesse público); II - Recusar fé aos documentos públicos; III - Criar distinções entre brasileiros ou preferências entre si."
  },
  {
    "id": 184,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Privativa da União (Art. 22)",
    "question": "No padrão recorrente da banca INBRASP, assinale a matéria cuja competência legislativa é PRIVATIVA DA UNIÃO, conforme o Art. 22 da CF/88:",
    "options": [
      "Direito civil, comercial, penal, processual, eleitoral, marítimo, aeronáutico, espacial e do trabalho.",
      "Direito tributário, financeiro, penitenciário, econômico e urbanístico.",
      "Proteção ao meio ambiente e controle da poluição em âmbito local.",
      "Fomento da produção agropecuária e organização do abastecimento alimentar municipal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 22, I da CF/88 (Mnemônico 'CAPACETE DE PIMENTA': Civil, Agrário, Penal, Aeronáutico, Comercial, Eleitoral, Trabalho, Espacial, Desapropriação, Processual, Marítimo). A opção (B) é competência concorrente da União/Estados/DF (Art. 24). A opção (C) e (D) são competências comuns (Art. 23)."
  },
  {
    "id": 185,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Delegação de Matéria Privativa da União (Art. 22, Parágrafo Único)",
    "question": "Embora as matérias do Art. 22 sejam privativas da União, a própria Constituição Federal prevê que os Estados e o DF poderão ser autorizados a legislar sobre questões específicas dessas matérias mediante:",
    "options": [
      "Lei complementar federal.",
      "Medida provisória do Presidente da República.",
      "Resolução conjunta do Senado Federal e da Câmara dos Deputados.",
      "Decreto regulamentar do Ministério da Justiça."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 22, Parágrafo único da CF/88: 'Lei complementar poderá autorizar os Estados a legislar sobre questões específicas das matérias relacionadas neste artigo'. Atenção: somente por Lei Complementar Federal (não por lei ordinária), apenas para questões específicas (não genéricas) e para todos os Estados indistintamente."
  },
  {
    "id": 186,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Comum (Art. 23 da CF/88)",
    "question": "O Art. 23 da CF/88 disciplina a competência comum (material/administrativa) da União, dos Estados, do Distrito Federal e dos Municípios. Constitui exemplo de competência comum de TODOS os entes federados:",
    "options": [
      "Cuidar da saúde e assistência pública, da proteção e garantia das pessoas com deficiência.",
      "Legislar privativamente sobre trânsito e transporte rodoviário interestadual.",
      "Emitir moeda de circulação nacional e fixar taxas de câmbio cambial.",
      "Decretar o estado de sítio e o estado de defesa em todo o território nacional."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 23, II da CF/88: 'cuidar da saúde e assistência pública, da proteção e garantia das pessoas com deficiência'. É competência material compartilhada por todos os entes (União, Estados, DF e Municípios)."
  },
  {
    "id": 187,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Concorrente e Exclusão do Município (Art. 24)",
    "question": "A competência legislativa CONCORRENTE prevista no Art. 24 da CF/88 (para legislar sobre direito tributário, financeiro, penitenciário, econômico e urbanístico) foi atribuída pela Constituição expressamente a:",
    "options": [
      "União, aos Estados e ao Distrito Federal, não figurando os Municípios no rol desse artigo.",
      "União, aos Estados, ao Distrito Federal e a todos os Municípios com mais de cem mil habitantes.",
      "Exclusivamente aos Municípios e ao Distrito Federal.",
      "Apenas à União e aos Municípios que possuam câmara municipal instalada."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 24, caput da CF/88: 'Compete à União, aos Estados e ao Distrito Federal legislar concorrentemente sobre...'. Os MUNICÍPIOS NÃO figuram no Art. 24! A competência dos Municípios em matéria concorrente é apenas SUPLEMENTAR à legislação federal e estadual no que couber, por força do Art. 30, II."
  },
  {
    "id": 188,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Normas Gerais vs Suplementares no Art. 24",
    "question": "No âmbito da legislação concorrente (Art. 24), a competência da União limitar-se-á a estabelecer normas gerais (§ 1º). Sobre essa dinâmica, assinale a opção correta:",
    "options": [
      "A superveniência de lei federal sobre normas gerais suspende a eficácia da lei estadual, no que lhe for contrário.",
      "A superveniência de lei federal revoga expressamente e extingue a lei estadual anterior por completo.",
      "Inexistindo lei federal sobre normas gerais, os Estados ficam impedidos de legislar sobre a matéria.",
      "A competência da União para normas gerais exclui a competência suplementar dos Estados-membros."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 24, § 4º da CF/88: 'A superveniência de lei federal sobre normas gerais suspende a eficácia da lei estadual, no que lhe for contrário'. Pegadinha favorita de concurso: a lei federal NÃO revoga a lei estadual, apenas SUSPENDE SUA EFICÁCIA naquilo que for incompatível."
  },
  {
    "id": 189,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Legislativa do Município (Art. 30, I e II)",
    "question": "De acordo com o Art. 30, I e II da CF/88, compete aos Municípios:",
    "options": [
      "Legislar sobre assuntos de interesse local e suplementar a legislação federal e a estadual no que couber.",
      "Legislar privativamente sobre direito processual civil e normas penais de menor potencial ofensivo.",
      "Fixar normas gerais de direito financeiro nacional com eficácia perante os Estados vizinhos.",
      "Instituir imposto sobre operações relativas à circulação de mercadorias e serviços (ICMS)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 30 da CF/88: 'Compete aos Municípios: I - legislar sobre assuntos de interesse local; II - suplementar a legislação federal e a estadual no que couber'. É o núcleo da autonomia legislativa do Município de Meruoca."
  },
  {
    "id": 190,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Municipal: Serviços Públicos e Transporte (Art. 30, V)",
    "question": "Nos termos do Art. 30, V da CF/88, compete ao Município organizar e prestar, diretamente ou sob regime de concessão ou permissão, os serviços públicos de interesse local, incluído o de:",
    "options": [
      "Transporte coletivo, que tem caráter essencial.",
      "Energia nuclear e exploração de jazidas de petróleo na plataforma continental.",
      "Correios e telégrafos em âmbito interestadual.",
      "Radiodifusão sonora e televisiva educativa regional."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 30, V da CF/88: 'organizar e prestar, diretamente ou sob regime de concessão ou permissão, os serviços públicos de interesse local, incluído o de transporte coletivo, que tem caráter essencial'."
  },
  {
    "id": 191,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Municipal: Solo Urbano e Plano Diretor (Art. 30, VIII)",
    "question": "Compete aos Municípios promover, no que couber, adequado ordenamento territorial, mediante planejamento e controle do uso, do parcelamento e da ocupação do:",
    "options": [
      "Solo urbano.",
      "Espaço aéreo nacional e rotas de aviação civil.",
      "Leito dos rios que banham mais de um Estado da Federação.",
      "Subsolo mineral e reservas de minérios estratégicos da União."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 30, VIII da CF/88: 'promover, no que couber, adequado ordenamento territorial, mediante planejamento e controle do uso, do parcelamento e da ocupação do solo urbano'. É a base para a criação do Plano Diretor e do Código de Obras Municipal."
  },
  {
    "id": 192,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Lei Orgânica Municipal e Quórum de Aprovação (Art. 29)",
    "question": "O Município reger-se-á por lei orgânica, votada em dois turnos, com o interstício mínimo de dez dias, e aprovada por:",
    "options": [
      "Dois terços dos membros da Câmara Municipal, que a promulgará.",
      "Maioria simples dos vereadores presentes, sendo sancionada pelo Prefeito.",
      "Maioria absoluta da Câmara, com homologação obrigatória pelo Governador.",
      "Três quintos dos votos dos parlamentares em sessão conjunta com o Judiciário."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 29, caput da CF/88: 'O Município reger-se-á por lei orgânica, votada em dois turnos, com o interstício mínimo de dez dias, e aprovada por dois terços dos membros da Câmara Municipal, que a promulgará'. O Prefeito NÃO sanciona nem veta a Lei Orgânica; ela é PROMULGADA diretamente pela Mesa da Câmara!"
  },
  {
    "id": 193,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Limites de Subsídio dos Vereadores (Art. 29, VI)",
    "question": "O subsídio dos Vereadores será fixado pelas respectivas Câmaras Municipais em cada legislatura para a subsequente, observados os limites da CF. Em municípios de até dez mil habitantes (faixa base), o subsídio máximo do Vereador corresponderá a qual percentual do subsídio dos Deputados Estaduais?",
    "options": [
      "20% (vinte por cento).",
      "50% (cinquenta por cento).",
      "75% (setenta e cinco por cento).",
      "10% (dez por cento)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 29, VI, 'a' da CF/88: em municípios de até 10.000 habitantes, o subsídio máximo do vereador é 20% do subsídio do Deputado Estadual. A escala sobe: 20%, 30%, 40%, 50%, 60% até 75% em municípios com mais de 500.000 habitantes."
  },
  {
    "id": 194,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Limite de Gasto com Folha de Pagamento da Câmara (Art. 29-A, § 1º)",
    "question": "A Câmara Municipal não gastará mais de qual percentual de sua receita total com folha de pagamento, incluído o gasto com o subsídio de seus Vereadores (Art. 29-A, § 1º da CF)?",
    "options": [
      "70% (setenta por cento).",
      "50% (cinquenta por cento).",
      "60% (sessenta por cento).",
      "80% (oitenta por cento)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 29-A, § 1º da CF/88: 'A Câmara Municipal não gastará mais de setenta por cento de sua receita com folha de pagamento, incluído o gasto com o subsídio de seus Vereadores'. O descumprimento desse limite constitui crime de responsabilidade do Presidente da Câmara (Art. 29-A, § 3º)."
  },
  {
    "id": 195,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Fiscalização Contábil e Tribunal de Contas (Art. 31)",
    "question": "A fiscalização do Município será exercida pelo Poder Legislativo Municipal, mediante controle externo, e pelos sistemas de controle interno do Executivo. O controle externo da Câmara Municipal é exercido com o auxílio do:",
    "options": [
      "Tribunal de Contas do Estado (ou do Município onde houver), cujo parecer prévio só deixa de prevalecer por decisão de dois terços dos vereadores.",
      "Tribunal de Justiça do Estado, mediante sentença transitada em julgado proferida anualmente.",
      "Ministério Público Estadual, através de inquérito civil conclusivo homologado pela Mesa.",
      "Conselho Fiscal de Contabilidade Comunitária eleito pelos contribuintes locais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 31, §§ 1º e 2º da CF/88: O controle externo é auxiliado pelo TCE. O parecer prévio do TCE sobre as contas anuais do Prefeito só pode ser rejeitado por decisão qualificada de DOIS TERÇOS (2/3) dos membros da Câmara Municipal."
  },
  {
    "id": 196,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Vedação de Novos Tribunais de Contas Municipais (Art. 31, § 4º)",
    "question": "Sobre a estrutura de controle externo das contas municipais, o Art. 31, § 4º da Constituição Federal expressamente estabelece que:",
    "options": [
      "É vedada a criação de Tribunais, Conselhos ou órgãos de Contas Municipais.",
      "Todos os municípios com mais de cinquenta mil eleitores devem instituir seu próprio Tribunal de Contas.",
      "Os Municípios podem criar órgãos de contas municipais mediante autorização prévia do Senado Federal.",
      "A fiscalização externa dos municípios dispensa a atuação de Tribunais de Contas estaduais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 31, § 4º da CF/88: 'É vedada a criação de Tribunais, Conselhos ou órgãos de Contas Municipais'. Apenas os tribunais municipais já existentes antes de 1988 (como os dos municípios de São Paulo e Rio de Janeiro) foram mantidos; é proibido criar novos."
  },
  {
    "id": 197,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Contas Municipais à Disposição dos Contribuintes (Art. 31, § 3º)",
    "question": "Conforme o Art. 31, § 3º da CF/88, as contas dos Municípios ficarão, anualmente, durante quantos dias, à disposição de qualquer contribuinte, para exame e apreciação, o qual poderá questionar-lhes a legitimidade, nos termos da lei?",
    "options": [
      "60 (sessenta) dias.",
      "30 (trinta) dias.",
      "90 (noventa) dias.",
      "15 (quinze) dias."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 31, § 3º da CF/88: 'As contas dos Municípios ficarão, no decorrer de sessenta dias, anualmente, à disposição de qualquer contribuinte, para exame e apreciação, o qual poderá questionar-lhes a legitimidade, nos termos da lei'."
  },
  {
    "id": 198,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Bens da União vs Bens dos Estados (Arts. 20 e 26)",
    "question": "A Constituição Federal define expressamente os bens pertencentes à União e aos Estados. Incluem-se entre os BENS DOS ESTADOS-MEMBROS (Art. 26 da CF/88):",
    "options": [
      "As águas superficiais ou subterrâneas, fluentes, emergentes e em depósito, ressalvadas, neste caso, na forma da lei, as decorrentes de obras da União.",
      "Os rios que banhem mais de um Estado da Federação ou sirvam de limite com países vizinhos.",
      "Os potenciais de energia hidráulica e os recursos minerais, inclusive os do subsolo.",
      "As terras devolutas indispensáveis à defesa das fronteiras e fortificações militares."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 26, I da CF/88. As águas que nascem e correm exclusivamente dentro do território de um único estado são bens do Estado. Rios que atravessam mais de um estado ou fazem fronteira com outro país (Art. 20, III), potenciais de energia hidráulica (Art. 20, VIII) e terras de fronteira (Art. 20, II) pertencem à UNIÃO."
  },
  {
    "id": 199,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Intervenção do Estado no Município (Art. 35 da CF/88)",
    "question": "O Estado-membro NÃO intervirá em seus Municípios, SALVO quando (Art. 35 da CF):",
    "options": [
      "Deixar de ser paga, sem motivo de força maior, por dois anos consecutivos, a dívida fundada.",
      "O prefeito pertencer a partido político de oposição ao governador do Estado.",
      "A câmara municipal aprovar moção de desconfiança contra a diretoria do hospital municipal.",
      "O município apresentar índice de desemprego superior à média estadual no semestre."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 35 da CF/88: O Estado só pode intervir no Município se: I - deixar de pagar dívida fundada por 2 anos consecutivos; II - não prestar contas devidas na lei; III - não aplicar o mínimo constitucional em saúde e educação; IV - o TJ prover representação para assegurar princípios ou prover execução de lei/ordem judicial."
  },
  {
    "id": 200,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Intervenção Federal em Municípios localizados em Estado",
    "question": "A respeito da intervenção federal em Municípios localizados dentro de um Estado-membro (como o Município de Meruoca no Estado do Ceará), é correto afirmar que:",
    "options": [
      "A União não intervém diretamente em Municípios localizados em Estados, cabendo ao próprio Estado a intervenção municipal (a intervenção federal direta em município só cabe em Território Federal).",
      "O Presidente da República pode decretar intervenção federal direta em qualquer município sem consultar o Governador do Estado.",
      "A intervenção no município é sempre realizada pelo Ministério Público Federal mediante portaria ministerial.",
      "O Governador do Estado pode intervir na União caso haja atraso no repasse do Fundo de Participação dos Estados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra do Art. 35 e Art. 36 da CF: O Estado é quem intervém em seus Municípios. A União só intervém diretamente em Municípios localizados em TERRITÓRIOS FEDERAIS (Art. 35, caput)."
  },

  # =========================================================================
  # LÍNGUA PORTUGUESA: ESTRUTURA E FORMAÇÃO DE PALAVRAS
  # QUESTÕES 201 A 220 (20 QUESTÕES)
  # =========================================================================
  {
    "id": 201,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Parassintética vs Prefixal e Sufixal",
    "question": "A DERIVAÇÃO PARASSINTÉTICA ocorre quando prefixo e sufixo são agregados simultaneamente ao radical, de modo que a palavra não existe sem um deles. Assinale a alternativa que apresenta um vocábulo formado por derivação parassintética:",
    "options": [
      "Anoitecer (a + noit + ecer)",
      "Infelizmente (in + feliz + mente)",
      "Deslealdade (des + leal + dade)",
      "Reorganização (re + organiza + ção)"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em 'a-noit-ecer', o prefixo 'a-' e o sufixo '-ecer' foram anexados simultaneamente ao radical 'noit-'. Se retirarmos o prefixo, não existe a palavra 'noitecer'; se retirarmos o sufixo, não existe 'anoite'. Já em 'infelizmente' (B) e 'deslealdade' (C), os afixos são independentes ('infeliz' e 'felizmente' existem no idioma, configurando derivação prefixal e sufixal)."
  },
  {
    "id": 202,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Regressiva (Deverbal)",
    "question": "A derivação regressiva (ou deverbal) consiste na formação de substantivos abstratos a partir de verbos, geralmente com a redução da terminação verbal para as vogais temáticas -a, -o, -e. Assinale o vocábulo formado por DERIVAÇÃO REGRESSIVA:",
    "options": [
      "O debate (derivado do verbo debater)",
      "O pescador (derivado do verbo pescar)",
      "A lealdade (derivado do adjetivo leal)",
      "O antebraço (derivado do substantivo braço)"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'O debate' é substantivo abstrato que indica ação, formado pela regressão do verbo 'debater' (perda da desinência infinitiva -r e fixação da vogal -e). Em (B), 'pescador' é derivação sufixal (-dor); em (C), 'lealdade' é derivação sufixal (-dade); em (D), 'antebraço' é derivação prefixal (ante-)."
  },
  {
    "id": 203,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Imprópria (Conversão)",
    "question": "A DERIVAÇÃO IMPRÓPRIA ocorre quando uma palavra muda de classe gramatical no contexto da oração sem que haja qualquer alteração em sua estrutura morfológica. Assinale a frase em que se constata a ocorrência de derivação imprópria:",
    "options": [
      "O 'sim' dos parlamentares foi decisivo para a promulgação da lei.",
      "O servidor realizou um trabalho rápido e eficiente durante a sessão.",
      "Eles discordaram profundamente das propostas apresentadas em plenário.",
      "A comissão permanente elaborou um parecer extremamente detalhado."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O vocábulo 'sim' é originalmente um advérbio de afirmação. Precedido pelo artigo definido 'o' ('O sim dos parlamentares'), foi substantivado (passou a funcionar como substantivo comum), configurando típico caso de derivação imprópria ou conversão."
  },
  {
    "id": 204,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Composição por Justaposição vs Aglutinação",
    "question": "Na formação de palavras por COMPOSIÇÃO, unem-se dois ou mais radicais. Quando os elementos componentes se unem mantendo a integridade fonética e gráfica de cada um, ocorre:",
    "options": [
      "Justaposição (ex: passatempo, pé-de-galinha, girassol).",
      "Aglutinação (ex: planalto, vinagre, pernilongo).",
      "Hibridismo morfológico greco-latino.",
      "Reduplicação silábica imitativa onomatopeica."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Justaposição une palavras sem perda fonética de seus elementos (passa + tempo = passatempo; gira + sol = girassol; embora dobre o 's' para manter o som, não há supressão fonética). Na aglutinação, há perda/fusão fonética (plano + alto = planalto; vinho + acre = vinagre)."
  },
  {
    "id": 205,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Composição por Aglutinação",
    "question": "Assinale a alternativa em que AMBAS as palavras foram formadas pelo processo de COMPOSIÇÃO POR AGLUTINAÇÃO:",
    "options": [
      "Planalto (plano + alto) e vinagre (vinho + acre).",
      "Guarda-roupa e couve-flor.",
      "Beija-flor e pontapé.",
      "Segunda-feira e micro-ondas."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em 'planalto' (plano + alto) e 'vinagre' (vinho + acre), houve alteração fonética e perda de elementos mórficos originais, caracterizando aglutinação. Todas as outras opções trazem termos compostos por justaposição."
  },
  {
    "id": 206,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Identificação do Radical",
    "question": "O RADICAL é o elemento mórfico fundamental e indivisível que contém o significado básico da palavra e é comum às palavras de uma mesma família (cognatas). Identifique a palavra que NÃO pertence à mesma família cognata das demais:",
    "options": [
      "Pedreiro, pedregulho, apedrejar e pedra.",
      "Livraria, livreiro, livrinho e livro.",
      "Terráqueo, terrestre, aterrar e terra.",
      "Cabelo, cabeceira, cabeçalho e cabeçudo."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. 'Cabelo' tem raiz etimológica ligada a pelos capilares (latim 'capillus'). Já 'cabeceira', 'cabeçalho' e 'cabeçudo' derivam do radical de 'cabeça' (latim 'capitia'). As opções A, B e C reúnem palavras legitimamente cognatas com o mesmo radical compartilhado."
  },
  {
    "id": 207,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Desinências Nominais de Gênero e Número",
    "question": "Na morfologia da Língua Portuguesa, as desinências nominais indicam gênero (masculino/feminino) e número (singular/plural). Na palavra 'MENINAS', os morfemas '-A-' e '-S' classificam-se, respectivamente, como:",
    "options": [
      "Desinência nominal de gênero feminino e desinência nominal de número plural.",
      "Vogal temática e sufixo aumentativo.",
      "Radical flexionado e consoante eufônica de ligação.",
      "Afixo derivacional e desinência verbal de pessoa."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Na estrutura 'MENIN-A-S': 'menin-' é o radical; '-a-' é a desinência nominal de gênero feminino; '-s' é a desinência nominal de número plural."
  },
  {
    "id": 208,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Vogal Temática Verbal e Tema",
    "question": "A VOGAL TEMÁTICA liga o radical às desinências e indica a conjugação verbal (1ª -a, 2ª -e, 3ª -i). O radical somado à vogal temática constitui o:",
    "options": [
      "Tema.",
      "Afixo composto.",
      "Cognato absoluto.",
      "Morfema zero."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Na morfologia verbal: Radical + Vogal Temática = TEMA. Exemplo: no verbo 'cantar', 'cant-' é o radical e '-a-' é a vogal temática da 1ª conjugação. O tema é 'canta-'."
  },
  {
    "id": 209,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Vogais e Consoantes de Ligação",
    "question": "Vogais e consoantes de ligação são elementos fonéticos eufônicos inseridos entre morfemas unicamente para facilitar a pronúncia, desprovidos de significado gramatical próprio. Há uma CONSOANTE DE LIGAÇÃO na palavra:",
    "options": [
      "Cafeteira (café + -t- + eira)",
      "Infelizmente (in + feliz + mente)",
      "Desleal (des + leal)",
      "Pedrada (pedra + ada)"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em 'café' + '-eira', a junção direta geraria o cacófato 'cafeeira'. Inseriu-se a consoante eufônica '-t-' (cafeteira) exclusivamente para fluidez fonética. Outros exemplos: pau-l-ada, cha-l-eira."
  },
  {
    "id": 210,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Hibridismo",
    "question": "O processo de formação de palavras em que ocorre a junção de elementos mórficos originários de IDIOMAS DIFERENTES é denominado:",
    "options": [
      "Hibridismo (ex: televisão: tele grego + visão latim; burocracia: bureau francês + cracia grego).",
      "Neologismo fonético espontâneo.",
      "Siglonimização e acrônimo.",
      "Onomatopeia imitativa de ruídos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Hibridismo é a formação de uma palavra com radicais ou afixos de línguas distintas. Exemplos clássicos: Televisão (tele = grego, visão = latim), Burocracia (bureau = francês, cracia = grego), Automóvel (auto = grego, móvel = latim)."
  },
  {
    "id": 211,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Onomatopeia",
    "question": "Assinale a alternativa que apresenta vocábulos formados por ONOMATOPEIA (reprodução aproximada de sons ou ruídos da natureza e de objetos):",
    "options": [
      "Tic-tac, zunzum, miau e coaxar.",
      "Amanhecer, entardecer e anoitecer.",
      "Fidalgo, aguardente e pernalta.",
      "Couve-flor, guarda-chuva e girassol."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A onomatopeia consiste na criação de vocábulos que buscam imitar sons ou ruídos reais: tic-tac (relógio), zunzum (zumbido), miau (gato), coaxar (sapo), pingue-pongue."
  },
  {
    "id": 212,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Prefixal com Prefixo Negativo",
    "question": "Os prefixos 'in-' (latim) e 'a-' (grego) denotam privação ou negação. Assinale a opção em que AMBAS as palavras apresentam prefixos com valor semântico de NEGAÇÃO:",
    "options": [
      "Inativo e atípico.",
      "Importar e adjunto.",
      "Progresso e antebraço.",
      "Submarino e supersensível."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'Inativo' = não ativo (in- negativo latino); 'Atípico' = não típico (a- de privação grego). Em (B), 'importar' traz o 'in-' com sentido de movimento para dentro; em (C), 'pro-' denota para a frente; em (D), 'sub-' significa debaixo."
  },
  {
    "id": 213,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Sufixos Formadores de Substantivos Abstratos",
    "question": "Os sufixos nominalizadores transformam verbos ou adjetivos em substantivos. O sufixo presente em 'ORGANIZAÇÃO' (-ção) indica precipuamente a noção de:",
    "options": [
      "Ação ou resultado de uma ação.",
      "Lugar ou estabelecimento comercial.",
      "Profissão ou agente executor.",
      "Grau diminutivo pejorativo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O sufixo '-ção' (organiza + ção, promulga + ção, delibera + ção) é um sufixo nominalizador deverbal que exprime o ato, ação ou o resultado da ação do verbo."
  },
  {
    "id": 214,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Siglas e Acrônimos",
    "question": "No vocabulário administrativo e legislativo, as palavras formadas pela combinação das letras ou sílabas iniciais de uma denominação composta (ex: MERCOSUL, UNESCO, EMBRAPA) que podem ser pronunciadas como uma palavra comum denominam-se:",
    "options": [
      "Acrônimos.",
      "Estrangeirismos arcaicos.",
      "Derivações parassintéticas truncadas.",
      "Arcaísmos de composição por justaposição."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Acrônimo é a sigla que se pronuncia como uma palavra contínua e natural da língua (ex: Embrapa, Mercosul, Petrobras, Unesco). Diferencia-se das siglas puras que exigem soletração letra a letra (ex: CPF, OAB, IPTU)."
  },
  {
    "id": 215,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Neologismo",
    "question": "O processo linguístico pelo qual novos termos são criados ou importados para suprir a necessidade de nomear novos conceitos científicos, tecnológicos ou socioculturais (ex: 'deletar', 'tuitar', 'printar') é chamado de:",
    "options": [
      "Neologismo.",
      "Solecismo de regência.",
      "Pleonasmo de reforço.",
      "Ambiguidade estilística."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Neologismo é a criação de palavras novas ou a atribuição de novos significados a termos preexistentes na língua, refletindo inovações da sociedade e tecnologia."
  },
  {
    "id": 216,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Palavra Primitiva vs Derivada",
    "question": "Em relação à relação morfológica entre primitivo e derivado, assinale o par em que a segunda palavra é DERIVADA da primeira:",
    "options": [
      "Lei -> Legalizar.",
      "História -> Histórico (ambas são primitivas).",
      "Vento -> Ventania (ambas são formadas por composição).",
      "Flor -> Floricultura (formada unicamente por hibridismo)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'Lei' é vocábulo primitivo (não se origina de outra palavra na língua portuguesa). 'Legalizar' é derivada de 'legal' (sua vez derivada de lei) por sufixação (-izar)."
  },
  {
    "id": 217,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Abreviatura vs Sigla vs Redução (Abreviação Vocabular)",
    "question": "O processo de ABREVIAÇÃO VOCABULAR (ou redução) consiste na eliminação de uma parte da palavra a fim de economizar tempo e esforço na comunicação falada ou escrita. Assinale o exemplo de abreviação vocabular:",
    "options": [
      "Foto (de fotografia), moto (de motocicleta) e fone (de telefone).",
      "OAB (Ordem dos Advogados do Brasil).",
      "Passatempo (de passa + tempo).",
      "Amanhecer (de a + manhã + ecer)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Abreviação vocabular (ou redução) é a redução de uma palavra longa mantendo o significado original: foto (fotografia), moto (motocicleta), fone (telefone), quilo (quilograma), cine (cinema)."
  },
  {
    "id": 218,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Desinência Modo-Temporal Verbal",
    "question": "Na forma verbal 'ESTUDÁVAMOS', o segmento mórfico '-VA-' classifica-se como:",
    "options": [
      "Desinência modo-temporal (indica pretérito imperfeito do modo indicativo).",
      "Desinência número-pessoal (indica primeira pessoa do plural).",
      "Vogal de ligação eufônica.",
      "Sufixo adverbializatório de intensidade."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em 'estud-á-va-mos': 'estud-' é o radical; '-a-' é a vogal temática; 'estuda-' é o tema; '-va-' é a desinência modo-temporal (DMT) do pretérito imperfeito do indicativo; '-mos' é a desinência número-pessoal (DNP) de 1ª pessoa do plural."
  },
  {
    "id": 219,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Análise Estrutural Completa de Vocábulo",
    "question": "Assinale a alternativa em que a divisão mórfica do vocábulo 'DESALINHAMENTO' e a identificação de seus elementos estão inteiramente corretas:",
    "options": [
      "Des- (prefixo) + alinh- (radical) + -a- (vogal temática) + -mento (sufixo derivacional formador de substantivo).",
      "Desalinha- (radical único) + -mento (desinência de número).",
      "Des- (afixo flexional) + alinhamento (palavra composta por aglutinação).",
      "De- (prefixo) + salinha (radical) + -mento (sufixo aumentativo)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'Desalinhamento' estrutura-se por: Prefixo 'des-' (sentido de negação/inversão) + Radical 'alinh-' (de linha) + Vogal temática '-a-' + Sufixo nominalizador '-mento' (formador de substantivo abstrato que indica ação ou resultado)."
  },
  {
    "id": 220,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Identificação Geral dos Processos em Concurso",
    "question": "Relacione as colunas quanto ao processo de formação de palavras:\n(1) Justaposição\n(2) Aglutinação\n(3) Parassíntese\n(4) Derivação Imprópria\n\n( ) Envergonhar\n( ) Guarda-noturno\n( ) O olhar triste da testemunha\n( ) Pernalta\n\nA sequência correta de preenchimento, de cima para baixo, é:",
    "options": [
      "3 — 1 — 4 — 2",
      "1 — 3 — 2 — 4",
      "3 — 2 — 1 — 4",
      "4 — 1 — 3 — 2"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Envergonhar: en- + vergonh- + -ar (parassíntese: 3); Guarda-noturno: guarda + noturno sem perda (justaposição: 1); O olhar triste: 'olhar' substantivado pelo artigo 'o' (derivação imprópria: 4); Pernalta: perna + alta com perda da vogal 'a' (aglutinação: 2). Sequência: 3, 1, 4, 2."
  }
]

print(f"[OK] Total de questões da Semana 2 / Dia 1 geradas: {len(QUESTOES_S2_D1)}")
