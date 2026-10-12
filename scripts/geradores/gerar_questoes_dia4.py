import json

# Definindo as 40 questões do Dia 4 (IDs 61 a 100)
QUESTOES_DIA4 = [
  # -------------------------------------------------------------------------
  # LÍNGUA PORTUGUESA (IDs 61 a 75: Fonologia, Ortografia, Acentuação e Crase)
  # -------------------------------------------------------------------------
  {
    "id": 61,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Gráfica: Regra das Proparoxítonas",
    "question": "No padrão da banca INBRASP, a regra de acentuação gráfica que justifica o acento na palavra 'LEGISLATIVO' não existe pois a palavra é paroxítona sem acento. Entretanto, assinale a alternativa em que TODAS as palavras são acentuadas rigorosamente pela regra das proparoxítonas:",
    "options": [
      "Político, cômputo, câmara e déficit.",
      "Técnico, caráter, público e relatório.",
      "Orgânico, histórico, mérito e autarquia.",
      "Público, relógio, secretária e país."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Todas as palavras de (A) são proparoxítonas (po-LÍ-ti-co, CÔM-pu-to, CÂ-ma-ra, DÉ-fi-cit), que são 100% acentuadas. Em (B), 'caráter' e 'relatório' são paroxítonas; em (C), 'autarquia' é paroxítona terminada em ditongo; em (D), 'país' é hiato e 'relógio' é paroxítona terminada em ditongo."
  },
  {
    "id": 62,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Gráfica: Regra dos Hiatos",
    "question": "Assinale a alternativa em que a palavra destacada recebe acento gráfico pela MESMA regra que justifica o acento na palavra 'SAÚDE':",
    "options": [
      "O servidor municipal goza de total autonomia no exercício da função pública.",
      "A saída de emergência da Câmara Municipal foi desobstruída pela fiscalização.",
      "O vereador realizou um discurso com alto teor patriótico perante a mesa.",
      "A assembleia legislativa deliberou favoravelmente à concessão do benefício."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. 'Sa-ú-de' e 'sa-í-da' são acentuadas pela REGRA DO HIATO: a vogal 'i' ou 'u' tônica, segunda vogal do hiato, sozinha na sílaba (ou com 's'), sem ser seguida de 'nh' e sem estar precedida de ditongo em paroxítona. 'Autonomia' e 'assembleia' não recebem acento; 'patriótico' é proparoxítona."
  },
  {
    "id": 63,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Ortografia: Novo Acordo Ortográfico (Ditongos Abertos)",
    "question": "De acordo com o Acordo Ortográfico vigente da Língua Portuguesa, os ditongos abertos 'EI' e 'OI' perderam o acento gráfico quando se encontram na posição de:",
    "options": [
      "Monossílabos tônicos (ex: dói, réis, méis).",
      "Oxítonas (ex: herói, troféu, constrói).",
      "Paroxítonas (ex: ideia, jiboia, assembleia, heroico).",
      "Proparoxítonas (ex: helicóptero, cômputo)."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O Acordo Ortográfico eliminou o acento dos ditongos abertos 'EI' e 'OI' exclusivamente nas palavras PAROXÍTONAS (i-dei-a, ji-boi-a, as-sem-blei-a, pla-tei-a). Nas oxítonas e monossílabos tônicos, o acento PERMANECE: he-rói, cons-trói, céu, réis."
  },
  {
    "id": 64,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Fonologia: Contagem de Fonemas e Letras",
    "question": "A palavra 'MUNICÍPIO' e a palavra 'TRABALHO' apresentam, respectivamente, o seguinte número de letras e fonemas:",
    "options": [
      "9 letras e 9 fonemas; 8 letras e 7 fonemas.",
      "9 letras e 8 fonemas; 8 letras e 8 fonemas.",
      "9 letras e 10 fonemas; 8 letras e 6 fonemas.",
      "8 letras e 8 fonemas; 7 letras e 6 fonemas."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em 'MU-NI-CÍ-PIO': 9 letras e 9 fonemas (não há dígrafos). Em 'TRA-BA-LHO': 8 letras e 7 fonemas, pois o dígrafo 'lh' representa um único fonema consonantal [λ]."
  },
  {
    "id": 65,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Fonologia: Encontros Vocálicos (Hiato vs Ditongo)",
    "question": "Considere as palavras: I. História; II. Juízes; III. Rainha; IV. Coordenar. Classificam-se, respectivamente, quanto aos encontros vocálicos, como:",
    "options": [
      "Ditongo crescente, Hiato, Hiato e Hiato.",
      "Ditongo decrescente, Ditongo crescente, Tritongo e Hiato.",
      "Hiato, Ditongo crescente, Ditongo decrescente e Tritongo.",
      "Ditongo crescente, Hiato, Ditongo decrescente e Hiato."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. I. His-tó-ria: semivogal + vogal (ditongo crescente oral); II. Ju-í-zes: duas vogais em sílabas separadas (hiato acentuado); III. Ra-i-nha: duas vogais em sílabas separadas (hiato, não acentuado antes de 'nh'); IV. Co-or-de-nar: repetição de vogais em sílabas separadas (hiato)."
  },
  {
    "id": 66,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego do Sinal Indicativo de Crase: Casos Proibidos",
    "question": "O emprego do sinal indicativo de crase é rigorosamente PROIBIDO na seguinte frase:",
    "options": [
      "O projeto de lei foi remetido à Comissão de Constituição e Justiça.",
      "O presidente da Câmara dirigiu-se a todos os vereadores com respeito.",
      "A sessão solene teve início às nove horas da manhã em ponto.",
      "O servidor compareceu à reunião extraordinária do plenário."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Em 'a todos os vereadores', o 'a' antecede pronome indefinido ('todos') e palavra masculina no plural ('vereadores'). Não há artigo definido feminino 'a', logo a crase é terminantemente proibida."
  },
  {
    "id": 67,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego da Crase: Casos Facultativos",
    "question": "A ocorrência do acento grave indicativo de crase é FACULTATIVA (opcional) em:",
    "options": [
      "O técnico legislativo entregou a ata à sua chefia imediata.",
      "A comissão parlamentar passou a investigar os fatos noticiados.",
      "O cidadão compareceu a pé até a portaria do prédio público.",
      "Ele redigiu a ata a lápis para posterior digitação oficial."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A crase é facultativa em três casos clássicos (Mnemônico 'NOME DE MULHER, ATÉ, MINHA'): 1. Antes de pronome possessivo feminino no singular ('à sua' ou 'a sua'); 2. Antes de nomes próprios femininos sem especificador ('à Maria' ou 'a Maria'); 3. Após a preposição 'até' ('até à' ou 'até a')."
  },
  {
    "id": 68,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego da Crase: Antes de Verbos",
    "question": "Analise a frase: 'O relator começou ___ expor as razões do veto e colocou o parecer ___ disposição da bancada'. Assinale a alternativa que preenche correta e respectivamente as lacunas:",
    "options": [
      "a — à",
      "à — à",
      "a — a",
      "à — a"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Antes de verbo ('expor'), não ocorre artigo feminino, logo usa-se apenas a preposição simples 'a' (sem crase). Na expressão 'à disposição', trata-se de locução adverbial/prepositiva com núcleo feminino, exigindo crase obrigatória."
  },
  {
    "id": 69,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Ortografia Oficial: Emprego de Mal vs Mau",
    "question": "Assinale a alternativa em que o termo sublinhado foi empregado em estrita conformidade com o padrão culto da língua:",
    "options": [
      "O servidor desempenhou mau as atribuições do seu cargo comissionado.",
      "Ele é um homem mal, incapaz de agir com empatia no atendimento ao público.",
      "Mal o presidente declarou aberta a sessão, o plenário ficou em silêncio.",
      "O projeto de lei foi mau redigido pela assessoria parlamentar."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. 'Mal' é conjunção temporal com sentido de 'assim que / logo que' ('Mal o presidente declarou aberta...'). Em (A), deveria ser 'desempenhou mal' (oposto de bem); em (B), 'homem mau' (oposto de bom); em (D), 'mal redigido' (oposto de bem redigido)."
  },
  {
    "id": 70,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Divisão Silábica e Separação de Dígrafos",
    "question": "Assinale a alternativa em que a partição silábica de todas as palavras está inteiramente CORRETA:",
    "options": [
      "Sub-lin-har, ex-ce-ção, car-ro e pneu-má-ti-co.",
      "Su-bli-nhar, ex-ce-ção, car-ro e p-neu-má-ti-co.",
      "Sub-li-nhar, e-xce-ção, ca-rro e pneu-má-ti-co.",
      "Sub-lin-har, ex-ce-ç-ão, ca-rro e pne-u-má-ti-co."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Os dígrafos 'rr', 'ss', 'sc', 'sç', 'xc' se SEPARAM na partição silábica (ex-ce-ção, car-ro). O prefixo 'sub' seguido de consoante mantém o 'b' na sílaba anterior: sub-lin-har. Encontros consonantais no início de palavra não se separam: pneu-má-ti-co."
  },
  {
    "id": 71,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego do Porquê / Por quê / Porque / Por que",
    "question": "Identifique a frase em que o uso do porquê está rigorosamente CORRETO:",
    "options": [
      "O projeto foi rejeitado por que a comissão apontou inconstitucionalidade.",
      "Não entendi o porquê de tanta discussão em torno de uma emenda simples.",
      "Os vereadores protestaram porque? Não houve justificativa clara.",
      "Por quê você não compareceu à audiência pública de Meruoca ontem?"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. 'O porquê' é substantivo (vem acompanhado de artigo ou determinante) e deve ser grafado junto e com acento circunflexo. Em (A), deveria ser 'porque' (conjunção explicativa/causal); em (C), 'por quê' (fim de frase interrogativa); em (D), 'Por que' (início de pergunta direta, separado e sem acento)."
  },
  {
    "id": 72,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Gráfica: Oxítonas Terminadas em A, E, O, EM",
    "question": "A palavra 'TAMBÉM' e a palavra 'PARABÉNS' recebem acento gráfico pela regra de acentuação das palavras:",
    "options": [
      "Oxítonas terminadas em -em e -ens.",
      "Paroxítonas terminadas em consoante nasal.",
      "Monossílabos tônicos terminados em ditongo nasal.",
      "Proparoxítonas aparentes ou eventuais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Acentuam-se as palavras oxítonas terminadas em -a(s), -e(s), -o(s), -em e -ens (ex: tam-bém, pa-ra-béns, ar-ma-zém, vinténs)."
  },
  {
    "id": 73,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Crase diante de Pronomes Demonstrativos",
    "question": "Assinale a frase em que a crase foi empregada CORRETAMENTE antes de pronome demonstrativo:",
    "options": [
      "Refiro-me àquele vereador que presidiu a comissão de finanças.",
      "Ele entregou o requerimento à esta servidora do protocolo.",
      "O parecer foi contrário à essa proposta orçamentária do prefeito.",
      "A moção de repúdio foi dirigida à quem faltou à sessão solene."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Ocorre crase na junção da preposição 'a' (exigida pela regência de 'referir-se a') com a letra 'a' inicial dos pronomes aquele, aquela, aquilo: 'Refiro-me àquele'. Antes de 'esta', 'essa' ou 'quem', a crase é proibida."
  },
  {
    "id": 74,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Diferencial e Novo Acordo",
    "question": "O Novo Acordo Ortográfico manteve o acento gráfico diferencial em um número muito reduzido de pares de palavras. Assinale a alternativa que contém uma palavra com acento diferencial OBRIGATÓRIO mantido:",
    "options": [
      "Pôde (pretérito perfeito do verbo poder, em oposição a pode, presente).",
      "Pára (verbo parar, em oposição à preposição para).",
      "Pêlo (substantivo, em oposição à contração pelo).",
      "Pólo (substantivo, em oposição à combinação polo)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Acordo Ortográfico aboliu o acento diferencial de pára/para, pêlo/pelo, pólo/polo. Foi MANTIDO obrigatoriamente em: PÔDE (passado) vs. PODE (presente) e PÔR (verbo) vs. POR (preposição). É facultativo em fôrma/forma."
  },
  {
    "id": 75,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego do Hífen com Prefixos",
    "question": "Com o Novo Acordo Ortográfico, usa-se o hífen quando o prefixo termina com a mesma vogal com que se inicia o segundo elemento. Assinale a grafia CORRETA:",
    "options": [
      "Micro-ondas e anti-inflamatório.",
      "Microondas e antiinflamatório.",
      "Micro-ondas e antiinflamatório.",
      "Microondas e anti-inflamatório."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra geral do hífen com prefixos: vogais iguais se separam por hífen (mi-cro-on-das, an-ti-in-fla-ma-tó-rio, au-to-ob-ser-va-ção); vogais diferentes se unem sem hífen (au-toes-ti-ma, an-ti-a-é-re-o)."
  },

  # -------------------------------------------------------------------------
  # DIREITO CONSTITUCIONAL: ARTS. 6º A 11 DA CF/88 (IDs 76 a 90: Direitos Sociais)
  # -------------------------------------------------------------------------
  {
    "id": 76,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 6º da CF/88: Rol dos Direitos Sociais",
    "question": "O Art. 6º da Constituição Federal de 1988 estabelece os direitos sociais fundamentais. Assinale a alternativa que contém APENAS direitos sociais expressamente elencados no caput desse dispositivo:",
    "options": [
      "Educação, saúde, alimentação, trabalho, moradia e transporte.",
      "Propriedade, liberdade de crença, previdência social e segurança.",
      "Inviolabilidade de domicílio, direito de herança, lazer e trabalho.",
      "Nacionalidade, direitos políticos, saúde e assistência aos desamparados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico 'EDU MORA LÁ, SAÚ TRABALHA ALI EM TRANSPORTE, SEGURA ASSIS PROSSEGUE PRENDENDO': Educação, Saúde, Alimentação, Trabalho, Moradia, Transporte, Lazer, Segurança, Previdência Social, Proteção à Maternidade e à Infância, e Assistência aos Desamparados (Art. 6º da CF/88)."
  },
  {
    "id": 77,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XIII da CF/88: Duração do Trabalho",
    "question": "Conforme o Art. 7º, XIII, da CF/88, a duração do trabalho normal dos trabalhadores urbanos e rurais não poderá ser superior a:",
    "options": [
      "8 horas diárias e 44 horas semanais, facultada a compensação de horários e a redução da jornada, mediante acordo ou convenção coletiva de trabalho.",
      "8 horas diárias e 40 horas semanais, vedada qualquer forma de compensação de horário.",
      "6 horas diárias e 36 horas semanais para todas as categorias profissionais urbanas.",
      "10 horas diárias e 48 horas semanais, desde que haja autorização do sindicato da categoria."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XIII da CF/88: 'duração do trabalho normal não superior a oito horas diárias e quarenta e quatro semanais, facultada a compensação de horários e a redução da jornada, mediante acordo ou convenção coletiva de trabalho'."
  },
  {
    "id": 78,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XIV da CF/88: Turnos Ininterruptos de Revezamento",
    "question": "A jornada de trabalho fixada pela Constituição Federal para o trabalho realizado em turnos ininterruptos de revezamento é de:",
    "options": [
      "6 horas, salvo negociação coletiva.",
      "8 horas improrrogáveis em qualquer hipótese.",
      "4 horas diárias com intervalo de 30 minutos.",
      "12 horas seguidas de 36 horas de descanso."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XIV da CF/88: 'jornada de seis horas para o trabalho realizado em turnos ininterruptos de revezamento, salvo negociação coletiva'."
  },
  {
    "id": 79,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XVI da CF/88: Remuneração da Hora Extra",
    "question": "Nos termos da Constituição Federal de 1988, a remuneração do serviço extraordinário (horas extras) será superior, no mínimo, à do normal em:",
    "options": [
      "50% (cinquenta por cento).",
      "20% (vinte por cento).",
      "100% (cem por cento).",
      "30% (trinta por cento)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XVI da CF/88: 'remuneração do serviço extraordinário superior, no mínimo, em cinquenta por cento à do normal'."
  },
  {
    "id": 80,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XVIII e XIX da CF/88: Licenças Gestante e Paternidade",
    "question": "Quanto à proteção à maternidade e à paternidade, a CF/88 assegura licença à gestante, sem prejuízo do emprego e do salário, com a duração de:",
    "options": [
      "120 dias, e licença-paternidade nos termos fixados em lei.",
      "90 dias, e licença-paternidade de 30 dias improrrogáveis.",
      "180 dias obrigatórios em todas as empresas privadas do país.",
      "60 dias, renováveis por igual período mediante atestado médico."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XVIII da CF/88: 'licença à gestante, sem prejuízo do emprego e do salário, com a duração de cento e vinte dias'. A prorrogação para 180 dias (Programa Empresa Cidadã / Estatutos de Servidores) decorre de lei, mas o texto constitucional expresso fixa 120 dias."
  },
  {
    "id": 81,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XXXIII da CF/88: Trabalho do Menor",
    "question": "Sobre a proibição de trabalho a menores de idade, a Constituição Federal estabelece expressamente a proibição de:",
    "options": [
      "Trabalho noturno, perigoso ou insalubre a menores de dezoito e de qualquer trabalho a menores de dezesseis anos, salvo na condição de aprendiz, a partir de quatorze anos.",
      "Qualquer trabalho a menores de dezoito anos, mesmo na condição de aprendiz em empresas familiares.",
      "Trabalho noturno a menores de dezesseis anos e de qualquer trabalho a menores de catorze anos, sem exceções.",
      "Trabalho insalubre a menores de vinte e um anos e aprendizagem a partir de doze anos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XXXIII da CF/88 (redação da EC 20/98): 'proibição de trabalho noturno, perigoso ou insalubre a menores de dezoito e de qualquer trabalho a menores de dezesseis anos, salvo na condição de aprendiz, a partir de quatorze anos'. Regra de ouro da INBRASP: 18 (noturno/perigoso/insalubre), 16 (regra geral de vedação) e 14 (aprendiz)."
  },
  {
    "id": 82,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XXI da CF/88: Aviso Prévio",
    "question": "A Constituição Federal de 1988 assegura o aviso prévio proporcional ao tempo de serviço, sendo de no mínimo:",
    "options": [
      "30 (trinta) dias, nos termos da lei.",
      "15 (quinze) dias para contratos de até um ano.",
      "60 (sessenta) dias para todos os trabalhadores urbanos.",
      "45 (quarenta e cinco) dias incondicionalmente."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XXI da CF/88: 'aviso prévio proporcional ao tempo de serviço, sendo no mínimo de trinta dias, nos termos da lei'."
  },
  {
    "id": 83,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XVII da CF/88: Férias Remuneradas",
    "question": "O gozo de férias anuais remuneradas assegurado pela Constituição Federal de 1988 prevê o pagamento de remuneração com acréscimo de:",
    "options": [
      "Pelo menos, um terço a mais do que o salário normal.",
      "Cinquenta por cento a mais do que a remuneração ordinária.",
      "Metade do salário base calculado sobre o último mês de trabalho.",
      "Vinte por cento a título de gratificação de descanso anual."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XVII da CF/88: 'gozo de férias anuais remuneradas com, pelo menos, um terço a mais do que o salário normal'."
  },
  {
    "id": 84,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, IX da CF/88: Remuneração do Trabalho Noturno",
    "question": "Nos termos do Art. 7º, IX, da CF/88, em relação ao trabalho noturno, é direito constitucional do trabalhador:",
    "options": [
      "Remuneração do trabalho noturno superior à do diurno.",
      "Jornada máxima reduzida para 4 horas sem adicional monetário.",
      "Folga semanal dobrada para quem cumpre jornada noturna.",
      "Aposentadoria especial automática aos cinco anos de trabalho noturno."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, IX da CF/88: 'remuneração do trabalho noturno superior à do diurno'."
  },
  {
    "id": 85,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, VI da CF/88: Irredutibilidade Salarial",
    "question": "A regra constitucional acerca do salário dos trabalhadores estabelece a sua irredutibilidade, SALVO:",
    "options": [
      "O disposto em convenção ou acordo coletivo de trabalho.",
      "Decisão unilateral discricionária do empregador em época de crise.",
      "Atraso no pagamento de tributos pelo estabelecimento comercial.",
      "Determinação verbal do delegado regional do trabalho."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, VI da CF/88: 'irredutibilidade do salário, salvo o disposto em convenção ou acordo coletivo'."
  },
  {
    "id": 86,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 8º, I da CF/88: Autonomia e Liberdade Sindical",
    "question": "Conforme o Art. 8º, I, da CF/88, é livre a associação profissional ou sindical, sendo expressamente VEDADA:",
    "options": [
      "Ao Poder Público a interferência e a intervenção na organização sindical, ressalvado o registro no órgão competente.",
      "A criação de sindicatos representativos de categorias diferenciadas.",
      "A filiação de servidores públicos a entidades de classe municipais.",
      "A cobrança de mensalidade associativa voluntária pelo sindicato."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 8º, I da CF/88: 'a lei não poderá exigir autorização do Estado para a fundação de sindicato, ressalvado o registro no órgão competente, vedadas ao Poder Público a interferência e a intervenção na organização sindical'."
  },
  {
    "id": 87,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 8º, II da CF/88: Princípio da Unicidade Sindical",
    "question": "O princípio da unicidade sindical estabelecido no Art. 8º, II, da CF/88 veda a criação de mais de uma organização sindical, em qualquer grau, representativa da mesma categoria:",
    "options": [
      "Na mesma base territorial, que será definida pelos trabalhadores interessados, não podendo ser inferior à área de um Município.",
      "No mesmo Estado da federação, devendo haver sindicato único estadual.",
      "Em todo o território nacional para uma mesma profissão regulamentada.",
      "Na mesma microrregião geográfica estabelecida pelo IBGE."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 8º, II da CF/88: 'é vedada a criação de mais de uma organização sindical, em qualquer grau, representativa de categoria profissional ou econômica, na mesma base territorial, que será definida pelos trabalhadores ou empregadores interessados, não podendo ser inferior à área de um Município'."
  },
  {
    "id": 88,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 8º, VIII da CF/88: Estabilidade do Dirigente Sindical",
    "question": "A estabilidade provisória do empregado sindicalizado que se candidata a cargo de direção ou representação sindical compreende o período:",
    "options": [
      "Desde o registro da candidatura e, se eleito, ainda que suplente, até um ano após o final do mandato, salvo se cometer falta grave nos termos da lei.",
      "Apenas durante os meses de exercício efetivo do mandato sindical na sede.",
      "A partir da posse até o dia do término estrito do mandato parlamentar.",
      "Desde a fundação do sindicato até a sua dissolução voluntária."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 8º, VIII da CF/88: 'é vedada a dispensa do empregado sindicalizado a partir do registro da candidatura a cargo de direção ou representação sindical e, se eleito, ainda que suplente, até um ano após o final do mandato, salvo se cometer falta grave nos termos da lei'."
  },
  {
    "id": 89,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 9º da CF/88: Direito de Greve",
    "question": "O direito de greve é expressamente garantido pelo Art. 9º da Constituição Federal de 1988, competindo aos:",
    "options": [
      "Trabalhadores decidir sobre a oportunidade de exercê-lo e sobre os interesses que devam por meio dele defender.",
      "Empregadores autorizar previamente a paralisação das atividades operacionais.",
      "Magistrados do trabalho convocar a greve mediante portaria ministerial.",
      "Prefeitos municipais decretar a legalidade do movimento paradista."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 9º, caput da CF/88: 'É assegurado o direito de greve, competindo aos trabalhadores decidir sobre a oportunidade de exercê-lo e sobre os interesses que devam por meio dele defender'."
  },
  {
    "id": 90,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 11 da CF/88: Representação de Empregados",
    "question": "Nas empresas com mais de quantos empregados é assegurada a eleição de um representante destes com a finalidade exclusiva de promover o entendimento direto com os empregadores (Art. 11 da CF)?",
    "options": [
      "Mais de 200 (duzentos) empregados.",
      "Mais de 100 (cem) empregados.",
      "Mais de 500 (quinhentos) empregados.",
      "Mais de 50 (cinquenta) empregados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 11 da CF/88: 'Nas empresas de mais de duzentos empregados, é assegurada a eleição de um representante destes com a finalidade exclusiva de promover-lhes o entendimento direto com os empregadores'."
  },

  # -------------------------------------------------------------------------
  # LEGISLAÇÃO MUNICIPAL: LEI ORGÂNICA DE MERUOCA (IDs 91 a 100: Arts. 1º a 15)
  # -------------------------------------------------------------------------
  {
    "id": 91,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Arts. 1º e 2º: Princípios e Autonomia Municipal",
    "question": "De acordo com os princípios fundamentais da Lei Orgânica do Município de Meruoca/CE, o Município integra a República Federativa do Brasil e o Estado do Ceará, sendo dotado de autonomia:",
    "options": [
      "Política, administrativa e financeira.",
      "Soberana, judiciária e militar.",
      "Legislativa apenas, dependendo administrativamente do Estado.",
      "Econômica, porém subordinada hierarquicamente ao Governo Estadual."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A Lei Orgânica de Meruoca consagra a tríplice autonomia municipal conferida pelo Art. 18 e 29 da CF/88: Autonomia Política (eleição de prefeitos e vereadores), Administrativa (organização dos serviços locais) e Financeira (instituição e arrecadação de tributos próprios)."
  },
  {
    "id": 92,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Soberania Popular no Município de Meruoca",
    "question": "Nos termos da Lei Orgânica Municipal, todo o poder emana do povo meruoquense, que o exerce por meio de representantes eleitos ou diretamente. São formas de exercício direto da soberania popular no Município:",
    "options": [
      "Plebiscito, referendo e iniciativa popular de projetos de lei.",
      "Ação popular, mandado de segurança e inquérito civil público.",
      "Audiência prévia do Tribunal de Contas e veto do prefeito.",
      "Votação nominal em comissões parlamentares de inquérito."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em consonância com o Art. 14 da CF/88 e a Lei Orgânica de Meruoca, a soberania popular direta é exercida mediante: 1. Plebiscito (consulta prévia); 2. Referendo (consulta posterior à lei); 3. Iniciativa popular de leis perante a Câmara Municipal."
  },
  {
    "id": 93,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Símbolos Oficiais do Município de Meruoca",
    "question": "São símbolos oficiais do Município de Meruoca expressamente consagrados em sua legislação fundamental:",
    "options": [
      "O Brasão, a Bandeira e o Hino do Município.",
      "O Selo Municipal, o Estandarte e o Brasão do Estado do Ceará.",
      "O Brasão e a Bandeira apenas, sendo o Hino de competência estadual.",
      "A Faixa do Prefeito e a Insígnia do Presidente da Câmara."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme preceitua a Lei Orgânica Municipal (em harmonia com o Art. 13, § 2º da CF/88), os símbolos representativos do Município de Meruoca são a Bandeira, o Brasão e o Hino municipais."
  },
  {
    "id": 94,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Poderes do Município de Meruoca",
    "question": "São Poderes do Município de Meruoca, independentes e harmônicos entre si:",
    "options": [
      "O Legislativo e o Executivo.",
      "O Legislativo, o Executivo e o Judiciário.",
      "O Executivo, o Judiciário e o Ministério Público Municipal.",
      "Apenas o Executivo, sendo o Legislativo um órgão consultivo auxiliar."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. No âmbito municipal NÃO HÁ Poder Judiciário nem Ministério Público local (ambos são órgãos estaduais/federais). Os únicos poderes municipais são o Poder Legislativo (Câmara Municipal) e o Poder Executivo (Prefeitura Municipal)."
  },
  {
    "id": 95,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Competência Privativa do Município: Tributos e Orçamento",
    "question": "Compete privativamente ao Município de Meruoca, no exercício de sua autonomia legislativa e administrativa:",
    "options": [
      "Instituir e arrecadar os tributos de sua competência e aplicar suas rendas, bem como fixar tarifas de serviços públicos municipais.",
      "Legislar privativamente sobre direito civil, penal e processual eleitoral.",
      "Emitir moeda municipal e controlar as taxas de juros bancários locais.",
      "Organizar e manter o Poder Judiciário e a Defensoria Pública da Comarca."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Compete ao Município instituir tributos municipais (IPTU, ISS, ITBI, taxas e contribuições de iluminação pública), aplicar rendas e fixar tarifas de transporte e serviços locais. Legislar sobre direito civil/penal e emitir moeda são competências privativas da União (Art. 22 da CF)."
  },
  {
    "id": 96,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Competência Privativa: Uso e Ocupação do Solo Urbano",
    "question": "É matéria de interesse local inserida na competência privativa do Município de Meruoca:",
    "options": [
      "Promover o adequado ordenamento territorial, mediante planejamento e controle do uso, do parcelamento e da ocupação do solo urbano.",
      "Explorar diretamente os serviços de telecomunicações e radiodifusão sonora.",
      "Disciplinar a navegação aérea e a infraestrutura aeroespacial da Serra da Meruoca.",
      "Autorizar a exploração de jazidas minerais e riquezas do subsolo na região."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 30, VIII da CF/88 e Lei Orgânica de Meruoca: o ordenamento territorial, zoneamento urbano e controle de parcelamento/ocupação do solo (Plano Diretor, código de obras) é competência eminentemente municipal."
  },
  {
    "id": 97,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Competência Comum do Município com a União e o Estado",
    "question": "Assinale a alternativa que indica uma competência COMUM do Município de Meruoca em cooperação com o Estado do Ceará e a União:",
    "options": [
      "Cuidar da saúde e assistência pública, da proteção e garantia das pessoas com deficiência.",
      "Criar e extinguir cargos privativos da Mesa Diretora da Assembleia Legislativa.",
      "Instituir o Imposto sobre Circulação de Mercadorias e Serviços (ICMS).",
      "Expedir passaportes e carteiras de identidade civil para estrangeiros."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 23 da CF/88 e Lei Orgânica de Meruoca: a prestação de serviços de saúde, proteção de vulneráveis e pessoas com deficiência, meio ambiente e educação básica é matéria de competência comum dos três entes federados."
  },
  {
    "id": 98,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Guarda Municipal e Segurança Patrimonial",
    "question": "Nos termos da Lei Orgânica e do Art. 144, § 8º da CF/88, o Município de Meruoca poderá constituir guarda municipal destinada precipuamente à:",
    "options": [
      "Proteção de seus bens, serviços e instalações.",
      "Investigação de crimes eleitorais e tráfico interestadual de drogas.",
      "Substituição das polícias militar e civil nas ações de policiamento ostensivo geral.",
      "Fiscalização do recolhimento de impostos da União e execução fiscal federal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 144, § 8º da CF/88 e legislação municipal: os municípios poderão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações, atuando também na segurança comunitária e patrimonial."
  },
  {
    "id": 99,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Patrimônio e Bens Municipais",
    "question": "Constituem bens do Município de Meruoca, conforme sua Lei Orgânica:",
    "options": [
      "Todas as coisas móveis e imóveis, direitos e ações que a qualquer título lhe pertençam.",
      "Exclusivamente os edifícios onde funcionam a Prefeitura e a Câmara Municipal.",
      "Apenas as praças e ruas pavimentadas pelo poder público municipal.",
      "Os rios navegáveis que banham mais de dois estados da federação."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Constituem patrimônio e bens do Município todos os bens móveis e imóveis, direitos, títulos da dívida pública, créditos e ações pertencentes à municipalidade a qualquer título."
  },
  {
    "id": 100,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Princípio da Publicidade e Publicação dos Atos Municipais",
    "question": "A publicação das leis e dos atos administrativos normativos da Câmara Municipal e da Prefeitura de Meruoca é requisito essencial de:",
    "options": [
      "Eficácia e validade perante os munícipes e a sociedade.",
      "Revogação tácita de todas as normas jurídicas anteriores.",
      "Descentralização administrativa forçada dos poderes públicos.",
      "Conversão obrigatória de projeto de lei em medida provisória."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Nenhum ato normativo ou lei municipal produz efeitos externos sem a devida publicação no órgão oficial ou mural público da Câmara/Prefeitura. A publicação é condição de EFICÁCIA e vigência da norma jurídica."
  }
]

print(f"Total de questões geradas: {len(QUESTOES_DIA4)}")
