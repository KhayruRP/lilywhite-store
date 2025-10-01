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
show_items → mengambil data Items berdasarkan id menggunakan get_object_or_404, mengembalikan 404 jika tidak ditemukan.

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

5. PROSEDUR
Registrasi (membuat akun)
Buka main/views.py, import UserCreationForm dan messages.
Tambahkan view register(request) yang:
- Inisialisasi UserCreationForm().
- Pada POST, validasi form.is_valid(), lalu form.save() untuk membuat user baru.
Buat main/templates/register.html, extend base.html, render form dengan {{ form.as_table }}, dan tombol submit. Sertakan {% csrf_token %}.
Daftarkan URL: di main/urls.py, path('register/', register, name='register').

Login
Di main/views.py, import AuthenticationForm, authenticate, dan login.
Tambahkan view login_user(request) yang:
Pada POST, buat AuthenticationForm(data=request.POST); jika valid, ambil user = form.get_user() dan panggil login(request, user).
Jika GET, buat AuthenticationForm(request) lalu render template.
Buat main/templates/login.html untuk merender form login (pakai {{ form.as_table }}, {% csrf_token %}, dan tautan ke halaman register).
Tambahkan URL path('login/', login_user, name='login').

Logout
Di main/views.py, import juga logout.
Tambahkan view logout_user(request) yang memanggil logout(request) lalu redirect('main:login').
Tambahkan tombol Logout di main/templates/main.html:
<a href="{% url 'main:logout' %}"><button>Logout</button></a>
(Gunakan {% url 'app_name:view_name' %} untuk resolusi URL dinamis.)
Tambahkan URL path('logout/', logout_user, name='logout').

Restriksi akses (hanya user login yang boleh masuk)
Di main/views.py, import login_required.
Pasang decorator @login_required(login_url='/login') di atas view yang ingin dibatasi (mis. show_main, show_Items). Pengunjung yang belum login akan dialihkan ke /login.

Menyimpan & menampilkan “last_login” via Cookies
Di main/views.py, import datetime, HttpResponseRedirect, reverse.
Pada login_user, setelah login(request, user), alih-alih redirect() langsung:
Buat response = HttpResponseRedirect(reverse("main:show_main"))
Set cookie: response.set_cookie('last_login', str(datetime.datetime.now()))
return response
Di show_main, pada context, ambil cookie aman dengan default:
'last_login': request.COOKIES.get('last_login', 'Never')

(Akan tampil di template sebagai info waktu login terakhir.)
Pada logout_user, setelah logout(request) kembalikan HttpResponseRedirect(...) lalu response.delete_cookie('last_login').
Tampilkan di main.html:
<h5>Sesi terakhir login: {{ last_login }}</h5>
(Opsional) Verifikasi cookie last_login, sessionid, csrftoken via DevTools → Application → Cookies.

Mengaitkan model konten (Items) ke User
Di main/models.py, import User dari django.contrib.auth.models.
Tambah field relasi:
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
on_delete=CASCADE: hapus user → seluruh Items user ikut terhapus.
null=True: data lama tetap valid meski belum punya user.
Migrasi skema: python manage.py makemigrations && python manage.py migrate. (WAJIB setiap ubah model.)
Di view pembuatan konten (mis. create_Items), simpan objek form dengan commit=False, isi Items_entry.user = request.user, lalu save().
Di show_main, sediakan filter berdasarkan query string:
filter=all → Items.objects.all()
filter=my → Items.objects.filter(user=request.user)
Juga ganti name pada context menjadi request.user.username.

Di main.html, tambahkan tombol filter:
<a href="?filter=all"><button type="button">All Items</button></a>
<a href="?filter=my"><button type="button">My Items</button></a>


