# 06_palindromo.py

def verificar_palindromo() -> None:
    """Verifica se uma palavra ou frase é um palíndromo."""

    print("=== Verificador de Palíndromos ===")

    texto = input("Digite uma palavra ou frase: ")

    # Remove espaços, pontuações simples e converte para minúsculas
    texto_limpo = "".join(
        char.lower() for char in texto if char.isalnum()
    )

    # Inverte o texto
    texto_invertido = texto_limpo[::-1]

    if texto_limpo == texto_invertido:
        print(f"✅ '{texto}' é um palíndromo!")
    else:
        print(f"❌ '{texto}' não é um palíndromo.")


if __name__ == "__main__":
    verificar_palindromo()
