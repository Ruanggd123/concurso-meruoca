import json, re

# =========================================================================
# 1. DEFINIÇÃO DAS 40 QUESTÕES DO DIA 5 (IDs 101 a 140)
# =========================================================================
QUESTOES_DIA5 = [
  # --- D. ADMINISTRATIVO: PODERES & ATRIBUTOS DO ATO (101 a 115) ---
  {
    "id": 101,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Vinculado vs Discricionário",
    "question": "Quanto à margem de liberdade conferida ao administrador público na prática de seus atos, assinale a opção correta:",
    "options": [
      "No ato discricionário, a lei concede margem de escolha ao gestor quanto à oportunidade e conveniência (mérito administrativo), sempre nos limites da lei.",
      "No ato vinculado, o administrador pode avaliar livremente a conveniência de conceder ou não uma licença quando o particular preencher todos os requisitos.",
      "O mérito do ato discricionário pode ser revisto pelo Poder Judiciário sob o aspecto da conveniência e da oportunidade da autoridade administrativa.",
      "Todo ato administrativo é discricionário, cabendo à autoridade decidir as sanções disciplinares independentemente de previsão legal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A discricionariedade confere juízo de mérito (conveniência e oportunidade) estritamente dentro das balizas da lei. O Judiciário fiscaliza a legalidade/moralidade, mas não pode substituir o mérito administrativo da decisão discricionária."
  },
  {
    "id": 102,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Abuso de Poder: Excesso vs Desvio de Poder",
    "question": "O abuso de poder constitui conduta ilegítima do agente público e manifesta-se sob duas modalidades distintas: o excesso de poder e o desvio de poder (ou desvio de finalidade). Ocorre EXCESSO DE PODER quando o agente público:",
    "options": [
      "Atua fora dos limites de sua competência legal ou excede os poderes que a lei lhe conferiu.",
      "Atua dentro de sua competência, mas com objetivo alheio ao interesse público ou para beneficiar amigo.",
      "Pratica um ato perfeitamente vinculado que cumpriu todas as formalidades do edital.",
      "Revoga um ato legal de sua própria lavra com base em razões supervenientes de interesse público."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico clássico: Excesso de Poder = vício de COMPETÊNCIA (o agente faz o que a lei não lhe permitiu). Desvio de Poder (ou Finalidade) = vício de FINALIDADE (o agente é competente, mas busca interesse privado ou perseguição)."
  },
  {
    "id": 103,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Disciplinar",
    "question": "O Poder Disciplinar é a prerrogativa conferida à Administração Pública para:",
    "options": [
      "Apurar infrações e aplicar penalidades aos servidores públicos e a particulares que possuam vínculo jurídico específico com o Estado.",
      "Aplicar multas e penalidades indistintamente a qualquer cidadão que transite em logradouro municipal sem habilitação.",
      "Fixar tarifas gerais de transporte urbano para toda a população da cidade.",
      "Editar decretos normativos de caráter autônomo sem previsão em lei formal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O poder disciplinar atinge quem tem vínculo especial/interno com o Estado (servidores públicos e contratados administrativos via licitação). A punição aos cidadãos em geral sem vínculo específico decorre do Poder de Polícia."
  },
  {
    "id": 104,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Regulamentar / Normativo",
    "question": "A respeito do Poder Regulamentar conferido aos Chefes do Poder Executivo, é correto afirmar que os decretos regulamentares:",
    "options": [
      "Destinam-se a dar fiel execução às leis, não podendo criar direitos, obrigações ou inovar originariamente na ordem jurídica.",
      "Podem contrariar a lei em caso de emergência orçamentária do município.",
      "Permitem a criação originária de novos tributos municipais sem passar pela Câmara de Vereadores.",
      "Subordinam hierarquicamente as leis votadas pelo Poder Legislativo municipal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 84, IV da CF/88. O poder regulamentar é de caráter secundário (intra legem): serve apenas para explicitar e regulamentar a lei existente para sua fiel execução, sendo vedado criar obrigações novas ou inovar originariamente."
  },
  {
    "id": 105,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder de Polícia: Conceito e Atributos",
    "question": "Conforme o Art. 78 do Código Tributário Nacional (CTN), o Poder de Polícia é a atividade da administração pública que condiciona ou restringe o uso de bens, atividades e direitos em prol do interesse público. São atributos clássicos do poder de polícia:",
    "options": [
      "Discricionariedade, autoexecutoriedade e coercibilidade.",
      "Irrevogabilidade, subordinação e imprescritibilidade.",
      "Gratuidade obrigatória, oralidade e retroatividade.",
      "Inalienabilidade, impenhorabilidade e imutabilidade."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico 'DAC': Discricionariedade (margem de escolha de atuação/sanção), Autoexecutoriedade (execução material direta sem prévia autorização judicial) e Coercibilidade (imposição imperativa de limites com força pública se necessário)."
  },
  {
    "id": 106,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Hierárquico",
    "question": "São faculdades e prerrogativas típicas decorrentes do exercício do Poder Hierárquico na Administração Pública, EXCETO:",
    "options": [
      "Aplicar sanções de interdição a estabelecimentos comerciais privados que violarem o código de posturas sanitárias.",
      "Dar ordens aos subordinados, ressalvadas as ordens manifestamente ilegais.",
      "Fiscalizar e controlar as atividades desempenhadas pelos órgãos inferiores.",
      "Delegar e avocar competências, nos termos e limites previstos na legislação."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A interdição de comércio privado decorre do Poder de Polícia (sobre particulares). O Poder Hierárquico atua estritamente na relação interna de subordinação e coordenação entre órgãos e agentes públicos (dar ordens, fiscalizar, delegar e avocar)."
  },
  {
    "id": 107,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Atributos do Ato Administrativo: PATI",
    "question": "A doutrina de Direito Administrativo consagrada nas provas da banca INBRASP sintetiza os atributos do ato administrativo no mnemônico 'PATI'. Quais são esses atributos?",
    "options": [
      "Presunção de legitimidade, Autoexecutoriedade, Tipicidade e Imperatividade.",
      "Publicidade, Autonomia, Temporalidade e Impessoalidade.",
      "Previsibilidade, Anterioridade, Transparência e Intangibilidade.",
      "Probidade, Acessibilidade, Tipicidade e Igualdade."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico PATI: Presunção de legitimidade/veracidade (atos presumem-se válidos até prova em contrário); Autoexecutoriedade (execução direta pelo Estado); Tipicidade (deve corresponder a figura prevista em lei); Imperatividade (impõe obrigações a terceiros independentemente de concordância)."
  },
  {
    "id": 108,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Presunção de Legitimidade e Veracidade",
    "question": "A presunção de legitimidade do ato administrativo produz como efeito prático processual a:",
    "options": [
      "Inversão do ônus da prova, cabendo a quem contesta o ato provar a sua ilegalidade ou falsidade.",
      "Impossibilidade definitiva de anulação do ato pelo Poder Judiciário.",
      "Dispensabilidade total de publicação dos atos no diário oficial do município.",
      "Transformação automática de atos discricionários em atos de império irrecorríveis."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A presunção de legitimidade é relativa (juris tantum): o ato nasce com aparência de legalidade e verdade fática, cabendo ao particular comprovar eventual defeito (inversão do ônus da prova)."
  },
  {
    "id": 109,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Autoexecutoriedade do Ato Administrativo",
    "question": "O atributo da AUTOEXECUTORIEDADE autoriza a Administração Pública a executar diretamente as suas decisões materiais sem a necessidade de prévia autorização judicial. Esse atributo:",
    "options": [
      "Não está presente em todos os atos administrativos, existindo quando expressamente previsto em lei ou em situações urgentes de defesa do interesse público.",
      "Existe indistintamente em 100% dos atos da administração, inclusive na cobrança coercitiva imediata de multas pecuniárias não pagas.",
      "Impede que o particular ingresse com mandado de segurança caso se sinta lesado em seu direito líquido e certo.",
      "Aplica-se somente aos atos editados pelo Poder Judiciário em suas funções típicas."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Pegadinha clássica: a autoexecutoriedade NÃO está em todos os atos! Ela não existe, por exemplo, na cobrança de multa em dinheiro (se o cidadão não pagar, o Estado não pode tomar o dinheiro à força; deve ingressar com Execução Fiscal no Judiciário)."
  },
  {
    "id": 110,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Imperatividade e Poder Extrínseco",
    "question": "A IMPERATIVIDADE (ou poder extroverso) do ato administrativo caracteriza-se por:",
    "options": [
      "Impor deveres e obrigações a terceiros unilateralmente, independentemente da concordância do destinatário.",
      "Conceder vantagens que dependem do prévio requerimento e anuência do cidadão.",
      "Garantir a imutabilidade dos atos municipais após decorridos 30 dias de sua publicação.",
      "Permitir ao servidor público o descumprimento de ordens emanadas de seus superiores diretos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A imperatividade permite impor obrigações coercitivas ao administrado (ex: multa de trânsito, interdição de vigilância sanitária). Não está presente em atos enunciativos (certidões) ou negociais (autorização, licença)."
  },
  {
    "id": 111,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Tipicidade no Ato Administrativo",
    "question": "O atributo da TIPICIDADE, formulado pela professora Maria Sylvia Zanella Di Pietro, preceitua que o ato administrativo deve:",
    "options": [
      "Corresponder a figuras previamente delineadas na lei para produzir os efeitos desejados, impedindo a prática de atos totalmente inominados.",
      "Ser redigido exclusivamente na língua portuguesa arcaica do período colonial.",
      "Conter obrigatoriamente cláusula de sigilo prévio por até 5 anos.",
      "Ser publicado em pelo menos três jornais impressos de circulação nacional."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Pela tipicidade, para cada finalidade pretendida a lei já define a espécie de ato cabível (ex: se quer punir, usa demissão/advertência; se quer autorizar, usa alvará). Isso impede que a autoridade crie atos extravagantes ou sem modelo na lei."
  },
  {
    "id": 112,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Ciclo do Poder de Polícia",
    "question": "A doutrina divide o Poder de Polícia em quatro fases ou ciclos: I. Ordem de polícia (legislação); II. Consentimento de polícia (licença/autorização); III. Fiscalização de polícia (inspeção); IV. Sanção de polícia (multa/interdição). É passível de delegação a entidades estatais de direito privado integrantes da administração indireta (ex: empresas públicas e sociedades de economia mista):",
    "options": [
      "As fases de consentimento, fiscalização e sanção, conforme entendimento fixado pelo STF no Tema 532 de repercussão geral.",
      "Apenas a ordem de polícia, sendo vedada a fiscalização.",
      "Todas as fases sem qualquer restrição, inclusive legislar privativamente sobre crimes.",
      "Nenhuma das fases, pois o poder de polícia é indelegável a qualquer ente."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O STF fixou a tese de que é constitucional a delegação do poder de polícia (consentimento, fiscalização e sanção) a pessoas jurídicas de direito privado integrantes da administração pública indireta de capital majoritariamente público que prestem serviços públicos em regime não concorrencial (ex: BHTrans, CET)."
  },
  {
    "id": 113,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Desvio de Finalidade (Art. 2º da Lei da Ação Popular)",
    "question": "O prefeito de determinado município remove 'ex officio' um guarda municipal para posto de serviço remoto em área rural unicamente como forma de castigo pessoal por divergência política partidária. Essa conduta do administrador público caracteriza vício insanável de:",
    "options": [
      "Desvio de finalidade (ou desvio de poder), tornando o ato de remoção nulo de pleno direito.",
      "Excesso de forma meramente acidental com convalidação automática.",
      "Exercício regular do poder disciplinar sem possibilidade de recurso ao Judiciário.",
      "Incompetência absoluta por ausência de concurso público."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A remoção de servidor tem como finalidade atender à necessidade do serviço público. Usá-la para perseguir ou punir desvia a finalidade legal do ato (desvio de poder), gerando nulidade absoluta por violação direta ao princípio da impessoalidade."
  },
  {
    "id": 114,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Taxas de Polícia vs Preços Públicos",
    "question": "Pela atividade regular do Poder de Polícia exercida pelo Município de Meruoca, a Constituição Federal autoriza a instituição de:",
    "options": [
      "Taxas pelo exercício do poder de polícia.",
      "Impostos progressivos de natureza punitiva.",
      "Contribuições de melhoria extraordinárias sem obra pública.",
      "Tarifas alfandegárias de fiscalização internacional."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 145, II da CF/88 e Art. 77 do CTN: as taxas são tributos cobrados em razão do exercício regular do poder de polícia (ex: taxa de fiscalização de funcionamento, taxa de vigilância sanitária) ou pela utilização efetiva/potencial de serviço público específico e divisível."
  },
  {
    "id": 115,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Distinção entre Atos Nulos e Anuláveis",
    "question": "No regime jurídico administrativo, quando um ato apresenta defeito quanto aos elementos de COMPETÊNCIA (desde que não seja exclusiva) ou de FORMA (desde que a lei não a exija como requisito de validade), o ato é passível de:",
    "options": [
      "Convalidação pela Administração Pública, aproveitando-se o ato com efeitos retroativos (ex tunc).",
      "Revogação obrigatória e irrecusável pelo Poder Judiciário.",
      "Cassação automática por descumprimento de deveres pelo particular.",
      "Prescrição imediata em 24 horas a contar da data de protocolo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico FO-CO: defeitos de Forma (não essencial) e Competência (não exclusiva) geram atos ANULÁVEIS que admitem convalidação pela própria Administração, desde que não acarretem lesão ao interesse público nem prejuízo a terceiros."
  },

  # --- NOÇÕES DE INFORMÁTICA: ALGORITMOS & PYTHON (116 a 130) ---
  {
    "id": 116,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Conceito de Algoritmo",
    "question": "No contexto da ciência da computação e do edital da Câmara de Meruoca, um ALGORITMO pode ser conceituado como:",
    "options": [
      "Uma sequência finita de passos lógicos, ordenados e bem definidos, que visa à resolução de um problema ou à execução de uma tarefa.",
      "Um programa executável binário restrito a sistemas operacionais de grande porte.",
      "Uma peça de hardware instalada na placa-mãe responsável por resfriar o processador.",
      "Um protocolo de rede utilizado exclusivamente para tráfego seguro de e-mails corporativos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Algoritmo é uma sequência lógica, finita, ordenada e não ambígua de instruções que, ao ser processada, transforma entradas em saídas para solucionar um problema."
  },
  {
    "id": 117,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Fluxogramas: Símbolo de Decisão (Losango)",
    "question": "Em um fluxograma que representa o fluxo de tramitação de um processo administrativo, o símbolo geométrico que representa uma tomada de DECISÃO ou desvio condicional (onde o fluxo pode seguir caminhos diferentes conforme a resposta Sim/Não) é o:",
    "options": [
      "Losango.",
      "Retângulo.",
      "Círculo ou elipse.",
      "Paralelogramo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Símbolos universais de fluxogramas: Losango = Decisão / Condição (teste lógico Se/Senão); Retângulo = Ação / Processamento / Atribuição; Oval/Elipse = Início ou Fim; Paralelogramo = Entrada ou Saída de dados."
  },
  {
    "id": 118,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Pseudocódigo e Estruturas Condicionais",
    "question": "Considere o seguinte trecho de pseudocódigo:\n\nSE (idade >= 18) ENTÃO\n    ESCREVA('Apto ao concurso')\nSENÃO\n    ESCREVA('Inapto por idade')\nFIMSE\n\nCaso o valor atribuído à variável 'idade' seja exatamente 18, o programa exibirá:",
    "options": [
      "Apto ao concurso",
      "Inapto por idade",
      "Erro de compilação por operador inexistente",
      "Nenhuma mensagem será exibida na tela"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O operador `>=` significa 'maior ou igual'. Como 18 é igual a 18, a condição é VERDADEIRA e o bloco do SE é executado, exibindo 'Apto ao concurso'."
  },
  {
    "id": 119,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Estruturas de Repetição (Laços / Loops)",
    "question": "Em lógica de programação, a estrutura que executa repetidamente um bloco de instruções ENQUANTO uma condição prévia permanecer verdadeira é chamada de:",
    "options": [
      "Laço de repetição ou loop (while / enquanto).",
      "Função recursiva estática imutável.",
      "Declaração de constante booleana.",
      "Instrução de salto incondicional irrestrita."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. As estruturas de repetição (laços ou loops) permitem executar comandos várias vezes. No laço `enquanto` (`while`), o teste é feito no início e o bloco roda enquanto o teste for verdadeiro."
  },
  {
    "id": 120,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Linguagem Python: Indentação Obrigatória",
    "question": "Diferentemente de linguagens como C ou Java que utilizam chaves `{ }` para delimitar blocos de comandos, a linguagem Python utiliza como delimitador obrigatório de blocos de código a:",
    "options": [
      "Indentação (espaçamento consistente à esquerda com espaços ou tabs).",
      "Utilização de ponto e vírgula ';' ao final de cada instrução.",
      "Inclusão da palavra reservada 'END' ao final de cada linha.",
      "Abertura e fechamento de colchetes '[ ]' em cada função."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em Python, a indentação não é apenas estética: ela define a hierarquia e o escopo dos blocos de código (corpo de funções, laços for/while, estruturas if/else)."
  },
  {
    "id": 121,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Tipos de Dados Básicos",
    "question": "Em Python, considere a atribuição: `total = 100`, `preco = 45.50` e `cargo = 'Técnico'`. Os tipos de dados primitivos dessas variáveis são, respectivamente:",
    "options": [
      "int (inteiro), float (número de ponto flutuante) e str (string / texto).",
      "number, decimal e char.",
      "integer, currency e varchar.",
      "long, double e text."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em Python, inteiros são do tipo `int`, números com casas decimais são do tipo `float` e cadeias de caracteres entre aspas são do tipo `str`."
  },
  {
    "id": 122,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Operadores Aritméticos Divisão e Resto",
    "question": "Na linguagem Python, o operador `//` realiza a divisão inteira e o operador `%` retorna o resto da divisão. Qual será o resultado das expressões `7 // 2` e `7 % 2`?",
    "options": [
      "3 e 1",
      "3.5 e 0.5",
      "3 e 0",
      "4 e 1"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 7 dividido por 2 dá quociente 3 e sobra resto 1. Logo, a divisão inteira `7 // 2` resulta em 3, e o módulo/resto `7 % 2` resulta em 1."
  },
  {
    "id": 123,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Listas e Indexação",
    "question": "Em Python, as listas são coleções ordenadas de elementos e possuem indexação baseada em zero. Dada a lista `bancas = ['CETREDE', 'CONSULPAM', 'INBRASP', 'IDECAN']`, a instrução `print(bancas[2])` exibirá na tela:",
    "options": [
      "INBRASP",
      "CONSULPAM",
      "CETREDE",
      "IDECAN"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A indexação em Python inicia em zero: `bancas[0]` = 'CETREDE', `bancas[1]` = 'CONSULPAM', `bancas[2]` = 'INBRASP', `bancas[3]` = 'IDECAN'."
  },
  {
    "id": 124,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Comentários de Linha",
    "question": "Na linguagem Python, qual caractere é utilizado para inserir comentários de linha única (instruções que são ignoradas pelo interpretador)?",
    "options": [
      "# (cerquilha / hashtag)",
      "// (duas barras inclinadas)",
      "/* (barra e asterisco)",
      "-- (dois traços)"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em Python, comentários de linha única começam com o caractere `#`. Em linguagens como C, Java e PHP usa-se `//`; em SQL usa-se `--`."
  },
  {
    "id": 125,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Estrutura Condicional (if / elif / else)",
    "question": "Analise o seguinte código em Python:\n\npontos = 85\nif pontos >= 90:\n    print('Aprovado em 1º Lugar')\nelif pontos >= 50:\n    print('Classificado')\nelse:\n    print('Reprovado')\n\nQual será a saída exibida no terminal?",
    "options": [
      "Classificado",
      "Aprovado em 1º Lugar",
      "Reprovado",
      "Aprovado em 1º Lugar e Classificado simultaneamente"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. `pontos = 85`. A primeira condição (`85 >= 90`) é Falsa. O interpretador salta para o `elif`: `85 >= 50` é Verdadeira. Portanto, executa `print('Classificado')` e encerra a estrutura condicional."
  },
  {
    "id": 126,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Operador de Exponenciação",
    "question": "Qual operador matemático é utilizado na linguagem Python para calcular a exponenciação (potência), por exemplo, dois elevado à terceira potência (2³)?",
    "options": [
      "** (dois asteriscos, ex: 2 ** 3)",
      "^ (acento circunflexo, ex: 2 ^ 3)",
      "pow$ (ex: 2 pow$ 3)",
      "^^ (dois circunflexos, ex: 2 ^^ 3)"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em Python, a potência é calculada com `**` (ex: `2 ** 3 = 8`). O operador `^` em Python é o operador bit a bit XOR (ou exclusivo), uma pegadinha clássica de concurso!"
  },
  {
    "id": 127,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Função len()",
    "question": "A função nativa `len()` em Python tem como finalidade:",
    "options": [
      "Retornar a quantidade de elementos de um objeto (como tamanho de uma lista ou comprimento de uma string).",
      "Converter um texto em letras maiúsculas.",
      "Ler uma entrada de dados digitada pelo usuário no teclado.",
      "Finalizar imediatamente a execução do programa em caso de erro."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. `len()` é a abreviação de 'length'. Exemplo: `len('Meruoca')` retorna 7; `len([10, 20, 30])` retorna 3."
  },
  {
    "id": 128,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Operadores Lógicos (and, or, not)",
    "question": "Em Python, os operadores lógicos booleanos para conjunção, disjunção e negação são grafados por extenso como:",
    "options": [
      "and, or, not",
      "&&, ||, !",
      ".AND., .OR., .NOT.",
      "e, ou, nao"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Python preza pela legibilidade e usa palavras em inglês em minúsculas: `and` (conjunção), `or` (disjunção) e `not` (negação). `&&` e `||` são de C/Java/JS."
  },
  {
    "id": 129,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Laço for e Função range()",
    "question": "Considere o código Python:\n\nsoma = 0\nfor i in range(1, 4):\n    soma += i\nprint(soma)\n\nLembrando que `range(1, 4)` gera os números 1, 2 e 3 (o limite superior 4 é exclusivo), qual valor será impresso?",
    "options": [
      "6",
      "10",
      "4",
      "3"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. `range(1, 4)` produz os valores 1, 2 e 3. Na 1ª iteração: soma = 0 + 1 = 1. Na 2ª iteração: soma = 1 + 2 = 3. Na 3ª iteração: soma = 3 + 3 = 6. Saída: 6."
  },
  {
    "id": 130,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Função print() e input()",
    "question": "As funções nativas de entrada e saída padrão em um terminal na linguagem Python são, respectivamente:",
    "options": [
      "input() para entrada de dados do usuário e print() para saída em tela.",
      "read() para entrada e write() para saída.",
      "scanf() para entrada e printf() para saída.",
      "cin para entrada e cout para saída."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em Python padrão: `input('Digite algo:')` lê dados do teclado em formato string, e `print('Mensagem')` imprime dados na tela do console."
  },

  # --- LEI ORGÂNICA DE MERUOCA: ARTS. 16 AO 30 (PODER LEGISLATIVO) (131 a 140) ---
  {
    "id": 131,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Poder Legislativo Municipal e Composição",
    "question": "O Poder Legislativo do Município de Meruoca é exercido pela Câmara Municipal, composta por Vereadores eleitos pelo sistema proporcional para um mandato de:",
    "options": [
      "4 (quatro) anos, correspondendo a uma legislatura.",
      "2 (dois) anos, permitida uma recondução consecutiva.",
      "5 (cinco) anos, em consonância com o mandato dos senadores.",
      "3 (três) anos, renovando-se por terços anuais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em conformidade com a CF/88 e a Lei Orgânica de Meruoca, o mandato dos Vereadores é de 4 anos. Cada período de 4 anos de mandato parlamentar corresponde a uma LEGISLATURA."
  },
  {
    "id": 132,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Posse dos Vereadores, Prefeito e Vice",
    "question": "Nos termos da Lei Orgânica Municipal, a posse dos Vereadores, do Prefeito e do Vice-Prefeito de Meruoca realizar-se-á em sessão solene de instalação no dia:",
    "options": [
      "1º de janeiro do ano subsequente ao da eleição.",
      "1º de fevereiro do ano da posse legislativa federal.",
      "15 de novembro, data da proclamação da República.",
      "1º de março, após o encerramento do recesso carnavalesco."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A instalação da legislatura e a posse dos Vereadores, Prefeito e Vice-Prefeito ocorre obrigatoriamente no dia 1º de JANEIRO do ano subsequente à eleição municipal."
  },
  {
    "id": 133,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Mesa Diretora da Câmara Municipal",
    "question": "Imediatamente após a posse dos Vereadores de Meruoca, sob a presidência do vereador mais votado dentre os presentes, proceder-se-á à eleição dos membros da:",
    "options": [
      "Mesa Diretora da Câmara Municipal.",
      "Comissão Mista de Finanças e Tributação.",
      "Bancada Governista de Apoio ao Poder Executivo.",
      "Junta Comercial e Fiscalizatória dos Bairros."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme a Lei Orgânica e o Regimento Interno, logo após o compromisso de posse no dia 1º de janeiro, os parlamentares elegem a Mesa Diretora da Câmara (Presidente, Vice-Presidente e Secretários)."
  },
  {
    "id": 134,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Quórum Geral de Deliberação na Câmara",
    "question": "Salvo disposição expressa em contrário da Lei Orgânica de Meruoca ou da Constituição Federal, as deliberações da Câmara Municipal e de suas Comissões serão tomadas por:",
    "options": [
      "Maioria de votos, presente a maioria absoluta de seus membros.",
      "Dois terços de votos, independentemente do número de presentes.",
      "Unanimidade obrigatória dos parlamentares diplomados.",
      "Voto exclusivo e soberano do Presidente da Mesa Diretora."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. É a regra geral da maioria simples (ou relativa): maioria dos votos dos presentes na sessão, desde que esteja presente a maioria absoluta (metade mais um) dos membros da Casa (Art. 47 da CF e Lei Orgânica)."
  },
  {
    "id": 135,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Imunidade Material dos Vereadores (Inviolabilidade)",
    "question": "Conforme o Art. 29, VIII da Constituição Federal e a Lei Orgânica de Meruoca, os Vereadores gozam de inviolabilidade por suas opiniões, palavras e votos:",
    "options": [
      "No exercício do mandato e na circunscrição do Município.",
      "Em qualquer lugar do território nacional, inclusive em viagens privadas de lazer.",
      "Apenas durante as sessões plenárias dentro do edifício da Câmara Municipal.",
      "Exclusivamente quando autorizados previamente pelo Presidente da Casa."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A imunidade material do Vereador é local: ele possui inviolabilidade civil e penal por palavras, votos e opiniões proferidas no exercício das funções parlamentares e restritas à CIRCUNSCRIÇÃO DO MUNICÍPIO de Meruoca."
  },
  {
    "id": 136,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Perda do Mandato por Falta às Sessões",
    "question": "Perderá o mandato o Vereador de Meruoca que deixar de comparecer, em cada sessão legislativa anual, sem justificativa legal ou licença concedida pela Casa, à:",
    "options": [
      "Terça parte (1/3) das sessões ordinárias da Câmara Municipal.",
      "Metade (1/2) das sessões extraordinárias convocadas pelo prefeito.",
      "Duas sessões solenes comemorativas consecutivas.",
      "Quinta parte (1/5) das reuniões das comissões temáticas."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 55, III da CF e Lei Orgânica: acarreta a perda do mandato parlamentar a ausência injustificada a 1/3 (uma terça parte) das sessões ordinárias do ano legislativo."
  },
  {
    "id": 137,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Remuneração dos Vereadores (Subsídio)",
    "question": "O subsídio dos Vereadores de Meruoca é fixado pela Câmara Municipal em cada legislatura para vigorar na subsequente, observados os limites constitucionais e o teto da receita municipal. O subsídio deve ser fixado sob a modalidade de:",
    "options": [
      "Parcela única, vedado o acréscimo de qualquer gratificação, adicional, abono, prêmio ou verba de representação.",
      "Salário base acrescido de 40% de gratificação de produtividade por projeto aprovado.",
      "Diárias cumulativas por sessão ordinária comparecida no mês.",
      "Comissão percentual sobre a arrecadação mensal do IPTU de Meruoca."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 39, § 4º da CF/88 e Lei Orgânica: os agentes políticos remuneram-se exclusivamente por SUBSÍDIO fixado em parcela única, sendo expressamente proibido o pagamento de penduricalhos, adicionais ou gratificações de gabinete."
  },
  {
    "id": 138,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Fiscalização Financeira e Controle Externo",
    "question": "A fiscalização contábil, financeira e orçamentária do Município de Meruoca será exercida pela Câmara Municipal, mediante controle externo, com o auxílio do:",
    "options": [
      "Tribunal de Contas do Estado do Ceará (TCE/CE).",
      "Tribunal de Contas da União (TCU) em primeira e última instância.",
      "Conselho Fiscal Popular eleito por voto secreto em cada bairro.",
      "Ministério da Fazenda e Receita Federal do Brasil."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O controle externo da Câmara Municipal sobre as contas do Município e do Prefeito é exercido com o auxílio do Tribunal de Contas do Estado (TCE/CE), que emite parecer prévio."
  },
  {
    "id": 139,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Rejeição do Parecer Prévio do TCE",
    "question": "O parecer prévio emitido pelo Tribunal de Contas sobre as contas que o Prefeito de Meruoca deve prestar anualmente só deixará de prevalecer por decisão de:",
    "options": [
      "Dois terços (2/3) dos membros da Câmara Municipal.",
      "Maioria absoluta dos vereadores presentes.",
      "Maioria simples mediante votação secreta.",
      "Unanimidade dos integrantes da comissão de orçamento."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 31, § 2º da CF/88 e Lei Orgânica de Meruoca: o parecer técnico do Tribunal de Contas tem peso qualificado e só pode ser derrubado pelo voto de 2/3 (dois terços) dos vereadores."
  },
  {
    "id": 140,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Comissões Parlamentares de Inquérito (CPIs)",
    "question": "As Comissões Parlamentares de Inquérito (CPI) na Câmara Municipal de Meruoca, que terão poderes de investigação próprios das autoridades judiciais, serão criadas mediante requerimento de:",
    "options": [
      "Um terço (1/3) dos membros da Câmara Municipal, para a apuração de fato determinado e por prazo certo.",
      "Metade mais um dos vereadores, para investigar condutas genéricas sem prazo determinado.",
      "Dois terços dos membros da Casa, exigindo-se aval prévio do juiz de direito da comarca.",
      "Qualquer cidadão que apresente abaixo-assinado com 50 assinaturas."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 58, § 3º da CF/88 e Lei Orgânica: a CPI é criada por requerimento de 1/3 (um terço) dos membros da Câmara, para apuração de FATO DETERMINADO e por PRAZO CERTO, sendo suas conclusões encaminhadas ao Ministério Público se for o caso."
  }
]

print(f"[OK] Total de questões do Dia 5 geradas: {len(QUESTOES_DIA5)}")
