import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Personaje", lowBound=0, upBound=40, cat='Integer')
x2 = pulp.LpVariable("Escenario", lowBound=0, upBound=30, cat='Integer')

# 3. Función Objetivo
model += 80 * x1 + 60 * x2, "Costo_Total"

# 4. Restricciones
model += 2 * x1 + 1 * x2 <= 12, "GPU_Horas"
model += 1 * x1 + 2 * x2 <= 14, "VRAM_GB"

# 5. Resolver y mostrar
model.solve()
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Personaje: {x1.varValue}")
print(f"Escenario: {x2.varValue}")
print(f"Ganancia Maxima: ${pulp.value(model.objective)}")
#source .venv/bin/activate