from scipy.optimize import minimize

D = 10000   # Demanda anual
S = 150     # Costo de ordenar
H = 3       # Costo de mantener por unidad al año

def costo_total(v):
    Q = v[0]
    return (D/Q)*S + (Q/2)*H

limites = [(1, None)]  # Q debe ser mayor a 0
iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    print(f"Iteración {iteracion[0]}: Q={v[0]:.4f}, costo={costo_total(v):.4f}")

resultado = minimize(costo_total, x0=[1], method='L-BFGS-B', callback=mostrar_avance, bounds=limites)
print("\nResultado final: Q* =", resultado.x[0], " Costo mínimo =", resultado.fun)