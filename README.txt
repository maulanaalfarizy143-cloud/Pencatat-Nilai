# Pencatat Nilai Ujian - Android APK

Aplikasi Python + Kivy untuk:
- mencatat nilai siswa per mata pelajaran
- menghitung rata-rata setiap siswa
- menampilkan siswa dengan rata-rata tertinggi
- menampilkan siswa dengan rata-rata terendah

## Cara membuat APK

Gunakan Linux/WSL Ubuntu yang sudah terpasang Python dan Buildozer.

1. Masuk ke folder proyek.
2. Instal dependensi:
   `pip install buildozer`
3. Jalankan:
   `buildozer android debug`
4. APK akan muncul di folder `bin/`.

Jika Buildozer meminta dependensi Android/Java/SDK, ikuti instruksi instalasinya.

File utama aplikasi: `main.py`
Konfigurasi APK: `buildozer.spec`