TUGAS 5
1) Dalam CSS, kalau ada beberapa selector yang mengatur elemen yang sama, browser akan memilih aturan berdasarkan spesifisitas (specificity) dan urutan penulisan. Prinsipnya, aturan yang lebih spesifik akan menang dari yang lebih umum. Urutannya seperti ini: inline style (misalnya style="..." langsung di elemen HTML) memiliki prioritas paling tinggi, lalu disusul oleh ID selector (contoh #judul), kemudian class, attribute, dan pseudo-class selector (contoh .container, [type="text"], :hover), dan terakhir element/tag selector (contoh div, p, h1). Jika ada dua aturan dengan tingkat spesifisitas yang sama, maka yang ditulis paling akhir di file CSS atau HTML akan digunakan. Selain itu, ada juga aturan !important yang bisa memaksa sebuah deklarasi CSS untuk diprioritaskan, meskipun sebenarnya cara ini sebaiknya dipakai hanya jika benar-benar diperlukan.

2) Responsive design penting agar tampilan dan fungsi web tetap nyaman dipakai di berbagai ukuran layar (HP, tablet, desktop) tanpa zoom/scroll horizontal, yang berdampak langsung pada UX, aksesibilitas, SEO, dan konversi. Contoh yang sudah responsif: Tokopedia/Instagram Web—grid, tipografi, dan tombol menyesuaikan lebar layar sehingga navigasi dan aksi tetap mudah di ponsel maupun desktop. Contoh yang belum/kurang responsif: banyak portal pemerintah lama atau situs sekolah lama—layout tabel fixed dan form melebar memaksa pengguna melakukan zoom dan scroll samping, membuat pengisian sulit serta rawan salah. Kesimpulannya, tanpa responsive design, situs cepat ditinggalkan pengguna mobile yang jumlahnya dominan.

3) Margin, border, dan padding adalah tiga hal penting dalam pengaturan tata letak elemen di sebuah halaman web. Margin merupakan jarak yang berada di luar sebuah elemen dan berfungsi untuk mengatur seberapa jauh elemen tersebut dari elemen lain di sekitarnya. Sementara itu, border adalah garis tepi yang mengelilingi elemen, mirip seperti bingkai foto yang membatasi isi dengan bagian luarnya. Padding berbeda lagi, yaitu ruang kosong di dalam elemen, antara isi konten (seperti teks atau gambar) dengan garis tepi (border). Dengan kata lain, margin mengatur jarak luar, border menjadi pembatas, dan padding mengatur jarak dalam. Ketiganya bisa diatur menggunakan CSS, misalnya dengan menuliskan margin: 20px; untuk memberi jarak luar, border: 2px solid black; untuk membuat bingkai hitam, dan padding: 15px; agar isi tidak terlalu menempel pada pinggir kotak. Bagi saya sebagai mahasiswa yang baru belajar, memahami perbedaan ketiganya sangat membantu untuk membuat tampilan web lebih rapi dan enak dilihat.

4) Flexbox dan Grid Layout adalah dua konsep penting dalam CSS yang digunakan untuk mengatur tata letak elemen di halaman web. Flexbox (flexible box) digunakan untuk menyusun elemen secara satu dimensi, artinya kita bisa dengan mudah mengatur posisi elemen secara horizontal (baris) atau vertikal (kolom). Misalnya, dengan flexbox kita bisa membuat menu navigasi agar otomatis merata, atau membuat elemen-elemen di dalam sebuah baris menyesuaikan ukuran ruang yang tersedia.

Sedangkan Grid Layout lebih cocok untuk tata letak dua dimensi, yaitu baris dan kolom sekaligus. Dengan grid, kita bisa membagi halaman menjadi beberapa bagian seperti header, sidebar, konten utama, dan footer, lalu menempatkan elemen sesuai posisi grid yang sudah didefinisikan. Grid memberi kontrol yang lebih rapi untuk layout yang kompleks.

Secara singkat, flexbox berguna saat kita ingin mengatur elemen secara linier dan responsif, seperti tombol yang sejajar atau card yang berderet, sedangkan grid lebih berguna untuk membuat kerangka halaman yang terstruktur dengan baris dan kolom, mirip tabel tapi lebih fleksibel.


