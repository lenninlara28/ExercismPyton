def recite(s_v, end_verse):
    """
    Este Metodo canta la letra de 'The Twelve Days Of Christmas'

    Parameters
    ----------
    start_verse : verso inicial
    end_verse : verso final

    Returns
    retorna la letra de la canción desde el verso inicial ingresado hasta
    el verso final ingresado
    """

    versos = ["", "two Turtle Doves,", "three French Hens,",
              "four Calling Birds, ", "five Gold Rings, ",
              "six Geese-a-Laying, ", "seven Swans-a-Swimming, ",
              "eight Maids-a-Milking, ", "nine Ladies Dancing, ",
              "ten Lords-a-Leaping, ", "eleven Pipers Piping, ",
              "twelve Drummers Drumming, "]
    ini = ["first", "second", "third", "fourth", "fifth", "sixth",
           "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    lt = [f"On the {ini[s_v - 1]} day of Christmas my true love gave to me: "]
    for verso in range(1, end_verse):
        lt.append((versos[s_v - verso]))
    lt.append("and a Partridge in a Pear Tree.")
    return lt
