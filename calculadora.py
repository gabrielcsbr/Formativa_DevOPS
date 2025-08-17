class Calculadora:
    # Soma dois números
    def soma(self, a: float, b: float) -> float:
        return a + b

    # Subtrai o segundo número do primeiro
    def subtracao(self, a: float, b: float) -> float:
        return a - b

    # Multiplica dois números
    def multiplicacao(self, a: float, b: float) -> float:
        return a * b

    # Divide o primeiro número pelo segundo, tratando divisão por zero
    def divisao(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("🚫 Erro: Divisão por zero não é permitida!")
        return a / b



if __name__ == "__main__":
    calc = Calculadora()

    print("\n==============================")
    print("🧮✨ Bem-vindo à Calculadora✨🧮")
    print("==============================\n")
    print("Aqui você pode realizar operações básicas de matemática 🎉\n")

    while True:
        print("\n🔹 Escolha uma operação:")
        print("➕ 1 - Soma")
        print("➖ 2 - Subtração")
        print("✖️ 3 - Multiplicação")
        print("➗ 4 - Divisão")
        print("🚪 5 - Sair")
        print("------------------------------")

        opcao = input("👉 Digite sua escolha: ")

        if opcao == "5":
            print("\n👋 Obrigado por usar a Calculadora! Até logo! ✨\n")
            break

        try:
            print("\nDigite os números para calcular:")
            n1 = float(input("🔢 Primeiro número: "))
            n2 = float(input("🔢 Segundo número: "))

            if opcao == "1":
                print(f"\n✅ Resultado: {n1} + {n2} = {calc.soma(n1, n2)}")
            elif opcao == "2":
                print(f"\n✅ Resultado: {n1} - {n2} = {calc.subtracao(n1, n2)}")
            elif opcao == "3":
                print(f"\n✅ Resultado: {n1} × {n2} = {calc.multiplicacao(n1, n2)}")
            elif opcao == "4":
                print(f"\n✅ Resultado: {n1} ÷ {n2} = {calc.divisao(n1, n2)}")
            else:
                print("\n⚠️ Opção inválida! Tente novamente.")
        except ValueError as e:
            print(f"\n🚫 Erro: {e}")
