# ============================================================
# Portada
# ============================================================
# Nombre: Saul Eduardo Mireles Reyna
# Matrícula: 2630171
# Grupo: IM-1-3
# ============================================================
# Resumen ejecutivo
# ============================================================
# En esta práctica se usan listas y tuplas para guardar y trabajar
# con datos. En el primer problema se manejan productos de una lista
# de compras y en el segundo se guardan coordenadas para calcular
# la distancia entre dos puntos. Las entradas se revisan para evitar
# que el programa trabaje con datos vacíos o con números incorrectos.

# ============================================================
# Principios y buenas prácticas
# ============================================================
# - Revisar los datos que escribe el usuario antes de usarlos.
# - Usar listas cuando se necesita agregar elementos.
# - Usar tuplas para guardar las coordenadas de cada punto.
# - Dar mensajes claros para saber si una entrada es incorrecta.

# ============================================================
# Problema 1: Shopping list basics
# ============================================================
# Descripción:
# El programa recibe varios productos separados por comas, agrega
# un producto nuevo y permite revisar si otro producto está en la lista.
#
# Entradas:
# - Lista inicial de productos separados por comas.
# - Producto que se quiere agregar.
# - Producto que se quiere buscar.
#
# Salidas:
# - Lista final de productos.
# - Cantidad de productos.
# - Resultado de la búsqueda (true o false).
# - Mensaje de error cuando algún dato está vacío.
#
# Validaciones:
# - La lista inicial debe tener al menos un producto.
# - El producto nuevo y el que se busca no deben estar vacíos.
# - Se quitan los espacios extra de los nombres.

print("--- Problem 1: Shopping list basics ---")

initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter a new item to add: ").strip()
search_item = input("Enter an item to search: ").strip()

items_list = []

for item in initial_items_text.split(","):
    item = item.strip()
    if item != "":
        items_list.append(item)

if len(items_list) == 0 or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list.append(new_item)
    found_item = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(found_item).lower()}")

print()

# ============================================================
# Problema 2: Points and distances with tuples
# ============================================================
# Descripción:
# El programa guarda dos puntos usando tuplas y calcula la distancia
# entre ellos con sus coordenadas X y Y.
#
# Entradas:
# - Coordenadas X y Y del primer punto.
# - Coordenadas X y Y del segundo punto.
#
# Salidas:
# - Coordenadas de los dos puntos.
# - Distancia entre ambos.
# - Mensaje de error si una coordenada no es numérica.
#
# Validaciones:
# - Las cuatro coordenadas deben ser números.
# - Se permite usar números negativos y decimales.

print("--- Problem 2: Points and distances with tuples ---")

try:
    x1 = float(input("Enter x coordinate of point 1: "))
    y1 = float(input("Enter y coordinate of point 1: "))
    x2 = float(input("Enter x coordinate of point 2: "))
    y2 = float(input("Enter y coordinate of point 2: "))

    point1 = (x1, y1)
    point2 = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Distance: {distance}")

except ValueError:
    print("Error: invalid input")

# ============================================================
# Conclusión
# ============================================================
# En esta práctica se usaron listas para guardar varios productos,
# agregar uno nuevo y revisar si un producto se encuentra en ellas.
# También se usaron tuplas para guardar las coordenadas de dos puntos.
# Al final, se comprobó que revisar las entradas ayuda a evitar errores
# cuando el usuario deja un dato vacío o escribe letras en vez de números.

# ============================================================
# Referencias
# ============================================================
# Python Software Foundation. Tutorial de Python: Estructuras de datos.
# https://docs.python.org/es/3/tutorial/datastructures.html
#
# Python Software Foundation. Tipos integrados: listas y tuplas.
# https://docs.python.org/3/library/stdtypes.html
