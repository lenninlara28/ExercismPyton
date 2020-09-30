def is_isogram(string):
    """
    Este Metodo define si una palabra es un isograma o no

    Parameters
    ----------
    string : Palabra a definir

    Returns
    retorna un true si la palabra es un isograma o false si no lo es.
    """
    string = string.lower()
    for x in range(len(string)):
        for i in range(len(string)):
            if x != i and string[x] == string[i] and string[x].isalpha():
                return False

    return True
