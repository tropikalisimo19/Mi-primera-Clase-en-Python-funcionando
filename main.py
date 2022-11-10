#Clase
class Fraction():
    ##ATRIBUTOS##
    numerator = 0
    denominator = 0
    ##Fin Atributos##

    ##CONSTRUCTOR##
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    ##FIN CONSTRUCTOR##

    ##Metodos##
    def multiplication(self,other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        print("\nLa multiplicación es:",numerator,"/",denominator)

    def division(self,other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        print("\nLa division es:",numerator,"/",denominator)

    def addition(self,other):
        if(self.denominator != other.denominator):
            denominator = self.denominator * other.denominator
            numerator = (self.numerator*other.denominator)+(other.numerator*self.denominator)
            print("\nLa suma es:",numerator,"/",denominator)
        else:
            numerator = self.numerator + other.numerator
            print("\nLa suma es:",numerator,"/",self.denominator)

    def subtraction(self,other):
        if(self.denominator != other.denominator):
            denominator = self.denominator * other.denominator
            numerator = (self.numerator*other.denominator)-(other.numerator*self.denominator)
            print("\nLa resta es:",numerator,"/",denominator)
        else:
            numerator = self.numerator - other.numerator
            print("\nLa resta es:",numerator,"/",self.denominator)


    ##INICIALIZAR VARIABLES##
numerator_1 = 0
numerator_2 = 0
denominator_1 = 0
denominator_2 = 0
f_1 = 0
f_2 = 0
opcion = 0
    ##ENTRADA DE DATOS##
numerator_1 = int(input("Numerador fraccion A: "))
int(input(denominator_1 == 0):
    denominator_1 = int(input("Denomiandor fraccion A: "))
    int(input(denominator_1!=0):
        break
    print("Ingresar otro dato que no sea 0")
numerator_2 = int(input("Numerador fraccion B: "))
int(input(denominator_2 == 0):
    denominator_2 = int(input("Denominador fraccion B: "))
    int(input(denominator_2!=0):
        break
    print("Ingresar otro dato que no sea 0")

f_1 = Fraction(numerator_1, denominator_1)
print("Fraccion A =",f_1.numerator,"/",f_1.denominator)
f_2 = Fraction(numerator_2, denominator_2)
print("Fraccion B =",f_2.numerator,"/",f_2.denominator)

        ##MOSTRAR EN PANTALLA##
print("\n========FRACCIONES MATEMATICAS========\n")
print("Si es suma seleccione la opción: (+)")
print("Si es resta seleccione la opción:(-)")
print("Si es multiplicacion seleccione la opción:(*)")
print("Si es division seleccione la opción:(/)\n")
print("===============================================\n")
opcion = input("Ingrese su opción (+ - * /):")

