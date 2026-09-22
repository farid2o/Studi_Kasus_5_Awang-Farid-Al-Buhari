## Studi_Kasus_5_Awang-Farid-Al-Buhari
# Sistem Pemesanan Hotel

Program sederhana berbasis Python untuk menghitung biaya pemesanan kamar hotel berdasarkan jenis kamar dan lama menginap (dihitung dari tanggal check-in dan check-out).

## Deskripsi Program

Program ini meminta pengguna memasukkan jenis kamar (standard atau deluxe), tanggal check-in, dan tanggal check-out. Selisih tanggal digunakan untuk menghitung jumlah malam menginap, lalu total biaya dihitung berdasarkan tarif kamar yang dipilih.

Tarif kamar:

Jenis Kamar	Tarif per Malam
Standard	Rp200.000
Deluxe	Rp350.000

## Penjelasan Kode Program
- def hitung_biaya_hotel(jenis_kamar, lama_menginap): Mendefinisikan sebuah function (fungsi) bernama hitung_biaya_hotel yang menerima dua parameter: jenis kamar dan lama menginap. Fungsi ini bertugas menghitung total biaya pemesanan.
- if / elif / else Struktur percabangan yang digunakan untuk menentukan tarif kamar. Program mengecek apakah jenis_kamar sama dengan "standard", jika tidak maka dicek lagi apakah "deluxe". Jika keduanya tidak cocok (misal salah ketik), tarif diset 0 sebagai penanganan kesalahan sederhana.
- total_biaya = tarif * lama_menginap Menghitung total biaya dengan mengalikan tarif per malam dengan jumlah malam menginap.
- return total_biaya Mengembalikan nilai total_biaya dari dalam fungsi, sehingga hasilnya bisa disimpan dan digunakan di luar fungsi (misalnya ditampung ke variabel total).
- input() Digunakan untuk menerima masukan langsung dari pengguna saat program dijalankan (jenis kamar dan tanggal). Hasil dari input() selalu berupa teks (string).
- int(input(...)) Karena tanggal digunakan untuk perhitungan matematika (pengurangan), hasil input() yang berupa teks perlu diubah menjadi bilangan bulat menggunakan int().
- lama_menginap = tanggal_checkout - tanggal_checkin Menghitung jumlah malam menginap dengan mengurangkan tanggal check-out dan tanggal check-in.
- hitung_biaya_hotel(jenis_kamar, lama_menginap) Memanggil fungsi yang telah dibuat dengan mengirimkan data jenis kamar dan lama menginap sebagai argumen, lalu hasilnya disimpan ke variabel total.
- print(...) Menampilkan seluruh informasi pemesanan (jenis kamar, tanggal check-in, tanggal check-out, lama menginap, dan total biaya) ke layar sebagai output akhir program.

## Cara Menjalankan
1. Pastikan Python sudah terinstal di komputer.
2. Simpan kode di atas ke dalam file, misalnya studikasus5.py.
3. Jalankan melalui terminal:
   python studikasus5.py
4. Masukkan jenis kamar (standard/deluxe) dan tanggal check-in serta check-out sesuai permintaan program.


## Screenshot Output Program

### Berikut adalah bukti bahwa program berhasil dijalankan:

<img width="460" height="276" alt="Screenshot 2026-09-22 224016" src="https://github.com/user-attachments/assets/8e0259fa-7f88-4832-b928-b8512e991992" />

