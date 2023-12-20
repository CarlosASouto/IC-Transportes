"""

    Autor: Carlos Henrique Alves Souto/Leonardo Becker de Oliveira
    Contato: carloshasouto@gmail.com
    Última atualização: 19/12/2023
    Link para o repositório: https://github.com/CarlosASouto/IC-Transportes

"""

import os

# Deixa todas as linhas da tabela com exatamente 1 segundo de diferença
def corrigeTabela(matriz):
    novaMatriz = []
    for i in range(len(matriz)):
        if (i > 0):
            timeAtual = matriz[i][0]
            timeAnterior = matriz[i-1][0]

            diffSegundos = abs(timeAtual-timeAnterior)
            if (diffSegundos == 1):
                novaMatriz.append(matriz[i])
            else:
                for j in range(diffSegundos):
                    novaMatriz.append((timeAnterior+j+1,)+matriz[i][1:])

            # Não é necessário comando para quando a diferença entre time é 0, não sendo necessário inserções
        # Primeira iteração
        else:
            novaMatriz.append(matriz[i])
    return novaMatriz



# Caso diretório não exista, cria o mesmo, caso contrario limpa o diretório
def limpaDiretorio(diretorio):
    if not os.path.exists(f'{diretorio}'):
        os.makedirs(f'{diretorio}')
    else:
        arquivos = os.listdir(diretorio)
        for i in arquivos:
            os.remove(f'{diretorio}/{i}')

def incrementaCondutor (condutorAtual):
    condutorAtual += 1
    return condutorAtual
