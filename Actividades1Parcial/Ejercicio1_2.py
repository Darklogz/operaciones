
import pulp

# 1. Definir el problema (Maxmimizar)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Esritorio", cat='Integer')
x2 = pulp.LpVariable("Laptop", cat='Integer')

# 3. Función Objetivo
model += 2000 * x1 + 4000 * x2, "Ganancia"

# 4. Restricciones
model += x1 + x2 <=60, "Maximo procesadores"
model += x1 + 3*x2 <=100, "Maximo tiempo"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Armar Escritorio: {x1.varValue}")
print(f"Armar Laptop: {x2.varValue}")
print(f"Costo Mínimo Diario: ${pulp.value(model.objective)}")

#source .venv/bin/activate
