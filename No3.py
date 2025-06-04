def hitung_huruf(teks):
    hasil = {}

    for huruf in teks:
        if huruf.isalpha():
            if huruf in hasil:
                hasil[huruf] += 1
            else:
                hasil[huruf] = 1

    hasil_urut = dict(sorted(hasil.items(), key=lambda x: x[0].lower()))

    list_hasil = []
    for k, v in hasil_urut.items():
        list_hasil.append(f'“{k}”: {v}')
    output = "[" + ", ".join(list_hasil) + "]"

    return output

print('Input : "Hello World"')
print("Output :", hitung_huruf("Hello World"))
print('Input : "Bismillah"')
print("Output :", hitung_huruf("Bismillah"))
print('Input : "MasyaAllah"')
print("Output :", hitung_huruf("MasyaAllah"))
