estudiantes = {
    1000640800: {"Nombre completo": "Carlos Perez", "Edad": 20, "Nota": 4.2},
    1000640801: {"Nombre completo": "Maria Gomez", "Edad": 22, "Nota": 3.8},
    1000640802: {"Nombre completo": "Juan Rodriguez", "Edad": 19, "Nota": 4.9},
    1000640803: {"Nombre completo": "Laura Torres", "Edad": 21, "Nota": 2.9},
    1000640804: {"Nombre completo": "Andres Martinez", "Edad": 23, "Nota": 2.5}
}

def agregar_estudiante_funcion(id_estudiante, nombre_completo, edad, nota):
    estudiantes[id_estudiante] = {
        "Nombre completo": nombre_completo,
        "Edad": edad,
        "Nota": nota
    }
    print(f"\033[92m\nEstudiante '{nombre_completo}' agregado correctamente.\033[0m")

def buscar_estudiante_id_funcion(id_estudiante_buscar):
    while True:
        if id_estudiante_buscar in estudiantes.keys():
            datos_estudiante = estudiantes[id_estudiante_buscar]
            print("\n\033[96mEstudiante encontrado:\033[0m")
            print(f"\033[95mID:\033[0m \033[94m{id_estudiante_buscar}\033[0m")
            print(f"\033[95mNombre completo:\033[0m \033[93m{datos_estudiante['Nombre completo']}\033[0m")
            print(f"\033[95mEdad:\033[0m \033[92m{datos_estudiante['Edad']}\033[0m")
            print(f"\033[95mNota:\033[0m \033[92m{datos_estudiante['Nota']}\033[0m")
            break
        else:
            print("\n\033[93mNo se encontró un estudiante con ese ID.\033[0m")
        break

def buscar_estudiante_nombre_funcion(nombre_estudiante_buscar):
    encontrado = False
    for id_estudiante, datos_estudiante in estudiantes.items():
        if nombre_estudiante_buscar.lower() in datos_estudiante["Nombre completo"].lower():
            print("\n\033[96mEstudiante encontrado:\033[0m")
            print(f"\033[95mID:\033[0m \033[94m{id_estudiante}\033[0m")
            print(f"\033[95mNombre completo:\033[0m \033[93m{datos_estudiante['Nombre completo']}\033[0m")
            print(f"\033[95mEdad:\033[0m \033[92m{datos_estudiante['Edad']}\033[0m")
            print(f"\033[95mNota:\033[0m \033[92m{datos_estudiante['Nota']}\033[0m")
            encontrado = True
    if not encontrado:
        print("\033[93m\nNo se encontró ningún estudiante con ese nombre.\033[0m")

def actualizar_estudiante_funcion(id_estudiante_actualizar):
    actualizado = False
    while True:
        nueva_edad_str = input("\nIngrese nueva edad del estudiante (Enter para dejar igual): ")
        if nueva_edad_str == "":
            break
        try:
            edad_actualizar = int(nueva_edad_str)
            if edad_actualizar > 0:
                estudiantes[id_estudiante_actualizar]["Edad"] = edad_actualizar
                actualizado = True
                break
            else:
                print("\033[91m\nEdad inválida. No se permiten valores negativos o cero.\033[0m")
        except ValueError:
            print("\033[91m\nEdad inválida. Debe ser un número entero.\033[0m")
    while True:
        nueva_nota_str = input("\nIngrese nueva nota del estudiante (Enter para dejar igual): ")
        if nueva_nota_str == "":
            break
        try:
            nota_actualizar = float(nueva_nota_str)
            if 0.0 <= nota_actualizar <= 5.0:
                estudiantes[id_estudiante_actualizar]["Nota"] = nota_actualizar
                actualizado = True
                break
            else:
                print("\033[91m\nNota inválida. Debe estar entre 0.0 y 5.0.\033[0m")
        except ValueError:
            print("\033[91m\nNota inválida. Debe ser un número decimal.\033[0m")
    if actualizado:
        print(f"\033[92m\nEstudiante {estudiantes[id_estudiante_actualizar]['Nombre completo']} actualizado correctamente.\033[0m")
    else:
        print("\033[93m\nNo se realizaron cambios.\033[0m")

def eliminar_estudiante_funcion(id_estudiante_eliminar):
    if id_estudiante_eliminar in estudiantes:
        nombre_eliminado = estudiantes[id_estudiante_eliminar]['Nombre completo']
        estudiantes.pop(id_estudiante_eliminar)
        print(f"\033[92m\nEstudiante {nombre_eliminado} eliminado correctamente.\033[0m")

def calcular_promedio_funcion():
    contador_estudiantes = 0
    total_notas = 0.0
    for estudiante in estudiantes.values():
        contador_estudiantes += 1
        total_notas += estudiante["Nota"]
    if contador_estudiantes > 0:
        promedio = total_notas / contador_estudiantes
        print((f"\033[94m\nEl promedio de notas es: {promedio:.2f}\033[0m"))
    else:
        print("\033[93m\nNo hay estudiantes registrados para calcular el promedio.\033[0m")

def mostrar_estudiantes_reprobados_funcion():
    estudiantes_reprobados = []
    for estudiante in estudiantes.values():
        if estudiante["Nota"] < 3.0:
            estudiantes_reprobados.append([estudiante["Nombre completo"], estudiante["Nota"]])
    if estudiantes_reprobados:
        print("\n\033[91mEstudiantes que están perdiendo:\033[0m")
        for estudiante_reprobado in estudiantes_reprobados:
            print(f"\033[95mNombre:\033[0m {estudiante_reprobado[0]}, \033[95mNota:\033[0m \033[91m{estudiante_reprobado[1]}\033[0m")
    else:
        print("\n\033[92mNingún estudiante está perdiendo actualmente.\033[0m")

