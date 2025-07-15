

{'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],  # Producto sin stock
}

# Función para mostrar stock por marca (Error 1: Repetición innecesaria de lógica)
def stock_marca(marca):
    marca = marca.strip().lower()  # Error: Usamos strip() y lower() innecesariamente en cada modelo
    for modelo, datos in productos.items():
        if marca == datos[0].lower():  # Condición más compleja de lo necesario
            cantidad = stock[modelo][1]
            print(f"Modelo: {modelo}, Stock: {cantidad}")  # No se maneja el caso sin stock correctamente

# Función para búsqueda por precio (Error 2: Validación de precios no óptima)
def busqueda_precio(p_min, p_max):
    if p_min < 0 or p_max < 0:  # Error: Control de precios negativos, pero falta mayor claridad
        print("Los precios no pueden ser negativos.")
        return
    resultados = []
    for modelo, datos in productos.items():
        precio = stock[modelo][0]
        if p_min <= precio <= p_max and stock[modelo][1] > 0:
            resultados.append(f"{datos[0]}--{modelo}")
   
    if len(resultados) > 0:
        resultados.sort()  # Error: El uso de len(resultados) es redundante; podemos usar 'if resultados'
        for resultado in resultados:
            print(resultado)
    else:
        print("No hay notebooks en ese rango de precios.")  # Mensaje podría ser más específico

# Función para actualizar el precio de un modelo (Error 3: Manejo de excepciones innecesario)
def actualizar_precio(modelo, p):
    try:
        if modelo not in stock:
            raise ValueError("El modelo no existe!!")  # Error: Excepción innecesaria
        stock[modelo][0] = p  # Aquí actualizamos el precio sin mucho control de entrada
        return True
    except ValueError as e:
        print(str(e))  # Error: Deberíamos manejar esto de manera más limpia
        return False

# Función principal que ejecuta el menú (Error 4: Lógica de flujo innecesaria)
def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
       
        try:
            opcion = int(input("Seleccione una opción: "))
           
            if opcion == 1:
                marca = input("Ingrese la marca: ")
                stock_marca(marca)  # Llamada repetitiva sin mejoras
       
            elif opcion == 2:
                while True:
                    try:
                        p_min = int(input("Ingrese el precio mínimo: "))
                        p_max = int(input("Ingrese el precio máximo: "))
                        if p_min > p_max:
                            print("El precio mínimo debe ser menor que el precio máximo.")
                            continue  # Repetimos el ciclo en vez de intentar solucionar elegantemente
                        busqueda_precio(p_min, p_max)
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
           
            elif opcion == 3:
                while True:
                    modelo = input("Ingrese el modelo a actualizar el precio: ")
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        if actualizar_precio(modelo, nuevo_precio):
                            print("Precio actualizado!!")
                        else:
                            print("El modelo no existe!!")
                       
                        actualizar_otro = input("¿Desea actualizar otro precio? (si/no): ").lower()
                        if actualizar_otro == "no":
                            break
                    except ValueError:
                        print("Debe ingresar un valor numérico para el precio.")
           
            elif opcion == 4:
                print("Programa finalizado.")
                break  # Aquí el break es innecesario porque solo hay un ciclo, pero el estudiante lo utiliza para más claridad
               
            else:
                print("Debe seleccionar una opción válida!!")
       
        except ValueError:
            print("Debe seleccionar una opción válida!!")

# Ejecución del programa
if __name__ == "__main__":
    main()