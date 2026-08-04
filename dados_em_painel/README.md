# Visualização de dados longitudinais

Material da videoaula **[Como visualizar dados longitudinais: linhas, heatmaps e painéis](https://youtu.be/Etwy8F1cmzA)**.

Dados longitudinais registram repetidamente uma mesma unidade ao longo do tempo. A visualização precisa representar simultaneamente trajetória, heterogeneidade entre unidades, densidade temporal e eventuais ausências. Não existe um gráfico universal: linhas favorecem trajetórias individuais; *heatmaps* favorecem padrões densos; pequenos múltiplos reduzem sobreposição; animações podem apoiar exposição oral, mas são inferiores a gráficos estáticos para comparação precisa.

## Arquivos

- [`tipos_graficos_dados_em_painel.pdf`](tipos_graficos_dados_em_painel.pdf): material conceitual da aula;
- [`grafico_animado_serie_temporal.ipynb`](grafico_animado_serie_temporal.ipynb): geração de dados sazonais sintéticos e animação por ano.

## Execução

```bash
conda activate ai-data-citizen
jupyter lab dados_em_painel/grafico_animado_serie_temporal.ipynb
```

O notebook exibe a animação no Jupyter. A exportação opcional para MP4 ou GIF requer `ffmpeg` ou Pillow, respectivamente.
