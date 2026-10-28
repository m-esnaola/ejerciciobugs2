"""
MÓDULO: Entornos de Desarrollo (1DM3)
RETO 3: Depuración de Código en VS Code
EJERCICIO: Sistema de Gestión de Notas (gestion_notas.py)

"""

def fn_CalcularMediaPonderada_fl(notas_lst, pesos_lst):
    """
    Calcula la nota media ponderada de un alumno.
    Cada nota se multiplica por su peso (los pesos suman 1.0).
    """
    suma_fl = 0.0
    i = 0

    while i < len(pesos_lst):
        suma_fl += notas_lst[i] * pesos_lst[i]
        i += 1

    media_fl = suma_fl / len(notas_lst)

    return media_fl

def fn_ContarAprobados_int(notas_lst, nota_corte_fl=5.0):
    """
    Cuenta cuántos alumnos han aprobado.
    Se aprueba con una nota igual o superior a la nota de corte.
    """
    aprobados_int = 0

    for nota_fl in notas_lst:
        if nota_fl > nota_corte_fl:
            aprobados_int += 1

    return aprobados_int

def fn_ObtenerNotaMinima_fl(notas_lst):
    """
    Devuelve la nota más baja de la clase.
    """
    minima_fl = 0

    for nota_fl in notas_lst:
        if nota_fl < minima_fl:
            minima_fl = nota_fl

    return minima_fl

def fn_ObtenerNotaMaxima_fl(notas_lst):
    """
    Devuelve la nota más alta de la clase.
    """
    maxima_fl = notas_lst[0]

    for nota_fl in notas_lst:
        if nota_fl > maxima_fl:
            maxima_fl = nota_fl

    return maxima_fl

def fn_ClasificarCalificacion_str(nota_fl):
    """
    Devuelve la calificación en texto según la nota:
    - >= 9: SOBRESALIENTE
    - >= 7: NOTABLE
    - >= 6: BIEN
    - >= 5: SUFICIENTE
    - < 5: INSUFICIENTE
    """
    if nota_fl >= 9:
        calificacion_str = "SOBRESALIENTE"
    elif nota_fl >= 7:
        calificacion_str = "NOTABLE"
    elif nota_fl >= 6:
        calificacion_str = "BIEN"
    elif nota_fl >= 5:
        calificacion_str = "SUFICIENTE"
    else:
        calificacion_str = "INSUFICIENTE"

    return calificacion_str

def main():
    print("=== SISTEMA DE GESTIÓN DE NOTAS - MÓDULO 1DM3 ===")

    # Datos de prueba
    notas_clase_lst = [7.5, 5.0, 8.0, 4.5, 9.0, 5.0, 6.0]
    notas_alumno_lst = [6.0, 8.0, 7.0]
    pesos_lst = [0.25, 0.25, 0.50]
    nota_corte_fl = 5.0

    print("\n1. Calculando la media ponderada del alumno...")
    media_fl = fn_CalcularMediaPonderada_fl(notas_alumno_lst, pesos_lst)
    calificacion_str = fn_ClasificarCalificacion_str(media_fl)
    print(f"   Media ponderada: {media_fl:.2f} -> {calificacion_str}")

    print("\n2. Estadísticas de la clase...")
    aprobados_int = fn_ContarAprobados_int(notas_clase_lst, nota_corte_fl)
    porcentaje_fl = aprobados_int / len(notas_clase_lst) * 100
    print(f"   Aprobados: {aprobados_int} de {len(notas_clase_lst)} ({porcentaje_fl:.2f}%)")

    minima_fl = fn_ObtenerNotaMinima_fl(notas_clase_lst)
    maxima_fl = fn_ObtenerNotaMaxima_fl(notas_clase_lst)
    print(f"   Nota mínima: {minima_fl:.2f}")
    print(f"   Nota máxima: {maxima_fl:.2f}")

if __name__ == "__main__":
    main()
