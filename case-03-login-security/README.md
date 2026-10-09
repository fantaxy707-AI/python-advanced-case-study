&#x20;Studi Kasus 3: Sistem Keamanan Akun \& Audit Log Login



Proyek ini mensimulasikan sistem validasi keamanan akun dan pencatatan riwayat login (audit trail) secara otomatis menggunakan Python.



&#x20;Konsep yang Digunakan



1\. Enkapsulasi \& Validation (‘@property’):

&#x20;  Memproteksi atribut ‘username’ dan ‘password’ pada class ‘User’ agar tidak dapat diisi data yang tidak valid secara langsung.



2\. Regular Expressions (‘re’):

&#x20;  - Username: Memastikan input berupa alfanumerik dan memiliki panjang minimal 5 karakter (‘^\[a-zA-Z0-9]{5,}$’).

&#x20;  - Password: Memastikan input memiliki panjang minimal 8 karakter dan mengandung setidaknya satu angka (‘^(?=.\\d).{8,}$’).



3\. Decorator (‘audit\_log’):

&#x20;  Bertindak sebagai wrapper pada fungsi login untuk mencegat dan mencatat timestamp, username, serta status percobaan login (BERHASIL/DITOLAK) beserta alasannya tanpa mengubah logika utama fungsi login.



Cara Menjalankan



1\. Pastikan berada di direktori ‘case-03-login-security’.

2\. Jalankan perintah berikut di terminal:

&#x20;  ‘‘‘bash

&#x20;  python main.py

