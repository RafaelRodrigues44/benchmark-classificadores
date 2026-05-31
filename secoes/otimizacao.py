import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def render():
    st.markdown('<div class="nature-h1">7. Calibração Fina do Limiar de Decisão Clínico</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        As evidências levantadas culminam no preceito de que, em determinados eixos dimensionais de dados biomédicos, as estruturas interligadas complexas falham em acompanhar a perfeição arquitetural de um modelo individual lapidado à exaustão. Retomando o SVM como campeão consolidado (98,25% de acurácia), procedemos com a desconstrução do ponto de corte engessado em 0.50 (probabilidade padrão de decisão) conforme discutido por Cortes e Vapnik [2].
    </p>
    """, unsafe_allow_html=True)

    tabela_html = """
    <style>
        .nature-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
            margin-bottom: 3rem;
            font-family: 'Inter', sans-serif;
        }

        .nature-table th {
            border-bottom: 2px solid #2c3e50;
            padding: 14px 10px;
            text-align: left;
            color: #2c3e50;
            font-weight: 600;
            font-size: 0.95rem;
        }

        .nature-table td {
            border-bottom: 1px solid #eaeaea;
            padding: 12px 10px;
            color: #444444;
            font-size: 0.95rem;
        }

        .nature-table tr.highlight {
            background-color: #f0f2f4;
        }

        .nature-table tr.highlight td {
            color: #2c3e50;
            font-weight: bold;
        }
    </style>

    <table class="nature-table">
        <thead>
            <tr>
                <th>Limiar (Threshold)</th>
                <th>Falsos Positivos (FP)</th>
                <th>Falsos Negativos (FN)</th>
                <th>Status do Modelo</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>0.50</td><td>0</td><td>2</td><td>Padrão de Fábrica</td></tr>
            <tr><td>0.45</td><td>0</td><td>2</td><td>Estável</td></tr>
            <tr><td>0.40</td><td>0</td><td>2</td><td>Estável</td></tr>
            <tr class="highlight"><td>0.35</td><td>0</td><td>1</td><td>ZONA DE CONVERGÊNCIA ÓTIMA</td></tr>
            <tr><td>0.30</td><td>1</td><td>1</td><td>Perda de Especificidade</td></tr>
        </tbody>
    </table>
    """

    st.markdown(tabela_html, unsafe_allow_html=True)

    col_analise, col_matriz = st.columns([1.6, 1], gap="large")

    with col_analise:
        st.markdown("""
        <div style="padding-right: 1.2rem; margin-top: 35px">
        <p class="nature-text">
            No aprendizado estatístico voltado à saúde, o recuo do limiar analítico costuma esbarrar em um paradoxo de trade-off direto entre sensibilidade e especificidade, conforme descrito na literatura clássica de Fawcett [1]. Surpreendentemente, a calibração paramétrica aplicada à superfície de decisão do SVM encontrou um ponto de eficiência assimétrico em 0.35, no qual a redução de falsos negativos não implicou aumento de falsos positivos.
        </p>
        <p class="nature-text">
            Esse comportamento sugere que a margem ótima do hiperplano não é necessariamente centrada no limiar padrão de 0.50, mas depende da distribuição dos erros clínicos e da geometria de separação do espaço de características.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col_matriz:
        st.markdown('<div style="padding-left: 0.8rem;">', unsafe_allow_html=True)

        fig_final, ax_final = plt.subplots(figsize=(4, 3))
        fig_final.patch.set_facecolor('#ffffff')
        ax_final.set_facecolor('#ffffff')

        cm_final = np.array([[72, 0], [1, 41]])

        sns.heatmap(
            cm_final,
            annot=True,
            fmt='d',
            cmap='Greys',
            cbar=False,
            xticklabels=['Pred: Benigno', 'Pred: Maligno'],
            yticklabels=['Real: Benigno', 'Real: Maligno'],
            annot_kws={"size": 11, "weight": "bold"}
        )

        plt.title("Matriz Final (Threshold 0.35)", color='#2c3e50', fontfamily='serif', weight='bold', fontsize=9)
        ax_final.tick_params(colors='#2c3e50', labelsize=8)

        st.pyplot(fig_final)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: 2.5rem; font-size: 0.95rem; line-height: 1.5; padding: 1.2rem; background-color: #f7f9fa; border-left: 4px solid #2c3e50; color: #222222;">
        <b>Conclusão Definitiva:</b> A redução do limiar de 0.50 para 0.35 reduziu os casos omissos (Falsos Negativos) pela metade — de 2 para apenas 1 — mantendo a taxa de Falsos Positivos em zero. Esses resultados reforçam a interpretação de que modelos baseados em margem, como o SVM, apresentam comportamento sensível à calibração de decisão, conforme estabelecido por Cortes e Vapnik [2].
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color: #e0e0e0; margin-top: 3rem; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size: 0.85rem; color: #666666; line-height: 1.6; font-family: 'Inter', sans-serif;">
        <p style="margin-bottom: 0.4rem;">[1] FAWCETT, T. An introduction to ROC analysis. Pattern Recognition Letters, 2006.</p>
        <p style="margin-bottom: 0.4rem;">[2] CORTES, C.; VAPNIK, V. Support-vector networks. Machine Learning, 1995.</p>
    </div>
    """, unsafe_allow_html=True)