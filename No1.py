list = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

huruf = []
angka = []

for item in list:
    item_str = str(item)
    if item_str.isalpha():
        huruf.append(item)
    else:
        angka.append(item)
huruf.sort()
angka.sort()

hasil = huruf + angka
print(hasil)
