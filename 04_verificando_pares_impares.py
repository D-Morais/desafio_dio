# 04_par_ou_impar.py

def verificar_paridade() -> None:
    """Verifica se um número inteiro é par ou ímpar."""

    print("=== Verificador de Números Pares e Ímpares ===")

    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")
        return

    if numero % 2 == 0:
        print(f"O número {numero} é PAR ✅")
    else:
        print(f"O número {numero} é ÍMPAR 🔹")


if __name__ == "__main__":
    verificar_paridade()
