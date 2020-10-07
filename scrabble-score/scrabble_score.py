def score(word, puntaje=0):
    """
    Este Metodo calcula un puntaje para una palabra, tomando puntos por letras

    Parameters
    word : palabra a calcular puntaje

    Returns
    retorna el puntaje de la palabra ingresada
    """

    for le in word.lower():
        if le in "aeioulnrst":
            puntaje = puntaje + 1
        if le in "dg":
            puntaje = puntaje + 2
        if le in "bcmp":
            puntaje = puntaje + 3
        if le in "fhvwy":
            puntaje = puntaje + 4
        if le in "k":
            puntaje = puntaje + 5
        if le in "jx":
            puntaje = puntaje + 8
        if le in "qz":
            puntaje = puntaje + 10
    return puntaje
