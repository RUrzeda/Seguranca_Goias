# 🛡️ Dashboard de Segurança Pública de Goiás (2017-2024)

Dashboard interativo desenvolvido em Streamlit para análise de indicadores criminais do estado de Goiás, com dados oficiais de fontes governamentais e instituições de pesquisa reconhecidas.

## 📊 Sobre o Projeto

Este dashboard apresenta uma análise temporal detalhada dos principais indicadores de segurança pública em Goiás entre 2017 e 2024, permitindo visualizar:

- **Mortes Violentas Intencionais (MVI):** Série histórica completa com taxas por 100 mil habitantes
- **Homicídios Dolosos/CVLI:** Crimes Violentos Letais Intencionais
- **Latrocínio:** Roubo seguido de morte
- **Roubo de Veículos:** Evolução e redução expressiva no período

## 🎯 Principais Insights

### ✅ Declínio Estrutural da Violência Letal

As **Mortes Violentas Intencionais (MVI)** apresentaram queda significativa:
- **2017:** 2.676 casos (taxa de 39,32 por 100 mil hab.)
- **2024:** 1.379 casos (taxa de 18,76 por 100 mil hab.)
- **Redução:** 48,5% em números absolutos

Em 2024, Goiás registrou a **9ª menor taxa estadual de MVI do Brasil**, segundo o Anuário Brasileiro de Segurança Pública.

### ✅ Eficácia Exponencial no Combate ao Crime Patrimonial

O **Roubo de Veículos** teve queda espetacular:
- **2018:** 10.104 casos (~28 veículos/dia)
- **2024:** 756 casos (~2 veículos/dia)
- **Redução:** 93%

### ⚠️ Anomalia do Latrocínio

Apesar da queda generalizada, o **Latrocínio** apresentou aumento recente:
- **2023:** 14 casos
- **2024:** 17 casos
- **Variação:** +21,4%

Este aumento ocorre em contexto de queda massiva dos roubos, indicando possível aumento da letalidade nos crimes remanescentes.

## 📚 Fontes de Dados e Metodologia

### Fontes Oficiais Utilizadas

