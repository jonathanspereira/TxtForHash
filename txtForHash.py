import hashlib


# Função para gerar hash do conteúdo de um arquivo
def gerar_hash_arquivo(nome_arquivo):
    try:
        # Abre o arquivo em modo de leitura binária
        with open(nome_arquivo, 'rb') as f:
            # Lê todo o conteúdo do arquivo
            conteudo = f.read()
            
            # Cria o objeto hash (usando SHA-256)
            hash_sha256 = hashlib.sha256()
            
            # Atualiza o hash com o conteúdo do arquivo
            hash_sha256.update(conteudo)
            
            # Retorna o hash em formato hexadecimal
            return hash_sha256.hexdigest()
    except FileNotFoundError:
        return "Arquivo não encontrado!"


# Nome do arquivo que será transformado em hash
nome_arquivo = 'texto.txt'

# Gera e exibe o hash do arquivo
hash_resultado = gerar_hash_arquivo(nome_arquivo)
print(f'O hash do arquivo {nome_arquivo} é: {hash_resultado}')
