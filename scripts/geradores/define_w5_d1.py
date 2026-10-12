import sys, json
sys.stdout.reconfigure(encoding='utf-8')

# 18 Questoes para Semana 5 Dia 1 (28/09/2026 - HOJE)
# Distribuicao perfeitamente balanceada: 5 A, 5 B, 4 C, 4 D
# Ratio de tamanho de alternativas estritamente calibrado (< 1.10) para nao destacar o gabarito.
W5_D1_QUESTIONS = [
  {
    "id": 649,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Conceito e Momentos do Controle Administrativo",
    "question": "Quanto ao momento de sua efetivação no âmbito da gestão pública, o controle exercido pelos órgãos competentes classifica-se em:",
    "options": [
      "Prévio (a priori), concomitante (pari passu) e posterior (a posteriori ou corretivo).",
      "Hierárquico (interno), funcional (externo) e sancionatório (de natureza penal pública).",
      "Originário (constitucional), derivado (infraconstitucional) e residual (supletivo).",
      "Vinculado (obrigatório), discricionário (facultativo) e sumário (sem formalidades)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Quanto ao momento em que se realiza, o controle classifica-se em: 1) Prévio (preventivo/a priori), que antecede a conclusão do ato (ex: autorização legislativa); 2) Concomitante, realizado durante a execução (ex: fiscalização de contratos); 3) Posterior (corretivo/a posteriori), que incide sobre atos já consumados (ex: julgamento de contas)."
  },
  {
    "id": 650,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Controle Externo Municipal e Auxílio do Tribunal de Contas (Art. 31 CF/88)",
    "question": "Nos termos expressos do Art. 31 da Constituição Federal de 1988, a fiscalização do Município será exercida pelo Poder Legislativo municipal, mediante controle:",
    "options": [
      "Judicial autônomo e pelos sistemas de auditoria contábil contratados por licitação.",
      "Externo, e pelos sistemas de controle interno do Poder Executivo municipal local.",
      "Hierárquico direto, com subordinação das secretarias municipais à Mesa da Câmara.",
      "Ministerial difuso, auxiliado privativamente pelos conselhos comunitários do bairro."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. CF/88, Art. 31: 'A fiscalização do Município será exercida pelo Poder Legislativo municipal, mediante controle externo, e pelos sistemas de controle interno do Poder Executivo municipal, na forma da lei.' O § 1º complementa que o controle externo da Câmara será exercido com o auxílio do Tribunal de Contas competente."
  },
  {
    "id": 651,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Parecer Prévio do Tribunal de Contas (CF/88, Art. 31, § 2º)",
    "question": "O parecer prévio emitido pelo órgão competente sobre as contas que o Prefeito deve anualmente prestar só deixará de prevalecer por decisão de:",
    "options": [
      "Maioria simples dos vereadores presentes na respectiva sessão plenária da Câmara.",
      "Maioria absoluta de todos os membros que compõem oficialmente o Poder Legislativo.",
      "Dois terços dos membros da Câmara Municipal, conforme quórum estrito da CF/88.",
      "Três quintos dos parlamentares municipais em votação realizada em dois turnos."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. CF/88, Art. 31, § 2º: 'O parecer prévio, emitido pelo órgão competente sobre as contas que o Prefeito deve anualmente prestar, só deixará de prevalecer por decisão de dois terços dos membros da Câmara Municipal.' Esse quórum qualificado de 2/3 é uma das regras mais cobradas pela INBRASP."
  },
  {
    "id": 652,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Competência para Julgamento das Contas do Prefeito (STF Temas 157 e 835)",
    "question": "Consoante a jurisprudência vinculante do Supremo Tribunal Federal sobre o julgamento das contas de governo e de gestão prestadas pelo Prefeito Municipal:",
    "options": [
      "Compete ao Tribunal de Contas julgar em definitivo as contas de gestão com eficácia eleitoral.",
      "Compete ao Ministério Público Estadual deliberar soberanamente sobre a rejeição das contas anuais.",
      "Compete exclusivamente à Câmara Municipal julgar ambas as contas para fins de inelegibilidade.",
      "Compete à Justiça Eleitoral analisar de forma originária o mérito contábil da execução municipal."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O STF pacificou nos Temas 157 e 835 de Repercussão Geral que compete EXCLUSIVAMENTE à Câmara Municipal o julgamento das contas do Prefeito, tanto as contas de governo quanto as contas de gestão (atuando como ordenador de despesas), sendo o parecer do Tribunal de Contas meramente opinativo, para fins de inelegibilidade da Lei da Ficha Limpa."
  },
  {
    "id": 653,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Julgamento de Contas dos Demais Administradores (CF/88, Art. 71, II)",
    "question": "Diferentemente das contas do chefe do Executivo, as contas dos demais administradores e responsáveis por dinheiros, bens e valores públicos são:",
    "options": [
      "Submetidas a referendo popular obrigatório mediante convocação expedida pelo parlamento.",
      "Homologadas pelo presidente da Câmara após parecer favorável da comissão permanente mista.",
      "Apreciadas unicamente pela Controladoria-Geral do Município sem qualquer recurso ao Judiciário.",
      "Julgadas diretamente pelo Tribunal de Contas, com eficácia de título executivo na condenação."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. CF/88, Art. 71, II: compete ao Tribunal de Contas 'julgar as contas dos administradores e demais responsáveis por dinheiros, bens e valores públicos'. E o § 3º do Art. 71 estabelece que as decisões do Tribunal de que resulte imputação de débito ou multa terão eficácia de título executivo."
  },
  {
    "id": 654,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Finalidades do Sistema de Controle Interno (CF/88, Art. 74)",
    "question": "De acordo com o Art. 74 da CF/88, os Poderes Legislativo, Executivo e Judiciário manterão sistema integrado de controle interno com a finalidade de:",
    "options": [
      "Avaliar o cumprimento das metas do PPA e apoiar o controle externo no exercício de sua missão.",
      "Substituir integralmente a fiscalização exercida pelos membros do Poder Legislativo municipal.",
      "Promover a instauração de inquéritos policiais contra servidores públicos em estágio probatório.",
      "Autorizar a concessão de empréstimos bancários internacionais para obras de infraestrutura local."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 74 da CF/88: os sistemas de controle interno têm por finalidade: I - avaliar o cumprimento das metas previstas no PPA, a execução dos programas de governo e dos orçamentos; II - comprovar a legalidade e eficácia da gestão; IV - apoiar o controle externo no exercício de sua missão institucional."
  },
  {
    "id": 655,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Dever Constitucional de Prestar Contas (CF/88, Art. 70, parágrafo único)",
    "question": "O princípio republicano impõe o dever de prestar contas. No ordenamento brasileiro, prestará contas qualquer pessoa física ou jurídica, pública ou privada, que:",
    "options": [
      "Utilize, arrecade, guarde, gerencie ou administre dinheiros, bens e valores públicos municipais.",
      "Exerça mandato representativo eletivo no Poder Legislativo por período superior a três legislaturas.",
      "Possua vínculo empregatício sob a CLT em empresas concessionárias privadas de serviços de água.",
      "Participe de certames licitatórios presenciais na modalidade leilão sem recolher caução inicial."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. CF/88, Art. 70, parágrafo único: 'Prestará contas qualquer pessoa física ou jurídica, pública ou privada, que utilize, arrecade, guarde, gerencie ou administre dinheiros, bens e valores públicos ou pelos quais a União [ou o Município] responda, ou que, em nome desta, assuma obrigações de natureza pecuniária.'"
  },
  {
    "id": 656,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Princípio da Autotutela Administrativa (Súmulas 346 e 473 do STF)",
    "question": "Em decorrência do princípio da autotutela consagrado na doutrina e na jurisprudência sumulada do STF, a administração pública possui a prerrogativa de:",
    "options": [
      "Executar penalidades corporais restritivas de liberdade a cidadãos inadimplentes com o fisco.",
      "Intervir militarmente nos poderes constituídos caso ocorra paralisação grevista dos servidores.",
      "Anular seus próprios atos quando eivados de vícios de legalidade, e revogá-los por conveniência.",
      "Alterar unilateralmente o valor dos subsídios dos vereadores fixados na legislatura antecedente."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Súmula 473 do STF: 'A administração pode anular seus próprios atos, quando eivados de vícios que os tornam ilegais, porque deles não se originam direitos; ou revogá-los, por motivo de conveniência ou oportunidade, respeitados os direitos adquiridos, e ressalvada, em todos os casos, a apreciação judicial.'"
  },
  {
    "id": 657,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Limites do Controle Judicial dos Atos Administrativos",
    "question": "No tocante à extensão do controle exercido pelo Poder Judiciário sobre os atos expedidos pela administração pública, é correto afirmar que o juiz:",
    "options": [
      "Pode avaliar a conveniência e oportunidade do ato discricionário praticado pelo gestor.",
      "Não pode intervir mesmo quando houver manifesta violação aos princípios do Art. 37 da CF.",
      "Tem o poder privativo de revogar atos administrativos com base em juízo de pura utilidade.",
      "Deve restringir sua atuação ao exame da legalidade e legitimidade, vedado o mérito do ato."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O controle judicial restringe-se aos aspectos de legalidade, legitimidade e moralidade do ato administrativo, sendo-lhe expressamente vedado ingressar no exame do mérito administrativo (conveniência e oportunidade da escolha discricionária do administrador), sob pena de violar a separação de Poderes (Art. 2º da CF/88)."
  },
  {
    "id": 658,
    "category": "especificos",
    "day": "w5_d1",
    "discipline": "Controle da Administração Pública",
    "topic": "Instrumentos de Controle Social: Ação Popular (CF/88, Art. 5º, LXXIII)",
    "question": "A Ação Popular, relevante mecanismo de controle social da administração previsto no Art. 5º, LXXIII da CF/88, tem como legitimado ativo exclusivo para sua propositura:",
    "options": [
      "Qualquer pessoa jurídica regularmente constituída com mais de um ano de atividade no país.",
      "Qualquer cidadão que comprove sua condição de eleitor no gozo de seus direitos políticos.",
      "O Ministério Público Estadual representado privativamente pelo procurador-geral de justiça.",
      "A comissão permanente de fiscalização e controle do Poder Legislativo municipal da comarca."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. CF/88, Art. 5º, LXXIII: 'qualquer CIDADÃO é parte legítima para propor ação popular que vise a anular ato lesivo ao patrimônio público ou de entidade de que o Estado participe, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural'. Cidadão = brasileiro no gozo de direitos políticos (com título de eleitor)."
  },
  {
    "id": 659,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Semântica: Sinonímia e Sentido Contextual",
    "question": "No trecho 'O plenário da Câmara anuiu integralmente à proposta do projeto de resolução', o vocábulo grifado 'anuiu' possui como sinônimo perfeito no contexto:",
    "options": [
      "Recusou expressamente os termos consignados na proposição apresentada pelos parlamentares.",
      "Adiou temporariamente o início da contagem dos prazos regimentais estipulados na Casa.",
      "Concordou com a matéria, expressando assentimento favorável à deliberação em julgamento.",
      "Questionou a validade material das regras orçamentárias estabelecidas pela mesa diretora."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. 'Anuir' significa concordar, assentir, consentir, aquiescer. No contexto, o plenário concordou (anuiu) com a proposta. Questão clássica de vocabulário da banca INBRASP."
  },
  {
    "id": 660,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Semântica: Antonímia e Relações de Oposição",
    "question": "A antonímia manifesta-se quando duas palavras estabelecem entre si uma relação de oposição semântica. O par de vocábulos que exemplifica essa relação é:",
    "options": [
      "Inócuo e inofensivo, ambos caracterizando fatos que não produzem qualquer dano à sociedade.",
      "Hediondo e repulsivo, qualificando condutas reprováveis que geram intensa aversão social.",
      "Insipiente e ignorante, referindo-se ambos à pessoa desprovida de conhecimentos formais.",
      "Efêmero e perene, expressando respectivamente o que é passageiro e o que é permanente."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. 'Efêmero' (que dura pouco, passageiro) e 'perene' (duradouro, eterno, permanente) são antônimos perfeitos. Os demais pares representam casos de sinonímia (inócuo = inofensivo; insipiente = ignorante; hediondo = repulsivo)."
  },
  {
    "id": 661,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Parônimos: Ratificar vs. Retificar",
    "question": "Assinale a alternativa que preenche correta e respectivamente as lacunas: 'O prefeito precisou _____ o decreto publicado com erro na data e, em seguida, a Câmara resolveu _____ o convênio firmado':",
    "options": [
      "Retificar (no sentido de corrigir) e ratificar (no sentido de confirmar e validar o ato).",
      "Ratificar (no sentido de anular) e retificar (no sentido de emendar as cláusulas do texto).",
      "Ratificar (no sentido de corrigir) e retificar (no sentido de validar as parcelas do fundo).",
      "Retificar (no sentido de suspender) e ratificar (no sentido de prorrogar o prazo do edital)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico clássico da INBRASP: Retificar = rEtificar (consErtar, corrigir); Ratificar = rAtificar (confirmAr, validar). Logo, o prefeito precisou retificar (corrigir o erro) e a Câmara resolveu ratificar (confirmar o convênio)."
  },
  {
    "id": 662,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Parônimos: Deferir vs. Diferir",
    "question": "A respeito do par de parônimos 'deferir' e 'diferir' na redação de despachos e correspondências administrativas, é correto afirmar que:",
    "options": [
      "Deferir expressa discordância jurídica, enquanto diferir significa aprovar pedido protocolado.",
      "Diferir é exclusivo da linguagem poética, não possuindo qualquer acepção na esfera pública.",
      "Ambos os vocábulos são sinônimos perfeitos aplicados indiferentemente no encerramento de parecer.",
      "Deferir significa conceder ou atender a um pedido, enquanto diferir expressa adiar ou divergir."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. 'Deferir' = conceder, aprovar, atender favoravelmente a um requerimento (ex: 'O presidente deferiu o pedido de licença'). 'Diferir' = adiar, prorrogar para momento futuro, ou ser diferente/divergir."
  },
  {
    "id": 663,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Parônimos: Eminente vs. Iminente",
    "question": "Na oração 'O _____ jurista alertou para o perigo _____ de desabamento do teto do plenário', as lacunas devem ser preenchidas, na norma culta, por:",
    "options": [
      "Iminente (no sentido de notável e ilustre) e eminente (no sentido de algo que vai ocorrer).",
      "Eminente (no sentido de ilustre e célebre) e iminente (no sentido de prestes a acontecer).",
      "Eminente (no sentido de imediato e próximo) e eminente (expressando gravidade técnica).",
      "Iminente (no sentido de autoridade pública) e iminente (indicando perigo de ampla monta)."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Eminente (com E) = excelente, elevado, ilustre, notável. Iminente (com I) = que está prestes a acontecer, imediato (perigo iminente). Logo: 'O eminente jurista alertou para o perigo iminente de desabamento'."
  },
  {
    "id": 664,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Homônimos Homófonos: Sessão vs. Seção vs. Cessão",
    "question": "Em um texto normativo da Câmara Municipal, os termos 'sessão', 'seção' e 'cessão' devem ser empregados respectivamente para indicar:",
    "options": [
      "Reunião de colegiado deliberativo, divisão ou setor administrativo e ato de ceder direitos.",
      "Ato de ceder patrimônio da Casa, reunião do plenário parlamentar e corte de dotação anual.",
      "Divisão interna do organograma, reunião solene de vereadores e renúncia tácita de mandato.",
      "Interrupção de expediente público, departamento da prefeitura e doação pura de imóvel local."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico clássico da INBRASP: 1) Sessão (com 3 's') = reunião, assembleia (ex: sessão plenária da Câmara); 2) Seção ou Secção (com ç) = parte, repartição, departamento, corte (ex: seção de protocolo); 3) Cessão (inicia com C) = ato de ceder, transferência de posse ou direito (ex: cessão de servidores)."
  },
  {
    "id": 665,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Semântica: Relações de Hiperonímia e Hiponímia",
    "question": "As noções de hiperonímia e hiponímia estabelecem relações semânticas de inclusão entre termos gerais e específicos. O par que expressa a relação de hiperônimo para hipônimo é:",
    "options": [
      "Viatura e meio de locomoção, indicando o caso particular antecedendo o conceito genérico.",
      "Veículo e viatura, em que o primeiro expressa a classe ampla e o segundo a espécie concreta.",
      "Portaria e ato normativo, sendo o primeiro o termo abrangente que engloba as demais leis.",
      "Requerimento e petição, representando duas palavras sinônimas sem qualquer vínculo de grau."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Hiperônimo é a palavra com sentido genérico, abrangente (ex: 'veículo'). Hipônimo é a palavra de sentido específico, particular, contida no hiperônimo (ex: 'viatura'). Logo, a relação de hiperônimo para hipônimo é Veículo (geral) -> Viatura (específico)."
  },
  {
    "id": 666,
    "category": "gerais",
    "day": "w5_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Semântica: Denotação vs. Conotação",
    "question": "Assinale a alternativa em que a palavra destacada foi empregada em sentido conotativo (figurado), distanciando-se de sua acepção denotativa (literal):",
    "options": [
      "O servidor arquivou todas as pastas de documentos fiscais nas prateleiras de aço.",
      "O debate político na comissão esquentou o clima entre os parlamentares da bancada.",
      "O motorista conduziu o veículo oficial da câmara até a sede do tribunal regional.",
      "O técnico administrativo protocolou o ofício no sistema eletrônico de informações."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Sentido denotativo é o sentido literal, real, dicionarizado da palavra. Sentido conotativo é o sentido figurado, metafórico. Na frase 'esquentou o clima', a palavra expressa que os ânimos ficaram exaltados (conotação), e não uma elevação física de temperatura térmica."
  }
]

if __name__ == "__main__":
    print(f"Total questoes: {len(W5_D1_QUESTIONS)}")
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    alertas = 0
    for q in W5_D1_QUESTIONS:
        lens = [len(o) for o in q["options"]]
        cor = q["correctAnswer"]
        counts[chr(65+cor)] += 1
        max_l = max(lens)
        min_l = min(lens)
        ratio = max_l / min_l
        cor_l = lens[cor]
        print(f"Q{q['id']}: Cor={chr(65+cor)} | Lens={lens} | Ratio={ratio:.2f} | CorLen={cor_l} (Max={max_l})")
        if ratio > 1.25:
            alertas += 1

    print("Distribuicao de gabarito:", counts)
    print("Total alertas de desbalanceamento:", alertas)
