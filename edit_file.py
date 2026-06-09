from pathlib import Path

file_path = input("Arquivo: ")

old_text = input("Texto antigo: ")

new_text = input("Texto novo: ")

path = Path(file_path)

content = path.read_text(
    encoding="utf-8",
    errors="ignore"
)

if old_text not in content:

    print("Texto não encontrado.")
    exit()

preview = content.replace(
    old_text,
    new_text
)

print("\nPREVIEW\n")
print(preview[:3000])

confirm = input(
    "\nAplicar mudança? (s/n): "
)

if confirm.lower() == "s":

    path.write_text(
        preview,
        encoding="utf-8"
    )

    print("Arquivo atualizado!")

else:
    print("Cancelado.")