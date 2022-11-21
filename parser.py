import time

Color_Off="\033[0m"       # Color reset
BGreen="\033[1;32m"       # Green
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green

class oraciones:
    
    sustantivos = ["manu", "jose", "julián", "pedro", "ana", "juan"]
    sustantivosImpro = ["niña", "casa", "carro", "pelota", "perro", "gato", "abeja", "payaso", "manzana", "cuchillo"]
    verbos= ["come","corre","salta","juega","baila","toma","estudia","lee","llora","programa", "pela"]
    adjetivos= ["dulce", "valiente", "brillante", "agradable", "amable", "bueno", "azul", "fuerte", "débil", "grande", "verde", "rapido"]
    artD = ["el", "los", "la", "las"]
    artInd = ["un", "uno", "una", "unas"]
    conectores = ["con", "y", "un", "una"]

    listaPalabras = None
    recorrido = 0

    def __init__(self, oracion):
        self.listaPalabras = oracion.split(" ")
    
    def comprobarOracion(self):
        verb = False

        for i in range(len(self.listaPalabras)):
            if self.verbos.__contains__(self.listaPalabras[i]):
                verb = True
                break

        if verb:
            try:
                self.verificador(self.listaPalabras)
            except:
                print("Oops algo inesperado ha sucedido, intenta nuevamente")
        else:
            self.imprimirValidacion(False)

    def verificador(self, listaPalabras):
        if self.tipo2(listaPalabras):
            self.imprimirValidacion(True)
        elif self.tipo5(listaPalabras):
            self.imprimirValidacion(True)
        elif self.tipo6(listaPalabras):
            self.imprimirValidacion(True)
        elif self.tipo8(listaPalabras):
            self.imprimirValidacion(True)
        elif self.variaciones(listaPalabras):
            self.imprimirValidacion(True)
        else:
            self.imprimirValidacion(False)
            
    def imprimirValidacion(self, cond):
        if cond:
            print(Green, "Frase válida\n", Color_Off)
        else:
            print(Red, "Frase inválida\n", Color_Off)


    #Verbos
    def tipo0(self, listaPalabras):
        if len(listaPalabras) == 1:
            if(self.verbos.__contains__(listaPalabras[0].lower())):
                return True
            else:
                return False
        else:
            return False

    #Adjetivos
    def tipo00(self, listaPalabras):
        if len(listaPalabras) == 1:
            if(self.adjetivos.__contains__(listaPalabras[0].lower())):
                return True
            else:
                return False
        else:
            return False
    #S or SI 
    def tipo1(self, listaPalabras):
        if len(listaPalabras) == 1:
            if(self.sustantivos.__contains__(listaPalabras[0].lower()) or self.sustantivosImpro.__contains__(listaPalabras[0].lower())):
                return True
            else:
                return False
        else:
            return False
    #Sustantivo + verbo
    def tipo2(self, listaPalabras):
        if len(listaPalabras) == 2:
            if(self.sustantivos.__contains__(listaPalabras[0].lower()) and self.verbos.__contains__(listaPalabras[1].lower())):
                return True
            else:
                return False
        else:
            return False

    #ArticuloI/D + SI
    def tipo3(self, listaPalabras):
        if len(listaPalabras) == 2:
            if((self.artD.__contains__(listaPalabras[0].lower()) or self.artInd.__contains__(listaPalabras[0].lower()) ) and self.sustantivosImpro.__contains__(listaPalabras[1].lower())):
                return True
            else:
                return False
        else:
            return False

    #SI + adjetivo 
    def tipo4(self, listaPalabras):
        if len(listaPalabras) == 2:
            if(self.sustantivosImpro.__contains__(listaPalabras[0].lower()) and self.adjetivos.__contains__(listaPalabras[1].lower())):
                return True
            else:
                return False
        else:
            return False

    #Sustantivo + Verbo + adjetivo
    def tipo5(self, listaPalabras):
        if len(listaPalabras) == 3:
            if((self.sustantivos.__contains__(listaPalabras[0].lower()) ) and self.verbos.__contains__(listaPalabras[1].lower()) and self.adjetivos.__contains__(listaPalabras[2].lower())):
                return True
            else:
                return False
        else:
            return False

    #ArticuloI/D + SI + Verbo
    def tipo6(self, listaPalabras):
        if len(listaPalabras) == 3:
            if((self.artD.__contains__(listaPalabras[0].lower()) or self.artInd.__contains__(listaPalabras[0].lower()) ) and self.sustantivosImpro.__contains__(listaPalabras[1].lower()) and self.verbos.__contains__(listaPalabras[2].lower())):
                return True
            else:
                return False
        else:
            return False

    #ArticuloI/D + SI + Adjetivo 
    def tipo7(self, listaPalabras):
        if len(listaPalabras) == 3:
            if((self.artD.__contains__(listaPalabras[0].lower()) or self.artInd.__contains__(listaPalabras[0].lower()) ) and self.sustantivosImpro.__contains__(listaPalabras[1].lower()) and self.adjetivos.__contains__(listaPalabras[2].lower())):
                return True
            else:
                return False
        else:
            return False

    #ArticuloI/D + SI + Adjetivo + Verbo
    def tipo8(self, listaPalabras):
        if len(listaPalabras) == 4:
            if((self.artD.__contains__(listaPalabras[0].lower()) or self.artInd.__contains__(listaPalabras[0].lower()) ) and self.sustantivosImpro.__contains__(listaPalabras[1].lower()) and self.adjetivos.__contains__(listaPalabras[2].lower()) and self.verbos.__contains__(listaPalabras[3].lower())):
                return True
            else:
                return False
        else:
            return False
        
    def variaciones(self, listaPalabras):
        conector = 0   
        menor = []

        if listaPalabras.__contains__(self.conectores[0]):
               conector = listaPalabras.index("con")
               menor.append(conector)
        if listaPalabras.__contains__(self.conectores[1]):
               conector = listaPalabras.index("y")
               menor.append(conector)
        if not self.recorrido == 0:
            if listaPalabras.__contains__(self.conectores[2]):
                conector = listaPalabras.index("un")
                menor.append(conector)
            if listaPalabras.__contains__(self.conectores[3]):
                    conector = listaPalabras.index("una")
                    menor.append(conector)
        else:
            tempList = listaPalabras[1:]
            if tempList.__contains__(self.conectores[2]):
                conector = tempList.index("un")+1
                menor.append(conector)
            if tempList.__contains__(self.conectores[3]):
                    conector = tempList.index("una")+1
                    menor.append(conector)

        if len(menor)>=1:
            menor.sort()
            conector = menor[0]
        
        self.recorrido += 1

        if conector >= 1:
            if self.tipo1(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            elif self.tipo2(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            elif self.tipo3(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            elif self.tipo4(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            elif self.tipo5(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            elif self.tipo6(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            elif self.tipo7(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            elif self.tipo8(listaPalabras[:conector]) and self.variaciones(listaPalabras[conector+1:]):
                return True
            else: 
                return False
        else:
            if self.tipo0(listaPalabras):
                return True
            elif self.tipo00(listaPalabras):
                return True
            elif self.tipo1(listaPalabras):
                return True
            elif self.tipo2(listaPalabras):
                return True
            elif self.tipo3(listaPalabras):
                return True
            elif self.tipo4(listaPalabras):
                return True
            elif self.tipo5(listaPalabras):
                return True
            elif self.tipo6(listaPalabras):
                return True
            elif self.tipo7(listaPalabras):
                return True
            elif self.tipo8(listaPalabras):
                return True
            else: 
                return False
            
       

def main():

    print(BGreen, "\n ------ANALIZADOR SINTÁCTICO------ \n\n")
    print(BWhite,"\tREALIZADO POR:\n")
    print(BCyan,"\tJOSÉ TORDECILLA")
    print(BCyan,"\tMANUELA CASTAÑO\n\n", Color_Off)

    print("*** Para terminar el programa escriba '0' en la consola")
    time.sleep(5)

    oracion = input(BWhite + "Ingrese la frase a validar \n" + Color_Off)
    while oracion != "0":
        oracionValidar = oraciones(oracion)
        oracionValidar.comprobarOracion()
        oracionValidar.recorrido = 0
        oracion = input(BWhite + "Ingrese la frase a validar \n" + Color_Off)
        

main()

