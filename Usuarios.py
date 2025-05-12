diccionarios_personas = {}
contador_id = 0

def imprimir_menu():
    """Imprime el menu principal con titulo y numeros en azul."""
    azul_oscuro = "\033[1;34m"
    gris_oscuro = "\033[1;30m"
    verde_oscuro = "\033[1;32m"
    azul_claro = "\033[1;36m"
    amarillo_suave = "\033[1;33m"

    print(f"\n{gris_oscuro}{'='*40}\033[0m")
    print(f"{gris_oscuro}{'='*10} {azul_oscuro}\033[1mMENU DE USUARIO\033[0m {gris_oscuro}{'='*10}\033[0m")
    print(f"{gris_oscuro}{'='*40}\033[0m")
    print(f"{azul_oscuro}1.\033[0m Crear Usuario")
    print(f"{azul_oscuro}2.\033[0m Consultar Usuarios")
    print(f"{azul_oscuro}3.\033[0m Eliminar Usuario")
    print(f"{azul_oscuro}4.\033[0m Modificar Usuario")
    print(f"{azul_oscuro}5.\033[0m Salir")
    print(f"{gris_oscuro}{'='*40}\033[0m")


def validar_entero(mensaje, color_error="\033[1;31m"):
    """Valida que la entrada del usuario sea un entero."""
    while True:
        entrada = input(f"\033[1;32m{mensaje}\033[0m")
        if entrada.isdigit():
            return int(entrada)
        else:
            print(f"{color_error}!Error! Ingresa un numero entero.\033[0m")

def crear_usuario():
    """Crea un nuevo usuario y lo agrega al diccionario."""
    global contador_id # Indica que se usara la variable global contador_id
    print(f"\n\033[1;34mCreando nuevo usuario...\033[0m")
    nombre = input(f"\033[1;32mIngrese Nombre: \033[0m")
    apellido = input(f"\033[1;32mIngrese Apellido: \033[0m")
    while True:
        correo = input(f"\033[1;32mIngrese Correo: \033[0m")
        if "@" in correo and "." in correo: # Verifica si el correo tiene el formato basico
            if any(usuario.get('correo') == correo for usuario in diccionarios_personas.values()):
                print(f"\033[1;31m!Error! Este correo ya esta registrado.\033[0m")
            else:
                break # Sale del bucle si el correo es valido y no esta registrado
        else:
            print(f"\033[1;31m!Error! Ingresa un correo valido.\033[0m")
    edad = validar_entero("Ingrese Edad: ")
    contador_id += 1 # Incrementa el contador para generar un nuevo ID
    id_usuario = str(contador_id) # Convierte el contador a string para usarlo como ID
    usuario = {"id": id_usuario, "nombre": nombre, "apellido": apellido, "correo": correo, "edad": edad}
    diccionarios_personas[id_usuario] = usuario # Agrega el nuevo usuario al diccionario usando el ID como clave
    print(f"\033[1;32mUsuario creado correctamente con ID: {id_usuario}\033[0m")

def consultar_usuarios():
    """Muestra la lista de usuarios registrados."""
    if diccionarios_personas: # Verifica si hay usuarios registrados
        print(f"\n\033[1;34mLa lista de usuarios es:\033[0m")
        for id_usuario, usuario in diccionarios_personas.items(): # Itera sobre los usuarios en el diccionario
            print(f"\n\033[1;33mID:\033[0m {id_usuario}")
            print(f"\t\033[1;32mNombre:\033[0m {usuario.get('nombre')}")
            print(f"\t\033[1;32mApellido:\033[0m {usuario.get('apellido')}")
            print(f"\t\033[1;32mCorreo:\033[0m {usuario.get('correo')}")
            print(f"\t\033[1;32mEdad:\033[0m {usuario.get('edad')}")
    else:
        print(f"\033[1;31mNo hay usuarios registrados.\033[0m")

