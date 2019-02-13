#P3 Brute Force
#Autor: Crisamer Ortega Gonzalez 10/1/2019
from Server import Server
from Iterator import Iterator
from itertools import product
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-tol", "--itertool", help="Ejecuta el programa mediante el algoritmo de combinaciones de itertools", action="store_true")
parser.add_argument("-s", "--selfit", help="Ejecuta el programa mediante el algoritmo de combinaciones desarrollado por el grupo de practicas (default)", action="store_true")
parser.add_argument("-m", "--multi", help="Eejecuta ejemplo de calculo de mutiplos", action="store_true")

args = parser.parse_args()

myHost = Server()
myHostTool = Server()


def main():


    if args.multi:
        print("Impresion de todos los numeros multiplos de 5")
        multiplos()
    if args.selfit or args.itertool or not args.multi:
        initServer()
        crackServer()


def initServer():

#/////////////// Anadir pruebas aqui (cuidado con tildes y caracteres raros): ///////////
    if args.selfit or not args.itertool:
        print("Para ejecutar el script con diferentes opciones ejecutar 'python main.py -h' \n")
        print("ATENCION: debido a la baja eficiencia del interprete de python en procesos pesados, las password para el iterador implementado por el grupo se mantienen a 4 caracteres o menos \n")
        myHost.add("Crisamer", "c5is")
        myHost.add("Admin", "roo")
        myHost.add("Maria", "maR")

    if args.itertool:
        myHostTool.add("Crisamer", "c5is")
        myHostTool.add("Admin", "root")
        myHostTool.add("Maria", "maRi4")

#///////////////////////////////////////////////


def crackServer():

    print("Aplicacion de fuerza bruta para hallar  password de usuarios :")

    symbols =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9'];

    #Ejecucion con con iterador implementado por el grupo de practicas
    if args.selfit or not args.itertool:

        found = True
        users = myHost.server.keys()

        for i in users:

            password = Iterator(symbols, len(myHost.server[i]))

            while myHost.server[i] !=  "".join(password.combination):

                try:
                    password.__next__()

                except StopIteration:

                    found = False
                    break

            if found == True :
                print("La password para el usuario %r es %r"%(i,''.join(password.combination)))

            else :
                print("Password no encontrada")


        #Ejecucion con con iterador implementado por funcionalidad itertools
    if args.itertool:

        for i in myHostTool.server.keys():
            password =product(symbols, repeat=len(myHostTool.server[i]))
            found = False

            for j in password:
                if myHostTool.server[i] == "".join(j) :
                    print("La password para el usuario %r es %r"%(i,''.join(j)))
                    found = True
                    break


            if found == False:
                print("pass no encontrada para %r"%(i))

def multiplos():

    num = 5 #<---- Alterar para buscar otro tipo de multiplos
    nums = [0,1,2,3,4,5,6,7,8,9]
    mult=Iterator(nums, 3)

    for i in range (0,999):

        try:
            mult.__next__()
            if int("".join(str(x) for x in mult.combination)) % num == 0 :
                print ("".join(str(x) for x in mult.combination))
        except StopIteration:
            print("Iterador excedido, revise el codigo (precaucion al iterar cifras grandes)")
            break

if __name__ == "__main__" :
    main()
