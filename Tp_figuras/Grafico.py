# Nombre: Marcos
# Apellido: Provenzano
# Division: 112
import pygame
from Funciones import *

#region Colores

colores = {"Blanco" : (255,255,255),
           "Negro" : (0,0,0),
           "Rojo" : (255,0,0),
           "Azul" : (0,0,255),
           "Verde" : (0,255,0),
           "Azul Claro" : (0,150,255)}
#endregion

#region Funciones para completar

def seleccionar_color(mensaje):
    #Desplegar en pantalla todos los colores. El usuario deberá seleccionar uno.
    color_retorno = None
    while color_retorno == None:
        print(f"\n{mensaje}")
        for color in colores:
            print(color)
        color_seleccionado = str(input()).upper()
        for color in colores:
            if color_seleccionado == color.upper():
                color_retorno = colores[color]
    return color_retorno
    
def calcular_figura(figura:dict, ventana):
    perimetro = None
    area = None
    que_figura = figura["figura"]
    
    match que_figura:
        case "Circulo":
            perimetro = calcular_perimetro_circulo(figura["radio"])
            area = calcular_area_circulo(figura["radio"])
            dibujar_circulo(ventana, figura)
        case "Rectangulo":
            perimetro = calcular_perimetro_rectangulo(figura["dimensiones"][0], figura["dimensiones"][1])
            area = calcular_area_rectangulo(figura["dimensiones"][0], figura["dimensiones"][1])
            dibujar_rectangulo(ventana, figura)
        case "Triangulo":
            perimetro = calcular_perimetro_triangulo_rectangulo(figura["dimensiones"][0], figura["dimensiones"][1])
            area = calcular_area_triangulo_rectangulo(figura["dimensiones"][0], figura["dimensiones"][1])            
            dibujar_triangulo(ventana, figura)
    escribir_resultados(ventana, perimetro, area)
#endregion

#region Metodos Graficos    
def graficar(figura):
    pygame.init()

    ventana_ppal = pygame.display.set_mode((1000,850))
    pygame.display.set_caption("FIGURAS")
    imagen = pygame.image.load("Tp_figuras\matematica.jpg")
    imagen = pygame.transform.scale(imagen, (1000,850))
    ventana_ppal.blit(imagen,(0,0))
    calcular_figura(figura, ventana_ppal)

    flag_run = True

    while flag_run:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_run = False
        pygame.display.update()

    pygame.quit()

def dibujar_circulo(ventana, figura):
    print(figura)
    pygame.draw.circle(ventana,figura["color"],figura["posicion"],figura["dimensiones"])

def dibujar_rectangulo(ventana, figura):
    pygame.draw.rect(ventana,figura["color"],(figura["posicion"][0],figura["posicion"][1],figura["dimensiones"][0],figura["dimensiones"][1]))

def dibujar_triangulo(ventana, figura):
    base = figura["dimensiones"][0]
    altura = figura["dimensiones"][1]
    pos_x = figura["posicion"][0]
    pos_y = figura["posicion"][1]
    puntos = [(pos_x,pos_y), (pos_x ,pos_y+altura),(pos_x + base,pos_y+altura)]

    # Dibuja un polígono con los puntos definidos
    pygame.draw.polygon(ventana, figura["color"], puntos)

def escribir_resultados(ventana, perimetro, area):
    perimetro_texto = f"Perimetro: {perimetro} px"
    area_texto = f"Area: {area} px"
    
    fuente = pygame.font.SysFont("consolas",60)
    texto = fuente.render(perimetro_texto, False, colores["Verde"],colores["Azul Claro"])
    ventana.blit(texto,(50,700))
    texto = fuente.render(area_texto, False, colores["Verde"],colores["Azul Claro"])
    ventana.blit(texto,(50,750))
#endregion 