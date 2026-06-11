
import pulp

# 1. Definir el problema (Maxmimizar)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("blade", cat='Integer')
x2 = pulp.LpVariable("rack", lowBound=2,  cat='Integer')

# 3. Función Objetivo
model += 10000 * x1 + 25000 * x2, "Eps"

# 4. Restricciones
model += 2*x1 + 5*x2 <=45, "Energía"
model += x1 + 3*x2 <=24, "Bahías"
model += 1500*x1 + 4000*x2 <=30000, "dinero"


# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"blade estándar: {x1.varValue}")
print(f"Rack pro: {x2.varValue}")
print(f"Ep maximo: {pulp.value(model.objective)}")

#source .venv/bin/activate