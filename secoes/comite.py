import streamlit as st

def render():
    st.markdown('<div class="nature-h1">4. Estruturação do Comitê de Arbitragem (Ensemble)</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="nature-h2">4.1. A Justificativa Teórica: A Sabedoria das Multidões</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="nature-text">
        O aprendizado estatístico por comitês (<i>Ensemble Learning</i>) fundamenta-se no clássico Teorema do Júri de Condorcet, originário das ciências políticas. O teorema postula que, se um grupo de eleitores independentes possui uma probabilidade individual de acertar uma decisão ligeiramente superior ao acaso, a probabilidade de o voto majoritário do grupo estar correto aproxima-se de 100% à medida que o grupo cresce [1]. Na ciência de dados oncológica, essa premissa é importada para construir arquiteturas onde a agregação de classificadores diversos (estatísticos, geométricos e lógicos) deve, teoricamente, neutralizar o viés individual de um algoritmo e reduzir a variância global [2]. O objetivo é simples: evitar que a limitação geométrica de um único modelo condene uma paciente a um falso diagnóstico.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="nature-h2">4.2. Como Funciona a Arquitetura Combinatória?</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="nature-text">
        Existem duas modalidades primárias para extrair uma predição unificada de um conjunto diversificado de motores algorítmicos:
    </p>
     """, unsafe_allow_html=True)
                
    st.markdown("""
    <div class="nature-text-list">  
                      
    * **Votação Majoritária (Hard Voting):** O veredito é gerado de forma democrática e bruta. Cada modelo gera uma saída binária (1 para Maligno, 0 para Benigno) e a classe que receber a maioria simples de votos "vence" [3].

    * **Votação Probabilística (Soft Voting):** Trata-se de uma abordagem matemática mais sofisticada e clínica. O sistema coleta a matriz de probabilidade contínua gerada por cada classificador (ex: o SVM tem 98% de certeza que é maligno, enquanto a Árvore de Decisão tem 55%). O algoritmo então calcula a média exata dessas certezas numéricas e só aplica o limiar de decisão após obter o consenso ponderado das confianças [4].

    </div>
    """, unsafe_allow_html=True)
   
    
    st.markdown('<div class="nature-h2">4.3 Construção do Motor: O Ecossistema Python</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="nature-text">
        Para operacionalizar essa validação acadêmica na prática, os seis classificadores individuais (SVM, Random Forest, Redes Neurais MLP, k-NN, Decision Tree e Naive Bayes) foram resgatados do ambiente de treinamento da Fase 1, já devidamente otimizados com seus melhores hiperparâmetros (encontrados via validação cruzada). 
    </p>
    <p class="nature-text">
        O orquestrador escolhido para unificar as opiniões foi o meta-estimador <b>VotingClassifier</b>, fornecido pela suíte <i>scikit-learn</i>. Optou-se estritamente pela modalidade de convergência <b>voting='soft'</b>. A justificativa metodológica para descartar o "hard voting" reside na necessidade médica de calibrar a incerteza: em tecidos de fronteira biológica, a magnitude da convicção de um modelo matemático maduro (como o SVM) não pode ser sumariamente rebaixada ao mesmo peso binário (0 ou 1) do "chute" incerto de um modelo que falhou na suposição de variáveis, como o Naive Bayes.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color: #e0e0e0; margin-top: 3rem; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-size: 0.85rem; color: #777777; line-height: 1.5; font-family: 'Inter', sans-serif;">
        <p style="margin-bottom: 0.4rem;">[1] POLIKAR, R. Ensemble based systems in decision making. <b>IEEE Circuits and Systems Magazine</b>, v. 6, n. 3, p. 21-45, 2006. (Análise sobre o teorema de Condorcet e a fundação preditiva).</p>
        <p style="margin-bottom: 0.4rem;">[2] DIETTERICH, T. G. Ensemble Methods in Machine Learning. <b>Multiple Classifier Systems</b>, LNCS, v. 1814, p. 1-15, 2000. (Fundamentação da redução de variância e viés em agrupamentos).</p>
        <p style="margin-bottom: 0.4rem;">[3] KUNCHEVA, L. I. <b>Combining pattern classifiers: methods and algorithms</b>. John Wiley & Sons, 2014.</p>
        <p style="margin-bottom: 0.4rem;">[4] HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. <b>The Elements of Statistical Learning</b>. Springer, 2009. (Mapeamento matemático entre regras de decisão hard vs soft e inferência contínua).</p>
    </div>
    """, unsafe_allow_html=True)