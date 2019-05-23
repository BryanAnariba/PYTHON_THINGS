#las funciones es como divide y venceras ya que uno divide codigo y puede enviar y devolver valores como no
#puede tener parametros o argumentos y se les denomina metodos a las funciones siempre y cuando este en 
#una clase


#funcion que no recibe parametros ejemplo un hola mundo
import math

def funcion_dev_hola():
    print("Hola Mundo")

def operaciones_basicas(numero1 , numero2):
    suma = float(numero1 + numero2)
    resta = float(numero1 - numero2)
    multiplicacion = float(numero1 * numero2)
    division = float(numero1 / numero2)
    modulo = float(numero1 % numero2)
    print("La suma es: ",suma)
    print("La resta es: ",resta)
    print("La multiplicacion es: ",multiplicacion)
    print("La division es: ",division)
    print("El modulo es: ",modulo)

def funcion_cuadratica(a,b,c):
    delta = float(b*b - 4*a*c)
    if(delta >= 0):
        x1 = float((-1*b + delta)/2*a)
        x2 = float((-1*b - delta)/2*a)
        print("El primer valor para X es: ",x1)
        print("El segundo valor para X es: ",x2)
    else:
        print("Lo siento son raices imaginarias")

def funcion_que_retorna(numero):
    valor = float(math.sqrt(numero))
    return valor


#llamando a la funcion que no recibe parametros solo devuelve hola mundo
funcion_dev_hola()
numero1 = float(input("Digite el Primer numero: "))
numero2 = float(input("Digite el segundo numero: "))
#llamando a la funcion que recibe 2 numeros como parametros1
operaciones_basicas(numero1 , numero2)
#llamando a la funcion_cuadratica que genera los dos valores de x
a = float(input("Digite el valor que acompaña al termino cuadratico: "))
b = float(input("Digite el valor que acompaña el termino lineal: "))
c = float(input("Digite el valor que acompaña el termino independiente: "))
funcion_cuadratica(a,b,c)
#llamando a la funcion_que_Retorna para devolver una raiz
numero = float(input("Digite un valor para sacar su RAIZ. "))
res = funcion_que_retorna(numero)
print(res)
