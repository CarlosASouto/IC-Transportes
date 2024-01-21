"""

    Autor: Carlos Henrique Alves Souto/Leonardo Becker de Oliveira
    Contato: carloshasouto@gmail.com
    Última atualização: 21/01/2024
    Link para o repositório: https://github.com/CarlosASouto/IC-Transportes

"""

import sys
import os
from local_libs import cards as cd
from local_libs import geraPlanilha as gp
from local_libs import utils
from local_libs import juntaVideo as jv
from local_libs import viagem as vg
from local_libs import constants as ct
from local_libs import criaBanco



# Entrada do condutor por argumento
try:
    condutor = sys.argv[1]
except:
    print("Condutor não informado!")
    print("Informe o condutor como argumento: ")
    print("> python3 processaDados.py 'codigo do condutor' ")
    sys.exit()

# Leitura dos cards e seus respectivos videos

condutores = condutor
totalCards = cd.obtemCards("./Driver "+condutor)

limparBanco = 1
indexInicial = 1
# Para cada Card obtido na leitura inicial é necessário gerar os arquivos de GPS e os videos concatenados
for card in totalCards:
    viagensBack = None
    viagensFront = None

    try:
        with open(card.diretorioGps, 'r') as arquivo:
            conteudoGPS = arquivo.readlines()
        arquivo.close()
    except:
        print("Erro ao abrir arquivo GPS")
        print("Lembrando que o arquivo de GPS deve estar dentro de cada Card")
        sys.exit()

    viagensBack = vg.preencheViagens(card.videosBack, "Back", indexInicial)
    viagensFront = vg.preencheViagens(card.videosFront, "Front", indexInicial)

    # Cria um banco contendo as informações de todos os cards ( formato arquivo txt )
    criaBanco.newBanco(conteudoGPS, card.nomeCard, limparBanco)
    limparBanco = 0

    # Criação e limpeza do diretorio GPS
    diretorioGPSConcatenado = f'{card.diretorio}/{ct.pastaArquivosGPS}'
    utils.limpaDiretorio(diretorioGPSConcatenado)

    # Gera os arquivos CSV que contém os dados das viagens com vídeo
    gp.geraPlanilhasOficial(viagensBack,condutor, condutores,
                                diretorioGPSConcatenado, indexInicial)

    # Gera o arquivo CSV que contém os dados das viagens sem vídeo
    gp.geraSemVideoCSV(viagensBack, condutor, diretorioGPSConcatenado)

    # Criação e limpeza do diretorio de videos concatenados
    diretorioVideosConcatenados = f'{card.diretorio}/{ct.pastaVideosConcatenados}'
    utils.limpaDiretorio(diretorioVideosConcatenados)

    # Concatena os vídeos
    if viagensBack:
        jv.concatenaVideos(viagensBack, card.diretorioBack,
                        diretorioVideosConcatenados, condutor, condutores)
        jv.concatenaVideos(viagensFront, card.diretorioFront,
                            diretorioVideosConcatenados, condutor, condutores)

    # Atualiza o indexInicial para o próximo Card, Card2 sequência do Card1 no número de viagem
    indexInicial = len(viagensBack)+1

    card.printParametros()
