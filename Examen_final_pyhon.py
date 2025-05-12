
inventario = {}

def product_5(inventario_local):
    count = True
    count2 = 0
    count3 = 1
    print("\n\033[94m\033[1m---Añadir 5 productos iniciales para continuar la gestion del inventario----\033[0m")
    while count :
        nombre = input(f"\n\033[1mIngrese el nombre del producto ({count3}): ").strip()
        if nombre in inventario_local:
         print(f"\n\033[93m El producto '{nombre}' ya existe\033[0m")

        count3 = count3+1
        count2 = count2+1
        while True:
            try:
                precio_str = input("\n\033[1mIngrese el precio del producto: ").replace(',', '.')
                precio = float(precio_str)
                if precio < 0:
                    print("\n\033[93m El precio debe ser un valor positivo.\033[0m")
                    continue
                break
            except ValueError:
                print("\n\033[93m Ingrese un numero valido para el precio.\033[0m")

        while True:
            try:
                cantidad_str = input("\n\033[1mIngrese la cantidad disponible: ")
                cantidad = int(cantidad_str)
                if cantidad < 0:
                    print("\n\033[93m La cantidad debe ser un valor positivo.\033[0m")
                    continue
                break
            except ValueError:
                print("\n\033[93m Ingrese un numero entero valido para la cantidad.\033[0m")

        inventario_local[nombre] = {'precio': precio, 'cantidad': cantidad}
        print(f"\n\033[1m\033[32mEl producto '{nombre}' ha sido añadido al inventario.\033[0m")
        
        if count2 == 5:
         count=False
        

def agregar_producto(inventario_local):
    print("\n\033[94m\033[1mAñadir Producto\033[0m")
    nombre = input("\n\033[1mIngrese el nombre del producto: ").strip()
    if nombre in inventario_local:
        print(f"\n\033[93m El producto '{nombre}' ya existe\033[0m")
        return
    while True:
        try:
            precio_str = input("\n\033[1mIngrese el precio del producto: ").replace(',', '.')
            precio = float(precio_str)
            if precio < 0:
                print("\n\033[93m El precio debe ser un valor positivo.\033[0m")
                continue
            break
        except ValueError:
            print("\n\033[93m Ingrese un numero valido para el precio.\033[0m")

    while True:
        try:
            cantidad_str = input("\n\033[1mIngrese la cantidad disponible: ")
            cantidad = int(cantidad_str)
            if cantidad < 0:
                print("\n\033[93m La cantidad debe ser un valor positivo.\033[0m")
                continue
            break
        except ValueError:
            print("\n\033[93m Ingrese un numero entero valido para la cantidad.\033[0m")

    inventario_local[nombre] = {'precio': precio, 'cantidad': cantidad}
    print(f"\n\033[1m\033[32mEl producto '{nombre}' ha sido añadido al inventario.\033[0m")

def consultar_producto(inventario_local):
    print("\n\033[94m\033[1mConsultar Producto\033[0m")
    nombre = input("\n\033[1mIngrese el nombre del producto que desea consultar: ").strip()
    if nombre in inventario_local:
        info_producto = inventario_local[nombre]
        precio = info_producto['precio']
        cantidad = info_producto['cantidad']
        print("\n")
        print("\033[1m" + "-" * 30 + "\033[0m")#marquetado
        print(f"\033[1m| \033[94m{'Producto':<15} \033[0m| {nombre:<12} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")#marquetado
        print(f"\033[1m| \033[94m{'Precio':<15}\033[0m | ${precio:11,.2f} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")#marquetado
        print(f"\033[1m|\033[94m {'Cantidad':<15}\033[0m | {cantidad:<12} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")
    else:
        print(f"\033[93m El producto '{nombre}' no se encuentra en el inventario.\033[0m")
    

