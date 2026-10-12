import json

QUESTOES_S3_D5 = [
  {
  "id": 521,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Iniciativa Popular (CF, Art. 29, XIII)",
  "question": "A Constituição Federal assegura a iniciativa popular de projetos de lei de interesse específico do Município. Nesse contexto, assinale a alternativa CORRETA:",
  "options": [
    "A iniciativa popular exige subscrição de no mínimo dez por cento dos eleitores do Município.",
    "A iniciativa popular é vedada aos Municípios, cabendo apenas à União e aos Estados.",
    "A iniciativa popular depende de autorização prévia do Prefeito para ser exercida.",
    "A iniciativa popular manifesta-se por projetos subscritos por no mínimo cinco por cento do eleitorado municipal."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. CF/88, Art. 29, XIII: iniciativa popular mediante manifestação de pelo menos 5% do eleitorado. Distrator A troca o percentual; C nega o instituto; D cria autorização inexistente."
},
  {
  "id": 522,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Iniciativa Privativa do Prefeito",
  "question": "No processo legislativo municipal, são de iniciativa privativa do Prefeito as leis que disponham sobre:",
  "options": [
    "Criação de cargos e funções na administração municipal e regime jurídico dos servidores.",
    "Organização dos serviços internos da Câmara e criação de seus cargos.",
    "Fixação dos subsídios dos Vereadores para a legislatura seguinte.",
    "Alteração do Regimento Interno da Câmara Municipal."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 61, § 1º, II: cargos, funções, empregos, regime jurídico e organização administrativa do Executivo. B e D são da Mesa/Câmara; C é da Câmara (cada legislatura fixa para a subsequente)."
},
  {
  "id": 523,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Iniciativa da Mesa Diretora",
  "question": "Compete privativamente à Mesa Diretora da Câmara a iniciativa de projetos de lei sobre:",
  "options": [
    "Aumento da remuneração dos servidores do Poder Executivo municipal.",
    "Criação de secretarias municipais e definição de suas atribuições.",
    "Organização dos serviços administrativos da Câmara e criação ou extinção de seus cargos.",
    "Instituição de impostos municipais sobre serviços de qualquer natureza."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. A Câmara organiza seus próprios serviços (função atípica administrativa). A e B são do Prefeito; D, embora municipal, não é iniciativa privativa da Mesa."
},
  {
  "id": 524,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Emendas, Substitutivos e Pareceres",
  "question": "Durante a tramitação de um projeto de lei na Câmara, é CORRETO afirmar que:",
  "options": [
    "A emenda supressiva acrescenta dispositivo novo ao texto da proposição.",
    "O substitutivo altera integralmente a proposição, substituindo seu texto.",
    "O parecer das comissões substitui a votação em plenário.",
    "A emenda aditiva elimina parte do texto sem deliberação."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Supressiva ELIMINA; aditiva ACRESCENTA; modificativa ALTERA redação; substitutivo SUBSTITUI tudo. Parecer instrui, não substitui o plenário."
},
  {
  "id": 525,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Sanção: Prazo e Silêncio",
  "question": "Aprovado um projeto de lei pela Câmara de Meruoca, o Prefeito terá 15 dias úteis para sancioná-lo ou vetá-lo. Decorrido esse prazo sem manifestação, é CORRETO afirmar que:",
  "options": [
    "O projeto é arquivado por decurso de prazo.",
    "O silêncio importa sanção tácita do projeto.",
    "O projeto retorna à Câmara para nova votação obrigatória.",
    "O veto é considerado automaticamente oposto."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Simetria com CF, Art. 66, § 3º: silêncio do Executivo em 15 dias úteis = sanção tácita. Não há arquivamento nem veto presumido."
},
  {
  "id": 526,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Veto: Espécies e Motivos",
  "question": "O Prefeito poderá vetar projeto de lei aprovado pela Câmara quando o julgar inconstitucional ou contrário ao interesse público. Sobre o veto, assinale a alternativa CORRETA:",
  "options": [
    "O veto é sempre total, não se admitindo veto parcial.",
    "O veto parcial alcança apenas textos integrais, nunca palavras isoladas.",
    "O veto pode ser total ou parcial, abrangendo inclusive palavra ou expressão isolada.",
    "O veto dispensa motivação, por ser ato discricionário puro."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. CF, Art. 66, § 2º: veto total ou parcial (este, sobre texto integral de artigo, parágrafo, inciso ou alínea — e, na prática legislativa, palavra/expressão). Exige motivação: inconstitucionalidade ou interesse público."
},
  {
  "id": 527,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Apreciação do Veto pela Câmara",
  "question": "Oposto o veto, a Câmara deverá apreciá-lo em 30 dias. É CORRETO afirmar que:",
  "options": [
    "O veto só pode ser rejeitado pelo voto da maioria absoluta dos membros da Câmara.",
    "O veto é derrubado por maioria simples dos vereadores presentes.",
    "Decorrido o prazo sem apreciação, o veto é automaticamente mantido.",
    "A apreciação do veto dispensa quórum mínimo de presença."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. CF, Art. 66, § 4º (simetria municipal): rejeição por maioria absoluta em 30 dias; não apreciado, SOBRESTA as demais deliberações (tranca a pauta) — jamais é mantido automaticamente."
},
  {
  "id": 528,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Promulgação: Prazos e Competência",
  "question": "Rejeitado o veto pela Câmara, o projeto será enviado ao Prefeito para promulgação em 48 horas. Se ele não o fizer, é CORRETO afirmar que:",
  "options": [
    "O Presidente da Câmara promulgará a lei em igual prazo de 48 horas.",
    "A lei jamais entrará em vigor por falta de promulgação.",
    "Qualquer vereador poderá promulgar a lei imediatamente.",
    "O Tribunal de Contas promulgará a lei no lugar do Prefeito."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. CF, Art. 66, § 7º: omisso o Prefeito em 48h, promulga o Presidente da Câmara (e, se este falhar, o Vice). Sem promulgação não há executoriedade — por isso a Constituição define substitutos."
},
  {
  "id": 529,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Fiscalização: Convocação e Sustação",
  "question": "No exercício da função fiscalizadora, a Câmara Municipal poderá:",
  "options": [
    "Convocar Secretários Municipais para prestar pessoalmente informações sobre assuntos de suas pastas.",
    "Demitir servidores do Poder Executivo por decisão de comissão.",
    "Anular atos do Prefeito por conveniência política, sem motivação.",
    "Sustar contratos administrativos regulares sem apontar ilegalidade."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 50: convocação de auxiliares para informações (recusa injustificada = crime de responsabilidade). Sustação de atos/contratos exige ilegalidade apontada (com o TCE). Demissão e anulação imotivada extrapolam a competência do Legislativo."
},
  {
  "id": 530,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Julgamento das Contas: Prefeito x Mesa",
  "question": "Quanto ao julgamento das contas no âmbito municipal, assinale a alternativa CORRETA:",
  "options": [
    "As contas do Prefeito são julgadas pelo Tribunal de Contas, sem qualquer participação da Câmara Municipal.",
    "As contas da Mesa da Câmara são julgadas pela própria Câmara, com total exclusão do Tribunal de Contas.",
    "Todas as contas municipais são julgadas pelo Prefeito, por ser o ordenador de despesas.",
    "As contas do Prefeito são julgadas pela Câmara, com parecer prévio do Tribunal de Contas; as da Mesa são julgadas diretamente pelo Tribunal."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. CF, Arts. 31 e 71: Prefeito = julgado pela Câmara (controle externo político, com parecer do TCE); Mesa/Câmara enquanto unidade gestora = julgada pelo TCE. Distrator A inverte; B exclui o TCE; D concentra tudo no Prefeito."
},
  {
  "id": 531,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Retângulo",
  "question": "O plenário da Câmara possui formato retangular com 12 metros de comprimento por 9 metros de largura. A área total desse plenário é de:",
  "options": [
    "42 m².",
    "54 m².",
    "108 m².",
    "216 m²."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Área = 12 × 9 = 108 m². A soma 42 é o perímetro; 216 é o dobro da área; 54 é a metade."
},
  {
  "id": 532,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Perímetro do Retângulo",
  "question": "Um terreno da Câmara mede 45 metros de comprimento por 25 metros de largura. Para cercá-lo totalmente, serão necessários:",
  "options": [
    "70 metros de cerca.",
    "1.125 metros de cerca.",
    "95 metros de cerca.",
    "140 metros de cerca."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Perímetro = 2 × (45 + 25) = 140 m. 1.125 é a área; 70 é metade do perímetro; 95 não corresponde a nenhuma operação válida."
},
  {
  "id": 533,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Quadrado",
  "question": "Uma sala de arquivo quadrada possui 12 metros de lado. Sua área corresponde a:",
  "options": [
    "48 m².",
    "144 m².",
    "24 m².",
    "72 m²."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Área = 12² = 144 m². 48 é o perímetro; 24 e 72 são frações sem base no cálculo."
},
  {
  "id": 534,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Triângulo",
  "question": "Um jardim triangular em frente à Câmara tem base de 10 metros e altura de 6 metros. Sua área é de:",
  "options": [
    "60 m².",
    "16 m².",
    "36 m².",
    "30 m²."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Área = (10 × 6) / 2 = 30 m². 60 esquece a divisão por 2 — erro clássico da banca; 16 soma base e altura; 36 não tem base no cálculo."
},
  {
  "id": 535,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Círculo",
  "question": "Uma praça circular possui raio de 7 metros. Adotando π = 3,14, sua área é de:",
  "options": [
    "43,96 m².",
    "153,86 m².",
    "21,98 m².",
    "307,72 m²."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Área = 3,14 × 7² = 153,86 m². 43,96 é o comprimento da circunferência (2πr); 307,72 dobra o raio; 21,98 não tem base."
},
  {
  "id": 536,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Volume do Paralelepípedo",
  "question": "Um depósito da Câmara mede 5 metros de comprimento, 4 metros de largura e 2,5 metros de altura. Seu volume é de:",
  "options": [
    "50 m³.",
    "45 m³.",
    "11,5 m³.",
    "100 m³."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Volume = 5 × 4 × 2,5 = 50 m³. 11,5 soma as medidas; 100 dobra o resultado."
},
  {
  "id": 537,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área e Rendimento (Piso)",
  "question": "Uma sala de 8 metros por 6 metros será revestida com placas que cobrem 16 m² cada. Serão necessárias:",
  "options": [
    "2 placas.",
    "4 placas.",
    "3 placas.",
    "6 placas."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Área = 48 m²; 48 / 16 = 3 placas exatas. 2 e 6 vêm de divisões erradas; 4 arredonda sem necessidade."
},
  {
  "id": 538,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Volume e Consumo (Caixa d'Água)",
  "question": "Uma caixa d'água de 2 m por 1,5 m por 1 m abastece um setor que consome 500 litros por dia. Sem reposição, a reserva dura:",
  "options": [
    "3 dias.",
    "5 dias.",
    "7 dias.",
    "6 dias."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Volume = 3 m³ = 3.000 litros; 3.000 / 500 = 6 dias. Exige a conversão m³→litros antes de dividir — pulo clássico da banca."
}
]

print(f"[OK] Total de questões S3/D5 geradas: {len(QUESTOES_S3_D5)}")