def eliminar_usuario():
    """Elimina un usuario del diccionario usando su nombre o ID."""
    if not diccionarios_personas: # Verifica si hay usuarios para eliminar
        print(f"\033[1;31mNo hay usuarios para eliminar.\033[0m")
        return

    print(f"\n\033[1;31mEliminando usuario...\033[0m")
    opcion_busqueda = input(f"\033[1;32mBuscar por (1) Nombre o (2) ID: \033[0m")

    usuario_encontrado_id = None # Inicializa la variable para almacenar el ID del usuario encontrado

    if opcion_busqueda == '1': # Busqueda por nombre
        nombre_eliminar = input(f"\033[1;32mIngrese el nombre del usuario a eliminar: \033[0m").lower()
        coincidencias = []
        for id_usuario, usuario in diccionarios_personas.items():
            if usuario.get('nombre', '').lower() == nombre_eliminar:
                coincidencias.append(id_usuario)
        if not coincidencias:
            print(f"\033[1;31mNo se encontro ningun usuario con el nombre '{nombre_eliminar}'.\033[0m")
            return
        elif len(coincidencias) == 1:
            usuario_encontrado_id = coincidencias[0]
        else:
            print(f"\033[1;33mSe encontraron varios usuarios con ese nombre. Por favor, especifique el ID del usuario que desea eliminar:\033[0m")
            for id_u in coincidencias:
                usuario_info = diccionarios_personas.get(id_u)
                if usuario_info:
                    print(f"\033[1;33mID: {id_u}, Nombre: {usuario_info.get('nombre')}, Apellido: {usuario_info.get('apellido')}\033[0m")
            id_eliminar = input(f"\033[1;32mIngrese el ID del usuario a eliminar: \033[0m")
            if id_eliminar in coincidencias:
                usuario_encontrado_id = id_eliminar
            else:
                print(f"\033[1;31mID invalido.\033[0m")
                return
    elif opcion_busqueda == '2': # Busqueda por ID
        id_eliminar = input(f"\033[1;32mIngrese el ID del usuario a eliminar: \033[0m")
        if id_eliminar in diccionarios_personas:
            usuario_encontrado_id = id_eliminar
        else:
            print(f"\033[1;31mNo se encontro ningun usuario con el ID '{id_eliminar}'.\033[0m")
            return
    else:
        print(f"\033[1;31mOpcion de busqueda invalida.\033[0m")
        return

    if usuario_encontrado_id:
        del diccionarios_personas[usuario_encontrado_id] # Elimina el usuario del diccionario
        print(f"\033[1;32mUsuario con ID '{usuario_encontrado_id}' eliminado correctamente.\033[0m")

