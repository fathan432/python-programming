# Harga tiket berdasarkan kategori usia
harga_anak = 30000
harga_dewasa = 50000
harga_lansia = 35000

# Minta input jumlah pembeli tiket
jumlah_pembeli = int(input("Masukkan jumlah pembeli tiket: "))

# Variabel untuk menyimpan total harga semua tiket
total_harga_semua_tiket = 0

# Loop untuk setiap pembeli
for i in range(jumlah_pembeli):
    print(f"\nPembeli ke-{i + 1}:")
    
    # Minta input usia dan jumlah tiket yang ingin dibeli
    usia = int(input("Masukkan usia pembeli: "))
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
    
    # Tentukan harga tiket berdasarkan kategori usia
    if usia <= 12:
        harga_tiket = harga_anak
    elif 12 < usia <= 60:
        harga_tiket = harga_dewasa
    else:
        harga_tiket = harga_lansia
    
    # Hitung total harga tiket untuk pembeli ini
    total_harga = harga_tiket * jumlah_tiket
    
    # Tambahkan ke total harga semua tiket
    total_harga_semua_tiket += total_harga
    
    # Tampilkan harga tiket untuk pembeli ini
    print(f"Harga tiket untuk pembeli ke-{i + 1}: Rp {harga_tiket}")
    print(f"Total harga untuk pembeli ke-{i + 1}: Rp {total_harga}")

# Tampilkan total harga untuk semua tiket yang dibeli
print(f"\nTotal harga untuk semua tiket yang dibeli: Rp {total_harga_semua_tiket}")