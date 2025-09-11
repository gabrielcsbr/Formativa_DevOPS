"""
Calculadora Simples — Projeto Somativa DevOPS
Arquivo principal da aplicação de terminal (Python 3.10+).

"""

__author__ = "Gabriel Cordeiro Antero"
__version__ = "1.0.0"
__license__ = "MIT"



class Calculadora:
    """Operações aritméticas básicas usadas pela interface de terminal."""

    def soma(self, a: float, b: float) -> float:
        """Retorna a soma de a e b."""
        return a + b

    def subtracao(self, a: float, b: float) -> float:
        """Retorna a subtração de a por b."""
        return a - b

    def multiplicacao(self, a: float, b: float) -> float:
        """Retorna o produto de a e b."""
        return a * b

    def divisao(self, a: float, b: float) -> float:
        """Retorna a divisão de a por b (lança ValueError se b == 0)."""
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
