import json

query = input("Símbolo: ").strip().lower()

with open("symbols.json", "r", encoding="utf-8") as f:
    symbols = json.load(f)

results = []

for symbol in symbols:

    if query in symbol["symbol"].lower():
        results.append(symbol)

print("\nRESULTADOS:\n")

for item in results:
    print(
        f"[{item['type']}] "
        f"{item['symbol']} "
        f"-> {item['file']}"
    )