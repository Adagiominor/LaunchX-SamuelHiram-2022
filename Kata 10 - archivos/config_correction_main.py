#SAMUEL HIRAM CASTRO MARTINEZ, KATA 10, INNOVACION VIRTUAL 2022

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError:
        print("No se puede abrir, error de permisos. uwu")


if __name__ == '__main__':
    main()
