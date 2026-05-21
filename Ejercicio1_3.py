
import pulp

# 1. Definir el problema (Maxmimizar)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("basico", cat='Integer')
x2 = pulp.LpVariable("profundo", cat='Integer')

# 3. Función Objetivo
model += 2 * x1 + 5 * x2, "seguridad"

# 4. Restricciones
model += x1 + 3*x2 <=18, "Cpu/s"
model += x1 + x2 <=8, "Ram/s"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Armar Tipo A: {x1.varValue}")
print(f"Armar Tipo B: {x2.varValue}")
print(f"Costo Mínimo Diario: ${pulp.value(model.objective)}")

#source .venv/bin/activate