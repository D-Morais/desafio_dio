# 03_operacoes_matematicas.py

def operacoes_matematicas() -> None:
    """Realiza uma operação matemática simples entre dois números informados pelo usuário."""
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: digite apenas números válidos.")
        return

    print("\nEscolha a operação desejada:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    operacao = input("Digite o número da operação: ").strip()

    if operacao == "1":
        resultado = num1 + num2
        simbolo = "+"
    elif operacao == "2":
        resultado = num1 - num2
        simbolo = "-"
    elif operacao == "3":
        resultado = num1 * num2
        simbolo = "*"
    elif operacao == "4":
        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
            return
        resultado = num1 / num2
        simbolo = "/"
    else:
        print("Operação inválida. Tente novamente.")
        return

    print(f"\nResultado: {num1} {simbolo} {num2} = {resultado:.2f}")


if __name__ == "__main__":
    operacoes_matematicas()
