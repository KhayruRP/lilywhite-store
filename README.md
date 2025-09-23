# lilywhite-store
Nama: Khayru Rafamanda Prananta
Kelas: PBP F
NPM: 2406495893


TUGAS 3
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


TUGAS 4
1. AuthenticationForm itu formulir login siap pakai dari Django. Fungsinya sederhana yaitu menerima nama pengguna dan password, lalu cek apakah kombinasi keduanya benar dan akun masih aktif. Kalau ada yang salah, formulir ini otomatis memberi pesan error. Biasanya dipakai bersama LoginView, jadi bisa punya fitur login yang “langsung jalan” tanpa bikin validasi sendiri.

Kelebihan
- Cepat dipakai
- Aman -> Validasi sudah benar, terhubung ke sistem autentikasi Django, dan pesan error tidak “membocorkan” detail sensitif.
- Terintegrasi
- Bisa diubah bebas: Bisa ganti label, pesan, atau tampilan (widget) tanpa harus menulis ulang logikanya.

Kekurangan
- Sederhana banget: Hanya username & password. Kalau mau login pakai email, nomor HP/OTP, atau 2FA, perlu custom atau pakai paket lain.
- Tampilan standar: Form ini tidak memberi gaya (UI) khusus. tetap perlu CSS/komponen sendiri agar terlihat modern.
- Fleksibilitas terbatas: Untuk alur login yang unik (misalnya “remember me”, captcha, rate-limit, kebijakan password khusus), biasanya harus subclass dan menambah logika.
- Kurang cocok untuk API/SPA: Ini dibuat untuk halaman HTML klasik. Kalau login via JSON/REST, lebih pas pakai Django REST Framework atau solusi lain.

2. Autentikasi itu memastikan siapa saya. Ibarat satpam cek identitas di pintu. Sedangkan otorisasi menentukan boleh ngapain setelah masuk—ibarat aturan, saya boleh ke lantai 2 tapi tidak ke ruang arsip. Di Django, saya login (misalnya pakai username–password). Kalau cocok, Django menandai saya sebagai “sudah masuk” sehingga halaman lain mengenali identitas saya. Setelah itu, Django menerapkan aturan akses seperti ada halaman yang hanya bisa dibuka jika sudah login, ada aksi yang butuh peran tertentu (misalnya editor atau admin), dan ada izin spesifik untuk menambah, mengubah, atau menghapus data. Jadi alurnya simpel: pertama identitas diverifikasi, lalu hak akses saya diperiksa sebelum suatu halaman atau tindakan diizinkan.

Setelah identitas saya jelas, Django mengecek apakah saya punya izin untuk melakukan tindakan tertentu: bisa berdasarkan peran/kelompok (misalnya “editor” atau “admin”) atau berdasarkan aksi spesifik seperti tambah, ubah, hapus, atau lihat pada data tertentu. Praktiknya, akses ke halaman atau fungsi “dipagar”—contohnya pakai aturan yang mewajibkan sudah login dulu, lalu ditambah pengecekan izin apakah saya memang berhak melakukan aksi tersebut. Di halaman admin Django hal ini paling terasa: hanya akun dengan hak yang tepat yang bisa masuk dan mengubah data

3. Cookies
Kelebihan:
- Tersimpan di browser, jadi tidak membebani server.
- Bertahan antar kunjungan (mis. tetap login, preferensi bahasa).
- Mudah dibaca dari front-end untuk hal ringan (tema gelap/terang).

Kekurangan:
- Ukuran kecil (umumnya <4 KB per cookie).
- Rentan dicuri/diubah kalau isinya sensitif atau tidak diamankan; ikut terkirim di setiap request sehingga menambah trafik.
- Butuh persetujuan/aturan privasi (mis. banner cookie).
- Risiko XSS/CSRF jika pengamanan lemah.

Session (server-side)
Kelebihan:
- Data sensitif tetap di server, browser cuma pegang ID-nya → lebih aman.
- Ukuran fleksibel dan mudah ganti struktur data.
- Bisa dibatalkan/di-logout pusat (hapus di server).

Kekurangan:
- Butuh penyimpanan server (memori/DB/redis), bisa memberatkan kalau user banyak.
- Skalabilitas lebih ribet (perlu sticky session atau shared store).
- Kedaluwarsa saat sesi habis, jadi kurang cocok untuk preferensi jangka panjang tanpa kombinasi lain.

4. Singkatnya, cookies tidak otomatis “aman” secara default—ada beberapa risiko yang perlu diwaspadai: bisa disadap di jaringan kalau tidak lewat HTTPS, dicuri via XSS (JavaScript jahat membaca cookie), disalahgunakan untuk CSRF (permintaan palsu memanfaatkan sesi aktif), atau disalahkonfigurasi (domain/path terlalu luas, masa berlaku terlalu lama, third-party tracking).

Bagaimana Django menanganinya?
- Atribut keamanan cookie: Django mendukung Secure (hanya terkirim lewat HTTPS), HttpOnly (tidak terbaca JavaScript), dan SameSite (default umumnya Lax untuk membatasi CSRF). Atur lewat SESSION_COOKIE_SECURE, SESSION_COOKIE_HTTPONLY, SESSION_COOKIE_SAMESITE, serta padanan untuk CSRF (CSRF_COOKIE_SECURE, CSRF_COOKIE_SAMESITE).
- Proteksi CSRF bawaan: CsrfViewMiddleware aktif pada proyek standar, membantu mencegah serangan CSRF.
- Penandatanganan (signing): Saat memakai backend cookie-based session, data sesi ditandatangani dengan SECRET_KEY (tidak bisa diubah penyerang tanpa ketahuan), meski tetap terbaca jika tidak dienkripsi—karena itu hindari menyimpan data sensitif di sana.
- Best practices siap pakai: Pakai HTTPS + SECURE_SSL_REDIRECT, pertimbangkan HSTS (SECURE_HSTS_SECONDS), set masa berlaku wajar (SESSION_COOKIE_AGE), batasi domain/path, dan jangan menaruh informasi rahasia langsung di cookie.

