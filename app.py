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

# GRÁFICO 1: MVI - Evolução Temporal
st.markdown("## 📊 1. Mortes Violentas Intencionais (MVI)")
st.markdown("### Queda de 48,5% em 8 anos")

col1, col2 = st.columns(2)

with col1:
    # Gráfico de linha com área
    fig_mvi_linha = go.Figure()
    fig_mvi_linha.add_trace(go.Scatter(
        x=df_filtrado['Ano'],
        y=df_filtrado['MVI_Casos'],
        mode='lines+markers',
        name='Casos de MVI',
        line=dict(color='#d62728', width=4),
        marker=dict(size=12, symbol='circle'),
        fill='tozeroy',
        fillcolor='rgba(214, 39, 40, 0.2)'
    ))
    
    fig_mvi_linha.update_layout(
        title="Evolução dos Casos Absolutos",
        xaxis_title="Ano",
        yaxis_title="Número de Casos",
        height=400,
        template='plotly_white',
        hovermode='x unified'
    )
    st.plotly_chart(fig_mvi_linha, use_container_width=True)

with col2:
    # Gráfico de barras com taxa
    fig_mvi_taxa = go.Figure()
    fig_mvi_taxa.add_trace(go.Bar(
        x=df_filtrado['Ano'],
        y=df_filtrado['Taxa_MVI_100k'],
        marker_color='#d62728',
        text=df_filtrado['Taxa_MVI_100k'].round(1),
        textposition='outside'
    ))
    
    fig_mvi_taxa.update_layout(
        title="Taxa por 100 mil Habitantes",
        xaxis_title="Ano",
        yaxis_title="Taxa por 100k hab.",
        height=400,
        template='plotly_white',
        showlegend=False
    )
    st.plotly_chart(fig_mvi_taxa, use_container_width=True)

st.markdown("---")

# GRÁFICO 2: Homicídios CVLI
if df_filtrado['Homicidios_CVLI_Casos'].notna().any():
    st.markdown("## 🔴 2. Homicídios Dolosos (CVLI)")
    st.markdown("### Redução de 49,6% desde 2020")
    
    df_cvli = df_filtrado[df_filtrado['Homicidios_CVLI_Casos'].notna()].copy()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de área
        fig_cvli = go.Figure()
        fig_cvli.add_trace(go.Scatter(
            x=df_cvli['Ano'],
            y=df_cvli['Homicidios_CVLI_Casos'],
            mode='lines+markers',
            name='Homicídios CVLI',
            line=dict(color='#ff7f0e', width=4),
            marker=dict(size=12),
            fill='tozeroy',
            fillcolor='rgba(255, 127, 14, 0.2)'
        ))
        
        fig_cvli.update_layout(
            title="Evolução dos Casos Absolutos",
            xaxis_title="Ano",
            yaxis_title="Número de Casos",
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig_cvli, use_container_width=True)
    
    with col2:
        # Gráfico de barras com taxa
        fig_cvli_taxa = go.Figure()
        fig_cvli_taxa.add_trace(go.Bar(
            x=df_cvli['Ano'],
            y=df_cvli['Taxa_CVLI_100k'],
            marker_color='#ff7f0e',
            text=df_cvli['Taxa_CVLI_100k'].round(1),
            textposition='outside'
        ))
        
        fig_cvli_taxa.update_layout(
            title="Taxa por 100 mil Habitantes",
            xaxis_title="Ano",
            yaxis_title="Taxa por 100k hab.",
            height=400,
            template='plotly_white',
            showlegend=False
        )
        st.plotly_chart(fig_cvli_taxa, use_container_width=True)
    
    st.markdown("---")

