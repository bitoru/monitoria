# Prova de Monitoria para Fundamentos da Computacao
# Questao #2
# Aluno: Vitor Fernandes

# le o arquivo com os nomes e medias dos alunos
# retorna as linhas contidas no arquivo
def ler_arquivo_de_medias():
    # abre o arquivo para leitura
    arquivo = open('final.txt', 'r')
    # recupera todas as linhas do arquivo
    linhas = arquivo.readlines()
    # fecha o arquivo para nao consumir memoria apos encerrar o programa
    arquivo.close()
    return linhas

# recebe uma lista de linhas com o formato: "nome,media\n"
# retorna uma lista em que cada item tem o formato de lista: [nome, media]
def separar_nomes_e_medias(linhas):
    # lista que sera retornada
    nomes_e_medias = []
    # loop percorrendo todas as linhas recebidas
    for linha in linhas:
        # caso a linha termine com um caractere de nova linha (\n),
        # remove esse caractere
        # aqui o nome e a media sao separados atraves do split, que
        # utiliza o caractere "," como separador
        nome_e_media = linha.replace('\n', '').split(',')
        # remove espacos em branco em volta do nome do aluno
        nome_e_media[0] = nome_e_media[0].strip()
        # adiciona [nome, media] a lista que sera retornada pela funcao
        nomes_e_medias.append(nome_e_media)
    return nomes_e_medias

# recebe a lista de nomes e medias e ordena
# utilizando o metodo bubble sort
def ordenar_alunos_por_nome(nomes_e_medias):
    j = len(nomes_e_medias)-1
    # percorre toda a lista utilizando o indice "j"
    while j>0:
        # percorre todos os itens ate o indice "j-1"
        for i in range(0,j):
            nome1 = nomes_e_medias[i][0]
            nome2 = nomes_e_medias[i+1][0]
            # compara os nomes dos alunos nas duas posicoes adjacentes
            if nome1 > nome2:
                # caso o nome mais a esquerda venha depois do nome mais a direita (alfabeticamente),
                # troca as posicoes
                nomes_e_medias[i],nomes_e_medias[i+1] = nomes_e_medias[i+1],nomes_e_medias[i]
        j = j-1

# procura pelo nome do aluno (nome_aluno) na lista de nomes e medias (nomes_e_medias)
# utilizando o metodo de busca binaria
# caso o aluno seja encontrado, retorna sua media (em ponto flutuante)
# caso contrario, retorna o valor "None"
# aqui tambem eh utilizada recursao
def procurar_media_aluno_binaria(nomes_e_medias, nome_aluno):
    # caso a lista passada esteja vazia o aluno nao existe
    # sendo assim, retorna None
    if len(nomes_e_medias) == 0:
        return None
    # o indice no meio da lista sera validado
    meio = int(len(nomes_e_medias)/2)
    # aqui eh utilizada a funcao .strip() da string para remover
    # espacos em branco em volta do nome do aluno
    if nomes_e_medias[meio][0] == nome_aluno.strip():
        # caso o nome informado como argumento da funcao seja
        # encontrado, retorna a media do aluno em ponto flutuante
        return float(nomes_e_medias[meio][1])
    else:
        # se o nome no meio da lista nao eh igual ao informado
        # continuar buscando pelo nome
        if nome_aluno.strip() < nomes_e_medias[meio][0]:
            # caso o nome informado venha antes (alfabeticamente) do nome no meio
            # busca pelos itens na primeira metade da lista
            return procurar_media_aluno_binaria(nomes_e_medias[:meio], nome_aluno)
        else:
            # caso o nome informado venha depois (alfabeticamente) do nome no meio
            # busca pelos itens na segunda metade da lista
            return procurar_media_aluno_binaria(nomes_e_medias[meio+1:], nome_aluno)

# le as linhas do arquivo que contem os nomes dos alunos e suas medias
linhas = ler_arquivo_de_medias()
# separa os nomes e medias para facilitar a busca
nomes_e_medias = separar_nomes_e_medias(linhas)
# ordena a lista de nomes e medias
ordenar_alunos_por_nome(nomes_e_medias)
# pede ao usuario que informe um nome de aluno a ser procurado
nome_aluno = input('Digite o nome do aluno para procurar a media: ')
# recupera a media do aluno informado
media_encontrada = procurar_media_aluno_binaria(nomes_e_medias, nome_aluno)

if media_encontrada is None:
    # caso o aluno nao seja encontrado, o valor da
    # variavel media_encontrada sera "None"
    print('Aluno', nome_aluno, 'nao encontrado')
else:
    # caso o aluno seja encontrado, imprime sua media
    # com duas casas decimais
    media = '{:0.2f}'.format(media_encontrada)
    print('Nome', nome_aluno, 'tem media', media)
