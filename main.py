import random

sustantivos = ["manu", "jose", "julián", "pedro", "ana"]

sustantivosImpro = ["niña", "casa", "carro", "pelota", "perro", "gato", "abeja", "payaso", "manzana", "cuchillo"]

verbos= ["come","corre","salta","juega","baila","toma","estudia","lee","llora","programa", "pela"]

adjetivos= ["dulce", "cansado", "amargo", "divertido", "amable", "bueno", "malo", "fuerte", "débil", "grande", "verde"]

artD = ["el", "los", "la", "las"]

artInd = ["un", "uno", "una", "unas"]

conectores = ["con", "y"]

def tipo0(palabras):
    #verificacion
    #Art + SustantivosImp 
    if (artD.__contains__(palabras[0].lower()) or artInd.__contains__(palabras[0].lower())) and sustantivosImpro.__contains__(palabras[1]):
        return True
    else:
        return False

def tipo1(palabras):
    #verificacion
    #Sustantivos + Verbo
    if (sustantivos.__contains__(palabras[0].lower()) and verbos.__contains__(palabras[1].lower())):
        return True
    else:
        return False


def tipo2(palabras):
    #verificacion
    #ArtD/artInd + SustativoImp + Verbo
    if (artD.__contains__(palabras[0].lower()) or artInd.__contains__(palabras[0].lower())) and sustantivosImpro.__contains__(palabras[1].lower()) and (verbos.__contains__(palabras[2].lower()) or adjetivos.__contains__(palabras[2])): 
        return True
    else:
        return False

def tipo3(palabras):
    #Verificación:
    #ArtD/artInd + SustativoImp + adjetivo + Verbo
    if (artD.__contains__(palabras[0].lower()) or artInd.__contains__(palabras[0].lower())) and sustantivosImpro.__contains__(palabras[1].lower()):
        if adjetivos.__contains__(palabras[2].lower()) and verbos.__contains__(palabras[3].lower()):
            return True
        else:
            return False
    else:
        return False



def posConector(listaPalabras):
    conector = 0
    for i in range(len(listaPalabras)):
        if conectores.__contains__(listaPalabras[i]) or artInd.__contains__(listaPalabras[i]):
            break
        conector+= 1

    if conector == len(listaPalabras) or conector < 1:
        conector = -1

    return conector

def tipo4(palabras):
    conector = posConector(palabras)
    validaciones = []
    if conector != (-1):
        cantidad = len(palabras[:conector])
    else:
        cantidad = len(palabras)

    if conector != (-1):
        if cantidad == 2 and tipo0(palabras[:conector]):
            validaciones.append(True)
            tipo4(palabras[conector:])
        elif cantidad == 2 and tipo1(palabras[:conector]):
            validaciones.append(True)
            tipo4(palabras[conector:])
        elif cantidad == 3 and tipo2(palabras[:conector]):
            validaciones.append(True)
            tipo4(palabras[conector:])
        elif cantidad == 4 and tipo3(palabras[:conector]):
            validaciones.append(True)
            tipo4(palabras[conector:])
        else:
            validaciones.append(False)
    else:
        if cantidad == 2 and tipo0(palabras):
            validaciones.append(True)
        elif cantidad == 2 and tipo1(palabras):
            validaciones.append(True)
        elif cantidad == 3 and tipo2(palabras):
            validaciones.append(True)
        elif cantidad == 4 and tipo3(palabras):
             validaciones.append(True)
        else:
            validaciones.append(False)
        
    if validaciones.__contains__(False):
        return False
    else:
        return True


def validar(frase):
    if frase:
        print("Frase válida \n")
    else:
        print("Frase inválida \n")

def main():
    while True:
        oracion = input("Ingrese la frase a validar \n")
        lista = oracion.split(" ")
        palabrasOracion = len(lista)
        checked = False

        if oracion != "0":
            if palabrasOracion < 2:
                print("Ingrese más palabras")
            elif palabrasOracion == 2:
                pal = tipo1(lista)
                if not pal:
                    pal = tipo0(lista)
                validar(pal)
            elif palabrasOracion == 3:
                pal = tipo2(lista)
                validar(pal)
            elif palabrasOracion == 4:
                pal = tipo3(lista)
                validar(pal)
            elif palabrasOracion > 4:
                pal = tipo4(lista)
                validar(pal)
            else:
                print("caso no encontrado")
        else:
            break

main()

