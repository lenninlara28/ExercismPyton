def distance(strand_a, strand_b, distancia=0):
    """
    Este Metodo Calcula La Distancia de Hamming de dos cadenas de ADN

    Parameters
    ----------
    strand_a : cadena de adn
    strand_b : cadena de adn

    Returns
    este metodo retorna un numero el cual es correspondiente a la distancia de
    hamming de las dos cadenas
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("ValueError")
    else:
        for x in range(len(strand_a)):
            if strand_a[x] != strand_b[x]:
                distancia += 1

    return distancia
