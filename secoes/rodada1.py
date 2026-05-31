import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def render():
    st.markdown('<div class="nature-h1">5. Análise da Primeira Rodada do Comitê: O Efeito da Diluição de Sinal</div>', unsafe_allow_html=True)

    col_text, col_img = st.columns([1.2, 1])

    with col_text:
        st.markdown("""
        <p class="nature-text">
            Com a arquitetura do <i>VotingClassifier</i> estruturada, foi injetado o subconjunto de testes estratificado (114 instâncias cegas) para avaliar o poder diagnóstico do comitê. Nesta primeira rodada analítica, os seis modelos especialistas receberam <b>pesos estritamente igualitários</b>. Isso configurou uma simulação de junta médica descentralizada onde a opinião de todos os seis computadores possui o exato mesmo impacto matemático na decisão clínica final.
        </p>
        <p class="nature-text">
            O diagnóstico da matriz de confusão revelou um comportamento severamente predatório conhecido na literatura como <b>diluição estatística de sinal</b> [1]. Ao forçar o sistema a ouvir todos os modelos, a qualidade final foi ancorada pelos componentes mais fracos. A interferência ruidosa e ortogonal gerada por estimadores de baixa especificidade (Árvore de Decisão e Naive Bayes) neutralizou o mapeamento perfeito dos hiperplanos de suporte (SVM).
        </p>
        """, unsafe_allow_html=True)

    with col_img:
        fig, ax = plt.subplots(figsize=(4.5, 3.5))
        fig.patch.set_facecolor('#ffffff')
        ax.set_facecolor('#ffffff')

        cm_comite = np.array([[71, 1], [3, 39]])

        grafite_cmap = sns.light_palette("#3b4a5a", as_cmap=True)
        sns.heatmap(
            cm_comite,
            annot=True,
            fmt='d',
            cmap=grafite_cmap,
            cbar=False,
            xticklabels=['Benigno', 'Maligno'],
            yticklabels=['Benigno', 'Maligno'],
            annot_kws={"size": 14, "weight": "bold"}
        )

        plt.title("Matriz de Confusão - Comitê Cego (Pesos Iguais)", fontsize=10, fontfamily='serif', color='#2c3e50', weight='bold')
        plt.ylabel('Realidade', fontsize=8, color='#2c3e50')
        plt.xlabel('Predição Coletiva', fontsize=8, color='#2c3e50')
        ax.tick_params(colors='#2c3e50')

        st.pyplot(fig)

    st.markdown('<div class="nature-insight" style="font-size: 0.95rem; line-height: 1.5; padding: 1.2rem; background-color: #f7f9fa; border-left: 4px solid #881111; margin-top: 0.8rem;"><b>Impacto Clínico Registrado:</b> A acurácia global regrediu para 96,49%. Contrastando com a perfeição isolada do SVM (que havia alcançado zero alarmes falsos e apenas 2 omissões), a topologia coletiva igualitária cedeu na zona de intersecção biológica: registrou 1 Falso Positivo e permitiu que 3 tumores malignos agressivos passassem despercebidos. O conjunto sacrificou a segurança oncológica em prol do consenso.</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text" style="margin-top: 1.5rem;">
        Do ponto de vista da teoria de aprendizado estatístico, este resultado é uma manifestação clássica da fragilidade de ensembles sob votação não-ponderada. Quando integramos um classificador robusto, como o SVM, com estimadores que exibem vieses indutivos distintos (como a Naive Bayes, que ignora a correlação entre as dimensões), o "consenso" não representa a verdade estatística, mas sim uma média forçada que puxa os modelos de alta performance para baixo. A literatura técnica denomina este comportamento como a falácia da agregação sem diversidade curada [1, 2].
    </p>
    <p class="nature-text">
        Este experimento elucida um paradigma crítico na engenharia de sistemas de suporte à decisão: a inteligência coletiva não é inerentemente superior à inteligência especializada em domínios de alta criticidade. Para aplicações médicas, onde a penalidade de um erro é assimétrica (um Falso Negativo custando uma vida, ao contrário de um Falso Positivo), a robustez do sistema não deve ser medida pela popularidade da decisão entre os algoritmos, mas pela capacidade de preservação do hiperplano de separação mais conservador e preciso. A partir desta falha da primeira rodada, torna-se evidente a necessidade de uma arquitetura baseada em pesos, onde a confiança do sistema é distribuída proporcionalmente ao desempenho histórico de cada especialista.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color: #e0e0e0; margin-top: 3rem; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size: 0.85rem; color: #777777; line-height: 1.5; font-family: 'Inter', sans-serif;">
        <p style="margin-bottom: 0.4rem;">[1] KUNCHEVA, L. I. <b>Combining pattern classifiers: methods and algorithms</b>. John Wiley & Sons, 2014. (Documentação da diluição de especialistas finos quando agregados a modelos fracos descalibrados).</p>
        <p style="margin-bottom: 0.4rem;">[2] HAND, D. J. Classifier technology and the illusion of progress. <b>Statistical Science</b>, v. 21, n. 1, p. 1-14, 2006. (Análise crítica entre a sofisticação teórica e o desempenho de generalização prática empírica).</p>
    </div>
    """, unsafe_allow_html=True)