import math

# Definir las variables
a = 10
b = 15
v1 = [5, 3]
v2 = [6, 8]

# Sumar los valores
c = a + b

# Restar los valores
d = a - b

# Multiplicar los valores
e = a * b

# Dividir los valores
f = a / b

# Elevar al cuadrado los valores
g = a**2
h = b**2

# Calcular la raíz cuadrada de los valores
i = a**0.5
j = b**0.5

# Calcular el módulo
m = a % b

# Calcular el promedio
p = (a + b) / 2

# Calcular el factorial
f1 = 1
for x in range(1, a+1):
  f1 = f1 * x
  
f2 = 1
for x in range(1, b+1):
  f2 = f2 * x

# Calcular el área del círculo
def area_circulo(radio):
  return 3.1416 * (radio ** 2)

# Calcular el área del cuadrado
def area_cuadrado(lado):
  return lado ** 2

# Calcular el perímetro de una circunferencia
def perimetro_circunferencia(radio):
  return 2 * 3.1416 * radio

# Calcular el área de un triángulo
def area_triangulo(base, altura):
  return (base * altura) / 2

# Calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
  return 3.1416 * (radio ** 2) * altura

# Mostramos el resultado
print("La suma es", c)
print("La resta es", d)
print("La multiplicación es", e)
print("La división es", f)
print("El cuadrado de", a, "es", g, "y el de", b, "es", h)
print("La raíz cuadrada de", a, "es", i, "y la de", b, "es", j)
print("El módulo es", m)
print("El promedio es", p)
print("El factorial de", a, "es", f1, "y el de", b, "es", f2)
print("El área del círculo es", area_circulo(a))
print("El área del cuadrado es", area_cuadrado(b))
print("El perímetro de la circunferencia es", perimetro_circunferencia(a))
print("El área del triángulo es", area_triangulo(a,b))
print("El volumen del cilindro es", volumen_cilindro(a,b))