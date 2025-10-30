# 01_concatenando_dados.py

def concatenar_dados() -> None:
    """Recebe dois textos e exibe o resultado concatenado."""
    primeiro_texto = input("Digite o primeiro texto: ").strip()
    segundo_texto = input("Digite o segundo texto: ").strip()

    # Forma 1: usando f-string
    resultado = f"{primeiro_texto} {segundo_texto}"

    # Forma 2 (opcional): usando o operador +
    # resultado = primeiro_texto + " " + segundo_texto

    print("\nResultado da concatenação:", resultado)


if __name__ == "__main__":
    concatenar_dados()
