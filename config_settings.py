"""
Arquivo de configuração central com todas as variáveis e parâmetros do projeto.
"""

# --- Diretórios ---
INPUT_DIR = 'docs'
OUTPUT_DIR = 'resultado'

# --- Nomes dos Arquivos de Entrada ---
ARQUIVO_CURSOS_ENTRADA = 'CodCursos.csv'
ARQUIVO_PRINCIPAL_ENTRADA = 'tester.csv'

# --- Nomes dos Arquivos de Saída ---
ARQUIVO_CURSOS_FILTRADOS_SAIDA = 'campus_filtrado.csv'
ARQUIVO_CURSOS_REMOVIDOS_SAIDA = 'campus_removidos.csv'
ARQUIVO_FINAL_SAIDA = 'arquivo_transformado.csv'

# --- Codificação de Arquivos ---
# A codificação de entrada é detectada automaticamente.
# A codificação de saída é usada ao salvar os arquivos.
ENCODING_SAIDA = 'iso-8859-1'

# --- Parâmetros da Transformação ---
ANO = 2025
SEMESTRE = 2

# --- Mapeamentos e Listas de Colunas ---
COLUNAS_FILTRAGEM_CURSO = ['NO_CAMPUS', 'CO_IES_CURSO', 'CO_CURSO_ACAD', 'NO_CURSO']

MAPEAMENTO_COLUNAS_FINAL = {
    'CO_CURSO_INSCRICAO': 'CO_INSCRICAO',
    'TIPO_CONCORRENCIA': 'CO_MODALIDADE_CONCORRENCIA',
    'COR_RACA': 'ETNIA_E_COR'
}

ORDEM_COLUNAS_FINAL = [
    'NU_ETAPA', 'NO_CAMPUS', 'CO_IES_CURSO', 'CO_CURSO_ACAD', 'NO_CURSO', 'DS_TURNO',
    'CO_INSCRICAO', 'NO_INSCRITO', 'NO_SOCIAL', 'NU_CPF_INSCRITO', 'DT_NASCIMENTO',
    'TP_SEXO', 'NO_MAE', 'DS_LOGRADOURO', 'NU_ENDERECO', 'DS_COMPLEMENTO',
    'SG_UF_INSCRITO', 'NO_MUNICIPIO', 'NO_BAIRRO', 'NU_CEP', 'NU_FONE1',
    'DS_EMAIL', 'NU_NOTA_L', 'NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_M', 'NU_NOTA_R',
    'ST_OPCAO', 'NO_MODALIDADE_CONCORRENCIA', 'CO_MODALIDADE_CONCORRENCIA',
    'NU_NOTA_CANDIDATO', 'ANONR', 'SEMESTRENR', 'ETNIA_E_COR'
]