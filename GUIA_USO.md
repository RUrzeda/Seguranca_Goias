# 🚀 Guia Rápido de Uso - Dashboard de Segurança Pública de Goiás

## 📋 Índice
1. [Instalação](#instalação)
2. [Executando o Dashboard](#executando-o-dashboard)
3. [Navegação e Funcionalidades](#navegação-e-funcionalidades)
4. [Interpretação dos Dados](#interpretação-dos-dados)
5. [Solução de Problemas](#solução-de-problemas)

---

## 🔧 Instalação

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/RUrzeda/Seguranca_Goias.git
cd Seguranca_Goias
```

### Passo 2: Criar Ambiente Virtual (Recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o Dashboard

### Comando Básico

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no navegador em `http://localhost:8501`

### Executar em Porta Específica

```bash
streamlit run app.py --server.port 8502
```

### Executar sem Abrir Navegador

```bash
streamlit run app.py --server.headless true
```

---

## 🎯 Navegação e Funcionalidades

### 1️⃣ Barra Lateral (Sidebar)

#### Filtro de Período
- **Localização:** Topo da barra lateral
- **Função:** Selecione o intervalo de anos para análise
- **Como usar:** Arraste os controles deslizantes para definir ano inicial e final
- **Exemplo:** Para analisar apenas 2020-2024, ajuste o slider para esses anos

#### Seleção de Indicadores
- **Localização:** Meio da barra lateral
- **Função:** Escolha quais indicadores visualizar nos gráficos
- **Opções disponíveis:**
  - ✅ MVI (Mortes Violentas Intencionais)
  - ✅ Homicídios CVLI
  - ✅ Latrocínio
  - ✅ Roubo de Veículos
- **Dica:** Desmarque indicadores para focar em análises específicas

### 2️⃣ Métricas Principais

**Localização:** Topo da página principal

Exibe 4 cartões com:
- Valor atual (2024)
- Variação percentual desde o ano inicial selecionado
- Indicador visual de tendência (🔻 queda / 🔺 alta)

**Interpretação das cores:**
- 🟢 Verde: Redução (positivo para criminalidade)
- 🔴 Vermelho: Aumento (negativo para criminalidade)

### 3️⃣ Seção de Insights

**Localização:** Abaixo das métricas

Apresenta análises automáticas dos dados:
- **Caixas azuis:** Insights positivos (reduções)
- **Caixas amarelas:** Alertas (aumentos ou anomalias)

### 4️⃣ Gráficos Interativos

#### Gráfico 1: Evolução das Taxas por 100 mil Habitantes
- **Tipo:** Linha
- **Função:** Mostra tendência temporal normalizada pela população
- **Interatividade:**
  - Passe o mouse sobre os pontos para ver valores exatos
  - Clique nas legendas para ocultar/mostrar séries
  - Use os botões de zoom no canto superior direito

#### Gráfico 2: Números Absolutos de Casos
- **Tipo:** Barras agrupadas
- **Função:** Compara valores absolutos entre indicadores
- **Interatividade:**
  - Passe o mouse sobre as barras para detalhes
  - Clique e arraste para zoom em período específico

#### Gráfico 3: Variação Percentual Anual
- **Tipo:** Barras
- **Função:** Mostra crescimento/redução ano a ano
- **Interpretação:**
  - Barras acima de zero: Aumento
  - Barras abaixo de zero: Redução
  - Linha tracejada: Referência zero

### 5️⃣ Tabela de Dados Detalhados

**Localização:** Parte inferior da página

- Exibe todos os dados brutos e calculados
- Valores ausentes aparecem como "N/D"
- Clique nos cabeçalhos para ordenar
- Use a barra de rolagem horizontal para ver todas as colunas

### 6️⃣ Metodologia e Fontes

**Localização:** Seção expansível no final

- Clique em "🔍 Clique para ver detalhes" para expandir
- Contém informações completas sobre:
  - Fontes de dados
  - Definições de indicadores
  - Lacunas conhecidas
  - Notas metodológicas

---

## 📊 Interpretação dos Dados

### Entendendo as Taxas por 100 mil Habitantes

**Por que usar taxas?**
- Permite comparação justa ao longo do tempo
- Compensa o crescimento populacional
- Padrão internacional em estudos de segurança

**Exemplo prático:**
- 2017: 2.676 casos de MVI / 6.805.532 habitantes = 39,32 por 100 mil
- 2024: 1.379 casos de MVI / 7.350.483 habitantes = 18,76 por 100 mil
- Mesmo com população maior, o risco individual caiu 52,3%

### Diferença entre MVI e CVLI

| Aspecto | MVI | CVLI |
|---------|-----|------|
| **Fonte** | FBSP (nacional) | SSP-GO (estadual) |
| **Inclui MDIP** | ✅ Sim | ❌ Não |
| **Uso** | Comparações nacionais | Políticas estaduais |
| **Disponibilidade** | 2017-2024 | 2020-2024 |

**MDIP:** Mortes Decorrentes de Intervenção Policial

### Valores "N/D" (Não Disponível)

Aparecem quando:
- Dados não foram coletados no período
- Fonte oficial não divulgou informação
- Mudança metodológica impediu comparação

**Não significa:**
- Que não houve ocorrências
- Erro no dashboard
- Problema com o sistema

---

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError"

**Causa:** Dependências não instaladas

**Solução:**
```bash
pip install -r requirements.txt
```

### Erro: "FileNotFoundError: dados.csv"

**Causa:** Executando app.py fora do diretório correto

**Solução:**
```bash
cd Seguranca_Goias
streamlit run app.py
```

### Dashboard não abre no navegador

**Solução 1:** Abra manualmente
- Copie a URL mostrada no terminal (ex: `http://localhost:8501`)
- Cole no navegador

**Solução 2:** Verifique a porta
```bash
streamlit run app.py --server.port 8502
```

### Gráficos não aparecem

**Causa:** Problema com Plotly

**Solução:**
```bash
pip install --upgrade plotly
```

### Dashboard muito lento

**Causa:** Cache não ativado ou muitos dados

**Solução:**
- O cache já está implementado no código
- Recarregue a página (F5)
- Reduza o período de análise usando o filtro

---

## 💡 Dicas de Uso

### Para Análises Rápidas
1. Use o filtro de período para focar em anos recentes (2020-2024)
2. Selecione apenas 1-2 indicadores por vez
3. Observe as métricas principais no topo

### Para Análises Detalhadas
1. Mantenha todos os indicadores selecionados
2. Analise o período completo (2017-2024)
3. Explore a tabela de dados detalhados
4. Leia a seção de metodologia

### Para Apresentações
1. Use o modo de tela cheia do navegador (F11)
2. Prepare filtros antes de apresentar
3. Use o zoom dos gráficos para destacar períodos
4. Exporte gráficos clicando no ícone de câmera (canto superior direito)

### Para Pesquisas
1. Consulte sempre a seção "Metodologia e Fontes"
2. Cite as fontes originais (FBSP, SSP-GO, IMB)
3. Documente as lacunas de dados em suas análises
4. Use as taxas por 100 mil habitantes para comparações

---

## 📞 Suporte

### Problemas Técnicos
- Abra uma issue no GitHub: https://github.com/RUrzeda/Seguranca_Goias/issues

### Dúvidas sobre Dados
- Consulte o README.md completo
- Verifique o arquivo `goias_seguranca_metadata.txt`
- Entre em contato com as fontes oficiais (FBSP, SSP-GO, IMB)

### Sugestões de Melhorias
- Envie um pull request no GitHub
- Descreva claramente a melhoria proposta

---

## 📚 Recursos Adicionais

- **README completo:** `README.md`
- **Metadados do dataset:** `goias_seguranca_metadata.txt`
- **Código-fonte:** `app.py`
- **Dados brutos:** `dados.csv`

---

**Desenvolvido com dados oficiais do FBSP, SSP-GO, IMB e IBGE**  
**Última atualização:** Outubro 2025
