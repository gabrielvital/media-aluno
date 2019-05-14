# ESTE CÓDIGO É APENAS UM EXERCÍCIO DE FIXAÇÃO DE ALGUNS CONCEITOS
# A IDEIA É COMPOR UM BOLETIM COM AS NOTAS DE DETERMINADO ALUNO EM DIFERENTES DISCIPLINAS
# AO FINAL, O CÓDIGO EXECUTA UM CÁLCULO PARA INFORMAR O COEFICIENTE DE RENDIMENTO DESTE ALUNO

matriz = [[1,2,3],[4,5,6]]

print("Boletim do aluno")
nome = input("Insira o nome do aluno: ")

print("Veja os códigos das disciplinas")
print("\n 1. Português"
      "\n 2. Matemática"
      "\n 3. Ciências"
      "\n 4. História"
      "\n 5. Geografia"
      "\n 6. Informática"
      "\n")

discip = 11
while discip != 0:
    discip = int(input("Digite o código da disciplina ou 0 (zero) para encerrar: "))

    if discip == 1:
        print("PORTUGUÊS")
        p1 = float(input("PROVA 1: "))
        p2 = float(input("PROVA 2: "))
        trab = float(input("TRABALHO: "))
        media = (p1 + p2 + trab) / 3
        matriz[0][0] = (p1 + p2 + trab) / 3

        print("Média: PORTUGUÊS: ", media)

        if media >= 7:
            print("APROVADO")
        else:
            if media < 5:
                print("REPROVADO")
            else:
                print("EM RECUPERAÇÃO")

    if discip == 2:
        print("MATEMÁTICA")
        p1 = float(input("PROVA 1: "))
        p2 = float(input("PROVA 2: "))
        trab = float(input("TRABALHO: "))
        media = (p1 + p2 + trab) / 3
        matriz[0][1] = (p1 + p2 + trab) / 3

        print("Média: MATEMÁTICA: ", media)

        if media >= 7:
            print("APROVADO")
        else:
            if media < 5:
                print("REPROVADO")
            else:
                print("EM RECUPERAÇÃO")

    if discip == 3:
        print("CIÊNCIAS")
        p1 = float(input("PROVA 1: "))
        p2 = float(input("PROVA 2: "))
        trab = float(input("TRABALHO: "))
        media = (p1 + p2 + trab) / 3
        matriz[0][2] = (p1 + p2 + trab) / 3

        print("Média: CIÊNCIAS: ", media)

        if media >= 7:
            print("APROVADO")
        else:
            if media < 5:
                print("REPROVADO")
            else:
                print("EM RECUPERAÇÃO")

    if discip == 4:
        print("HISTÓRIA")
        p1 = float(input("PROVA 1: "))
        p2 = float(input("PROVA 2: "))
        trab = float(input("TRABALHO: "))
        media = (p1 + p2 + trab) / 3
        matriz[1][0] = (p1 + p2 + trab) / 3

        print("Média: HISTÓRIA: ", media)

        if media >= 7:
            print("APROVADO")
        else:
            if media < 5:
                print("REPROVADO")
            else:
                print("EM RECUPERAÇÃO")

    if discip == 5:
        print("GEOGRAFIA")
        p1 = float(input("PROVA 1: "))
        p2 = float(input("PROVA 2: "))
        trab = float(input("TRABALHO: "))
        media = (p1 + p2 + trab) / 3
        matriz[1][1] = (p1 + p2 + trab) / 3

        print("Média: GEOGRAFIA: ", media)

        if media >= 7:
            print("APROVADO")
        else:
            if media < 5:
                print("REPROVADO")
            else:
                print("EM RECUPERAÇÃO")

    if discip == 6:
        print("INFORMÁTICA")
        p1 = float(input("PROVA 1: "))
        p2 = float(input("PROVA 2: "))
        trab = float(input("TRABALHO: "))
        media = (p1 + p2 + trab) / 3
        matriz[1][2] = (p1 + p2 + trab) / 3

        print("Média: INFORMÁTICA: ", media)

        if media >= 7:
            print("APROVADO")
        else:
            if media < 5:
                print("REPROVADO")
            else:
                print("EM RECUPERAÇÃO")

else:
    print("Boletim de {}".format(nome))
    print("PORTUGUÊS: ", matriz[0][0])
    print("MATEMÁTICA: ", matriz[0][1])
    print("CIÊNCIAS: ", matriz[0][2])
    print("HISTÓRIA: ", matriz[1][0])
    print("GEOGRAFIA: ", matriz[1][1])
    print("INFORMÁTICA: ", matriz[1][2])
    cr = (matriz[0][0]+matriz[0][1]+matriz[0][2]+matriz[1][0]+matriz[1][1]+matriz[1][2])/6
    print("COEFICIENTE DE RENDIMENTO (CR): ", cr)
