import json
from pathlib import Path

print("=" * 50)
print("EXTRATOR DE SÍMBOLOS")
print("=" * 50)

symbol_name = input("\nSímbolo: ").strip()

# Carrega símbolos
with open("symbols.json", "r", encoding="utf-8") as f:
    symbols = json.load(f)

# Arquivos encontrados
files_found = set()

for item in symbols:

    if item["symbol"].lower() == symbol_name.lower():
        files_found.add(item["file"])

if not files_found:
    print("\nSímbolo não encontrado.")
    exit()

# Cria pasta de saída
output_dir = Path("extracted_symbols")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / f"{symbol_name}.txt"

with open(output_file, "w", encoding="utf-8") as out:

    out.write(f"SÍMBOLO: {symbol_name}\n")
    out.write("=" * 80 + "\n\n")

    for file_path in sorted(files_found):

        out.write("\n")
        out.write("=" * 80 + "\n")
        out.write(f"ARQUIVO: {file_path}\n")
        out.write("=" * 80 + "\n\n")

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                content = f.read()

            out.write(content)
            out.write("\n\n")

            print(f"[OK] {file_path}")

        except Exception as e:

            print(f"[ERRO] {file_path}")
            print(e)

print("\nArquivo gerado:")
print(output_file)