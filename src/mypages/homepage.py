import streamlit as st


def page():
    st.markdown(
        """
        <main class="home_container">
                <h1>Análise de Chamados abertos no 1746 </h1>
                <p> Este é um projeto de análise de dados do 1746, o canal de comunicação da Prefeitura do Rio de Janeiro.
                    Aqui, você pode visualizar informações como a quantidade de chamados abertos em um dia, os tipos de
                    chamados mais comuns, e a quantidade de chamados por região.
                </p>
                <h2>Conjunto de Dados </h2>
                <p> Os dados utilizados nesse projeto são: </p>
                <ul>
                    <li> Chamados do 1746: Dados relacionados a chamados de serviços públicos na cidade do Rio de Janeiro. </li>
                    <li> Bairros do Rio de Janeiro: Dados sobre os bairros da cidade do Rio de Janeiro - RJ. </li>
                    <li> Ocupação Hoteleira em Grandes Eventos no Rio: Dados contendo o período de duração de alguns grandes eventos que ocorreram no Rio de Janeiro em 2022 e 2023 e a taxa de ocupação hoteleira da cidade nesses períodos. </li>
                </ul>
                <h2>Estrutura da Página </h2>
                <p> Na barra lateral ao lado, é possível navegar entre as páginas do projeto. As páginas disponíveis são: </p>
                <ul>
                    <li> Página Inicial: Apresentação do projeto e dos dados utilizados. </li>
                    <li> Chamados em um dia: Análise dos chamados abertos no 1746 para um dia específico. </li>
                    <li> Chamados por subtipo: Análise dos chamados por subtipo, por exemplo, perturbação do sossego, reparo de luminária, etc. </li>
                </ul>
        </main>
    """,  # noqa
        unsafe_allow_html=True,
    )
