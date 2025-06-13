import os
import src.config as config
from src.file_manipulation import ler_csv, salvar_csv
from src.data_processing import filtrar_cursos_unicos, transformar_dados_principais

def rodar_pipeline_filtragem():
    """
    Executa o pipeline para filtrar os cursos únicos do arquivo de entrada de cursos.
    """
    print("\n--- INICIANDO ETAPA 1: Filtragem de Cursos ---\n")
    # A chamada foi simplificada, sem o parâmetro de encoding
    df_cursos = ler_csv(config.PATH_CURSOS_ENTRADA)
    
    if df_cursos is None:
        print("\n--- ETAPA 1 FALHOU: Não foi possível ler o arquivo de cursos. ---")
        return

    total_original = len(df_cursos)
    print(f"Total de linhas no arquivo original: {total_original}")
    
    df_filtrado, df_removidos = filtrar_cursos_unicos(
        df_cursos, 
        'CO_IES_CURSO', 
        config.COLUNAS_FILTRAGEM_CURSO
    )
    
    print(f"Número de cursos únicos: {len(df_filtrado)}")
    print(f"Número de linhas duplicadas/removidas: {len(df_removidos)}")
    
    if total_original == len(df_filtrado) + len(df_removidos):
        print("Nenhuma linha foi perdida durante a filtragem.")
    else:
        print("Atenção: A soma das partes não corresponde ao total original.")
        
    salvar_csv(df_filtrado, config.PATH_CURSOS_FILTRADOS_SAIDA, config.ENCODING_SAIDA)
    salvar_csv(df_removidos, config.PATH_CURSOS_REMOVIDOS_SAIDA, config.ENCODING_SAIDA)
    print("\n--- ETAPA 1 CONCLUÍDA ---")


def rodar_pipeline_principal():
    """
    Executa o pipeline principal para transformar os dados usando o arquivo de cursos filtrado.
    """
    print("\n--- INICIANDO ETAPA 2: Transformação Principal ---\n")
    
    dtype_chave = {'CO_IES_CURSO': str}

    # As chamadas foram simplificadas, sem o parâmetro de encoding
    df_principal = ler_csv(config.PATH_PRINCIPAL_ENTRADA, dtype=dtype_chave)
    df_mapeamento = ler_csv(config.PATH_CURSOS_FILTRADOS_SAIDA, dtype=dtype_chave)

    if df_principal is None or df_mapeamento is None:
        print("\n--- ETAPA 2 FALHOU: Não foi possível ler um dos arquivos de entrada. ---")
        return

    df_final = transformar_dados_principais(df_principal, df_mapeamento, config)
    
    salvar_csv(df_final, config.PATH_FINAL_SAIDA, config.ENCODING_SAIDA)
    print("\n--- ETAPA 2 CONCLUÍDA ---")


if __name__ == '__main__':
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)
        print(f"Diretório '{config.OUTPUT_DIR}' criado.")

    rodar_pipeline_filtragem()
    rodar_pipeline_principal()