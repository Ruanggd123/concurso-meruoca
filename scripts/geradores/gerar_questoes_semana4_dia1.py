import json

QUESTOES_S4_D1 = [
  {
  "id": 569,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Mesa Diretora: Mandato",
  "question": "Quanto ao mandato dos membros da Mesa Diretora da Câmara Municipal, a regra regimental mais comum estabelece que:",
  "options": [
    "O mandato é vitalício, só se encerrando com a renúncia expressa do ocupante.",
    "O mandato é de dois anos, permitida a recondução para o mesmo cargo na eleição imediatamente subsequente, observada a Lei Orgânica.",
    "O mandato coincide com o do Prefeito e não admite qualquer recondução.",
    "Os membros da Mesa são escolhidos por sorteio a cada sessão ordinária."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Padrão regimental: mandato de 2 anos (metade da legislatura), com possibilidade de recondução nos termos da Lei Orgânica. Vitaliciedade e sorteio inexistem; coincidir com o prefeito não é regra."
},
  {
  "id": 570,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Destituição de Membro da Mesa",
  "question": "A destituição de membro da Mesa Diretora que se omita ou exorbite de suas atribuições regimentais depende, em regra, de:",
  "options": [
    "Decisão judicial de primeira instância, sem participação da Câmara.",
    "Decreto do Prefeito determinando o afastamento imediato.",
    "Deliberação do Plenário pelo voto de dois terços dos vereadores, assegurada ampla defesa.",
    "Simples requerimento verbal de qualquer cidadão presente à sessão."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. A Mesa é eleita pela Câmara e só por ela pode ser destituída: quórum qualificado de 2/3 com contraditório e ampla defesa. Prefeito e Judiciário não destituem mesa diretora."
},
  {
  "id": 571,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Presidente: Representação da Câmara",
  "question": "Entre as atribuições do Presidente da Câmara Municipal inclui-se:",
  "options": [
    "Nomear os Secretários Municipais do Poder Executivo.",
    "Julgar crimes comuns praticados por qualquer cidadão do Município.",
    "Representar a Câmara em juízo e fora dele, bem como dar posse a Prefeito, Vice e Vereadores.",
    "Arrecadar diretamente os tributos municipais e executar o orçamento."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O Presidente é a face institucional do Legislativo: representa-o judicial e extrajudicialmente e preside a posse dos eleitos. Nomear secretários, julgar crimes e arrecadar são funções alheias ao cargo."
},
  {
  "id": 572,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Presidente: Direção dos Trabalhos",
  "question": "Na direção dos trabalhos plenários, compete ao Presidente da Câmara, entre outras atribuições:",
  "options": [
    "Votar em todas as matérias com peso dobrado em relação aos demais vereadores.",
    "Proibir qualquer vereador de apresentar requerimentos durante a legislatura.",
    "Alterar sozinho o texto de leis já aprovadas antes da promulgação.",
    "Abrir, presidir e encerrar as sessões, manter a ordem e suspender a sessão quando necessário."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Poderes de polícia dos trabalhos: abrir/presidir/encerrar, manter a ordem, suspender. Voto sem peso dobrado, vedação de requerimentos e alteração unilateral de lei aprovada são incompatíveis com o cargo."
},
  {
  "id": 574,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Sessões Ordinárias e Períodos Legislativos",
  "question": "As sessões legislativas ordinárias da Câmara Municipal realizam-se, por simetria com o modelo constitucional, em dois períodos anuais, compreendidos, em regra, entre:",
  "options": [
    "2 de fevereiro a 17 de julho e 1º de agosto a 22 de dezembro, com recessos em janeiro e parte de julho e dezembro.",
    "1º de janeiro a 31 de dezembro, sem qualquer recesso parlamentar.",
    "Apenas no mês de fevereiro de cada ano, em sessão única anual.",
    "Os dias de carnaval e as festas juninas, por tradição municipal."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 57: 02/02–17/07 e 01/08–22/12. Recesso não significa paralisação total: comissões e convocações extraordinárias subsistem."
},
  {
  "id": 575,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Sessões Extraordinárias",
  "question": "Sobre as sessões extraordinárias da Câmara Municipal, é CORRETO afirmar que:",
  "options": [
    "Ocorrem todos os dias úteis do ano, independentemente de convocação.",
    "Destinam-se a homenagens e comemorações, sem qualquer deliberação.",
      "Convocadas no recesso para matéria urgente e determinada, sem extra remuneratório.",
    "Podem tratar de qualquer assunto, ainda que estranho ao ato de convocação."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Extraordinária = recesso + matéria certa e urgente + sem extra remuneratório (CF, Art. 57, § 7º, por simetria). Homenagens são das solenes; a pauta vincula-se à convocação."
},
  {
  "id": 576,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Sessões Solenes e Secretas",
  "question": "As sessões solenes e as sessões secretas distinguem-se porque:",
  "options": [
    "Ambas servem apenas para a votação do orçamento anual.",
    "As solenes são sempre secretas e as secretas são sempre solenes.",
    "Nenhuma delas admite a presença de vereadores, sendo realizadas só por servidores.",
    "As solenes destinam-se a atos cívicos e homenagens, sem deliberação; secretas: sigilo regimental decidido pelo Plenário."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Solene = celebração (posse, títulos, homenagens), sem voto. Secreta = sigilo regimental, decidida pelo Plenário. Confundi-las é a pegadinha clássica."
},
  {
  "id": 577,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Abertura da Sessão e Quórum",
  "question": "Para a abertura das sessões plenárias e para as deliberações da Câmara, os quóruns regimentais típicos exigem, respectivamente:",
  "options": [
    "Unanimidade para abrir e maioria simples para deliberar.",
      "Um terço para abrir; maioria absoluta presente para deliberar.",
    "Apenas o Presidente presente para abrir e deliberar sozinho.",
    "Dois terços para abrir e unanimidade para qualquer deliberação."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Abertura com 1/3; deliberação com maioria absoluta presente decidindo por maioria de votos (CF, Art. 47, por simetria). Unanimidade e decisão solitária inexistem como regra."
},
  {
  "id": 579,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Poder Conclusivo das Comissões",
  "question": "Em regra regimental, as comissões permanentes da Câmara podem deliberar de forma conclusiva, dispensando a votação em Plenário, quando:",
  "options": [
      "Se o Regimento autorizar, com recurso de um décimo para o Plenário.",
    "Em todas as matérias, esvaziando por completo as funções do Plenário.",
    "Apenas quando o Prefeito autorizar previamente cada deliberação.",
    "Jamais, pois toda matéria exige votação em Plenário sem exceção."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 58, § 2º, I: poder conclusivo previsto no Regimento, com recurso de 1/10 para o Plenário. Não é geral nem depende do Prefeito; tampouco é vedado em absoluto."
},
  {
  "id": 580,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "CPI: Poderes e Destino",
  "question": "As Comissões Parlamentares de Inquérito da Câmara Municipal possuem poderes de investigação próprios das autoridades judiciais e, ao final dos trabalhos, deverão:",
  "options": [
    "Condenar criminalmente os investigados, fixando penas de prisão.",
    "Arquivar sigilosamente o relatório, vedada qualquer divulgação.",
    "Encaminhar suas conclusões ao Ministério Público para as providências cabíveis, quando for o caso.",
    "Substituir o Tribunal de Contas no julgamento das contas do Prefeito."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. CPI investiga com poderes judiciais (quebra de sigilo mediante decisão, oitivas), mas não julga nem condena: remete ao MP. Arquivamento sigiloso obrigatório e substituição do TCE inexistem."
},
  {
  "id": 583,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Processos de Votação",
  "question": "Quanto aos processos de votação no Plenário da Câmara, a regra regimental típica estabelece que:",
  "options": [
    "Toda votação é secreta, sem exceção, inclusive nas eleições da Mesa.",
    "A votação simbólica é a regra geral e a nominal realiza-se mediante requerimento aprovado pelo Plenário.",
    "A votação simbólica é proibida e todas as matérias exigem chamada nominal.",
    "O voto é sempre aberto por aclamação, vedado qualquer registro individual."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Simbólica (permanecem sentados/aprovado) como regra; nominal (chamada com registro) por requerimento. Votação sempre secreta ou sempre por aclamação contrariam o padrão."
},
  {
  "id": 585,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Legislatura e Sessão Legislativa",
  "question": "No Poder Legislativo municipal, distinguem-se legislatura e sessão legislativa porque:",
  "options": [
    "Ambas têm duração de trinta dias e se confundem integralmente.",
    "A legislatura dura um ano e a sessão legislativa dura quatro anos.",
    "Legislatura = mandato de 4 anos; sessão legislativa = cada ano de trabalhos.",
    "A sessão legislativa só existe em ano eleitoral."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Legislatura = 4 anos (mandato); sessão legislativa = cada ano civil de trabalhos (com os dois períodos e recessos). Inverter ou igualar os conceitos é o erro cobrado."
},
  {
  "id": 588,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Assistir (Presenciar)",
  "question": "Assinale a frase em que o verbo ASSISTIR foi empregado com a regência correta no sentido de presenciar:",
  "options": [
    "Os vereadores assistiram à sessão solene de abertura dos trabalhos.",
    "Os vereadores assistiram a sessão solene de abertura dos trabalhos.",
    "Os vereadores assistiram na sessão solene de abertura dos trabalhos.",
    "Os vereadores assistiram para a sessão solene de abertura dos trabalhos."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Assistir = presenciar é VTI com preposição A. Como 'sessão' é palavra feminina determinada, soma-se o artigo: a + a = À (crase obrigatória). Sem crase, com EM ou PARA, a regência está errada."
},
  {
  "id": 590,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Visar (Almejar vs Mirar)",
  "question": "Assinale a frase em que o verbo VISAR está corretamente empregado:",
  "options": [
    "O projeto visa o fortalecimento da agricultura familiar.",
    "O projeto visa ao fortalecimento da agricultura familiar.",
    "O atirador visou a o alvo antes de disparar.",
    "O servidor visou de assinar o documento oficial."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Almejar = VTI com A ('visa AO fortalecimento'); como 'fortalecimento' é masculino, não há crase. Mirar = VTD ('visou o alvo'); pôr visto = VTD ('visou o documento'). As demais violam cada regência."
},
  {
  "id": 591,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Aspirar (Almejar vs Sorver)",
  "question": "Assinale a alternativa em que o verbo ASPIRAR está correto:",
  "options": [
    "O vereador aspira o cargo de presidente da Mesa.",
    "O paciente aspira a o oxigênio pelo cateter.",
    "A indústria aspira em novos mercados consumidores.",
    "O vereador aspira ao cargo de presidente da Mesa."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Almejar = VTI com A ('aspira AO cargo', sem crase por ser masculino); sorver/respirar = VTD ('aspira o oxigênio'). EM não rege nenhum dos sentidos."
},
  {
  "id": 592,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Obedecer e Desobedecer",
  "question": "Os verbos OBEDECER e DESOBEDECER são transitivos indiretos. Assinale a frase correta:",
  "options": [
    "Os servidores obedeceram o regimento interno da Câmara.",
    "Os servidores obedeceram com o regimento interno da Câmara.",
    "Os servidores desobedeceram de todas as normas regimentais.",
    "Os servidores obedeceram ao regimento interno da Câmara."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Obedecer/desobedecer exigem preposição A (VTI): 'obedecer AO regimento'. Sem preposição ou com COM/DE, a regência está errada. Sem crase aqui porque 'regimento' é masculino."
},
  {
  "id": 593,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Pagar e Perdoar (VTDI)",
  "question": "PAGAR e PERDOAR são bitransitivos: coisa sem preposição, pessoa com preposição. Assinale a frase correta:",
  "options": [
    "A Prefeitura pagou aos fornecedores as faturas em atraso.",
    "A Prefeitura pagou os fornecedores as faturas em atraso.",
    "O presidente perdoou a ofensa ao colega arrependido.",
    "O presidente perdoou o colega a ofensa sofrida."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Coisa = OD ('as faturas', sem preposição); pessoa = OI ('AOS fornecedores'). Em C/D os papéis se invertem: o correto seria 'perdoou AO colega A ofensa' (pessoa com A, coisa sem)."
},
  {
  "id": 594,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência Nominal",
  "question": "A regência nominal estuda a preposição exigida pelos nomes. Assinale a alternativa em que a regência nominal está correta:",
  "options": [
    "O técnico mostrou-se obediente o regulamento da Câmara.",
    "A comissão está favorável com a aprovação do projeto.",
    "O técnico mostrou-se obediente ao regulamento da Câmara.",
    "Os vereadores são aptos em legislar sobre a matéria."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Obediente/favorável pedem A ('obediente AO', 'favorável À aprovação'); apto pede A ou PARA ('aptos A legislar'). COM e EM violam a regência desses nomes."
}
]

print(f"[OK] Total de questões S4/D1 geradas: {len(QUESTOES_S4_D1)}")
