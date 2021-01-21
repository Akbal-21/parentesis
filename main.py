import random as rd


def manual():
    cad = input('ingrese una cadena de parentesis: ')
    start(cad)


def auto():
    k = rd.randint(1, 10)
    cad = ''

    for i in range(k):
        j = rd.choice(['(', ')'])
        cad = f'{cad}{j}'
    print(cad)
    start(cad)


def salir():
    exit()


def start(cad):
    file = open('Grama.txt', 'w')
    cadToList = list(cad)
    parent = []
    Reglas = []
    Reglas.insert(0, 'B')
    print(f'{Reglas} \t \t {" ".join(cadToList)}')
    file.write(f'{" ".join(Reglas)} \t \t \t {" ".join(cadToList)}\n')

    if cad.index('(') == 0:
        for i in range(len(cad)):
            cadToList.pop(0)
            if cad[i] == '(':
                parent.append('(')
                Reglas.insert(0, 'R')
            elif cad[i] == ')':
                AUX = Reglas.pop(0)
                if AUX != 'R':
                    print('Cadena no valida')
                    break
                else:
                    parent.append(')')
            if i < (len(cad)):
                print(parent, end='')
                file.write(f'{" ".join(parent)}')
                print(f'{Reglas} \t \t {" ".join(cadToList)}')
                file.write(f'{" ".join(Reglas)} \t \t \t {" ".join(cadToList)}\n')
    else:
        print('Cadena no valida')
        exit()

    AUX = Reglas.pop(0)
    if not Reglas:
        print('Cadena no valida')
        exit()
    else:
        AUX = Reglas.pop(0)
    if AUX == 'R':
        print('Cadena no valida')
        exit()
    elif AUX == 'B':
        Reglas.append('e')
        print(parent, end=' ')
        print(Reglas)
        file.write(f"{''.join(parent)}{''.join(Reglas)}\n")
        exit()


if __name__ == "__main__":
    print('''
        1.-Manual
        2.-Automatica
        3.-Salir
         ''')
    op = int(input('Ingrese una opcion: '))
    opc = [manual, auto, salir]
    output = opc[op - 1]()
    print(opc)
