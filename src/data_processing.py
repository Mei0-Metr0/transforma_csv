import pandas as pd
from typing import Tuple
from src.file_manipulation import limpar_espacos

def filtrar_cursos_unicos(df: pd.DataFrame, chave: str, colunas_desejadas: list) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Filtra um DataFrame para manter apenas cursos únicos baseados em uma chave.

    Retorna:
        Uma tupla contendo (df_unicos, df_removidos).
    """
    df_removidos = df[df.duplicated(subset=[chave], keep='first')]
    df_sem_duplicadas = df.drop_duplicates(subset=[chave], keep='first')
    df_filtrado_final = df_sem_duplicadas[colunas_desejadas]
    
    return df_filtrado_final, df_removidos

def transformar_dados_principais(df_principal: pd.DataFrame, df_de_para: pd.DataFrame, config: object) -> pd.DataFrame:
    """
    Executa a transformação principal dos dados, mesclando, renomeando e adicionando colunas.
    """
    df_principal.columns = df_principal.columns.str.strip()
    df_de_para.columns = df_de_para.columns.str.strip()

    # Limpa espaços na coluna chave e verifica duplicatas no arquivo de mapeamento
    df_de_para['CO_IES_CURSO'] = df_de_para['CO_IES_CURSO'].apply(limpar_espacos)
    duplicatas = df_de_para[df_de_para.duplicated(subset=['CO_IES_CURSO'], keep=False)]

    if not duplicatas.empty:
        print("\nAtenção: Foram encontradas duplicatas na chave 'CO_IES_CURSO' do arquivo de mapeamento.")
        print(duplicatas.sort_values(by='CO_IES_CURSO'))
    else:
        print("\nNenhuma duplicata encontrada na chave do arquivo de mapeamento.")
        
    # Mescla os dataframes
    df_final = pd.merge(df_principal, df_de_para[['CO_IES_CURSO', 'CO_CURSO_ACAD']], on='CO_IES_CURSO', how='left')
    
    # Renomeia, adiciona e reordena colunas
    df_final.rename(columns=config.MAPEAMENTO_COLUNAS_FINAL, inplace=True)
    df_final['ANONR'] = config.ANO
    df_final['SEMESTRENR'] = config.SEMESTRE
    
    # Reordena e garante que todas as colunas desejadas existam
    df_final = df_final.reindex(columns=config.ORDEM_COLUNAS_FINAL)
    
    for col in df_final.select_dtypes(include=['object']).columns:
        df_final[col] = df_final[col].map(limpar_espacos, na_action='ignore')
    
    return df_final