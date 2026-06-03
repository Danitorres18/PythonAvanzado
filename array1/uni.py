a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

suma = [a[i] + b[i] for i in range(len(a))]
resta = [b[i] - a[i] for i in range(len(a))]
multiplicacion = [a[i] * b[i] for i in range(len(a))]

print("Suma:          ", suma)
print("Resta:         ", resta)
print("Multiplicación:", multiplicacion)

print("Promedio:", sum(a) / len(a))
print("Máximo:  ", max(a))
print("Mínimo:  ", min(a))