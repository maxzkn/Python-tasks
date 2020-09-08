command = ""
uzvestas = False
sustabdytas = False

while command.lower() != "quit":
    command = input("Iveskite komanda: ")
    if command.lower() == "start" and uzvestas is False:
        print("Automobilis uzvestas")
        uzvestas = True
        sustabdytas = False
    elif command.lower() == "start" and uzvestas is True:
        print("Automobilis jau uzvestas!")
    elif command.lower() == "stop" and sustabdytas is False:
        print("Automobilis sustabdytas")
        uzvestas = False
        sustabdytas = True
    elif command.lower() == "stop" and sustabdytas is True:
        print("Automobilis jau sustabdytas!")
    elif command.lower() == "help":
        print("""
        Komanda - start - Uzvesti automobili
        Komanda - stop - Sustabdyti automobili
        Komanda - quit - Sustabdyti programa
        """)