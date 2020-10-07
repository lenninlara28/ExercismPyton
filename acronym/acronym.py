def abbreviate(words, acronimo=""):
    """
    Este Metodo Convierte una frase a su acrónimo.

    Parameters
    words : Palabra a abreviar

    Returns
    Retorna las siglas de las iniciales de la frase ingresada
    """

    if "'" in words:
        words = words.replace("'", "")
    words = words.title()
    for letras in words:
        if letras.isalpha and letras.isupper():
            acronimo = acronimo + letras[0].upper()
    return acronimo
