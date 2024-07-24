def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("S. Sair")
        operacao = input("Selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a calculadora")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida")
            continue

        numero_1 = float (input("Primeiro numero:"))
        numero_2 = float (input("Segundo numero:"))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da operação é: ", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da operação é: ", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da operação é: ", resultado)

        else: 
            if numero_2 == 0:
                print("Divisões por zero não são possiveis.")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da operação é: ", resultado)

calculadora()
