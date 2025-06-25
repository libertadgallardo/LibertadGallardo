

# Acá acordamos el stock de entradas para la funcion de "CATS" para el día Viernes y Sábado respectivamente 
stock_func1 = 150
stock_func2 = 180
compradores = {} # Acá creamos una lista para alamcenar los compradores en una sola variable

# Acá creamos el bloque de código para la opcion 1
def comprar_entrada(nombre, funcion): # Acá definimos una función con el nombre comprar_entrada y sus parámetros.
    global stock_func1, stock_func2 # Global para modificar una variable exterior(global)

    if nombre in compradores:
        return "Error. El nombre ya está registrado." # Verifica si el nombre ya está registrado

 # Este bloque permite comprar entradas a la funcion del día viernes, descontando la cantidad al stock inicial. Si queda stock mostrará compra exitosa, sino mostrará no hay entradas.
    if funcion == "1" and stock_func1 > 0:   
        compradores[nombre] = "Cats Día Viernes"
        stock_func1 -= 1       
        return "Compra registrada exitosamente para Cats Día Viernes." 
    elif funcion == "2" and stock_func2 > 0:
        compradores[nombre] = "Cats Día Sábado"
        stock_func2 -= 1
        return "Compra registrada exitosamente para Cats Día Sábado."
    else:
        return "Error. No hay entradas disponibles para esta función."

# Acá creamos el bloque de código para la opción 2
def cambiar_funcion(nombre):
    global stock_func1, stock_func2

# Acá verifica si el nombre se encuentra en la variable compradores para así cambiar la función si es así. Si existe podrá cambiar la función sino, arrojará Error. El comprador no existe
    if nombre in compradores:
        print(f"Actualmente estás registrado en: {compradores[nombre]}.")
        cambio = input("¿Deseas cambiar de función? (sí/no): ").lower() # Aca convertimos lo ingresado a lower para que el programa no malinterprete

        if cambio == "sí":
            if compradores[nombre] == "Cats Día Viernes" and stock_func2 > 0:  # Aca se verifica que hayan entradas para la funcion 2. El programa tomará caminos dependiendo.
                compradores[nombre] = "Cats Día Sábado"
                stock_func1 += 1 # Devuelve entrada a funcion 1
                stock_func2 -= 1 # Resta entrada a funcion 2
                return "Cambio exitoso a Cats Día Sábado."
            elif compradores[nombre] == "Cats Día Sábado" and stock_func1 > 0: 
                compradores[nombre] = "Cats Día Viernes"
                stock_func2 += 1
                stock_func1 -= 1
                return "Cambio exitoso a Cats Día Viernes."
            else:
                return "Error. No hay entradas disponibles en la función deseada."
        else:
            return "No se realizó el cambio de función."
    else:
        return "Error. El comprador no existe."

# Creamos el bloque de código para la opción 3
def mostrar_totales():
    total_dispo = stock_func1 + stock_func2
    total_vendidas = (150 - stock_func1) + (180 - stock_func2)
    print(f"Entradas disponibles: {total_dispo}")
    print(f"Entradas vendidas: {total_vendidas}")

# Bucle principal
def menu():
    while True:
        print("/n--- Cartelera teatro CafeConLeche y sus distintos musicales.---")
        print("1. Comprar entrada")
        print("2. Cambio de función")
        print("3. Mostrar totales")
        print("4. Salir")
        opc = input("Selecciona una opción: ")

        if opc == "1":
            nombre = input("Ingresa tu nombre: ")
            funcion = input("Selecciona la función (1.Día Viernes, 2.Día Sábado): ")
            print(comprar_entrada(nombre, funcion))

        elif opc == "2":
            nombre = input("Ingresa tu nombre para cambiar de función: ")
            print(cambiar_funcion(nombre))

        elif opc == "3":
            mostrar_totales()

        elif opc == "4":
            print("Programa terminado...")
            break

        else:
            print("Debe ingresar una opción válida!!")

menu()