def volver_menu_o_salir():
    while True:
        opcion_salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
        if opcion_salida == "s":
            return False
        elif opcion_salida == "n":
            print("\033[93m\nSaliendo del sistema...\033[0m")
            exit()
        else:
            print("\033[91m\nPor favor ingresa 's' para sí o 'n' para no.\033[0m")

def avanzar_funcion_agregar():
    while True:
        continuar_agregar = input("\033[93m\n¿Deseas continuar ingresando estudiantes?: S()si N()no:\033[0m").lower()
        if continuar_agregar == "n":
            return volver_menu_o_salir()
        elif continuar_agregar == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 's' para sí o 'n' para no.\033[0m")

def avanzar_funcion_buscar():
    while True:
        buscar_otra_vez = input("\033[93m\n¿Deseas buscar otro estudiante?: S()si N()no: \033[0m").lower()
        if buscar_otra_vez == "n":
            return volver_menu_o_salir()
        elif buscar_otra_vez == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 's' para sí o 'n' para no.\033[0m")

def avanzar_funcion_actualizar():
    while True:
        continuar_actualizar = input("\033[93m\n¿Deseas actualizar otro estudiante? S(si) N(no): \033[0m").lower()
        if continuar_actualizar == "n":
            return volver_menu_o_salir()
        elif continuar_actualizar == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 's' para sí o 'n' para no.\033[0m")

def avanzar_funcion_eliminar():
    while True:
        continuar_eliminar = input("\033[93m\n¿Deseas eliminar otro estudiante? S(si) N(no): \033[0m").lower()
        if continuar_eliminar == "n":
            return volver_menu_o_salir()
        elif continuar_eliminar == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 's' para sí o 'n' para no.\033[0m")

while True:
    print("\033[93m\nBienvenido a la gestión de estudiantes\033[0m.")
    print("\033[93m\nOpciones que puede realizar\033[0m")
    print("\033[1;34m1. Agregar estudiante.\033[0m")
    print("\033[1;34m2. Buscar estudiante.\033[0m")
    print("\033[1;34m3. Actualizar estudiante.\033[0m")
    print("\033[1;34m4. Eliminar estudiante.\033[0m")
    print("\033[1;34m5. Calcular promedio.\033[0m")
    print("\033[1;34m6. Lista de estudiantes reprobados.\033[0m")
    print("\033[1;34m7. Salir.\033[0m")
    while True:
        try:
            opcion = int(input("\n\033[96mElije la opción que deseas: \033[0m"))
            if 1 <= opcion <= 7:
                break
            else:
                print("\n\033[93m\nIngrese una opción válida (1-7).\033[0m")
        except ValueError:
            print("\n\033[91mPor favor ingrese un número entero.\033[0m")
    match opcion:
        case 1:
            while True:
                id_nuevo = int(input("\nIngrese el ID del nuevo estudiante: "))
                nombre_nuevo = input("Ingrese el nombre completo del nuevo estudiante: ")
                while True:
                    try:
                        edad_nueva = int(input("Ingrese la edad del nuevo estudiante: "))
                        if edad_nueva > 0:
                            break
                        else:
                            print("\033[91m\nLa edad debe ser un número positivo.\033[0m")
                    except ValueError:
                        print("\033[91m\nPor favor ingrese un número entero para la edad.\033[0m")
                while True:
                    try:
                        nota_nueva = float(input("Ingrese la nota del nuevo estudiante (0.0-5.0): "))
                        if 0.0 <= nota_nueva <= 5.0:
                            break
                        else:
                            print("\033[91m\nLa nota debe estar entre 0.0 y 5.0.\033[0m")
                    except ValueError:
                        print("\033[91m\nPor favor ingrese un número para la nota.\033[0m")
                agregar_estudiante_funcion(id_nuevo, nombre_nuevo, edad_nueva, nota_nueva)
                if not avanzar_funcion_agregar():
                    break
        case 2:
            while True:
                buscar_por = input("\n¿Buscar por ID (i) o Nombre (n)?: ").lower()
                if buscar_por == "i":
                    id_buscar = int(input("Ingrese el ID del estudiante a buscar: "))
                    buscar_estudiante_id_funcion(id_buscar)
                elif buscar_por == "n":
                    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
                    buscar_estudiante_nombre_funcion(nombre_buscar)
                else:
                    print("\033[91m\nOpción inválida. Ingrese 'i' o 'n'.\033[0m")
                if not avanzar_funcion_buscar():
                    break
        case 3:
            while True:
                id_actualizar = int(input("\nIngrese el ID del estudiante que desea actualizar: "))
                if id_actualizar in estudiantes:
                    actualizar_estudiante_funcion(id_actualizar)
                else:
                    print("\033[93m\nNo se encontró un estudiante con ese ID.\033[0m")
                if not avanzar_funcion_actualizar():
                    break
        case 4:
            while True:
                id_eliminar = int(input("\nIngrese el ID del estudiante que desea eliminar: "))
                if id_eliminar in estudiantes:
                    eliminar_estudiante_funcion(id_eliminar)
                else:
                    print("\033[93m\nNo se encontró un estudiante con ese ID.\033[0m")
                if not avanzar_funcion_eliminar():
                    break
        case 5:
            calcular_promedio_funcion()
            volver_menu_o_salir()
        case 6:
            mostrar_estudiantes_reprobados_funcion()
            volver_menu_o_salir()
        case 7:
            print("\033[93m\nSaliendo...\033[0m")
            print("\033[93m\nGracias Vuelva pronto\033[0m")
            exit()