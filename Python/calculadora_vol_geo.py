# Función principal
def main():
    width, height, depth = 0.0, 0.0, None
    print("Calculadora de Volumen y Área Geométrica")
    width = get_user_input("Ingrese el ancho en metros : ")
    height = get_user_input("Ingrese la altura en metros : ")
    depth = get_user_input_or_empty("Ingrese la profundidad en metros o vacío para calcular el área: ")
    calculate_area_or_volume(width, height, depth)


# Función para obtener el input de usuario
def get_user_input(msg):
    while True:
        value = input(msg)
        try:
            number = float(value)
            if number < 0:
                print("⚠️ No se permiten números negativos.")
                continue
            return number
        except ValueError:
            print("⚠️ Por favor ingrese números.")


# Función para obtener número o vacío
def get_user_input_or_empty(msg):
    while True:
        valor = input(msg)

        if valor.strip() == "":
            return None

        try:
            return float(valor)
        except ValueError:
            print("⚠️ Ingrese un número o deje vacío.")


# Función para calcular el volumen o el área
def calculate_area_or_volume(width, height, depth):
    if depth is None:
        calculate_area(width, height)
    else:
        calculate_volume(width, height, depth)


# Función para calcular el área
def calculate_area(width, height):
    area = width * height
    print(f"El área es: {area} m2.")


# Función para calcular el volumen
def calculate_volume(width, height, depth):
    volume = width * height * depth
    print(f"El volumen es: {volume} m3.")


# Inicio de la aplicacion de la calculadora de volumen y geometria
if __name__ == "__main__":
    main()