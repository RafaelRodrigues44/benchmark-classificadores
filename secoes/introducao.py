import streamlit as st

def render():
    st.markdown('<div class="nature-h1">1. Introdução</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        Na oncologia clínica moderna, o diagnóstico precoce e preciso do carcinoma de mama permanece como um dos 
        desafios mais críticos e determinantes para o prognóstico e sobrevida global das pacientes [1]. A transição 
        da análise puramente histopatológica subjetiva para sistemas de triagem e suporte à decisão assistidos por 
        computador (CAD - <i>Computer-Aided Diagnosis</i>) fundamenta-se na necessidade de mitigar o erro humano e 
        padronizar métricas de predição [2]. No contexto do Aprendizado de Máquina (<i>Machine Learning</i>) aplicado 
        à saúde, o mapeamento de padrões morfológicos e estruturais exige que os sistemas computacionais operem sob 
        uma métrica de sensibilidade extremada. A falha crítica primária neste domínio reside no erro de omissão 
        diagnóstica — o Falso Negativo —, cujas consequências estendem-se do atraso terapêutico ao desfecho clínico 
        fatal, sobrepujando o custo operacional de um Falso Positivo (alarme falso), o qual pode ser resolvido por 
        exames confirmatórios subsequentes [3].
    </p>

    <p class="nature-text">
        Este estudo propõe uma investigação comparativa, sistemática e exaustiva entre diferentes paradigmas de 
        classificação supervisionada. A fundamentação teórica e metodológica desta pesquisa alinha-se às diretrizes 
        e taxonomia consolidadas pelo Serviço Federal de Processamento de Dados (Serpro) e pela Escola Nacional de 
        Administração Pública (Enap) [4], estruturando-se através de três eixos fundamentais de indução computacional:
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        Este estudo propõe uma investigação comparativa, sistemática e exaustiva entre diferentes paradigmas de 
        classificação supervisionada. A fundamentação teórica e metodológica desta pesquisa alinha-se às diretrizes 
        e taxonomia consolidadas pelo Serviço Federal de Processamento de Dados (Serpro) e pela Escola Nacional de 
        Administração Pública (Enap) [4], estruturando-se através de três eixos fundamentais de indução computacional:
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nature-text-list">
    
    * **Paradigma Probabilístico:** Representado pelo Classificador Bayesiano (*Naïve Bayes*), fundamentado no Teorema de Bayes sob a assunção de independência condicional dos atributos [5].

    * **Paradigma Geométrico e de Margens:** Composto pelo algoritmo *k-Nearest Neighbors* (k-NN), baseado em métricas de distância em espaços multidimensionais [6], e pelo *Support Vector Machine* (SVM), focado na otimização de hiperplanos de separação de margem máxima via funções de Kernel [7].

    * **Paradigma Lógico e Conexionista:** Compreendendo as Árvores de Decisão (*Decision Trees*), que segmentam o espaço amostral através de critérios de entropia e ganho de informação [8], além das Redes Neurais Artificiais (*Multi-Layer Perceptron* - MLP), baseadas na convergência de gradientes via retropropagação do erro para aproximação de funções não lineares complexas [9].
    
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        É crucial ressaltar, contudo, que no atual estágio do desenvolvimento computacional, a análise preditiva via 
        algoritmos de aprendizado de máquina estabelece-se estritamente como uma porta de entrada metodológica e uma ferramenta 
        de triagem preliminar [11]. As saídas binárias geradas pelos classificadores operam de maneira passiva como uma segunda 
        opinião de suporte à decisão clínica, sem caráter substitutivo aos métodos tradicionais de avaliação médica e exames histopatológicos 
        soberanos. A utilidade prática dessa camada de inteligência artificial reside na sua capacidade de atuar como um sistema de 
        classificação de urgência (<i>triage optimization</i>), acelerando o encaminhamento de casos categorizados como positivos para 
        uma análise humana aprofundada baseada na correlação imediata com os sintomas relatados pelo paciente [12].
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        A presente pesquisa teve sua origem no aprofundamento técnico decorrente da participação em formações e experiências anteriores 
        voltadas à ciência de dados, aprendizado de máquina e análise preditiva. A partir da consolidação de conhecimentos prévios 
        em engenharia de software, modelagem computacional e interpretação analítica de dados, identificou-se a oportunidade de expandir 
        a investigação para um contexto experimental mais rigoroso, orientado à avaliação comparativa de classificadores supervisionados 
        aplicados ao diagnóstico do câncer de mama. Nesse contexto, o estudo foi estruturado como uma iniciativa de pesquisa independente 
        com foco simultâneo na ampliação do embasamento teórico, na validação prática de arquiteturas preditivas e na análise crítica 
        de estratégias de otimização de desempenho em cenários reais de classificação binária assistida por inteligência artificial.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="nature-h1">Contexto de Formação</p>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        Parte do aprofundamento teórico e metodológico desta pesquisa foi desenvolvida
        durante programas de formação complementar em ciência de dados e inteligência artificial.
    </p>
    """, unsafe_allow_html=True)

    with open("assets/certificado.pdf", "rb") as file:
        st.download_button(
            label="Certificado de Formação",
            data=file,
            file_name="certificado.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.markdown("""
    <p class="nature-text">
        O objetivo central desta pesquisa reside em desafiar empiricamente uma das premissas mais difundidas no 
        desenvolvimento de sistemas inteligentes modernos: a suposição de que arquiteturas combinatórias complexas, 
        baseadas em inteligência coletiva (<i>Ensemble Methods</i>), superam invariavelmente o desempenho de modelos 
        especialistas singulares (<i>Single Experts</i>) [10]. Avalia-se o comportamento desses seis classificadores base, 
        aplicados ao conjunto de dados <i>Wisconsin Breast Cancer</i>, sob topologias de comitês de votação unificados, 
        buscando identificar a ocorrência de fenômenos de diluição de sinal ou contaminação estatística em cenários de 
        fronteiras de decisão cinzentas e limítrofes.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color: #e0e0e0; margin-top: 3rem; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size: 0.85rem; color: #777777; line-height: 1.5; font-family: 'Inter', sans-serif;">
        <p style="margin-bottom: 0.4rem;">[1] SUNG, H. et al. Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries. <b>CA: A Cancer Journal for Clinicians</b>, v. 71, n. 3, p. 209-249, 2021.</p>
        <p style="margin-bottom: 0.4rem;">[2] GIGER, M. L. Machine Learning in Medical Imaging. <b>Journal of the American College of Radiology</b>, v. 15, n. 3, p. 512-520, 2018.</p>
        <p style="margin-bottom: 0.4rem;">[3] PECK, D. J. et al. Evaluation of False-Negative Appraisals in Mammography Screening. <b>The Lancet Oncology</b>, v. 22, n. 4, p. 488-497, 2022.</p>
        <p style="margin-bottom: 0.4rem;">[4] SERPRO; ENAP. <b>Ciência de Dados: Técnicas Avançadas de Classificação e Aprendizado de Máquina</b>. Escola Nacional de Administração Pública, Brasil, 2026.</p>
        <p style="margin-bottom: 0.4rem;">[5] MITCHELL, T. M. <b>Machine Learning</b>. 1. ed. New York: McGraw-Hill, 1997.</p>
        <p style="margin-bottom: 0.4rem;">[6] FIX, E.; HODGES, J. L. Discriminatory Analysis. <b>International Statistical Review</b>, v. 57, n. 3, p. 238-247, 1989.</p>
        <p style="margin-bottom: 0.4rem;">[7] CORTES, C.; VAPNIK, V. Support-Vector Networks. <b>Machine Learning</b>, v. 20, n. 3, p. 273-297, 1995.</p>
        <p style="margin-bottom: 0.4rem;">[8] QUINLAN, J. R. Induction of Decision Trees. <b>Machine Learning</b>, v. 1, n. 1, p. 81-106, 1986.</p>
        <p style="margin-bottom: 0.4rem;">[9] RUMELHART, D. E.; HINTON, G. E.; WILLIAMS, R. J. Learning representations by back-propagating errors. <b>Nature</b>, v. 323, p. 533–536, 1986.</p>
        <p style="margin-bottom: 0.4rem;">[10] DIETTERICH, T. G. Ensemble Methods in Machine Learning. <b>Multiple Classifier Systems</b>, LNCS, v. 1814, p. 1-15, 2000.</p>
        <p style="margin-bottom: 0.4rem;">[11] TOPOL, E. J. High-performance medicine: the convergence of human and artificial intelligence. <b>Nature Medicine</b>, v. 25, n. 1, p. 44-56, 2019.</p>
        <p style="margin-bottom: 0.4rem;">[12] SHORTLIFFE, E. H.; SEPÚLVEDA, M. J. Clinical Decision Support in the Era of Artificial Intelligence. <b>JAMA</b>, v. 320, n. 21, p. 2199-2200, 2018.</p>
    </div>
    """, unsafe_allow_html=True)

