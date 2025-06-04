def pattern_count(teks, pattern):
    panjang_teks = len(teks)
    panjang_pattern = len(pattern)

    if panjang_pattern == 0 or panjang_pattern > panjang_teks:
        return 0

    jumlah = 0
    posisi = 0

    while posisi <= panjang_teks - panjang_pattern:
        cocok = True
        for i in range(panjang_pattern):
            if teks[posisi + i] != pattern[i]:
                cocok = False
                break
        if cocok:
            jumlah = jumlah + 1
        posisi = posisi + 1

    return jumlah

# Contoh 1
teks = "palindrom"
pattern = "ind"
hasil = pattern_count(teks, pattern)
print("Input  :", teks)
print("Pattern:", pattern)
print("Output :", hasil)
print()

# Contoh 2
teks = "abakadabra"
pattern = "ab"
hasil = pattern_count(teks, pattern)
print("Input  :", teks)
print("Pattern:", pattern)
print("Output :", hasil)
print()

# Contoh 3
teks = "hello"
pattern = ""
hasil = pattern_count(teks, pattern)
print("Input  :", teks)
print("Pattern:", pattern)
print("Output :", hasil)
print()

# Contoh 4
teks = "ababab"
pattern = "aba"
hasil = pattern_count(teks, pattern)
print("Input  :", teks)
print("Pattern:", pattern)
print("Output :", hasil)
print()

# Contoh 5
teks = "aaaaaa"
pattern = "aa"
hasil = pattern_count(teks, pattern)
print("Input  :", teks)
print("Pattern:", pattern)
print("Output :", hasil)
print()

# Contoh 6
teks = "hell"
pattern = "hello"
hasil = pattern_count(teks, pattern)
print("Input  :", teks)
print("Pattern:", pattern)
print("Output :", hasil)
print()
