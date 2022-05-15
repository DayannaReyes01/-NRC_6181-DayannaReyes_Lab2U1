#Calcular el area de un triangulo equilatero
#Se declara las variables Base y Altura
base=float(input("Ingrese la base del triangulo: ")) #Se pide ingresar los datos pedidos en el programa
altura=float(input("Ingrese la altura del triangulo: "))
#Funcion para calcular el area del triangulo
def Areatriangulo():
    #Formula para calcular el area
  Area=base*altura/2
  print("El area del triangulo equilatero es: ", Area)
  #Se retorna el area
  return Area
  #Se llama a la funcion
Areatriangulo() 