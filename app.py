import streamlit as st
import base64
from secoes import (
    abstract,
    introducao,
    metodologia,
    classificadores,
    comite,
    rodada1,
    rodada2,
    otimizacao,
    conclusao,
    trabalhos_futuros
)

def get_image_base64(path):
    with open(path, "rb") as image_file:
        return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode()}"

foto_base64 = get_image_base64("assets/foto.jpeg")

st.set_page_config(
    page_title="Benchmarking modelos de classificação",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("styles/main.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

secoes_map = {
    "Resumo": "Resumo",
    "1. Introdução": "Introdução",
    "2. Metodologia": "Metodologia",
    "3. Classificadores Isolados": "Classificadores Isolados",
    "4. Estruturação do Comitê": "Estruturação do Comitê",
    "5. Comitê - Análise da Rodada 1 (Cega)": "Rodada 1 (Cega)",
    "6. O Avanço da Rodada 2 (Pesos)": "Rodada 2 (Pesos)",
    "7. Otimização de Threshold (SVM Campeão)": "Otimização de Threshold",
    "8. Conclusão": "Conclusão",
    "9. Trabalhos Futuros": "Trabalhos Futuros",
    "10. Materiais Suplementares": "Materiais Suplementares"
}

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-header">
            <span class="sidebar-icon">🔬</span>
            <span class="sidebar-text">BENCHMARKING - MODELOS DE CLASSIFICAÇÃO</span>
        </div>
        <hr class="sidebar-divider">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="profile-container">
            <img src="{foto_base64}" class="profile-photo">
            <div class="profile-info">
                <div class="profile-name">Rafael Rodrigues</div>
                <div class="profile-role">Engenheiro de Software</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    secao = st.radio(
        "Navegação",
        options=list(secoes_map.keys()),
        format_func=lambda x: secoes_map[x]
    )

st.markdown(
    """
    <p class="nature-title-pt">
    Avaliação Comparativa de Modelos de Classificação e Estratégias de Ensemble para o Diagnóstico de Câncer de Mama
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="nature-title-en">
    Comparative Evaluation of Classification Models and Ensemble Strategies for Breast Cancer Diagnosis
    </p>
    """,
    unsafe_allow_html=True
)

if secao == "Resumo":
    abstract.render()

elif secao == "1. Introdução":
    introducao.render()

elif secao == "2. Metodologia":
    metodologia.render()

elif secao == "3. Classificadores Isolados":
    classificadores.render()

elif secao == "4. Estruturação do Comitê":
    comite.render()

elif secao == "5. Comitê - Análise da Rodada 1 (Cega)":
    rodada1.render()

elif secao == "6. O Avanço da Rodada 2 (Pesos)":
    rodada2.render()

elif secao == "7. Otimização de Threshold (SVM Campeão)":
    otimizacao.render()

elif secao == "8. Conclusão":
    conclusao.render()

elif secao == "9. Trabalhos Futuros":
    trabalhos_futuros.render()

elif secao == "10. Materiais Suplementares":

    st.markdown('<div class="nature-h1">Materiais Suplementares</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <p class="nature-text">
        Os notebooks abaixo contêm os experimentos completos, análises estatísticas,
        treinamento dos modelos e procedimentos de otimização utilizados nesta pesquisa.
        </p>
        """,
        unsafe_allow_html=True
    )

    notebooks = {
        "Notebook 01 — Modelo KNN": "assets/notebooks/01_knn_gov.ipynb",
        "Notebook 02 — Modelo Naive Bayes": "assets/notebooks/02_naive_bayes.ipynb",
        "Notebook 03 — Modelo Árvore de Decisão": "assets/notebooks/03_tree.ipynb",
        "Notebook 04 — Modelo Random Forest": "assets/notebooks/04_random_forest.ipynb",
        "Notebook 05 — Modelo Rede Neural": "assets/notebooks/05_redes_neurais.ipynb",
        "Notebook 06 — Modelo SVM": "assets/notebooks/06_svm.ipynb",
        "Notebook 07 — Análise do Comitê": "assets/notebooks/07_comite_analise.ipynb",
    }

    for nome, caminho in notebooks.items():
        with open(caminho, "rb") as file:
            st.download_button(
                label=f"📎 {nome}",
                data=file,
                file_name=caminho.split("/")[-1],
                mime="application/x-ipynb+json",
                use_container_width=True
            )

    st.markdown(
        """
        <p class="nature-h1">Base de Dados</p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="nature-text">
        Os experimentos desta pesquisa utilizaram a base
        Breast Cancer Wisconsin Diagnostic Dataset.
        </p>
        """,
        unsafe_allow_html=True
    )

    with open("assets/datasets/breast-cancer.csv", "rb") as file:
        st.download_button(
            label="📄 Download — breast-cancer.csv",
            data=file,
            file_name="breast-cancer.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.markdown(
        """
        <div style="margin-top: .7rem;">
            <a href="https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data"
               target="_blank"
               style="
                    text-decoration:none;
                    color:#7a7a7a;
                    font-size:.88rem;
                    font-weight:500;
               ">
               🔗 Fonte Oficial do Dataset — Kaggle
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="footer-container">
        <p>Manuscrito de Pesquisa Independente • Rafael Rodrigues • 2026</p>
        <p>rafael.rodrigues85@hotmail.com</p>
    </div>
    """,
    unsafe_allow_html=True
)