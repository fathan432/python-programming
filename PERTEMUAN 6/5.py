umur = int(input("Masukan umur anda: "))

if umur < 13:
    print("Anda masih anak-anak")
elif umur >= 13 and umur < 18:
    print("Anda remaja")
elif umur >= 18 and umur < 60:
    print("Anda dewasa")
else:
    print("Anda sudah tua")