def actualizar_precio(inventario_local):
    print("\n\033[94m\033[1mActualizar Precio\033[0m")
    nombre = input("\n\033[1mIngrese el nombre del producto cuyo precio quiere actualizar: ").strip()
    if nombre in inventario_local:
        while True:
            try:
                nuevo_precio_str = input("\n\033[1mIngrese el nuevo precio: ").replace(',', '.')
                nuevo_precio = float(nuevo_precio_str)
                if nuevo_precio < 0:
                    print("\n\033[93mEl precio debe ser un valor positivo.\033[0m")
                    continue
                inventario_local[nombre]['precio'] = nuevo_precio
                print(f"\n\033[1m\033[32mEl precio de '{nombre}' ha sido actualizado a ${nuevo_precio:,.2f}.\033[0m")
                break
            except ValueError:
                print("\n\033[93mPor favor, ingrese un numero valido para el precio.\033[0m")
    else:
        print(f"\n\033[93m El producto '{nombre}' no se encuentra en el inventario.\033[0m")


def eliminar_producto(inventario_local):
    print("\n\033[94m\033[1mEliminar Producto\033[0m")
    nombre = input("\033[1mIngrese el nombre del producto que quiere eliminar: ").strip()
    if nombre in inventario_local:
        del inventario_local[nombre]
        print(f"\n\033[1m\033[31mEl producto '{nombre}' ha sido eliminado.\033[0m")
    else:
        print(f"\n\033[93m El producto no se encuentra en el inventario.\033[0m")

def calcular_valor_total(inventario_local):
    print("\n\033[94m\033[1mValor Total del Inventario\033[0m")
    valor_total_lambda = lambda inventario: sum(producto['precio'] * producto['cantidad'] for producto in inventario.values())
    valor_total = valor_total_lambda(inventario_local)
    print(f"\n\033[1mEl valor total del inventario es: ${valor_total:,.2f}\033[0m")
    return 

def mostrar_inventario(inventario_local):
    print("\n\033[94m\033[1mMostrar Inventario\033[0m")
    if not inventario_local:
        print("\033[1m\n\033[93m\El inventario está vacio.\033[0m")
        return
    print("\n\033[94m\033[1mInventario Actual: \033[0m")
    count4 = 0
    for nombre, info_producto in inventario_local.items():
        count4 = count4 +1
        precio = info_producto['precio']
        cantidad = info_producto['cantidad']
        print(f"\n\033[1mProducto({count4}): {nombre}, Precio: ${precio:,.2f}, Cantidad: {cantidad}\033[0m")
    print("-" * 35)


product_5(inventario)
while True:
   
    print("\n\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[94m\033[1m" + "  SISTEMA DE INVENTARIO  ".center(35) + "\033[0m")
    print("\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[1m  Opciones:\033[0m")
    print(f"\033[1m  1. Añadir producto{''.ljust(31)}\033[0m")
    print(f"\033[1m  2. Consultar producto{''.ljust(29)}\033[0m")
    print(f"\033[1m  3. Actualizar precio{''.ljust(30)}\033[0m")
    print(f"\033[1m  4. Eliminar producto{''.ljust(30)}\033[0m")
    print(f"\033[1m  5. Calcular valor total del inventario{''.ljust(24)}\033[0m")
    print(f"\033[1m  6. Mostrar inventario{''.ljust(27)}\033[0m")
    print(f"\033[1m  7. Salir{''.ljust(34)}\033[0m")
    print("\033[94m" + "═" * 35 + "\033[0m")

    opcion = input("\033[94m\033[1mSeleccione una opcion: \033[0m")#
    if opcion == '1':
        agregar_producto(inventario)
    elif opcion == '2':
        consultar_producto(inventario)
    elif opcion == '3':
        actualizar_precio(inventario)
    elif opcion == '4':
        eliminar_producto(inventario)
    elif opcion == '5':
        valor_total = calcular_valor_total(inventario)
    elif opcion == '6':
        mostrar_inventario(inventario)
    elif opcion == '7':
        print("\n\033[94m\033[1mSaliendo del programa\033[0m")
        break
    else:
        print("\n\033[93m Opcion invalida. seleccione una opcion valida.\033[0m")
