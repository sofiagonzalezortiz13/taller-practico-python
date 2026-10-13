from pathlib import Path
import runpy


def main():
    carpeta_ejercicios = Path(__file__).resolve().parent
    ejercicios = sorted(
        (archivo for archivo in carpeta_ejercicios.glob("*.py") if archivo.name != Path(__file__).name),
        key=lambda archivo: archivo.name.lower(),
    )

    if not ejercicios:
        print("No hay ejercicios disponibles.")
        return

    while True:
        print("\n=== Menú de ejercicios ===")
        for numero, ejercicio in enumerate(ejercicios, start=1):
            nombre = ejercicio.stem.replace("_", " ").capitalize()
            print(f"{numero}. {nombre}")
        print("0. Salir")

        opcion = input("Elige un ejercicio: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if not opcion.isdigit() or not 1 <= int(opcion) <= len(ejercicios):
            print("Opción no válida. Intenta de nuevo.")
            continue

        ejercicio_elegido = ejercicios[int(opcion) - 1]
        print(f"\n--- Iniciando {ejercicio_elegido.stem} ---")
        runpy.run_path(str(ejercicio_elegido), run_name="__main__")


if __name__ == "__main__":
    main()