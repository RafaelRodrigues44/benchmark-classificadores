import streamlit as st

def render():

    st.markdown('<div class="nature-h1">Resumo</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
    O diagnóstico assistido por inteligência artificial tornou-se uma das principais frentes de pesquisa em oncologia computacional, especialmente em cenários que exigem elevada sensibilidade para detecção precoce de tumores malignos. Embora métodos de ensemble sejam frequentemente adotados como estratégias para maximizar desempenho preditivo, sua eficácia depende da calibração adequada dos modelos participantes. Neste estudo, foram avaliados seis classificadores de machine learning utilizando o conjunto de dados Wisconsin Breast Cancer: k-Nearest Neighbors, Naive Bayes, Árvore de Decisão, Random Forest, Rede Neural Multicamadas e Support Vector Machine. Inicialmente, os modelos foram integrados em um comitê por votação suave, cuja configuração não ponderada demonstrou degradação do desempenho clínico ao aumentar a ocorrência de Falsos Negativos. Em contraste, o Support Vector Machine apresentou o melhor desempenho individual, alcançando acurácia de 98,25%. A aplicação posterior de técnicas de calibração do limiar de decisão permitiu reduzir pela metade os Falsos Negativos, passando de dois para apenas um caso, sem introduzir Falsos Positivos adicionais. Os resultados demonstram que a otimização criteriosa de um modelo especialista pode superar arquiteturas coletivas amplas quando o objetivo principal é maximizar a segurança diagnóstica em ambientes médicos de alta criticidade.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text" style="font-size:0.95rem; margin-top:-0.3rem;">
    <b>Palavras-chave:</b> aprendizado de máquina, inteligência artificial aplicada à saúde, Support Vector Machine, Threshold Tuning, métodos de ensemble, câncer de mama.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nature-h1">Abstract</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
    Artificial intelligence-assisted diagnosis has become a major research direction in computational oncology, particularly in scenarios requiring high sensitivity for early malignant tumor detection. Although ensemble methods are commonly employed to maximize predictive performance, their effectiveness strongly depends on proper calibration of participating models. In this study, six machine learning classifiers were evaluated using the Wisconsin Breast Cancer dataset: k-Nearest Neighbors, Naive Bayes, Decision Tree, Random Forest, Multilayer Perceptron Neural Network, and Support Vector Machine. Initially, the models were integrated into a soft-voting committee whose unweighted configuration degraded clinical performance by increasing the number of False Negatives. In contrast, the Support Vector Machine achieved the best standalone performance, reaching an accuracy of 98.25%. Subsequent decision-threshold calibration further improved diagnostic sensitivity, reducing False Negatives from two to one case while maintaining zero False Positives. These findings suggest that careful optimization of a specialist model may outperform broad collective architectures when diagnostic safety is the primary objective in high-stakes medical environments.
    </p>
    """, unsafe_allow_html=True)

    st.markdown(
        '<p class="nature-text" style="font-size:0.95rem;"><b>Keywords:</b> Machine Learning, Healthcare Artificial Intelligence, Support Vector Machine, Threshold Tuning, Ensemble Methods, Breast Cancer.</p>',
        unsafe_allow_html=True
    )

