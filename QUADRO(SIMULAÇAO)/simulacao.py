import pygame
import numpy as np
import math
##########
pygame.init()
size = (800,600)
tela = pygame.display.set_mode(size)
pygame.display.set_caption("Janela")
fonte = pygame.font.match_font("arial")
preto = (0,0,0)
###############
x1,y1,largura,altura = 150,120,500,350
coordenadas_dentro = (largura * altura)
###############
raio = 3
areaCirculo = math.pi * (raio ** 2)
##############
numDados = 1000
probabilidade = (areaCirculo / coordenadas_dentro) * 100
###########
def texto(texto, tamanho, cor,x,y):
    fonteF = pygame.font.Font(fonte, tamanho)
    texto = fonteF.render(texto, True, cor)
    textoRect = texto.get_rect()
    textoRect = (x,y) # 230 e 50
    tela.blit(texto, textoRect)
    
print(f"I retangulo contem {coordenadas_dentro} coordenadas")

def simularDados():
    coordenadas_x = np.random.uniform(x1,x1 + largura, numDados)
    coordenadas_y = np.random.uniform(y1, y1 + altura, numDados)
    dardos_dentro = ((coordenadas_x <= x1 + largura) & (coordenadas_y <= y1 + altura))
    return coordenadas_x, coordenadas_y, dardos_dentro

executando = True
exibirTexto = False
exibirDados = False
coordenadas_x, coordenadas_y, dardos_dentro = simularDados()

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            coordenadas = pygame.mouse.get_pos()
            exibirTexto = True
            exibirDados = True
            print("Clicou em: ", coordenadas)
            
            
    tela.fill((255,255,255))
    
    pygame.draw.rect(tela, (255,0,0), (x1,y1,largura,altura)) 
    texto("Escolha um ponto no quadro", 32,preto, 230,50)

    if exibirTexto:
        texto("O ponto escolhido foi: " + str(coordenadas), 32,preto,200,500)
    
    if exibirDados:
        for i in range(len(dardos_dentro)):
            if dardos_dentro[i]:
                pygame.draw.circle(tela, (0,0,255), (int(coordenadas_x[i]), int(coordenadas_y[i])),raio)

                if abs(coordenadas_x[i] - coordenadas[0]) < 5 and abs(coordenadas_y[i] - coordenadas[1]) < 5:
                    texto("O dardo acertou o seu ponto!", 32,preto,200,550)
    
    texto("A probabilidade eh: " + str(probabilidade) + "%", 16,preto,0,0)
    pygame.display.flip()      




pygame.quit()    