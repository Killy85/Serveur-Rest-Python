import elffile

if __name__ == "__main__":
    try:
        f = elffile.open(name='acc')
        print("Gazi il est content tu as compris le format")
    except:
        print("Bouffe ta mère chien de la casse, c'est pas un exec!");