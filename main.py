##CLASE##
class Fraction():
    ##ATRIBUTOS##
    numerator = 0
    denominator = 1
    ##FIN ATRIBUTOS##

    ##CONSTRUCTOR##
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    ##FIN CONSTRUCTOR##

    ##METODOS##
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
fraction1 = 0
fraction2 = 0
opcion = 0
    ##ENTRADA DE DATOS##
numerator_1 = int(input("Numerador fraccion A: "))
denominator_1 = int(input("Denominador fraccio A:"))
numerator_2 = int(input("Numerador fraccion B: "))
denominator_2 = int(input("Denominador fraccio B:"))

fraction1 = Fraction(numerator_1, denominator_1)
print("Fraccion A =",fraction1.numerator,"/",fraction1.denominator)
fraction2 = Fraction(numerator_2, denominator_2)
print("Fraccion B =",fraction2.numerator,"/",fraction2.denominator)

        ##MOSTRAR EN PANTALLA##
print("\n========FRACCIONES MATEMATICAS========\n")
print("Si es suma seleccione la opción: (+)")
print("Si es resta seleccione la opción:(-)")
print("Si es multiplicacion seleccione la opción:(*)")
print("Si es division seleccione la opción:(/)\n")
print("===============================================\n")
opcion = input("Ingrese su opción (+ - * /):")

if(opcion =='+'):
    fraction1.addition(fraction2)
elif(opcion =='-'):
    fraction1.substraccion(fraction2)
elif(opcion =='*'):
    fraction1.multiplication(fraction2)
elif(opcion =='/'):
    fraction1.division(fraction2)
else:
    print("ingrese un simbolo adecuado")
