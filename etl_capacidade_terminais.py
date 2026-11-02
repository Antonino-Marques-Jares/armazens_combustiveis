#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Produção de Petróleo, Líquidos de Gás Natural (LGN) e Gás Natural
Capacidade de Armazenagem de Terminais

Autor: Antonino Marques Jares
Fonte: Dados Abertos do GovBR
"""

import json
from datetime import datetime
from pathlib import Path

import pandas as pd

# ============================================================
# Configurações de caminhos
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
PASTA_ETL = BASE_DIR / "etl"

CAMINHO_CSV = Path(
    r"D:\ETL\nivel_01_bronze\capacidade_de_armazenagem_de_terminais"
    r"\capacidade-armazenagem-terminais.csv"
)
CAMINHO_SAIDA = PASTA_ETL / "armazens_combustiveis.json"


# ============================================================
# 1) Leitura dos dados brutos
# ============================================================
def carregar_terminais(caminho: Path = CAMINHO_CSV) -> pd.DataFrame:
    if not caminho.exists():
        raise FileNotFoundError(f"CSV não encontrado: {caminho}")
    return pd.read_csv(caminho, sep=",", encoding="utf-8", low_memory=False)


# ============================================================
# 2) Renomeação de colunas
# ============================================================
def renomear_colunas(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(
        columns={
            "Tipo": "tipo",
            "Municipio": "municipio",
            "UF": "uf",
            "Operador": "operador",
            "Capacidade_nominal_petroleo": "petroleo",
            "Capacidade_nominal_derivados_biocombustiveis": "derivados_biocombustiveis",
            "Capacidade_nominal_GLP": "glp",
        }
    )


# ============================================================
# 3) Tratamento: remoção e reordenação de colunas
# ============================================================
def tratar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["Numero_de_tanques"], errors="ignore")
    df = df[
        [
            "uf",
            "municipio",
            "tipo",
            "operador",
            "petroleo",
            "derivados_biocombustiveis",
            "glp",
        ]
    ]
    return df


# ============================================================
# 4) Serialização para JSON
# ============================================================
def _nativo(v):
    """Converte tipos numpy para tipos nativos Python (e NaN -> None)."""
    if pd.isna(v):
        return None
    if hasattr(v, "item"):
        return v.item()
    return v


def gerar_json(
    df_terminais: pd.DataFrame,
    caminho_saida: Path = CAMINHO_SAIDA,
) -> dict:
    registros = [
        {k: _nativo(v) for k, v in reg.items()}
        for reg in df_terminais.to_dict(orient="records")
    ]

    saida = {
        "metadados": {
            "data_ultima_atualizacao": datetime.now().strftime("%d-%m-%Y"),
            "responsavel": "Antonino Marques Jares",
            "fonte": "https://dados.gov.br/dados/conjuntos-dados/instalacoes-portuarias",
            "orgao": "CGU",
        },
        "dados": registros,
    }

    # Cria a pasta de saída se não existir
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(saida, f, ensure_ascii=False, indent=2)

    print(f"Arquivo gerado com {len(registros)} registros.")
    print("Data de atualização:", saida["metadados"]["data_ultima_atualizacao"])
    return saida


# ============================================================
# Pipeline principal
# ============================================================
def main() -> None:
    print("[1/4] Lendo CSV...")
    print("      Caminho:", CAMINHO_CSV)
    df_terminais = carregar_terminais()
    print("      OK — shape:", df_terminais.shape)

    print("[2/4] Renomeando colunas...")
    df_terminais = renomear_colunas(df_terminais)

    print("[3/4] Tratando e reordenando colunas...")
    df_terminais = tratar_colunas(df_terminais)
    print("      Colunas finais:", list(df_terminais.columns))

    print("[4/4] Gerando JSON...")
    gerar_json(df_terminais)
    print("      JSON em:", CAMINHO_SAIDA.resolve())
    print("      Existe?", CAMINHO_SAIDA.exists())


if __name__ == "__main__":
    main()