def hitung_biaya_hotel(jenis_kamar, lama_menginap):
    if jenis_kamar == "standard":
        tarif = 200000
    elif jenis_kamar == "deluxe":
        tarif = 350000
    else:
        tarif = 0

    total_biaya = tarif * lama_menginap
    return total_biaya

jenis_kamar = input("masukkan jenis kamar (standard/deluxe): ")
tanggal_checkin = int(input("masukkan tanggal check-in: "))
tanggal_checkout = int(input("masukkan tanggal check-out: "))

lama_menginap = tanggal_checkout - tanggal_checkin
total = hitung_biaya_hotel(jenis_kamar, lama_menginap)

print("Jenis Kamar       :", jenis_kamar)
print("Tanggal Check-in  :", tanggal_checkin)
print("Tanggal Check-out :", tanggal_checkout)
print("Lama Menginap     :", lama_menginap, "malam")
print("Total Biaya       : Rp", total)