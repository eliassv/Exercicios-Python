'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe
o tempo aproximado de download do arquivo usando este link (em minutos)'''
arquivo = input('Digite o tamano do arquivo: (em Mb)')
arquivo = float(arquivo)
internet = input('Velocidade da internet: (em Mbps)')
internet = float(internet)
temposeg = arquivo / internet
print ('')
print ('O tempo aproximado de download do arquivo {:.2f} Mb é de {:.2f} minutos'.format(arquivo,(temposeg / 60)))
