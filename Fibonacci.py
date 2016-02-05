iteraciones = raw_input("Ingrese un numero para las iteraciones de la serie de Fibonacci ")
iteraciones =u""+iteraciones
while iteraciones.isnumeric()== False:
    iteraciones = raw_input("Ingrese un numero para las iteraciones de la serie de Fibonacci ")
    iteraciones =u""+iteraciones;
print iteraciones
salida = ""
actual = 1
anterior = 0
resultado = -0
for num in range(0, int(iteraciones)):
    resultado = actual+anterior
    anterior = actual
    salida=salida + str(resultado)
    if num<int(iteraciones)-1:
        salida=salida+","
    actual = resultado

print "Serie Fibonacci con " + iteraciones + " iteraciones:"
print salida