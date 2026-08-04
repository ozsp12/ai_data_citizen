# AI Data Citizen

Repositório didático de análise de dados com Python, SQL, DAX e ferramentas de visualização. O material combina videoaulas, notebooks comentados, conjuntos de dados sintéticos e arquivos de apoio para desenvolver autonomia na exploração, transformação e comunicação de dados.

O percurso principal contém três unidades. Elas podem ser estudadas em sequência, mas cada uma também funciona de forma independente.

## Videoaulas e materiais

### 1. Trilha rápida do analista de dados

[![Trilha rápida do analista de dados](https://img.youtube.com/vi/dLDmXewxwpA/hqdefault.jpg)](https://youtu.be/dLDmXewxwpA)

**[Aula “trilha rápida do analista de dados”: exemplos de funções Python, SQL e DAX muito utilizadas](https://youtu.be/dLDmXewxwpA)**

Introdução operacional às funções mais frequentes de `pandas`, comandos SQL executados com DuckDB e conceitos básicos de DAX utilizados no Power BI.

- [Guia da unidade](fast_track/README.md)
- [Notebook](fast_track/fast_track.ipynb)
- [Dados em CSV](fast_track/df_fast_track.csv) e [Parquet](fast_track/df_fast_track.parquet)
- [Relatório Power BI](fast_track/fast_track.pbix)

### 2. Análise rápida de precificação e elasticidade

[![Quick and dirty: precificação e elasticidade](https://img.youtube.com/vi/Vn45DCpdXNw/hqdefault.jpg)](https://youtu.be/Vn45DCpdXNw)

**[“Quick and dirty”: análise de dados com Python — precificação e elasticidade](https://youtu.be/Vn45DCpdXNw)**

Exemplo sintético de uma esteira analítica para explorar relações entre preço, demanda, agregação por faixas e ajustes lineares ou quadráticos.

- [Guia da unidade](quick_dirty_analytics/README.md)
- [Notebook](quick_dirty_analytics/precificacao_elasticidade.ipynb)

> O notebook é uma demonstração computacional. Seu índice sintético denominado `Elasticidade` não é uma estimativa causal de elasticidade-preço e não deve orientar decisões comerciais sem desenho de identificação, dados adequados e análise de incerteza.

### 3. Visualização de dados longitudinais

[![Como visualizar dados longitudinais](https://img.youtube.com/vi/Etwy8F1cmzA/hqdefault.jpg)](https://youtu.be/Etwy8F1cmzA)

**[Como visualizar dados longitudinais: linhas, heatmaps e painéis](https://youtu.be/Etwy8F1cmzA)**

Discussão sobre escolhas gráficas para observações repetidas no tempo, incluindo linhas, mapas de calor, painéis e uma animação reprodutível de séries temporais sintéticas.

- [Guia da unidade](dados_em_painel/README.md)
- [Notebook de animação](dados_em_painel/grafico_animado_serie_temporal.ipynb)
- [Material da aula em PDF](dados_em_painel/tipos_graficos_dados_em_painel.pdf)

## Materiais complementares

| Pasta | Conteúdo |
|---|---|
| [`analise_dados_com_duckdb/`](analise_dados_com_duckdb/README.md) | Exercícios de exploração e modelagem de dados de eventos, assinaturas e vídeos com SQL e DuckDB |
| [`visualizacoes/`](visualizacoes/README.md) | Galeria de gráficos estáticos e animados com Matplotlib, Seaborn e Plotly |

## Objetivos de aprendizagem

Ao trabalhar com os materiais, o estudante deverá ser capaz de:

- inspecionar, filtrar, ordenar e agregar tabelas com `pandas`;
- formular consultas SQL para seleção, agregação e manipulação de dados;
- reconhecer o papel do contexto de filtro em medidas DAX;
- construir uma análise exploratória de precificação sem confundi-la com inferência causal;
- escolher representações adequadas para séries temporais e dados longitudinais;
- documentar parâmetros, fontes, limitações e resultados de uma análise reproduzível.

## Ambiente computacional

Crie o ambiente Conda compartilhado por todas as unidades:

```bash
git clone https://github.com/ozsp12/ai_data_citizen.git
cd ai_data_citizen
conda env create -f requirements.yml
conda activate ai-data-citizen
jupyter lab
```

Abra o notebook desejado e execute as células em ordem. Para exportar animações em MP4 é necessário ter `ffmpeg`, incluído no ambiente Conda. O arquivo `.pbix` requer Power BI Desktop e não é executado pelo ambiente Python.

## Estrutura

```text
ai_data_citizen/
├── fast_track/                 # Python, SQL e DAX
├── quick_dirty_analytics/      # precificação e índice sintético de elasticidade
├── dados_em_painel/            # visualização longitudinal
├── analise_dados_com_duckdb/   # exercícios complementares de SQL
├── visualizacoes/              # galeria de gráficos
├── REFERENCES.md
├── CITATION.cff
└── requirements.yml
```

## Uso responsável

Os dados gerados nos notebooks são sintéticos, salvo indicação explícita em contrário. Resultados exploratórios descrevem a amostra ou o mecanismo simulado; não estabelecem causalidade, previsão fora da amostra ou recomendação de negócio por si mesmos. Em aplicações reais, registre a origem dos dados, valide qualidade e representatividade, defina métricas antes da análise e quantifique incertezas.

## Referências e citação

A bibliografia de Python, SQL, DAX, visualização e análise longitudinal está em [`REFERENCES.md`](REFERENCES.md). Para citar o repositório, utilize os metadados de [`CITATION.cff`](CITATION.cff).

## Autor

**Dr. Osvaldo L. Santos-Pereira** — [Página acadêmica](https://ozsp12.github.io/) · [Lattes](http://lattes.cnpq.br/6730251976463283) · [ORCID](https://orcid.org/0000-0003-2231-517X) · [Google Scholar](https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en) · [ResearchGate](https://www.researchgate.net/profile/Osvaldo-Santos-Pereira) · [GitHub](https://github.com/ozsp12) · [LinkedIn](https://www.linkedin.com/in/ozsp12) · [Substack](https://substack.com/@olsp1982) · [Medium](https://medium.com/@ozsp12) · [YouTube](https://www.youtube.com/@ozlsp12) · [X](https://x.com/ozsp12)
