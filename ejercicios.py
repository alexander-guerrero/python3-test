
class Ejercicios():

    # Ejercicio 1
    # Escriba un programa que reciba como entrada dos números, y los muestre
    # ordenados de menor a mayor
    def ordenaNumeros(self, num1, num2):
        if num1 < num2:
            print(str(num1) + ', ' + str(num2))
        else:
            print(str(num2) + ', ' + str(num1))
    
    # Ejercicio 2
    # Escriba un programa que determine si un caracter ingresado es letra, número, o
    # ninguno de los dos. En caso que sea letra, determine si es mayúscula o
    # minúscula.
    def determinaCaracter(self, caracter):
        try:
            int(caracter)
            print('Es numero')
        except:
            if caracter.isupper():
                print('Es letra mayuscula')
            else:
                print('Es letra minuscula')
    
    # Ejercicio 3
    # Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número
    # ingresado por el usuario
    def tablaMultiplicar(self, num):
        for i in range(10):
            print(str(num) + 'x' + str(i+1) + '=' + str(num*(i+1)))

    # Ejercicio 4
    # Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta
    # la ingresada por el usuario
    def potencias(self, num):
        i = 0
        while i <= num:
            print('2^' + str(i) + '=' + str(pow(2, i)))
            i+=1

ej01 = Ejercicios()
ej01.ordenaNumeros(7, 3)

ej02 = Ejercicios()
ej02.determinaCaracter('13424A')

ej03 = Ejercicios()
ej03.tablaMultiplicar(5)

ej04 = Ejercicios()
ej04.potencias(5)