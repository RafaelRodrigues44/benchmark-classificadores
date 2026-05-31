import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def render():
    st.markdown(
        '<div class="nature-h1">6. A Rodada 2: O Avanço da Ponderação Meritocrática</div>',
        unsafe_allow_html=True
    )

    col_text, col_img = st.columns([1.2, 1])

    with col_text:
        st.markdown("""
        <style>
        .code {
            display: table; /* Funciona como bloco, mas assume o tamanho exato do conteúdo */
            margin: 0.5rem auto !important; /* Força o alinhamento centralizado no Streamlit */

            background: #f6f8fa;
            border: 1px solid #d0d7de;

            padding: 0.6rem 0.6rem !important;

            font-family: "Times New Roman", Times, serif;
            font-size: 0.95rem;
            color: #1f2328;

            border-radius: 4px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            white-space: nowrap;
        }
        .nature-text {
            /* Opcional: Garante boa leitura do texto justificando ou alinhando à esquerda */
            text-align: justify; 
        }
        </style>

        <p class="nature-text">
            Após a falha analítica na primeira rodada, a arquitetura foi reajustada para aplicar um sistema de <b>pesos hierárquicos</b> no <i>VotingClassifier</i>. Em vez de uma democracia ingênua, implementamos um regime meritocrático:
        </p>

        <code class="code">weights=[5, 4, 3, 1, 1, 1]</code>

        <p class="nature-text">
            Este vetor de ponderação foi derivado diretamente da performance isolada de cada modelo na Fase 1, calculada através da área sob a curva (AUC). O SVM (peso 5) assumiu o papel normativo central, seguido pela Random Forest (peso 4) e Redes Neurais (peso 3). Modelos de alta variância ou vieses teóricos divergentes, como o Naive Bayes e a Árvore de Decisão, foram reduzidos a um papel de desempate periférico (peso 1), minimizando sua capacidade de corromper a fronteira de decisão coletiva.
        </p>
        """, unsafe_allow_html=True)

    with col_img:
        fig, ax = plt.subplots(figsize=(4.5, 3.5))
        fig.patch.set_facecolor('#ffffff')
        ax.set_facecolor('#ffffff')

        cm_comite_pesos = np.array([[72, 0], [2, 40]])

        grafite_cmap = sns.light_palette("#3b4a5a", as_cmap=True)

        sns.heatmap(
            cm_comite_pesos,
            annot=True,
            fmt='d',
            cmap=grafite_cmap,
            cbar=False,
            xticklabels=['Benigno', 'Maligno'],
            yticklabels=['Benigno', 'Maligno'],
            annot_kws={"size": 14, "weight": "bold"}
        )

        plt.title(
            "Matriz de Confusão - Comitê Ponderado (Pesos Ajustados)",
            fontsize=10,
            fontfamily='serif',
            color='#2c3e50',
            weight='bold'
        )

        plt.ylabel('Realidade', fontsize=8, color='#2c3e50')
        plt.xlabel('Predição Coletiva', fontsize=8, color='#2c3e50')
        ax.tick_params(colors='#2c3e50')

        st.pyplot(fig)

    st.markdown(
        '<div class="nature-insight" style="font-size: 0.95rem; line-height: 1.5; padding: 1.2rem; background-color: #f7f9fa; border-left: 4px solid #198754; margin-top: 0.8rem;"><b>Evolução Clínica Registrada:</b> A introdução da hierarquia de pesos restaurou a integridade do diagnóstico. O comitê ponderado convergiu para o desempenho do SVM isolado, eliminando a diluição de sinal. A taxa de Falsos Negativos reduziu-se de 3 para 2 casos, demonstrando que a inteligência coletiva só é superior à individual quando os especialistas possuem voz proporcional à sua capacidade de generalização e baixa taxa de viés indutivo [1, 2].</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <p class="nature-text" style="margin-top: 1.5rem;">
        Esta configuração de pesos corrigiu o ruído estatístico identificado na rodada anterior. Ao relegar os estimadores ruidosos a um papel secundário, a fronteira de decisão do comitê deixou de ser uma média aritmética simplista e tornou-se uma <b>combinação convexa de especialistas</b>. A eficácia demonstrada aqui valida a hipótese de que o desempenho de sistemas <i>ensemble</i> em medicina depende menos do número de algoritmos integrados e mais da capacidade de filtragem seletiva de especialistas baseados na confiabilidade de suas margens de erro [3].
    </p>
    """, unsafe_allow_html=True)

    st.markdown(
        "<hr style='border-color: #e0e0e0; margin-top: 3rem; margin-bottom: 1.5rem;'>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="font-size: 0.85rem; color: #777777; line-height: 1.5; font-family: 'Inter', sans-serif;">
        <p style="margin-bottom: 0.4rem;">[1] KUNCHEVA, L. I. <b>Combining pattern classifiers: methods and algorithms</b>. John Wiley & Sons, 2014.</p>
        <p style="margin-bottom: 0.4rem;">[2] WOLPERT, D. H. Stacked generalization. <b>Neural Networks</b>, v. 5, n. 2, p. 241-259, 1992.</p>
        <p style="margin-bottom: 0.4rem;">[3] ZHOU, Z. H. <b>Ensemble Methods: Foundations and Algorithms</b>. Chapman and Hall/CRC, 2012.</p>
    </div>
    """, unsafe_allow_html=True)