# GRÁFICO 3: Roubo de Veículos - DESTAQUE
if df_filtrado['Roubo_Veiculo_Casos'].notna().any():
    st.markdown("## 🚗 3. Roubo de Veículos")
    st.markdown("### 🎯 Redução Espetacular de 93%")
    
    df_rv = df_filtrado[df_filtrado['Roubo_Veiculo_Casos'].notna()].copy()
    
    # Gráfico grande destacando a queda
    fig_rv = go.Figure()
    
    # Adicionar barras com cores degradê
    cores = ['#2ca02c' if i == 0 else '#90EE90' for i in range(len(df_rv))]
    
    fig_rv.add_trace(go.Bar(
        x=df_rv['Ano'],
        y=df_rv['Roubo_Veiculo_Casos'],
        marker_color=cores,
        text=df_rv['Roubo_Veiculo_Casos'].astype(int),
        textposition='outside',
        textfont=dict(size=14, color='black')
    ))
    
    # Adicionar anotação destacando a queda
    fig_rv.add_annotation(
        x=df_rv['Ano'].iloc[0],
        y=df_rv['Roubo_Veiculo_Casos'].iloc[0],
        text=f"<b>2018: {int(df_rv['Roubo_Veiculo_Casos'].iloc[0]):,} casos</b><br>28 veículos/dia",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#2ca02c",
        ax=-80,
        ay=-80,
        font=dict(size=12, color="#2ca02c")
    )
    
    fig_rv.add_annotation(
        x=df_rv['Ano'].iloc[-1],
        y=df_rv['Roubo_Veiculo_Casos'].iloc[-1],
        text=f"<b>2024: {int(df_rv['Roubo_Veiculo_Casos'].iloc[-1]):,} casos</b><br>2 veículos/dia",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#2ca02c",
        ax=80,
        ay=-80,
        font=dict(size=12, color="#2ca02c")
    )
    
    fig_rv.update_layout(
        title="Evolução do Roubo de Veículos: De 28 para 2 veículos roubados por dia",
        xaxis_title="Ano",
        yaxis_title="Número de Casos",
        height=500,
        template='plotly_white',
        showlegend=False
    )
    
    st.plotly_chart(fig_rv, use_container_width=True)
    
    st.markdown("---")

# GRÁFICO 4: Latrocínio - ALERTA
if df_filtrado['Latrocinio_Casos'].notna().any():
    st.markdown("## ⚠️ 4. Latrocínio (Roubo seguido de Morte)")
    st.markdown("### Único indicador com aumento em 2024")
    
    df_lat = df_filtrado[df_filtrado['Latrocinio_Casos'].notna()].copy()
    
    # Criar cores: verde para queda, vermelho para aumento
    cores_lat = []
    for i in range(len(df_lat)):
        if i == 0:
            cores_lat.append('#2ca02c')
        else:
            if df_lat['Latrocinio_Casos'].iloc[i] < df_lat['Latrocinio_Casos'].iloc[i-1]:
                cores_lat.append('#2ca02c')  # Verde para queda
            else:
                cores_lat.append('#d62728')  # Vermelho para aumento
    
    fig_lat = go.Figure()
    fig_lat.add_trace(go.Bar(
        x=df_lat['Ano'],
        y=df_lat['Latrocinio_Casos'],
        marker_color=cores_lat,
        text=df_lat['Latrocinio_Casos'].astype(int),
        textposition='outside',
        textfont=dict(size=14)
    ))
    
    # Destacar o aumento em 2024
    fig_lat.add_annotation(
        x=df_lat['Ano'].iloc[-1],
        y=df_lat['Latrocinio_Casos'].iloc[-1],
        text="<b>⚠️ Aumento de 21,4%</b><br>Requer atenção!",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#d62728",
        ax=60,
        ay=-60,
        font=dict(size=12, color="#d62728")
    )
    
    fig_lat.update_layout(
        title="Evolução do Latrocínio: Tendência de queda interrompida em 2024",
        xaxis_title="Ano",
        yaxis_title="Número de Casos",
        height=450,
        template='plotly_white',
        showlegend=False
    )
    
    st.plotly_chart(fig_lat, use_container_width=True)
    
    st.markdown("---")

# GRÁFICO 5: Comparação Geral - Redução Percentual
st.markdown("## 📉 5. Visão Geral: Redução da Criminalidade")

