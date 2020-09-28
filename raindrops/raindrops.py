def convert(number, result=""):
    """
    Este Metodo convierte un número en una cadena que contenga sonidos de gotas
    de lluvia correspondientes a ciertos factores potenciales.


    Parameters
    ----------
    number = numero a convertir.

    Returns
    Retorna Una Cadena de PlingPlongPlang o en su caso el mismo numero
    """

    if number % 3 == 0:
        result = result + "Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        result = f"{number}"
    return result
