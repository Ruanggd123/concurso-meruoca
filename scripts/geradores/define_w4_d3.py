import json

# Definicao das 18 questoes refinadas e perfeitamente balanceadas de w4_d3
W4_D3_QUESTIONS = [
  {
    "id": 613,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Princípio da Exclusividade (CF/88, Art. 165, § 8º)",
    "question": "O princípio orçamentário da exclusividade veda que a Lei Orçamentária Anual contenha matéria estranha à previsão da receita e à fixação da despesa. Contudo, a Constituição Federal ressalva expressamente da proibição:",
    "options": [
      "A criação de cargos públicos e a concessão de reajustes salariais para os servidores da administração.",
      "A autorização para abertura de créditos suplementares e contratação de operações de crédito da receita.",
      "A fixação dos subsídios dos vereadores e dos secretários municipais para a legislatura subsequente.",
      "A majoração das alíquotas de tributos municipais para cobrir despesas imprevistas de calamidade."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. CF/88, Art. 165, § 8º: 'A lei orçamentária anual não conterá dispositivo estranho à previsão da receita e à fixação da despesa, não se incluindo na proibição a autorização para abertura de créditos suplementares e contratação de operações de crédito, ainda que por antecipação de receita, nos termos da lei.' Essa é a clássica ressalva constitucional cobrada pela INBRASP."
  },
  {
    "id": 614,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Princípio da Universalidade e Orçamento Bruto (Lei 4.320/64)",
    "question": "A regra que determina que a Lei de Orçamento deve consignar todas as receitas e despesas pelos seus totais globais, vedadas quaisquer deduções parciais no cálculo, consagra diretamente o princípio orçamentário do:",
    "options": [
      "Orçamento Bruto, complementar ao princípio clássico da universalidade.",
      "Equilíbrio Financeiro, vedando abertura de créditos sem recurso prévio.",
      "Exclusividade Material, proibindo normas estranhas na lei orçamentária.",
      "Não Afetação de Receitas, proibindo vinculação prévia de impostos gerais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 6º da Lei nº 4.320/1964: 'Todas as receitas e despesas constarão da Lei de Orçamento pelos seus totais, vedadas quaisquer deduções.' Trata-se do Princípio do Orçamento Bruto, que complementa a Universalidade (Art. 2º da mesma lei)."
  },
  {
    "id": 615,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Princípio da Anualidade / Periodicidade (Lei 4.320/64, Art. 34)",
    "question": "No regime financeiro e orçamentário da administração pública brasileira, o princípio da anualidade ou periodicidade determina de forma peremptória que:",
    "options": [
      "O orçamento deve ser aprovado até o encerramento do primeiro trimestre do ano.",
      "O exercício financeiro coincidirá estritamente com o ano civil, de 1º de janeiro a 31 de dezembro.",
      "A vigência da lei orçamentária anual coincide com o mandato eletivo de quatro anos.",
      "As receitas e despesas devem ser revisadas a cada dois anos pelo Poder Legislativo."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 34 da Lei nº 4.320/1964: 'O exercício financeiro coincidirá com o ano civil.' Portanto, tem início em 1º de janeiro e término em 31 de dezembro de cada ano civil."
  },
  {
    "id": 616,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Plano Plurianual (PPA - CF/88, Art. 165, § 1º)",
    "question": "Conforme preceitua o Art. 165, § 1º da Constituição Federal de 1988, a lei que instituir o Plano Plurianual (PPA) estabelecerá, de forma regionalizada:",
    "options": [
      "A fixação detalhada dos tributos e alíquotas municipais aplicáveis durante os quatro anos.",
      "As diretrizes, objetivos e metas da administração pública para as despesas de capital e contínuas.",
      "A estimativa das receitas de capital e a tabela de remuneração de todos os servidores da Casa.",
      "Os limites prudenciais de gastos com pessoal e os índices de endividamento da gestão municipal."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. CF/88, Art. 165, § 1º: 'A lei que instituir o plano plurianual estabelecerá, de forma regionalizada, as diretrizes, objetivos e metas da administração pública federal para as despesas de capital e outras delas decorrentes e para as relativas aos programas de duração continuada.' Mnemônico DOM (Diretrizes, Objetivos e Metas)."
  },
  {
    "id": 617,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Vigência e Tramitação do Plano Plurianual (PPA)",
    "question": "A respeito da vigência temporal e do período de aplicação do Plano Plurianual (PPA) na administração pública brasileira, é correto afirmar que:",
    "options": [
      "Sua vigência coincide rigidamente com o mandato do chefe do Poder Executivo (início no 1º ano).",
      "Sua vigência é de quatro anos, com início no 2º ano do mandato e término no 1º ano do subsequente.",
      "Sua vigência é bienal, exigindo que o Poder Executivo envie um novo projeto a cada dois anos.",
      "Sua vigência é de cinco anos ininterruptos, vinculando obrigatoriamente duas gestões inteiras."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O PPA vigora por 4 anos, iniciando-se no segundo ano do mandato do chefe do Executivo e encerrando-se no final do primeiro ano do mandato seguinte (art. 35, § 2º, I do ADCT), garantindo a continuidade das políticas públicas."
  },
  {
    "id": 618,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Lei de Diretrizes Orçamentárias (LDO - CF/88, Art. 165, § 2º)",
    "question": "A Lei de Diretrizes Orçamentárias (LDO) desempenha papel de elo entre o planejamento estratégico (PPA) e o operacional (LOA). É atribuição precípua da LDO:",
    "options": [
      "Compreender as metas e prioridades da gestão, orientar a feitura da LOA e dispor sobre tributos.",
      "Autorizar a contratação de servidores públicos efetivos e definir os programas sociais plurianuais.",
      "Fixar os valores nominais de todas as despesas e prever a arrecadação de tributos para o ano.",
      "Homologar os balanços gerais do exercício anterior e fiscalizar o limite da dívida consolidada."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 165, § 2º da CF/88: 'A lei de diretrizes orçamentárias compreenderá as metas e prioridades da administração pública federal, estabelecerá as diretrizes de política fiscal e respectivas metas [...] orientará a elaboração da lei orçamentária anual, disporá sobre as alterações na legislação tributária e estabelecerá a política de aplicação das agências financeiras oficiais de fomento.'"
  },
  {
    "id": 619,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Composição da Lei Orçamentária Anual (CF/88, Art. 165, § 5º)",
    "question": "De acordo com o Art. 165, § 5º da CF/88, a Lei Orçamentária Anual (LOA) compreende obrigatoriamente três orçamentos integrados, que são:",
    "options": [
      "Orçamento de Investimentos, Orçamento Plurianual e Orçamento de Despesas Extraordinárias.",
      "Orçamento Fiscal, Orçamento de Investimento das Estatais e Orçamento da Seguridade Social.",
      "Orçamento Operacional, Orçamento de Pessoal e Encargos e Orçamento de Manutenção da Câmara.",
      "Orçamento Corrente, Orçamento de Capital e Orçamento da Dívida Fundada Consolidada Municipal."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. CF/88, Art. 165, § 5º: O orçamento fiscal (I), o orçamento de investimento das empresas estatais (II) e o orçamento da seguridade social (III). Mnemônico clássico: FIS (Fiscal, Investimento, Seguridade)."
  },
  {
    "id": 620,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Espécies de Créditos Adicionais (Lei 4.320/64, Art. 41)",
    "question": "Quando durante a execução orçamentária surge a necessidade de realizar uma despesa para a qual já existe dotação orçamentária própria, porém insuficiente, deve-se abrir crédito:",
    "options": [
      "Extraordinário, mediante edição de decreto municipal fundamentado em situação de comoção pública.",
      "Especial, destinado a criar programa governamental novo não contemplado na lei orçamentária original.",
      "Suplementar, destinado especificamente a reforçar dotação orçamentária pré-existente e insuficiente.",
      "Ordinário, condicionado à prévia aprovação de lei complementar de responsabilidade fiscal da Casa."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Lei nº 4.320/64, Art. 41, I: 'créditos suplementares, os destinados a refôrço de dotação orçamentária'. Já os créditos especiais (inciso II) destinam-se a despesas para as quais não haja dotação orçamentária específica."
  },
  {
    "id": 621,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Fontes de Recursos para Créditos Adicionais (Lei 4.320/64, Art. 43)",
    "question": "A abertura dos créditos suplementares e especiais depende da existência de recursos disponíveis. A Lei nº 4.320/64 considera fonte de recurso legal para esse fim:",
    "options": [
      "O superávit financeiro apurado em balanço patrimonial do exercício imediatamente anterior.",
      "A expectativa de crescimento econômico e projeção de inflação para o semestre seguinte.",
      "O aumento discricionário da base de cálculo do imposto predial sem respaldo legal expresso.",
      "A retenção preventiva de parcelas salariais devidas aos servidores do Poder Legislativo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 43, § 1º da Lei 4.320/64 elenca 4 fontes: I - superávit financeiro do exercício anterior; II - excesso de arrecadação; III - anulação parcial ou total de dotações; IV - operações de crédito. Também há a reserva de contingência (LRF)."
  },
  {
    "id": 622,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Créditos Extraordinários (CF/88, Art. 167, § 3º)",
    "question": "No que tange aos créditos extraordinários no ordenamento constitucional brasileiro, é correto afirmar que são abertos exclusivamente para atender a despesas:",
    "options": [
      "De capital decorrentes de atrasos de fornecedores em obras públicas de execução regular.",
      "Correntes fixadas a menor na Lei Orçamentária Anual por equívoco da comissão mista da Casa.",
      "Imprevisíveis e urgentes, como as decorrentes de guerra, comoção interna ou calamidade pública.",
      "Institucionais da Câmara Municipal para aquisição de novos sistemas de votação eletrônica."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 167, § 3º da CF/88: 'A abertura de crédito extraordinário somente será admitida para atender a despesas imprevisíveis e urgentes, como as decorrentes de guerra, comoção interna ou calamidade pública, observado o disposto no art. 62.'"
  },
  {
    "id": 623,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Campos de E-mail: Para, Cc e Cco",
    "question": "Um servidor público envia uma mensagem oficial preenchendo: Para: chefe@orgao.gov.br, Cc: colega@orgao.gov.br e Cco: fiscal@orgao.gov.br. Nessa situação comunicativa:",
    "options": [
      "O destinatário em 'Cc' não saberá que o destinatário em 'Para' recebeu a referida mensagem.",
      "O destinatário em 'Cco' verá os outros endereços, mas nenhum deles saberá que 'Cco' a recebeu.",
      "Os três servidores saberão com exatidão quem são todos os participantes que receberam o e-mail.",
      "O e-mail será bloqueado pelo servidor de correio por misturar campos abertos com campos ocultos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O campo Cco (Cópia Carbono Oculta / BCC) oculta o endereço de quem está nele. Quem está em Cco enxerga os campos Para e Cc, mas ninguém em Para ou Cc sabe da existência do Cco."
  },
  {
    "id": 624,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Protocolos de Correio Eletrônico: SMTP vs. POP3 vs. IMAP",
    "question": "Em relação aos protocolos da arquitetura TCP/IP utilizados no serviço de correio eletrônico, o protocolo responsável especificamente pelo envio (saída) de mensagens é o:",
    "options": [
      "IMAP (Internet Message Access Protocol), que faz o envio criptografado e seguro da mensagem.",
      "POP3 (Post Office Protocol), que realiza o despacho e distribuição do e-mail no servidor.",
      "SMTP (Simple Mail Transfer Protocol), responsável direto pelo envio e trânsito da mensagem.",
      "SNMP (Simple Network Management Protocol), encarregado de enviar dados de correio na rede."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O SMTP (Simple Mail Transfer Protocol) é o protocolo padrão para ENVIO (saída) de e-mails. Mnemônico clássico de concurso: SMTP = 'Sua Mensagem Tá Partindo'. POP3 e IMAP são para recebimento/leitura."
  },
  {
    "id": 625,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Diferença Operacional entre POP3 e IMAP",
    "question": "Ao configurar uma conta de correio eletrônico corporativo em um aplicativo cliente, a principal diferença operacional entre os protocolos POP3 e IMAP reside no fato de que:",
    "options": [
      "O POP3 exige autenticação por certificado digital, enquanto o IMAP opera sem necessidade de senha.",
      "O IMAP sincroniza as pastas em nuvem no servidor, enquanto o POP3 baixa os e-mails para o computador.",
      "O POP3 funciona exclusivamente em redes locais internas, enquanto o IMAP opera na internet pública.",
      "O IMAP apaga os arquivos do servidor após a leitura, enquanto o POP3 cria cópias espelhadas na web."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O IMAP mantém as mensagens e pastas no servidor, sincronizando o status de leitura em múltiplos dispositivos. O POP3 baixa as mensagens para a máquina local do usuário e, por padrão, as exclui do servidor."
  },
  {
    "id": 626,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Portas Padrão de E-mail: SMTP Seguro (STARTTLS)",
    "question": "No Brasil, para coibir a proliferação de spams e modernizar a segurança da infraestrutura, a antiga porta 25 do protocolo SMTP foi oficialmente substituída pela porta padrão:",
    "options": [
      "587 (Porta de Submission com autenticação STARTTLS recomendada pelo CGI.br/CERT.br).",
      "110 (Porta padrão tradicional reservada para o recebimento de mensagens do protocolo POP3).",
      "993 (Porta segura criptografada utilizada para o acesso remoto de caixas postais via IMAP).",
      "443 (Porta de navegação web segura utilizada pelos navegadores para comunicação HTTPS)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A porta 587 (Submission / SMTP autenticado) substituiu a porta 25 no Brasil para envio de e-mails por usuários finais. A porta 110 é do POP3 simples, a 993 é do IMAP SSL e a 443 é do HTTPS."
  },
  {
    "id": 627,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Cliente de E-mail: Mozilla Thunderbird",
    "question": "O Mozilla Thunderbird é um aplicativo de correio eletrônico amplamente empregado na administração pública. Constitui uma característica técnica verdadeira desse software:",
    "options": [
      "Exigir licença paga por posto de trabalho para instalação em órgãos do Poder Legislativo.",
      "Ser um programa gratuito de código aberto (open source) que suporta contas IMAP e POP3.",
      "Funcionar apenas no sistema Windows, sendo incompatível com distribuições Linux e macOS.",
      "Impedir a anexação de arquivos PDF ou compactados para evitar transmissão de malwares."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O Mozilla Thunderbird é um software livre, gratuito e de código aberto (open-source), multiplataforma (roda em Windows, Linux, macOS), que suporta contas POP3, IMAP e SMTP com gerenciamento de múltiplos perfis."
  },
  {
    "id": 628,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Ferramentas de Mensageria: WhatsApp Web",
    "question": "A respeito do uso do WhatsApp Web no ambiente de trabalho administrativo para atendimento institucional ao cidadão, é correto afirmar que:",
    "options": [
      "Permite o envio de mensagens, documentos e áudios diretamente pela interface do navegador.",
      "Exige a digitação manual de login e senha alfanumérica criada previamente pelo suporte de TI.",
      "Impede a transmissão de arquivos no formato PDF ou imagens para computadores corporativos.",
      "Funciona de forma autônoma sem necessidade de vínculo com a conta do aplicativo móvel."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O WhatsApp Web permite enviar mensagens, imagens, áudios e documentos (PDF, planilhas, textos) pelo navegador. A sincronização inicial é realizada por leitura de QR Code vinculado à conta do celular."
  },
  {
    "id": 629,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Ferramentas de Mensageria: Telegram",
    "question": "Diferentemente de outros aplicativos de mensagens instantâneas, o Telegram destaca-se no uso institucional por apresentar como diferencial técnico relevante:",
    "options": [
      "Arquitetura em nuvem que permite uso independente em múltiplos aparelhos e canais públicos.",
      "Limite rígido de apenas 256 participantes em qualquer grupo institucional de trabalho da Casa.",
      "Armazenamento de conversas restrito à memória física local do celular do servidor público.",
      "Obrigatoriedade de instalação de certificado digital A3 para acesso às salas de conversa."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Telegram é baseado em nuvem (cloud-based), permitindo acesso simultâneo e independente no desktop, web e celular, além de oferecer canais de transmissão para audiências ilimitadas e grupos de até 200.000 membros."
  },
  {
    "id": 630,
    "category": "gerais",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Ferramentas de Colaboração: Discord",
    "question": "O Discord, ferramenta de comunicação e colaboração em tempo real, organiza suas comunidades e grupos de trabalho administrativo principalmente por meio de:",
    "options": [
      "Servidores estruturados em canais distintos de texto e voz com atribuição de cargos e papéis.",
      "Linhas de transmissão individuais baseadas exclusivamente em envio sequencial de mensagens SMS.",
      "Pastas compactadas em formato ZIP enviadas como anexos por intermédio de servidores FTP.",
      "Planilhas eletrônicas compartilhadas que limitam o acesso a apenas dois membros simultâneos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Discord organiza suas equipes em 'Servidores' (guilds), que são subdivididos em canais de texto e canais de voz/vídeo, permitindo definir permissões granulares por meio de cargos e funções (roles)."
  }
]

print(f"Total w4_d3 preparadas: {len(W4_D3_QUESTIONS)}")
for q in W4_D3_QUESTIONS:
    lens = [len(o) for o in q["options"]]
    cor = q["correctAnswer"]
    max_l = max(lens)
    min_l = min(lens)
    ratio = max_l / min_l
    cor_l = lens[cor]
    print(f"Q{q['id']}: Cor={chr(65+cor)} | Lens={lens} | Ratio={ratio:.2f} | CorLen={cor_l} (Max={max_l})")
