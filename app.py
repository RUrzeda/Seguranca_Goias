import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Segurança Pública - Goiás",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .insight-box {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2ca02c;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff7f0e;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Carregar dados
@st.cache_data
def load_data():
    df = pd.read_csv('dados.csv')
    return df

df = load_data()

# Header
st.markdown('<div class="main-header">🛡️ Dashboard de Segurança Pública de Goiás</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Análise de Indicadores Criminais (2017-2024)</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Configurações")
st.sidebar.markdown("---")

# Filtro de período
anos_disponiveis = df['Ano'].tolist()
ano_inicio, ano_fim = st.sidebar.select_slider(
    "Selecione o período de análise:",
    options=anos_disponiveis,
    value=(anos_disponiveis[0], anos_disponiveis[-1])
)

# Filtrar dados
df_filtrado = df[(df['Ano'] >= ano_inicio) & (df['Ano'] <= ano_fim)]

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Indicadores Disponíveis")
indicadores = st.sidebar.multiselect(
    "Selecione os indicadores:",
    ['MVI', 'Homicídios CVLI', 'Latrocínio', 'Roubo de Veículos'],
    default=['MVI', 'Homicídios CVLI', 'Roubo de Veículos']
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Sobre")
st.sidebar.info("""
**Dashboard desenvolvido com dados oficiais:**
- Anuário Brasileiro de Segurança Pública (FBSP)
- Secretaria de Segurança Pública de Goiás (SSP-GO)
- Instituto Mauro Borges (IMB)
- IBGE
""")

# Métricas principais
st.markdown("## 📈 Indicadores Principais")

col1, col2, col3, col4 = st.columns(4)

with col1:
    mvi_atual = df_filtrado['MVI_Casos'].iloc[-1]
    mvi_anterior = df_filtrado['MVI_Casos'].iloc[0]
    variacao_mvi = ((mvi_atual - mvi_anterior) / mvi_anterior) * 100
    st.metric(
        "MVI (2024)",
        f"{int(mvi_atual):,}",
        f"{variacao_mvi:.1f}% desde {ano_inicio}",
        delta_color="inverse"
    )

with col2:
    if df_filtrado['Homicidios_CVLI_Casos'].notna().any():
        cvli_atual = df_filtrado['Homicidios_CVLI_Casos'].dropna().iloc[-1]
        cvli_anterior = df_filtrado['Homicidios_CVLI_Casos'].dropna().iloc[0]
        variacao_cvli = ((cvli_atual - cvli_anterior) / cvli_anterior) * 100
        st.metric(
            "Homicídios CVLI (2024)",
            f"{int(cvli_atual):,}",
            f"{variacao_cvli:.1f}%",
            delta_color="inverse"
        )
    else:
        st.metric("Homicídios CVLI", "N/D", "Dados não disponíveis")

with col3:
    if df_filtrado['Latrocinio_Casos'].notna().any():
        lat_atual = df_filtrado['Latrocinio_Casos'].dropna().iloc[-1]
        lat_anterior = df_filtrado['Latrocinio_Casos'].dropna().iloc[0]
        variacao_lat = ((lat_atual - lat_anterior) / lat_anterior) * 100
        st.metric(
            "Latrocínio (2024)",
            f"{int(lat_atual):,}",
            f"{variacao_lat:.1f}%",
            delta_color="inverse"
        )
    else:
        st.metric("Latrocínio", "N/D", "Dados não disponíveis")

with col4:
    if df_filtrado['Roubo_Veiculo_Casos'].notna().any():
        rv_atual = df_filtrado['Roubo_Veiculo_Casos'].dropna().iloc[-1]
        rv_anterior = df_filtrado['Roubo_Veiculo_Casos'].dropna().iloc[0]
        variacao_rv = ((rv_atual - rv_anterior) / rv_anterior) * 100
        st.metric(
            "Roubo de Veículos (2024)",
            f"{int(rv_atual):,}",
            f"{variacao_rv:.1f}%",
            delta_color="inverse"
        )
    else:
        st.metric("Roubo de Veículos", "N/D", "Dados não disponíveis")

st.markdown("---")

# Insights principais
st.markdown("## 💡 Principais Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="insight-box">
        <h3>✅ Declínio Estrutural da Violência Letal</h3>
        <p>As <strong>Mortes Violentas Intencionais (MVI)</strong> caíram de <strong>2.676 casos em 2017</strong> 
        para <strong>1.379 em 2024</strong>, representando uma <strong>redução de 48,5%</strong>.</p>
        <p>A <strong>taxa por 100 mil habitantes</strong> despencou de <strong>39,32</strong> para <strong>18,76</strong>, 
        posicionando Goiás com a <strong>9ª menor taxa estadual do Brasil</strong> em 2024.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="insight-box">
        <h3>✅ Eficácia no Combate ao Crime Patrimonial</h3>
        <p>O <strong>Roubo de Veículos</strong> teve queda espetacular de <strong>93%</strong> entre 2018 e 2024, 
        passando de <strong>10.104 casos</strong> para apenas <strong>756 casos</strong>.</p>
        <p>A média diária caiu de <strong>28 veículos roubados</strong> em 2018 para apenas 
        <strong>2 veículos por dia</strong> em 2024.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="warning-box">
    <h3>⚠️ Anomalia do Latrocínio</h3>
    <p>Apesar da queda generalizada, o <strong>Latrocínio</strong> apresentou <strong>aumento de 21,4%</strong> 
    entre 2023 (14 casos) e 2024 (17 casos), indicando possível aumento da letalidade nos roubos remanescentes.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Gráficos
st.markdown("## 📊 Análise Temporal dos Indicadores")

# Gráfico 1: Evolução das Taxas por 100 mil habitantes
st.markdown("### Evolução das Taxas por 100 mil Habitantes")

fig1 = go.Figure()

if 'MVI' in indicadores:
    fig1.add_trace(go.Scatter(
        x=df_filtrado['Ano'],
        y=df_filtrado['Taxa_MVI_100k'],
        mode='lines+markers',
        name='Taxa MVI',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))

if 'Homicídios CVLI' in indicadores and df_filtrado['Taxa_CVLI_100k'].notna().any():
    fig1.add_trace(go.Scatter(
        x=df_filtrado['Ano'],
        y=df_filtrado['Taxa_CVLI_100k'],
        mode='lines+markers',
        name='Taxa Homicídios CVLI',
        line=dict(color='#ff7f0e', width=3),
        marker=dict(size=8)
    ))

if 'Latrocínio' in indicadores and df_filtrado['Taxa_Latrocinio_100k'].notna().any():
    fig1.add_trace(go.Scatter(
        x=df_filtrado['Ano'],
        y=df_filtrado['Taxa_Latrocinio_100k'],
        mode='lines+markers',
        name='Taxa Latrocínio',
        line=dict(color='#d62728', width=3),
        marker=dict(size=8)
    ))

if 'Roubo de Veículos' in indicadores and df_filtrado['Taxa_Roubo_Veiculo_100k'].notna().any():
    fig1.add_trace(go.Scatter(
        x=df_filtrado['Ano'],
        y=df_filtrado['Taxa_Roubo_Veiculo_100k'],
        mode='lines+markers',
        name='Taxa Roubo de Veículos',
        line=dict(color='#2ca02c', width=3),
        marker=dict(size=8)
    ))

fig1.update_layout(
    xaxis_title="Ano",
    yaxis_title="Taxa por 100 mil habitantes",
    hovermode='x unified',
    height=500,
    template='plotly_white',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Números Absolutos
st.markdown("### Evolução dos Números Absolutos de Casos")

fig2 = go.Figure()

if 'MVI' in indicadores:
    fig2.add_trace(go.Bar(
        x=df_filtrado['Ano'],
        y=df_filtrado['MVI_Casos'],
        name='MVI',
        marker_color='#1f77b4'
    ))

if 'Homicídios CVLI' in indicadores and df_filtrado['Homicidios_CVLI_Casos'].notna().any():
    fig2.add_trace(go.Bar(
        x=df_filtrado['Ano'],
        y=df_filtrado['Homicidios_CVLI_Casos'],
        name='Homicídios CVLI',
        marker_color='#ff7f0e'
    ))

if 'Roubo de Veículos' in indicadores and df_filtrado['Roubo_Veiculo_Casos'].notna().any():
    fig2.add_trace(go.Bar(
        x=df_filtrado['Ano'],
        y=df_filtrado['Roubo_Veiculo_Casos'],
        name='Roubo de Veículos',
        marker_color='#2ca02c'
    ))

fig2.update_layout(
    xaxis_title="Ano",
    yaxis_title="Número de Casos",
    hovermode='x unified',
    height=500,
    template='plotly_white',
    barmode='group',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Variação Percentual Anual
st.markdown("### Variação Percentual Anual")

df_variacao = df_filtrado.copy()
df_variacao['Var_MVI'] = df_variacao['MVI_Casos'].pct_change() * 100
df_variacao['Var_CVLI'] = df_variacao['Homicidios_CVLI_Casos'].pct_change() * 100
df_variacao['Var_Latrocinio'] = df_variacao['Latrocinio_Casos'].pct_change() * 100
df_variacao['Var_Roubo_Veiculo'] = df_variacao['Roubo_Veiculo_Casos'].pct_change() * 100

fig3 = go.Figure()

if 'MVI' in indicadores:
    fig3.add_trace(go.Bar(
        x=df_variacao['Ano'],
        y=df_variacao['Var_MVI'],
        name='MVI',
        marker_color='#1f77b4'
    ))

if 'Homicídios CVLI' in indicadores:
    fig3.add_trace(go.Bar(
        x=df_variacao['Ano'],
        y=df_variacao['Var_CVLI'],
        name='Homicídios CVLI',
        marker_color='#ff7f0e'
    ))

if 'Latrocínio' in indicadores:
    fig3.add_trace(go.Bar(
        x=df_variacao['Ano'],
        y=df_variacao['Var_Latrocinio'],
        name='Latrocínio',
        marker_color='#d62728'
    ))

if 'Roubo de Veículos' in indicadores:
    fig3.add_trace(go.Bar(
        x=df_variacao['Ano'],
        y=df_variacao['Var_Roubo_Veiculo'],
        name='Roubo de Veículos',
        marker_color='#2ca02c'
    ))

fig3.add_hline(y=0, line_dash="dash", line_color="gray")

fig3.update_layout(
    xaxis_title="Ano",
    yaxis_title="Variação Percentual (%)",
    hovermode='x unified',
    height=500,
    template='plotly_white',
    barmode='group',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# Tabela de dados
st.markdown("## 📋 Dados Detalhados")

# Preparar dados para exibição
df_display = df_filtrado.copy()
df_display['Populacao_Estimada'] = df_display['Populacao_Estimada'].apply(lambda x: f"{int(x):,}")
df_display = df_display.fillna('N/D')

st.dataframe(df_display, use_container_width=True, hide_index=True)

st.markdown("---")

# Metodologia e Fontes
st.markdown("## 📚 Metodologia e Fontes de Dados")

with st.expander("🔍 Clique para ver detalhes sobre metodologia e fontes"):
    st.markdown("""
    ### Fontes de Dados
    
    #### 1. MVI (Mortes Violentas Intencionais)
    - **Fonte:** Anuário Brasileiro de Segurança Pública 2025 (FBSP)
    - **URL:** [https://forumseguranca.org.br](https://forumseguranca.org.br)
    - **Cobertura:** 2017-2024 (série completa)
    - **Definição:** Inclui Homicídio Doloso, Latrocínio, Lesão Corporal Seguida de Morte e Mortes Decorrentes de Intervenção Policial
    
    #### 2. População Estimada
    - **Fonte:** IBGE (via Anuário FBSP)
    - **Cobertura:** 2017-2024 (série completa)
    - **Referência:** 1º de julho de cada ano
    
    #### 3. Homicídios Dolosos/CVLI
    - **Fonte:** SSP-GO via Instituto Mauro Borges (IMB)
    - **Documento:** "Goiás em Dados 2024"
    - **Cobertura:** 2020-2024
    - **Definição:** Crimes Violentos Letais Intencionais (exclui MDIP)
    
    #### 4. Latrocínio
    - **Fonte:** SSP-GO via IMB
    - **Cobertura:** 2021-2024
    - **Definição:** Roubo seguido de morte
    
    #### 5. Roubo de Veículos
    - **Fonte:** SSP-GO
    - **Cobertura:** 2018, 2021-2024
    
    ### Lacunas Conhecidas
    
    - **Homicídios CVLI:** Dados não disponíveis para 2017-2019
    - **Latrocínio:** Dados não disponíveis para 2017-2020
    - **Roubo de Veículos:** Dados não disponíveis para 2017, 2019-2020
    
    ### Notas Metodológicas
    
    1. **MVI vs CVLI:** MVI inclui mortes por intervenção policial, CVLI não inclui
    2. **Censo 2022:** Ajuste populacional pode afetar comparações entre 2022-2023
    3. **Taxas:** Calculadas por 100 mil habitantes usando população estimada do IBGE
    4. **Investimentos:** R$ 17 bilhões investidos em segurança pública (2019-2024)
    
    ### Contexto das Políticas Públicas
    
    A partir de 2019, o Governo de Goiás implementou uma série de reformas na segurança pública:
    - Integração das forças policiais
    - Aprimoramento dos batalhões
    - Formação de pessoal na área de inteligência
    - Investimento em infraestrutura, armamentos e tecnologia
    - Reajuste salarial para agentes de segurança
    
    Esses investimentos e reformas resultaram em quedas consistentes e significativas em todos os principais indicadores criminais.
    """)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p><strong>Dashboard de Segurança Pública de Goiás</strong></p>
    <p>Desenvolvido com dados oficiais | Última atualização: Outubro 2025</p>
    <p>📊 Dados: FBSP, SSP-GO, IMB, IBGE | 🛠️ Tecnologia: Streamlit + Plotly</p>
</div>
""", unsafe_allow_html=True)
