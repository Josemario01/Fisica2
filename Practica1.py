# Programa que calcula la fuerza eléctrica entre dos cargas puntuales
# Q1 está en el origen (0, 0)
# Q2 puede ubicarse en cualquier punto del plano cartesiano
# Se grafica el vector de fuerza sobre Q2

import math
import matplotlib.pyplot as plt

def graficar_vector_fuerza(x2, y2, fx, fy, q1, q2):
    plt.figure(figsize=(6, 6))
    plt.quiver(x2, y2, fx, fy, angles='xy', scale_units='xy', scale=1, color='g', label='Fuerza sobre Q2')
    plt.plot(0, 0, 'ro' if q1 > 0 else 'bo', label='Q1 (origen)')
    plt.plot(x2, y2, 'ro' if q2 > 0 else 'bo', label='Q2 (posición variable)')
    plt.xlim(min(-10, x2 - 2), max(10, x2 + 2))
    plt.ylim(min(-10, y2 - 2), max(10, y2 + 2))
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Fuerza Eléctrica sobre Q2')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()

def calcular_fuerza_electrica(q1, q2, x2, y2):
    k = 9 * 10**9  # Constante eléctrica (N·m²/C²)
    distancia = math.sqrt(x2**2 + y2**2)

    if distancia == 0:
        raise ValueError("Las cargas no pueden estar en la misma posición.")

    # Cálculo de la fuerza
    fuerza_magnitud = k * q1 * q2 / distancia**2
    fx = fuerza_magnitud * (x2 / distancia)
    fy = fuerza_magnitud * (y2 / distancia)

    print(f"\nVector de Fuerza sobre Q2 ubicada en ({x2}, {y2}):")
    print(f"Fx = {fx:.4e} N")
    print(f"Fy = {fy:.4e} N")

    graficar_vector_fuerza(x2, y2, fx, fy, q1, q2)

# ========= PROGRAMA PRINCIPAL =========

print("==== CÁLCULO DE FUERZA ELÉCTRICA ENTRE DOS CARGAS PUNTUALES ====\n")
try:
    q1 = float(input("Ingrese el valor de la carga Q1 (en Coulombs): "))
    q2 = float(input("Ingrese el valor de la carga Q2 (en Coulombs): "))
    x2 = float(input("Ingrese la coordenada X de la carga Q2 (en metros): "))
    y2 = float(input("Ingrese la coordenada Y de la carga Q2 (en metros): "))

    calcular_fuerza_electrica(q1, q2, x2, y2)

except ValueError as e:
    print(f"Error: {e}")
