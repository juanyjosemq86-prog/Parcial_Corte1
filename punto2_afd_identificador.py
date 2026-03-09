def es_letra(c):
    return c.isalpha()

def es_numero(c):
    return c.isdigit()


def afd_identificador(cadena):

    estado = "q0"

    for c in cadena:

        if estado == "q0":
            if es_letra(c):
                estado = "q1"
            else:
                estado = "q_dead"

        elif estado == "q1":
            if es_letra(c) or es_numero(c):
                estado = "q1"
            else:
                estado = "q_dead"

        elif estado == "q_dead":
            return "NO ACEPTA"

    if estado == "q1":
        return "ACEPTA"
    else:
        return "NO ACEPTA"


def pruebas_archivo():

    with open("pruebas2.txt", "r") as f:

        for linea in f:
            cadena = linea.strip()
            print(cadena, "->", afd_identificador(cadena))


pruebas_archivo()