import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from texto_magico import inverter_texto, gritar_texto
except ImportError:
    try:
        from texto_magico.texto_magico import inverter_texto, gritar_texto
    except ImportError as exc:
        raise SystemExit("Biblioteca Texto Mágico não encontrada. Execute este app a partir do diretório do submódulo.") from exc


def main() -> None:
    print("=== Texto Mágico ===")
    print("Escolha uma opção:")
    print("1 - Inverter texto")
    print("2 - Gritar texto")
    print("0 - Sair")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        texto = input("Digite o texto: ")
        print(inverter_texto(texto))
    elif opcao == "2":
        texto = input("Digite o texto: ")
        print(gritar_texto(texto))
    elif opcao == "0":
        print("Até logo!")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
