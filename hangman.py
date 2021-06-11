from random import randint
import os

def run():
    with open("./archivos/data.txt", "r", encoding= "utf-8") as f:
        contador = 0
        palabras = []
        for line in f:
            palabras.append(line.rstrip())
            contador +=1
        
        numero =  randint(0, contador-1)
        palabra = palabras[numero]
        palabra = list(palabra)
       
     
     
    os.system("cls")
    print("Empieza el juego")
    #print(palabra)
    palabra_actual = list("_" * len(palabra))
    cant_barraspiso = len(palabra_actual)
    print(palabra_actual)
    while cant_barraspiso > 0: #Mientras la cantidad de "_" sea mayor a 0 ejecutese
        letra = input("Adivina la palabra: ")
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_actual[i] = letra
                cant_barraspiso -= 1
            
        print(palabra_actual)
       

if __name__ == "__main__":
    run()