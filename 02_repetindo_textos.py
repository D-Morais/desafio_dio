# 02_repetindo_textos.py

def repetir_texto() -> None:
    """Repete um texto digitado pelo usuário o número de vezes informado."""
    texto = input("Digite o texto que deseja repetir: ").strip()

    try:
        repeticoes = int(input("Digite o número de vezes que deseja repetir o texto: "))
    except ValueError:
        print("Erro: digite um número inteiro válido.")
        return

    if repeticoes <= 0:
        print("Por favor, insira um número maior que zero.")
        return

    resultado = (texto + " ") * repeticoes

    print("\nTexto repetido:")
    print(resultado.strip())


if __name__ == "__main__":
    repetir_texto()
