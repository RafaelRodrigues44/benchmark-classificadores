import streamlit as st

def render():

    st.markdown('<div class="nature-h1">Conclusão</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text">
        Este estudo analisou o desempenho de modelos clássicos de aprendizado de máquina aplicados ao diagnóstico do câncer de mama, com ênfase na comparação entre abordagens individuais e estratégias de ensemble. Os resultados indicam que a superioridade teórica de comitês de modelos não se traduz automaticamente em desempenho clínico superior, especialmente quando há ausência de calibração adequada entre os estimadores.
    </p>

    <p class="nature-text">
        O Support Vector Machine demonstrou consistência superior em relação aos demais classificadores avaliados, apresentando não apenas elevada acurácia global, mas também estabilidade na fronteira de decisão. A análise de sensibilidade ao limiar de decisão revelou que pequenas variações no threshold produzem impactos significativos na taxa de falsos negativos, o que é crítico em contextos médicos de alto risco.
    </p>

    <p class="nature-text">
        A investigação também evidenciou que arquiteturas de votação simples tendem a introduzir ruído estatístico quando combinam modelos com diferentes regimes de viés e variância, levando à degradação de sinais discriminativos fortes. Nesse sentido, a ideia de “inteligência coletiva” em aprendizado supervisionado deve ser reinterpretada como um problema de calibração estrutural e não apenas de agregação.
    </p>

    <p class="nature-text">
        Por fim, os resultados reforçam que a performance em tarefas clínicas não deve ser avaliada apenas por métricas agregadas, mas pela análise explícita de erros assimétricos, especialmente falsos negativos. A otimização do limiar de decisão mostrou-se uma estratégia simples, porém altamente efetiva para aumentar a segurança diagnóstica sem necessidade de reestruturação do modelo base.
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
        <b>Síntese Final:</b> Em problemas biomédicos de alta criticidade, modelos de margem máxima aliados à calibração de decisão demonstram desempenho mais confiável do que ensembles não regulados, sobretudo quando o custo de erro é assimétrico.
    </div>
    """, unsafe_allow_html=True)