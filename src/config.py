import os
import config_settings as settings

ANO = settings.ANO
SEMESTRE = settings.SEMESTRE
ENCODING_SAIDA = settings.ENCODING_SAIDA
INPUT_DIR = settings.INPUT_DIR
OUTPUT_DIR = settings.OUTPUT_DIR
COLUNAS_FILTRAGEM_CURSO = settings.COLUNAS_FILTRAGEM_CURSO
MAPEAMENTO_COLUNAS_FINAL = settings.MAPEAMENTO_COLUNAS_FINAL
ORDEM_COLUNAS_FINAL = settings.ORDEM_COLUNAS_FINAL

# Caminhos Completos de Entrada
PATH_CURSOS_ENTRADA = os.path.join(
    settings.INPUT_DIR, settings.ARQUIVO_CURSOS_ENTRADA
)
PATH_PRINCIPAL_ENTRADA = os.path.join(
    settings.INPUT_DIR, settings.ARQUIVO_PRINCIPAL_ENTRADA
)

# Caminhos Completos de Saída
PATH_CURSOS_FILTRADOS_SAIDA = os.path.join(
    settings.OUTPUT_DIR, settings.ARQUIVO_CURSOS_FILTRADOS_SAIDA
)
PATH_CURSOS_REMOVIDOS_SAIDA = os.path.join(
    settings.OUTPUT_DIR, settings.ARQUIVO_CURSOS_REMOVIDOS_SAIDA
)
PATH_FINAL_SAIDA = os.path.join(
    settings.OUTPUT_DIR, settings.ARQUIVO_FINAL_SAIDA
)