#### 1. Anuário Brasileiro de Segurança Pública (FBSP)
- **Instituição:** Fórum Brasileiro de Segurança Pública
- **Website:** [https://forumseguranca.org.br](https://forumseguranca.org.br)
- **Dados utilizados:**
  - Mortes Violentas Intencionais (MVI) - 2017 a 2024
  - População estimada (IBGE) - 2017 a 2024
- **Arquivo fonte:** `anuario-2025-dados.xlsx`
- **URL de download:** [https://forumseguranca.org.br/wp-content/uploads/2025/07/anuario-2025-dados.xlsx](https://forumseguranca.org.br/wp-content/uploads/2025/07/anuario-2025-dados.xlsx)

**Sobre o FBSP:** O Fórum Brasileiro de Segurança Pública é uma organização não-governamental reconhecida nacionalmente pela compilação e padronização de dados de segurança pública de todas as Unidades Federativas do Brasil. O Anuário é a publicação mais completa e confiável sobre estatísticas criminais no país.

#### 2. Secretaria de Segurança Pública de Goiás (SSP-GO)
- **Instituição:** Governo do Estado de Goiás
- **Website:** [https://goias.gov.br/seguranca](https://goias.gov.br/seguranca)
- **Dados utilizados:**
  - Roubo de Veículos - 2018, 2021-2024
  - Balanços anuais de criminalidade
- **Fontes específicas:**
  - [Redução de 93% no roubo de veículos](https://agenciacoradenoticias.go.gov.br/144342-goias-registra-reducao-de-93-no-roubo-a-veiculos-em-seis-anos)
  - [Balanço das ações de 2024](https://goias.gov.br/seguranca/seguranca-publica-de-goias-divulga-balanco-das-acoes-de-2024)

#### 3. Instituto Mauro Borges (IMB)
- **Instituição:** Governo do Estado de Goiás
- **Website:** [https://goias.gov.br/imb](https://goias.gov.br/imb)
- **Dados utilizados:**
  - Homicídios Dolosos/CVLI - 2020-2024
  - Latrocínio - 2021-2024
  - Análises estatísticas consolidadas
- **Documento principal:** "Goiás em Dados 2024"
- **URL:** [https://goias.gov.br/imb/wp-content/uploads/sites/29/2025/02/Goias_em_dados_2024.pdf](https://goias.gov.br/imb/wp-content/uploads/sites/29/2025/02/Goias_em_dados_2024.pdf)

**Sobre o IMB:** O Instituto Mauro Borges é o órgão oficial de estatística do Estado de Goiás, responsável pela produção e disseminação de informações estatísticas, geográficas, cartográficas e de estudos socioeconômicos sobre o estado.

#### 4. Instituto Brasileiro de Geografia e Estatística (IBGE)
- **Instituição:** Governo Federal
- **Website:** [https://www.ibge.gov.br](https://www.ibge.gov.br)
- **Dados utilizados:**
  - Projeções populacionais anuais para Goiás (referência: 1º de julho)
  - Dados do Censo Demográfico 2022
- **Acesso:** Via Anuário FBSP e relatórios IMB

### Metodologia de Coleta e Harmonização

#### Processo de ETL (Extract, Transform, Load)

1. **Extração:**
   - Download do arquivo Excel do Anuário FBSP 2025
   - Acesso a relatórios técnicos do IMB
   - Coleta de dados de balanços da SSP-GO

2. **Transformação:**
   - Filtragem de dados específicos de Goiás (UF = GO)
   - Harmonização de definições criminais entre fontes
   - Cálculo de taxas por 100 mil habitantes
   - Tratamento de valores ausentes (N/D)

3. **Carregamento:**
   - Consolidação em arquivo CSV único
   - Validação de consistência temporal
   - Documentação de lacunas conhecidas

#### Definições e Conceitos

**MVI (Mortes Violentas Intencionais):**
- Definição padronizada pelo FBSP
- Inclui: Homicídio Doloso + Latrocínio + Lesão Corporal Seguida de Morte + Mortes Decorrentes de Intervenção Policial (MDIP)
- Métrica mais abrangente de violência letal

**CVLI (Crimes Violentos Letais Intencionais):**
- Definição utilizada pela SSP-GO
- Inclui: Homicídio Doloso + Latrocínio + Lesão Corporal Seguida de Morte
- **Não inclui** Mortes Decorrentes de Intervenção Policial
- Utilizado nos relatórios estaduais de Goiás

**Latrocínio:**
- Crime patrimonial (roubo) que resulta em morte da vítima
- Tipificado no Art. 157, §3º do Código Penal Brasileiro

**Roubo de Veículos:**
- Subtração de veículo automotor mediante violência ou grave ameaça
- Inclui automóveis, motocicletas e outros veículos

#### Cálculo de Taxas

As taxas por 100 mil habitantes foram calculadas usando a fórmula:

```
Taxa = (Número de Casos / População Estimada) × 100.000
```

A população estimada utilizada é sempre a projeção do IBGE para 1º de julho de cada ano, conforme metodologia padrão em estudos de segurança pública.

### Lacunas de Dados Conhecidas

| Indicador | Período Completo | Lacunas | Cobertura |
|-----------|------------------|---------|-----------|
| MVI | 2017-2024 | Nenhuma | 100% |
| População | 2017-2024 | Nenhuma | 100% |
| Homicídios CVLI | 2020-2024 | 2017-2019 | 62,5% |
| Latrocínio | 2021-2024 | 2017-2020 | 50% |
| Roubo de Veículos | 2018, 2021-2024 | 2017, 2019-2020 | 62,5% |

**Motivo das lacunas:**
- Dados de 2017-2019 não disponibilizados em formato estruturado pelos órgãos estaduais
- Mudanças metodológicas na coleta e divulgação de dados
- Priorização de séries históricas mais recentes nos relatórios oficiais

### Notas Metodológicas Importantes

#### 1. Diferença entre MVI e CVLI
O MVI (utilizado pelo FBSP) é mais abrangente que o CVLI (utilizado pela SSP-GO) pois inclui as Mortes Decorrentes de Intervenção Policial. Para análises comparativas nacionais, o MVI é preferível. Para análises focadas em políticas estaduais, o CVLI pode ser mais apropriado.

#### 2. Impacto do Censo 2022
O Censo Demográfico de 2022 revisou as projeções populacionais anteriores do IBGE. Isso causou:
- Descontinuidade no denominador usado para calcular taxas
- Salto populacional entre 2022 (7.055.228) e 2023 (7.350.483)
- Necessidade de cautela ao comparar taxas entre 2022 e 2023

Apesar disso, a tendência de queda nos números absolutos de crimes permanece clara e consistente.

#### 3. Contextualização das Políticas Públicas

A partir de 2019, o Governo de Goiás implementou reformas estruturais na segurança pública:

- **Integração das forças policiais:** Polícia Militar, Polícia Civil e Polícia Penal
- **Investimento financeiro:** Mais de R$ 17 bilhões (2019-2024)
- **Infraestrutura:** Construção de penitenciárias, delegacias e batalhões
- **Tecnologia:** Sistemas de inteligência, rastreamento e monitoramento
- **Recursos humanos:** Concursos, capacitação e reajuste salarial
- **Operações integradas:** Bloqueios, patrulhamento ostensivo e ações preventivas

Esses investimentos são citados como fatores determinantes para a redução consistente da criminalidade observada nos dados.

## 🚀 Como Executar o Dashboard

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/RUrzeda/Seguranca_Goias.git
cd Seguranca_Goias
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Execução

Execute o dashboard com o comando:
```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no navegador em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
dashboard_seguranca_goias/
│
├── app.py                          # Aplicação principal do Streamlit
├── dados.csv                       # Dataset consolidado
├── requirements.txt                # Dependências Python
├── README.md                       # Este arquivo
└── goias_seguranca_metadata.txt   # Metadados detalhados do dataset
```

## 🛠️ Tecnologias Utilizadas

- **Streamlit:** Framework para criação de dashboards interativos
- **Pandas:** Manipulação e análise de dados
- **Plotly:** Visualizações interativas e gráficos
- **Python 3.11:** Linguagem de programação

## 📈 Funcionalidades do Dashboard

- ✅ Filtro de período temporal (slider interativo)
- ✅ Seleção de indicadores para análise
- ✅ Métricas principais com variação percentual
- ✅ Gráficos interativos de séries temporais
- ✅ Análise de variação percentual anual
- ✅ Tabela de dados detalhados
- ✅ Documentação completa de metodologia e fontes
- ✅ Insights contextualizados com políticas públicas

## 📊 Visualizações Disponíveis

1. **Evolução das Taxas por 100 mil Habitantes:** Gráfico de linhas mostrando a tendência temporal das taxas normalizadas
2. **Números Absolutos de Casos:** Gráfico de barras agrupadas comparando indicadores
3. **Variação Percentual Anual:** Análise de crescimento/redução ano a ano
4. **Tabela de Dados Completa:** Todos os dados brutos e calculados

## 🔍 Interpretação dos Resultados

### Tendências Positivas

- **Queda consistente da violência letal:** Redução de 48,5% no MVI entre 2017-2024
- **Supressão do crime patrimonial:** Redução de 93% no roubo de veículos
- **Posicionamento nacional favorável:** 9ª menor taxa de MVI do Brasil em 2024

### Pontos de Atenção

- **Latrocínio em alta:** Aumento de 21,4% entre 2023-2024 requer investigação
- **Lacunas de dados:** Séries históricas incompletas para alguns indicadores
- **Efeito Censo 2022:** Descontinuidade populacional afeta comparações de taxas

## 📝 Citação e Referências

Se utilizar este dashboard ou dados em pesquisas ou publicações, favor citar:

**Formato ABNT:**
```
URZEDA, R. Dashboard de Segurança Pública de Goiás (2017-2024). GitHub, 2025. 
Disponível em: https://github.com/RUrzeda/Seguranca_Goias. Acesso em: [data].
```

**Fontes de dados citadas:**
```
FÓRUM BRASILEIRO DE SEGURANÇA PÚBLICA. Anuário Brasileiro de Segurança Pública 2025. 
São Paulo: FBSP, 2025. Disponível em: https://forumseguranca.org.br

GOIÁS. Instituto Mauro Borges de Estatísticas e Estudos Socioeconômicos. 
Goiás em Dados 2024. Goiânia: IMB, 2024.

GOIÁS. Secretaria de Segurança Pública. Balanço das Ações de Segurança Pública 2024. 
Goiânia: SSP-GO, 2025.

IBGE. Projeções da População do Brasil e Unidades da Federação. 
Rio de Janeiro: IBGE, 2024.
```

## 🤝 Contribuições

Contribuições são bem-vindas! Se você identificar:
- Erros nos dados ou cálculos
- Fontes adicionais de dados
- Melhorias nas visualizações
- Sugestões de novas análises

Por favor, abra uma *issue* ou envie um *pull request*.

## 📄 Licença

Este projeto utiliza dados públicos de fontes governamentais e está disponível para uso educacional e de pesquisa.

## 👤 Autor

**RUrzeda**
- GitHub: [@RUrzeda](https://github.com/RUrzeda)
- Repositório: [Seguranca_Goias](https://github.com/RUrzeda/Seguranca_Goias)

## 📞 Contato e Suporte

Para dúvidas sobre:
- **Metodologia e fontes:** Consulte este README ou o arquivo `goias_seguranca_metadata.txt`
- **Funcionamento do dashboard:** Abra uma issue no GitHub
- **Dados oficiais:** Entre em contato diretamente com as instituições fonte (FBSP, SSP-GO, IMB)

---

**Última atualização:** Outubro de 2025  
**Versão do dashboard:** 1.0  
**Período dos dados:** 2017-2024
