def calcular_promedio_ponderado(notas, ponderaciones):
  """Calcular el promedio ponderado de notas."""
  if not notas or not ponderaciones or len(notas) != len(ponderaciones):
    return 0
  suma_ponderada = sum([nota * ponderacion for nota, ponderacion in zip(notas, ponderaciones)])
  suma_ponderaciones = sum(ponderaciones)
  return suma_ponderada / suma_ponderaciones

notas = []
ponderaciones = []
for i in range(5):
  nota = float(input(f"Ingrese la nota {i+1}: "))
  ponderacion = float(input(f"Ingrese la ponderación para la nota {i+1}: "))
  notas.append(nota)
  ponderaciones.append(ponderacion)

promedio_ponderado = calcular_promedio_ponderado(notas, ponderaciones)
print(f"El promedio ponderado de las 5 notas es: {promedio_ponderado}")

if promedio_ponderado >= 3.0:
  print("El estudiante ha aprobado.")
else:
  print("El estudiante ha reprobado.")