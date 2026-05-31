import streamlit as st

def render():

    st.markdown('<div class="nature-h1">Trabalhos Futuros</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        Os próximos passos desta linha de pesquisa envolvem a expansão da análise para bases de dados multicêntricas, com maior variabilidade populacional, visando avaliar a generalização dos modelos em cenários clínicos reais.
    </p>

    <p class="nature-text">
        Adicionalmente, pretende-se investigar arquiteturas híbridas que combinem modelos de margem (como SVM) com redes neurais profundas, explorando mecanismos de fusão que preservem interpretabilidade clínica sem sacrificar desempenho preditivo.
    </p>

    <p class="nature-text">
        Outro ponto relevante consiste na incorporação de técnicas de calibração probabilística mais avançadas, como Platt Scaling e isotonic regression, além da análise de custo assimétrico diretamente na função de perda.
    </p>

    <p class="nature-text">
        Por fim, futuros estudos devem considerar a integração desses modelos em sistemas de apoio à decisão clínica em tempo real, com validação prospectiva em ambiente hospitalar.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        margin-top: 1.2rem;
        font-size: 0.95rem;
        line-height: 1.5;
        padding: 1rem 1.2rem;
        background-color: #f7f9fa;
        border-left: 4px solid #2c3e50;
        color: #222222;
    ">
        <b>Direção Futura:</b> A evolução natural deste trabalho aponta para sistemas híbridos interpretáveis, calibrados por custo clínico assimétrico e validados em ambientes reais de tomada de decisão médica.
    </div>
    """, unsafe_allow_html=True)