import pandas as pd
import re
from typing import Optional

def limpar_espacos(texto: any) -> any:
    """Remove excesso de espaços de uma string."""
    if isinstance(texto, str):
        return re.sub(r'\s+', ' ', texto).strip()
    return texto

def ler_csv(file_path: str, sep: str = ';', dtype: Optional[dict] = None) -> Optional[pd.DataFrame]:
    """
    Lê um arquivo CSV, testando automaticamente uma lista de codificações comuns.
    Retorna None se o arquivo não for encontrado ou nenhuma codificação funcionar.
    """
    encodings_to_try = ['utf-8-sig', 'iso-8859-1', 'utf-8', 'latin-1']
    
    print(f"Lendo o arquivo: '{file_path}'...")
    try:
        for encoding in encodings_to_try:
            try:
                df = pd.read_csv(file_path, sep=sep, encoding=encoding, dtype=dtype)
                print(f"-> Sucesso! Arquivo lido com a codificação '{encoding}'.")
                return df
            except UnicodeDecodeError:
                continue

        print(f"ERRO: Nenhuma codificação compatível encontrada para o arquivo '{file_path}'.")
        print(f"Codificações tentadas: {encodings_to_try}")
        return None

    except FileNotFoundError:
        print(f"ERRO: O arquivo '{file_path}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return None

def salvar_csv(df: pd.DataFrame, file_path: str, encoding: str, sep: str = ';'):
    """Salva um DataFrame em um arquivo CSV."""
    try:
        df.to_csv(file_path, sep=sep, index=False, encoding=encoding)
        print(f"Arquivo salvo com sucesso em: '{file_path}'")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")