def modificar_usuario():
    """Modifica la informacion de un usuario existente buscando por nombre o ID."""
    if not diccionarios_personas: # Verifica si hay usuarios para modificar
        print(f"\n\033[1;31mNo hay usuarios para modificar.\033[0m")
        return

    print(f"\n\033[1;34mModificando usuario...\033[0m")
    opcion_busqueda = input(f"\033[1;32mBuscar por (1) Nombre o (2) ID: \033[0m")

    usuario_encontrado_id = None # Inicializa la variable para almacenar el ID del usuario encontrado
    usuario_a_modificar = None # Inicializa la variable para almacenar el usuario a modificar

    if opcion_busqueda == '1': # Busqueda por nombre
        nombre_buscar = input(f"\033[1;32mIngrese el nombre del usuario a modificar: \033[0m").lower()
        coincidencias = []
        for id_usuario, usuario in diccionarios_personas.items():
            if usuario.get('nombre', '').lower() == nombre_buscar:
                coincidencias.append(id_usuario)
        if not coincidencias:
            print(f"\033[1;31mNo se encontro ningun usuario con el nombre '{nombre_buscar}'.\033[0m")
            return
        elif len(coincidencias) == 1:
            usuario_encontrado_id = coincidencias[0]
            usuario_a_modificar = diccionarios_personas[usuario_encontrado_id]
        else:
            print(f"\033[1;33mSe encontraron varios usuarios con ese nombre. Por favor, especifique el ID del usuario que desea modificar:\033[0m")
            for id_u in coincidencias:
                usuario_info = diccionarios_personas.get(id_u)
                if usuario_info:
                    print(f"\033[1;33mID: {id_u}, Nombre: {usuario_info.get('nombre')}, Apellido: {usuario_info.get('apellido')}\033[0m")
            id_modificar = input(f"\033[1;32mIngrese el ID del usuario a modificar: \033[0m")
            if id_modificar in coincidencias:
                usuario_encontrado_id = id_modificar
                usuario_a_modificar = diccionarios_personas[usuario_encontrado_id]
            else:
                print(f"\033[1;31mID invalido.\033[0m")
                return
    elif opcion_busqueda == '2': # Busqueda por ID
        id_modificar = input(f"\033[1;32mIngrese el ID del usuario a modificar: \033[0m")
        if id_modificar in diccionarios_personas:
            usuario_encontrado_id = id_modificar
            usuario_a_modificar = diccionarios_personas[usuario_encontrado_id]
        else:
            print(f"\033[1;31mNo se encontro ningun usuario con el ID '{id_modificar}'.\033[0m")
            return
    else:
        print(f"\033[1;31mOpcion de busqueda invalida.\033[0m")
        return

    if usuario_a_modificar:
        print(f"\n\033[1;33mIngrese la nueva informacion (deje en blanco para mantener el valor actual):\033[0m")
        nuevo_nombre = input(f"\033[1;32mNuevo nombre ({usuario_a_modificar.get('nombre', '')}): \033[0m")
        if nuevo_nombre:
            usuario_a_modificar["nombre"] = nuevo_nombre
        nuevo_apellido = input(f"\033[1;32mNuevo apellido ({usuario_a_modificar.get('apellido', '')}): \033[0m")
        if nuevo_apellido:
            usuario_a_modificar["apellido"] = nuevo_apellido
        while True:
            nuevo_correo = input(f"\033[1;32mNuevo correo ({usuario_a_modificar.get('correo', '')}): \033[0m")
            if nuevo_correo == "" or ("@" in nuevo_correo and "." in nuevo_correo):
                if nuevo_correo and nuevo_correo != usuario_a_modificar.get('correo') and any(u.get('correo') == nuevo_correo for u in diccionarios_personas.values()):
                    print(f"\033[1;31m!Error! Este correo ya esta registrado.\033[0m")
                else:
                    usuario_a_modificar["correo"] = nuevo_correo if nuevo_correo else usuario_a_modificar.get('correo')
                    break
            else:
                print(f"\033[1;31m!Error! Ingresa un correo valido.\033[0m")
        nueva_edad_str = input(f"\033[1;32mNueva edad ({usuario_a_modificar.get('edad', '')}): \033[0m")
        if nueva_edad_str:
            if nueva_edad_str.isdigit():
                usuario_a_modificar["edad"] = int(nueva_edad_str)
            else:
                print(f"\033[1;31m!Error! La edad debe ser un numero entero.\033[0m")
        print(f"\033[1;32mUsuario con ID '{usuario_encontrado_id}' modificado correctamente.\033[0m")

while True:
    print("\033[H\033[J", end="")
    imprimir_menu()
    opcion = input(f"\033[1;32mSeleccione una opcion: \033[0m")

    if opcion == '1':
        crear_usuario()
    elif opcion == '2':
        consultar_usuarios()
        input(f"\n\033[1;32mPresione Enter para continuar...\033[0m")
    elif opcion == '3':
        eliminar_usuario()
        input(f"\n\033[1;32mPresione Enter para continuar...\033[0m")
    elif opcion == '4':
        modificar_usuario()
        input(f"\n\033[1;32mPresione Enter para continuar...\033[0m")
    elif opcion == '5':
        print(f"\n\033[1;35mSaliendo del programa. !Hasta luego!\033[0m")
        break
    else:
        print(f"\n\033[1;31m!Error! Opcion invalida. Intente de nuevo.\033[0m")
        input(f"\n\033[1;32mPresione Enter para continuar...\033[0m")