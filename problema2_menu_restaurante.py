# Fase 5 - Evaluación Final POA
# Curso: Fundamentos de Programación (213022) - UNAD
# Estudiante: Brayan Stick Calderón Rivera
# Problema 2: promoción sobre productos del menú de un restaurante

# Condiciones de la promoción, definidas antes de procesar el menú
CATEGORIA_OBJETIVO = "Plato fuerte"
UMBRAL_PRECIO = 25000          # el precio base debe ser mayor a este valor
PORCENTAJE_DESCUENTO = 0.15    # 15 %

# Matriz del menú: [Nombre del producto, Categoría, Precio base]
menu = [
    ["Bandeja paisa", "Plato fuerte", 32000],
    ["Ajiaco santafereño", "Plato fuerte", 28000],
    ["Sancocho de gallina", "Plato fuerte", 25000],
    ["Arroz con pollo", "Plato fuerte", 22000],
    ["Empanadas x3", "Entrada", 9000],
    ["Patacón con hogao", "Entrada", 12000],
    ["Limonada de coco", "Bebida", 10000],
    ["Jugo de lulo", "Bebida", 7000],
    ["Postre de natas", "Postre", 9500],
]


def calcular_precio_final(categoria, precio_base):
    """Devuelve el precio final del producto.

    Aplica el descuento solo si el producto pertenece a la categoría
    objetivo y su precio base supera el umbral. En otro caso devuelve
    el precio base sin cambios.
    """
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        descuento = precio_base * PORCENTAJE_DESCUENTO
        return precio_base - descuento
    return precio_base


def formato_pesos(valor):
    """Escribe un valor en pesos con punto como separador de miles."""
    return "$" + f"{valor:,.0f}".replace(",", ".")


def mostrar_informe(matriz):
    """Recorre la matriz y muestra precio base y precio final de cada producto."""
    print("PROMOCIÓN DEL MENÚ")
    print(f"Categoría objetivo: {CATEGORIA_OBJETIVO}")
    print(f"Umbral de precio: mayor a {formato_pesos(UMBRAL_PRECIO)}")
    print(f"Descuento: {PORCENTAJE_DESCUENTO * 100:.0f} %")
    print("-" * 72)
    print(f"{'Producto':<22}{'Categoría':<14}"
          f"{'Precio base':>12}{'Precio final':>14}{'Promo':>8}")
    print("-" * 72)

    productos_con_promocion = 0
    for fila in matriz:
        nombre = fila[0]
        categoria = fila[1]
        precio_base = fila[2]
        precio_final = calcular_precio_final(categoria, precio_base)

        if precio_final < precio_base:
            aplica = "Sí"
            productos_con_promocion += 1
        else:
            aplica = "No"

        print(f"{nombre:<22}{categoria:<14}{formato_pesos(precio_base):>12}"
              f"{formato_pesos(precio_final):>14}{aplica:>8}")

    print("-" * 72)
    print(f"Productos con promoción: {productos_con_promocion} de {len(matriz)}")


# Programa principal
mostrar_informe(menu)
