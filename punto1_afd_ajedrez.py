import re

# Expresión regular del lenguaje
patron = r'^[a-z]{1,3}(->|X)[a-z]{1,2}[0-9]?$'

def verificar_movimiento(mov):
    
    if re.match(patron, mov):
        print("ACEPTA")
    else:
        print("NO ACEPTA")


def main():

    print("Verificador de movimientos de ajedrez")

    while True:
        mov = input("Ingrese movimiento (o 'salir'): ")

        if mov.lower() == "salir":
            break

        verificar_movimiento(mov)


if __name__ == "__main__":
    main()