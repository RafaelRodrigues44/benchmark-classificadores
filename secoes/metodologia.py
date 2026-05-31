import streamlit as st

def render():
    st.markdown('<div class="nature-h1">2. Metodologia e Pipeline de Dados</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="nature-h2">2.1. Natureza da Base de Dados</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="nature-text">
        O repositório de dados utilizado para o treinamento e validação dos modelos é o <i>Breast Cancer Wisconsin (Diagnostic) Data Set</i>, extraído do repositório de Aprendizado de Máquina da UCI e publicamente disponibilizado através da plataforma Kaggle [1]. O conjunto é composto por 569 instâncias (pacientes), das quais 357 são diagnosticadas como benignas (B) e 212 como malignas (M).
    </p>
    <p class="nature-text">
        Os preditores consistem em 30 variáveis contínuas (tipo numérico float64) derivadas da digitalização de imagens de Punção Aspirativa por Agulha Fina (PAAF) de massas mamárias. O algoritmo de extração de características calcula dez características reais do núcleo celular presente na imagem: raio, textura, perímetro, área, suavidade, compacidade, concavidade, pontos côncavos, simetria e dimensão fractal. Para cada característica, a base registra a média (mean), o erro padrão (se) e o pior valor (worst - a média dos três maiores valores). Além dos preditores, a base possui uma coluna de identificação (id) descartada por não possuir variância preditiva, e a variável alvo (diagnosis).
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nature-h2">2.2. Pré-processamento e Validação Estocástica</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="nature-text">
        <p>
            A preparação do plano de dados seguiu um fluxo linear focado na estabilização matemática dos atributos, estruturado através das seguintes implementações técnicas:
        </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nature-text-list">  
                     
    * **LabelEncoder (extraído do módulo preprocessing da biblioteca scikit-learn):** Classe utilitária projetada para converter rótulos categóricos textuais em representações numéricas discretas. No ecossistema deste projeto, mapeou os diagnósticos qualitativos da base eliminando strings, definindo a classe maligna como 1 (positivo) e a classe benigna como 0 (negativo).
    
    * **StandardScaler (extraído do módulo preprocessing da biblioteca scikit-learn):** Algoritmo de escala que aplica a padronização z-score aos atributos. Ele calcula a média e a variância de cada coluna de forma isolada, transformando os dados para que passem a apresentar média zero e desvio padrão unitário. Esta operação neutralizou a dominância artificial de variáveis de grande magnitude (como a área do tumor) sobre indicadores decimais (como a dimensão fractal), viabilizando o cálculo correto de distâncias geométricas e hiperplanos nos algoritmos subsequentes.
    
    * **train_test_split (extraído do módulo model_selection da biblioteca scikit-learn):** Função de amostragem que realiza a divisão aleatória do conjunto de dados em frações distintas de treino e teste. Configurada com o parâmetro de estratificação ativo, ela garantiu a manutenção da proporção exata entre tecidos saudáveis e tumorais em ambos os subconjuntos. O processo isolou 80% das amostras para ajuste de parâmetros e reteve 20% (114 pacientes: 72 benignos e 42 malignos) para atestar a capacidade de generalização em ambiente controlado de teste.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nature-h2">2.3. Fase 1: Treinamento de Modelos Especialistas (Single Experts)</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="nature-text">
        A primeira fase metodológica consistiu na otimização paramétrica de seis arquiteturas algorítmicas distintas, processadas de forma isolada sobre a mesma base de dados. O refinamento de cada motor matemático utilizou os seguintes componentes estruturais:
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nature-text-list">
                 
    * **GridSearchCV (extraído do módulo model_selection da biblioteca scikit-learn):** Ferramenta de otimização combinatória que realiza uma busca exaustiva sobre uma grade de hiperparâmetros predefinida. Ela avalia automaticamente todas as combinações possíveis de parâmetros para um algoritmo, selecionando a configuração que maximiza a métrica estatística de interesse.

    * **StratifiedKFold (extraído do módulo model_selection da biblioteca scikit-learn):** Gerador de validação cruzada que divide os dados de treinamento em K partes (dobras) de tamanhos iguais, garantindo que cada dobra seja representativa da distribuição original das classes. Utilizado aqui com 5 dobras acoplado ao GridSearchCV, ele blindou o processo contra o sobreajuste (overfitting), validando a estabilidade de cada modelo candidato em subconjuntos rotativos antes da homologação final.
    
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nature-text">
    <p class="nature-text">
        Sob este arranjo, foram ajustados o k-Nearest Neighbors (KNeighborsClassifier), o Naïve Bayes (GaussianNB), a Árvore de Decisão (DecisionTreeClassifier), a floresta aleatória (RandomForestClassifier), o Perceptron Multicamadas (MLPClassifier) e o classificador por vetores de suporte (SVC), configurado com suporte à probabilidade ativo para permitir análises posteriores de limiares clínicos.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nature-h2">2.4. Fase 2: Estruturação do Comitê Global (Ensemble)</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="nature-text">
        Após o congelamento das melhores parametrizações individuais de cada estimador, a segunda fase consistiu na consolidação dessas respostas em uma arquitetura combinatória unificada, utilizando o seguinte componente de agregação:
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nature-text-list">
                
    * **VotingClassifier (extraído do módulo ensemble da biblioteca scikit-learn):** Meta-classificador projetado para combinar as predições de um ecossistema de algoritmos base através de regras de votação compartilhada. Configurado no modo soft, ele instrui o sistema a calcular a média ponderada ou aritmética das probabilidades contínuas atribuídas a cada classe por todos os modelos integrantes, aplicando o ponto de corte binário sobre o vetor resultante para obter o veredito final. Na Fase 2, todos os seis membros atuaram com pesos rigorosamente idênticos.
                
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nature-h2">2.5. Fase 3: Refinamento e Ponderação Paramétrica</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="nature-text">
        A terceira e última fase metodológica aplicou uma estratégia de filtragem adaptativa para conter os efeitos da contaminação estatística observada na etapa anterior. O <b>VotingClassifier</b> foi reconstruído introduzindo o vetor de hiperparâmetro weights, aplicando multiplicadores lineares assimétricos baseados no desempenho isolado medido na Fase 1. Os algoritmos de maior poder preditivo e estabilidade de margem (como o SVM e a Random Forest) receberam pesos elevados, enquanto os algoritmos de alta variância ou vieses probabilísticos acentuados foram rebaixados a papéis secundários de desempate periférico, blindando a fronteira de decisão coletiva.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="nature-insight"><b>Nota de Metodologia Computacional:</b> Todo o pipeline estrutural foi desenvolvido utilizando a linguagem Python, apoiando-se na biblioteca pandas para a manipulação tabular inicial da base de dados e na suíte scikit-learn para a orquestração e execução de todos os métodos de aprendizado estatístico e validação cruzada.</div>', unsafe_allow_html=True)

    st.markdown("""
    <p class="nature-text" style="font-size: 0.85rem; color: #777777; margin-top: 2rem;">
        [1] KAGGLE. Breast Cancer Dataset. Disponível na plataforma digital open-source: https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset. Base original contendo os 30 atributos dimensionais do estudo de Wisconsin.
    </p>
    """, unsafe_allow_html=True)