# Calcular reduções totais
reducao_mvi = ((df_filtrado['MVI_Casos'].iloc[-1] - df_filtrado['MVI_Casos'].iloc[0]) / df_filtrado['MVI_Casos'].iloc[0]) * 100

reducoes = {
    'Indicador': [],
    'Redução (%)': [],
    'Cor': []
}

reducoes['Indicador'].append('MVI')
reducoes['Redução (%)'].append(reducao_mvi)
reducoes['Cor'].append('#d62728')

if df_filtrado['Homicidios_CVLI_Casos'].notna().any():
    df_cvli_temp = df_filtrado[df_filtrado['Homicidios_CVLI_Casos'].notna()]
    reducao_cvli = ((df_cvli_temp['Homicidios_CVLI_Casos'].iloc[-1] - df_cvli_temp['Homicidios_CVLI_Casos'].iloc[0]) / df_cvli_temp['Homicidios_CVLI_Casos'].iloc[0]) * 100
    reducoes['Indicador'].append('Homicídios CVLI')
    reducoes['Redução (%)'].append(reducao_cvli)
    reducoes['Cor'].append('#ff7f0e')

if df_filtrado['Roubo_Veiculo_Casos'].notna().any():
    df_rv_temp = df_filtrado[df_filtrado['Roubo_Veiculo_Casos'].notna()]
    reducao_rv = ((df_rv_temp['Roubo_Veiculo_Casos'].iloc[-1] - df_rv_temp['Roubo_Veiculo_Casos'].iloc[0]) / df_rv_temp['Roubo_Veiculo_Casos'].iloc[0]) * 100
    reducoes['Indicador'].append('Roubo de Veículos')
    reducoes['Redução (%)'].append(reducao_rv)
    reducoes['Cor'].append('#2ca02c')

if df_filtrado['Latrocinio_Casos'].notna().any():
    df_lat_temp = df_filtrado[df_filtrado['Latrocinio_Casos'].notna()]
    reducao_lat = ((df_lat_temp['Latrocinio_Casos'].iloc[-1] - df_lat_temp['Latrocinio_Casos'].iloc[0]) / df_lat_temp['Latrocinio_Casos'].iloc[0]) * 100
    reducoes['Indicador'].append('Latrocínio')
    reducoes['Redução (%)'].append(reducao_lat)
    # Cor vermelha se aumentou, verde se diminuiu
    reducoes['Cor'].append('#d62728' if reducao_lat > 0 else '#2ca02c')

df_reducoes = pd.DataFrame(reducoes)

fig_reducoes = go.Figure()
fig_reducoes.add_trace(go.Bar(
    y=df_reducoes['Indicador'],
    x=df_reducoes['Redução (%)'],
    orientation='h',
    marker_color=df_reducoes['Cor'],
    text=df_reducoes['Redução (%)'].round(1).astype(str) + '%',
    textposition='outside',
    textfont=dict(size=14, color='black')
))

fig_reducoes.add_vline(x=0, line_dash="dash", line_color="gray", line_width=2)

fig_reducoes.update_layout(
    title=f"Variação Percentual dos Indicadores ({ano_inicio}-{ano_fim})",
    xaxis_title="Variação Percentual (%)",
    yaxis_title="",
    height=400,
    template='plotly_white',
    showlegend=False
)

st.plotly_chart(fig_reducoes, use_container_width=True)

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
    
    #### 2. Homicídios Dolosos/CVLI
    - **Fonte:** SSP-GO via Instituto Mauro Borges (IMB)
    - **Cobertura:** 2020-2024
    
    #### 3. Latrocínio
    - **Fonte:** SSP-GO via IMB
    - **Cobertura:** 2021-2024
    
    #### 4. Roubo de Veículos
    - **Fonte:** SSP-GO
    - **Cobertura:** 2018, 2021-2024
    
    ### Notas Metodológicas
    
    - **Taxas:** Calculadas por 100 mil habitantes usando população estimada do IBGE
    - **MVI vs CVLI:** MVI inclui mortes por intervenção policial, CVLI não inclui
    - **Censo 2022:** Ajuste populacional pode afetar comparações entre 2022-2023
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
