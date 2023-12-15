"""

    Autor: Carlos Henrique Alves Souto/Leonardo Becker de Oliveira
    Contato: carloshasouto@gmail.com
    Última atualização: 14/12/2023
    Link para o repositório: https://github.com/CarlosASouto/IC-Transportes

"""

import os
import subprocess
import sys

# Concatena os videos de uma viagem
def concatenaVideos(viagens, diretorioCard, diretorioVideosConcatenados, condutor, condutores):
    playlist_file = 'playlist.txt'
    for viagem in viagens:
        with open(playlist_file, 'w') as pFile:
            for video in viagem.elementos:
                pFile.write(f"file '{diretorioCard}/{video}'\n")
        if condutor == "./":
            for driver in condutores:
                separado = driver.split(' ')
                codigo = separado[1]
                nomeVideo = f'{diretorioVideosConcatenados}/Viagem{codigo}{viagem.index}-{viagem.nome}-{viagem.categoria}.mp4'         
        else:    
            nomeVideo = f'{diretorioVideosConcatenados}/Viagem{condutor}{viagem.index}-{viagem.nome}-{viagem.categoria}.mp4'
        command = ['ffmpeg', '-f', 'concat', '-safe', '0',
                   '-i', playlist_file, '-c', 'copy', nomeVideo]
        
        # Se na chamada do programa for passado "0" como argumento, não é feita a concatenação dos vídeos
        try:
            if(sys.argv[2]!="0"):
                subprocess.run(command)
        except:
            subprocess.run(command)
        os.remove(playlist_file)

    pFile.close()
