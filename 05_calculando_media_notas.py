# 05_media_notas.py

def calcular_media() -> None:
    """Calcula a média de três notas e informa a situação do aluno."""

    print("=== Calculadora de Média de Notas ===")

    notas = []

    for i in range(1, 4):
        try:
            nota = float(input(f"Digite a {i}ª nota: "))
            if nota < 0 or nota > 10:
                print("Erro: a nota deve estar entre 0 e 10.")
                return
            notas.append(nota)
        except ValueError:
            print("Erro: insira apenas números válidos.")
            return

    media = sum(notas) / len(notas)

    print(f"\nMédia final: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado ✅")
    elif 5 <= media < 7:
        print("Situação: Recuperação ⚠️")
    else:
        print("Situação: Reprovado ❌")


if __name__ == "__main__":
    calcular_media()
