# lilywhite-store
LANGKAH PENGERJAAN [Soal 1]

LANGKAH PERSIAPAN
1. Buat repositori baru di github dan clone di folder tugas 2 ini
2. Buat requirements.txt dan lakukan install dengan pip install -r requirements.txt buat proyek django dengan run 
"django-admin startproject [nama proyek] ." di terminal folder. Untuk proyek kali ini saya namakan lily_white
3. Buka file .env dan tambahkan konfigurasi PRODUCTION=False. buat file .env.prod dengan mengisi kredensial pribadi sesuai yang dikirim di email. 
4. Menambahkan allowed host -> ["localhost", "127.0.0.1"] di settings.py . Di file itu juga tambahkan "PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'"
5. lanjut buat persiapan django

LANGKAH DJANGO
1. Activate virtual environment dengan run "source env/bin/activate"
2. run "python manage.py startapp main" di terminal untuk membuat aplikasi baru dengan nama main. kemudian di file setting.py, di INSTALLED_APPS tambahkan "main" di dalam kurung siku
3. lanjut buat view web

LANGKAH TEMPLATE
1. Buat folder baru yaitu templates dalam folder main. Kemudian di dalam templates buat main.html
LANGKAH TESTING DI LOCAL HOST

LANGAK DEPLOY PWS