5) 
1) Pasang Tailwind, saya menggunakan ini
- Buka templates/base.html.
- Tambahkan meta viewport dan script Tailwind CDN tepat di dalam <head>:
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://cdn.tailwindcss.com"></script>
- Simpan. Ini bikin tampilan responsif di HP dan bisa pakai kelas Tailwind

2) Konfigurasi file statis + CSS global (supaya form rapi)
- Di settings.py, tambahkan middleware WhiteNoise pas di bawah SecurityMiddleware, dan atur STATIC_URL, STATICFILES_DIRS (mode dev) / STATIC_ROOT (mode production). Contohnya ada di hal. 10
- Buat folder static/css/ lalu file global.css
- Hubungkan global.css ke base.html dengan {% load static %} dan <link rel="stylesheet" href="{% static 'css/global.css' %}"/>. 

3) Navbar yang responsif (ada tombol Login/Logout)
- Buat templates/navbar.html berisi judul, link Home, Create Items, dan blok kondisi user (kalau login → tampil “Welcome …” + Logout; kalau belum → Login & Register)
- Styling Tailwind dan tombol menu mobile (burger).
- Di halaman lain, panggil navbar dengan {% include 'navbar.html' %}

4) Halaman Login (rapi + ada pesan error)
- Buat templates/login.html.
- Struktur + kelas Tailwind + cara nampilin error per-field/non-field dan pesan messages.
- (Di views.py) Pakai AuthenticationForm dan login(request, user)

5) Halaman Register (rapi + validasi)
- Buat templates/register.html.
- pastikan views.py memakai UserCreationForm.

6) Kartu Berita & Halaman Home (dengan filter + “Last login”)
- Buat templates/card_items.html untuk 1 kartu berita (gambar, kategori, badge Featured/Hot, judul, ringkasan, tombol Edit/Delete kalau pemilik)
- Buat/ubah templates/main.html:
Header “Latest Football Items”.
Bagian Filter: tombol “All Items” dan “My Items”.
Tampilkan “Last login: {{ last_login }}” di sisi kanan saat user sudah login
Kalau tidak ada berita, tampilkan kartu kosong dengan gambar static/image/no-items.png
(Opsional) Untuk benar-benar mengisi {{ last_login }}, di view login_user kamu bisa set cookie last_login setelah sukses login, lalu di show_main ambil dengan request.COOKIES.get('last_login', 'Never'). Template-nya sudah menyiapkan tempatnya

7) Halaman Detail Items
Buat templates/items_detail.html untuk tampilan 1 artikel lengkap (kategori, tanggal, views, gambar, konten, author)

8) Halaman Create Items
Buat templates/create_items.html berisi form (label, field, error per-field) dan tombol Publish/Cancel

9) Halaman Edit Items
Buat templates/edit_items.html (layout mirip Create)

10) Fitur Edit & Delete di sisi server (views + urls + tombol di UI)
EDIT
- Di views.py, buat fungsi edit_items(request, id) yang ambil objek dengan get_object_or_404, bungkus ItemsForm(instance=items), form.is_valid() → form.save() → redirect. 
- Buat templates/edit_items.html
- Daftarkan URL: path('items/<uuid:id>/edit', edit_items, name='edit_items')
- Tampilkan tombol Edit di kartu/home hanya untuk pemilik berita

DELETE
- Di views.py, buat delete_items(request, id) → get_object_or_404 → delete() → HttpResponseRedirect(reverse('main:show_main'))
- Daftarkan URL: path('items/<uuid:id>/delete', delete_items, name='delete_items')
- Munculkan tombol Delete di kartu/home (hanya pemilik)

11) testing
python manage.py runserver lalu buka http://localhost:8000. Lihat apakah navbar muncul, filter jalan, login/register tampil rapi, tombol Edit/Delete muncul saat login sebagai pemilik dari barang yang di jual.