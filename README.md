# AI Data Citizen

Repositório didático de análise de dados com Python, SQL, DAX e ferramentas de visualização. Os materiais combinam videoaulas, notebooks comentados, dados sintéticos e arquivos de apoio. O objetivo é desenvolver autonomia para inspecionar e transformar tabelas, formular consultas, construir análises exploratórias e escolher representações gráficas adequadas. Ao concluir as três unidades principais, o estudante deverá compreender operações essenciais de `pandas`, SQL e DAX; reconhecer os limites de uma análise exploratória de precificação; e visualizar séries temporais e dados longitudinais com clareza.

| Seção | Conteúdo | Pasta |
|---:|---|---|
| 1 | Funções essenciais de Python, SQL e DAX | [`fast_track/`](fast_track/README.md) |
| 2 | Precificação e índice sintético de elasticidade | [`quick_dirty_analytics/`](quick_dirty_analytics/README.md) |
| 3 | Visualização de dados longitudinais | [`dados_em_painel/`](dados_em_painel/README.md) |
| — | Exercícios de SQL com DuckDB | [`analise_dados_com_duckdb/`](analise_dados_com_duckdb/README.md) |
| — | Exemplos adicionais de visualização | [`visualizacoes/`](visualizacoes/README.md) |

# Trilha rápida do analista de dados

Esta unidade apresenta operações frequentes de análise tabular. O notebook utiliza dados sintéticos para demonstrar inspeção, seleção, filtros, agrupamentos e tratamento de ausências com `pandas`; consultas e operações básicas com SQL e DuckDB; e funções introdutórias de DAX aplicadas ao Power BI.

**Vídeo:** [Aula “trilha rápida do analista de dados”: exemplos de funções Python, SQL e DAX muito utilizadas](https://youtu.be/dLDmXewxwpA)

**Materiais:** [`fast_track.ipynb`](fast_track/fast_track.ipynb) · [`df_fast_track.csv`](fast_track/df_fast_track.csv) · [`df_fast_track.parquet`](fast_track/df_fast_track.parquet) · [`fast_track.pbix`](fast_track/fast_track.pbix)

# Análise rápida de precificação e elasticidade

Esta unidade constrói uma esteira exploratória com dados sintéticos, agregação por faixas, gráficos de preço e captação e ajustes lineares ou quadráticos. A coluna denominada `Elasticidade` é um índice criado para a demonstração computacional; não constitui uma estimativa causal de elasticidade-preço e não deve, isoladamente, orientar decisões comerciais.

**Vídeo:** [“Quick and dirty”: análise de dados com Python — precificação e elasticidade](https://youtu.be/Vn45DCpdXNw)

**Material:** [`precificacao_elasticidade.ipynb`](quick_dirty_analytics/precificacao_elasticidade.ipynb)

# Visualização de dados longitudinais

Esta unidade discute como representar observações repetidas ao longo do tempo por linhas, mapas de calor e painéis. O material compara as finalidades dessas representações e inclui um notebook que gera séries semanais sintéticas e uma animação por ano.

**Vídeo:** [Como visualizar dados longitudinais: linhas, heatmaps e painéis](https://youtu.be/Etwy8F1cmzA)

**Materiais:** [`grafico_animado_serie_temporal.ipynb`](dados_em_painel/grafico_animado_serie_temporal.ipynb) · [`tipos_graficos_dados_em_painel.pdf`](dados_em_painel/tipos_graficos_dados_em_painel.pdf)

# Referências

A bibliografia de Python, bancos de dados, DAX, visualização, análise longitudinal e inferência está reunida em [`REFERENCES.md`](REFERENCES.md). Os metadados para citação do repositório estão em [`CITATION.cff`](CITATION.cff).

# Autor

**Dr. Osvaldo L. Santos-Pereira** — [Página acadêmica](https://ozsp12.github.io/) · [Lattes](http://lattes.cnpq.br/6730251976463283) · [ORCID](https://orcid.org/0000-0003-2231-517X) · [Google Scholar](https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en) · [ResearchGate](https://www.researchgate.net/profile/Osvaldo-Santos-Pereira) · [GitHub](https://github.com/ozsp12) · [LinkedIn](https://www.linkedin.com/in/ozsp12) · [Substack](https://substack.com/@olsp1982) · [Medium](https://medium.com/@ozsp12) · [YouTube](https://www.youtube.com/@ozlsp12) · [X](https://x.com/ozsp12)
