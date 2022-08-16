""" LUIZ FERNANDO REIS PEREIRA, BCC TURMA U, 2° PERIODO"""

""" Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de operações que serão realizadas entre dois conjuntos de dados.  """

OpLines = []; ListOp = []; Arrfile = []; count = 0; Op = -2; j = 0; I = []
with open("infile", 'r') as file:
    QuantOp = file.readline(1)
    QuantLines = 1+int(QuantOp)*3
    while count <= QuantLines:
        count = count + 1 
        var = list(file.readlines(count))
        for j in var:
            if j != '\n':
                if j.find('\n'):
                    j = j.removesuffix("\n")
                Arrfile.append(j)
    for i in range(int(QuantOp)):
        Op = Op+2
        OpLines.append(Arrfile.pop(Op))
file.close
for i in OpLines:
    ConjuntoA = Arrfile.pop(0).split(', '); ConjuntoB = Arrfile.pop(0).split(', '); I.clear()
    if i == "U":
        for a in ConjuntoA:
            if a in ConjuntoB:
                pass                
            else:
                ConjuntoB.append(a)
        print(ConjuntoB)
    elif i == "I":
        for a in ConjuntoA:
            if a in ConjuntoB:
                I.append(a)
    elif i == "D":
        for a in ConjuntoA:
            if a not in ConjuntoB:
                I.append(a)
        print(I)
    elif i == "C":
        ConjuntoA = list(set(ConjuntoA)); ConjuntoB = list(set(ConjuntoB))
        for a in ConjuntoA:
            for b in ConjuntoB:
                print(f'({a}{b})', end=',')
            print('\n')
