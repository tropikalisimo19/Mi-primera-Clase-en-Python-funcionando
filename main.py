#Clase
class Fraction():
    ##Atributos##
    numerator = 0
    denominator = 0
    ##Fin Atributos##

    ##Constructor##
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    ##Fin Constructor##

    ##Metodos##
    def multiplication(self,other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        print("\nEl resultado de la multiplicacion:",numerator,"/",denominator)

    def division(self,other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        print("\nEl resultado de la division:",numerator,"/",denominator)

    def addition(self,other):
        if(self.denominator != other.denominator):
            denominator = self.denominator * other.denominator
            numerator = (self.numerator*other.denominator)+(other.numerator*self.denominator)
            print("\nEl resultado de la suma:",numerator,"/",denominator)
        else:
            numerator = self.numerator + other.numerator
            print("\nEl resultado de la suma:",numerator,"/",self.denominator)

    def subtraction(self,other):
        if(self.denominator != other.denominator):
            denominator = self.denominator * other.denominator
            numerator = (self.numerator*other.denominator)-(other.numerator*self.denominator)
            print("\nEl resultado de la resta:",numerator,"/",denominator)
        else:
            numerator = self.numerator - other.numerator
            print("\nEl resultado de la resta:",numerator,"/",self.denominator)


#Iniciar variables
numerator_1 = 0
numerator_2 = 0
denominator_1 = 0
denominator_2 = 0
f_1 = 0
f_2 = 0
opcion = 0
#Entrada de datos
numerator_1 = int(input("Numerador fraccion A: "))
while(denominator_1 == 0):
    denominator_1 = int(input("Denomiandor fraccion A: "))
    if(denominator_1!=0):
        break
    print("Ingrese un denominador distinto de 0")
numerator_2 = int(input("Numerador fraccion B: "))
while(denominator_2 == 0):
    denominator_2 = int(input("Denominador fraccion B: "))
    if(denominator_2!=0):
        break
    print("Ingrese un denominador distinto de 0")
#asignar variables
f_1 = Fraction(numerator_1, denominator_1)
print("Fraccion A =",f_1.numerator,"/",f_1.denominator)
f_2 = Fraction(numerator_2, denominator_2)
print("Fraccion B =",f_2.numerator,"/",f_2.denominator)
#Menu
print("\n---------OPERACIONES MATEMATICAS CON FRACCIONES---------\n")
print("SUMA(+)")
print("RESTA(-)")
print("MULTIPLICACION(*)")
print("DIVISION(/)\n")
print("---------------------------------------------------------\n")
opcion = input("Ingrese la operacion a realizar (+ - * /):")

match(opcion):
    case '+':
        f_1.addition(f_2)
    case '-':
        f_1.subtraction(f_2)
    case '*':
        f_1.multiplication(f_2)
    case '/':
        f_1.division(f_2)