# lilywhite-store
Nama: Khayru Rafamanda Prananta
Kelas: PBP F
NPM: 2406495893

ScreenShot JSON dan XML: ristek.link/KhayruRPrananta-Tugas2-Screenshot

SOAL
1) Data delivery bertujuan untuk mengirimkan data dari tempat penyimpanan ke orang atau aplikasi yang membutuhkannya. Kita butuh data delivery agar data dari server bisa dikirim ke user atau sistem secara cepat dan selalu terupdate, sehingga informasi dapat dipakai

2) Saya lebih suka JSON karena praktis, ringan, dan sesuai dengan kebutuhan aplikasi modern yang membutuhkan kecepatan serta kemudahan integrasi. JSON menjadi lebih populer dibanding XML karena strukturnya sederhana, mudah dibaca manusia, gampang dicerna oleh berbagai bahasa pemrograman, dan mendukung komunikasi data yang efisien, sehingga banyak digunakan sebagai standar dalam pengembangan API dan platform berbasis web saat ini.

3) Method is_valid() digunakan untuk cek apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang sudah didefinisikan. Validasi ini mmeliputi:
- Apakah semua field yang wajib/required sudah diisi.
- Apakah tipe data yang dimasukkan sesuai
- Apakah aturan tambahan terpenuhi.

Jika semua validasi lolos, is_valid() akan return True. Jika ada kesalahan, akan return False.

Method is_valid() dibutuhkan agar data yang salah tidak masuk ke database, pengguna mendapat feedback yang jelas jika ada kesalahan input, dan keamanan terjaga dari input berbahaya

4) {% csrf_token %} diperlukan untuk mencegah CSRF (Cross-Site Request Forgery) yaitu jenis serangan di mana penyerang memaksa browser korban mengirimkan permintaan (biasanya POST) ke website yang sudah diautentikasi sehingga tindakan tidak diinginkan terjadi atas nama korban.

Kita membutuhkan csrf_token pada form Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), karena tanpa token ini permintaan POST bisa ditolak oleh middleware bawaan Django atau, jika proteksi dimatikan, penyerang dapat membuat halaman berbahaya yang secara otomatis mengirimkan permintaan ke server dengan memanfaatkan cookie sesi korban sehingga tindakan penting seperti mengganti password atau menghapus data dapat dilakukan tanpa sepengetahuan pengguna.

Bagaimana penyerang memanfaatkan ini (alur singkat):
1. Korban login ke xyz.com.
2. Korban mengunjungi halaman jahat milik penyerang.
3. Halaman jahat berisi form atau skrip yang mengirim POST ke xyz.com/change_email/ atau xyz.com/transfer/ dengan parameter yang diinginkan.
4. Browser korban otomatis mengirimkan cookie sesi ke xyz.com, sehingga server menganggap permintaan sah dari korban.
5. Jika server tidak memeriksa CSRF token, aksi itu dijalankan — penyerang berhasil memanfaatkan otorisasi korban.

5) saya akan jelaskan secara singkat saja
1. Buat direktori templates di root proyek dan tambahkan berkas base.html sebagai template dasar dengan blok {% block meta %} dan {% block content %}.

2. Buka settings.py, pada variabel TEMPLATES tambahkan baris 'DIRS': [BASE_DIR / 'templates'], lalu tambahkan URL proyek PWS ke dalam CSRF_TRUSTED_ORIGINS.

3. Buat berkas forms.py di aplikasi main yang berisi ItemsForm (ModelForm) dengan field: title, content, category, thumbnail, dan is_featured.

4. Tambahkan fungsi di views.py:
show_main → mengambil semua objek Items dari database.
create_items → menampilkan dan memproses form penambahan item baru.
show_items → mengambil data News berdasarkan id menggunakan get_object_or_404, mengembalikan 404 jika tidak ditemukan.

5. Update urls.py dengan routing baru untuk fungsi-fungsi di views.py.

6. Buat main.html di folder main/templates, isi blok content untuk menampilkan daftar data items serta tombol “Add Items” yang mengarahkan ke halaman form.

7. Buat dua file template baru di folder templates:
- create_items.html → halaman untuk menambahkan item baru.
- items_detail.html → halaman untuk menampilkan detail item tertentu.

8. TTambahkan method show xml dan json di views.py . juga import HttpResponse dan Serializer pada bagian paling atas. Tambah method show xml dan json by id. 

9. Tambahkan routing URL untuk mengakses data dalam format XML maupun JSON, baik untuk seluruh data maupun berdasarkan id tertentu.