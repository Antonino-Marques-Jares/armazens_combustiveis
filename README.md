![Terminal](terminais_combustivel.jpg)

# armazens_combustiveis
Armazéns de Combustíveis pelo Brasil

## Fonte dos Armazens:
[![Dados Abertos](govbr.webp)](https://dados.gov.br/dados/conjuntos-dados/capacidade-de-armazenagem-de-terminais)

### Informações de latitude e longitude dos Municípios Brasileiros

- https://github.com/kelvins/municipios-brasileiros/blob/main/csv/estados.csv
- https://github.com/kelvins/municipios-brasileiros/blob/main/csv/municipios.csv

### Passo 1 - Baixe o arquivos CSV: 

- capacidade-armazem-terminais.csv
- estados.csv
- municipios.csv

### Passo 2 - Execute o programa capacidade_terminais.ipynb.

  No programa criamos o data frame df_armazens

  Criamos com base nos csvs estados.csv e municipios.csv o df_municipios que consta a posição geográfica de cada Município.

  Juntando as informações relevantes no **df_final** ficamos com as seguintes colunas :

  - Municipio <- É o nome do Município sem acentos o caracteres especiais. Foi uma padronização para executar o Join.
  - Estado <- Nome do Estado
  - Capacidade_nominal_petroleo
  - Capacidade_nominal_derivados_biocombustiveis
  - Capacidade_nominal_GLP
  - latitude
  - longitude

  Criamos um json a partir do df_final.
  
  **Criamos um html com o json incorporado onde é exibido o mapa.**

**Autor:** 

Antonino Marques Jares

**Atualizado em:** 

04/07/2025

**Projeto no GitHub:** 

[Bacias Hidrográficas](https://github.com/Antonino-Marques-Jares/armazens_combustiveis/tree/main)

**Página Publicação:** 

[Área de Trampo - Mapa de armazens de combustíveis](https://www.areadetrampo.com.br/armazens-de-combustiveis-pelo-brasil/))



