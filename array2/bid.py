notas = {
        [15,18,17],
        [12,14,16],
        [20,19,18]
        }

print("Matriz de notas:")
for fila in notas:
    print(fila)

print ("\n Todas las notas")
for i in range(len(notas)):
    for j in range (len(notas[1])):
        print(f"Estudiante {i+1}, Curso {j+1}: {notas[i][j]}")

