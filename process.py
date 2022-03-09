import sys

bad_suffix2 = "  ZAKUP PRZY UŻYCIU KARTY W KRAJU"
bad_suffix = "                                                     transakcja nierozliczona"
contents = sys.stdin.readlines()

transactions = []

while True:
    if len(contents) == 0:
        break

    entry = contents.pop()
    if len(entry.strip()) == 0:
        continue
    
    transactions.append(entry.replace(" PLN", "").replace(bad_suffix, "").replace(bad_suffix2, "").strip())
    
    if entry.strip().startswith('#'):
        break


transactions.reverse()

print("\n".join(transactions), end='')

