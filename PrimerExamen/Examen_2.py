import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("ilustraciones", cat='Integer')
x2 = pulp.LpVariable("íconos", lowBound=0, upBound=8, cat='Integer')

# 3. Función Objetivo
model += 40 * x1 + 20 * x2, "Ganancia Maxima"

# 4. Restricciones
model += 2 * x1 + x2 <= 12, "horas trabajador"
model += x1 + x2 <= 24, "horas servidor"
model += x1 >= 0, "no negativo"
model += x2 >= 0, "no negativo 2"
model += x1 >= 2, "pago inicial"
model += x2 <= 8, "máximo de iconos"

# 5. Resolver y mostrar
model.solve()
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"ilustraciones: {x1.varValue}")
print(f"íconos: {x2.varValue}")
print(f"Ganancia Maxima: ${pulp.value(model.objective)}")
#source .venv/bin/activate