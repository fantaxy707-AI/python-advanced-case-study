Studi Kasus 2: Simulasi Sensor IoT



Kode ini mensimulasikan pembacaan suhu dari sensor IoT secara terus-menerus.



Konsep yang dipakai di sini adalah fungsi generator dengan perintah ‘yield’. Alasannya murni buat efisiensi memori. Bayangkan kalau sensor mengirim jutaan data suhu sekaligus, RAM laptop pasti jebol kalau disuruh menampung semuanya barengan di dalam satu variabel atau list biasa. 



Dengan memakai ‘yield’, program hanya memproduksi dan mengeluarkan satu angka suhu tepat saat kita memintanya lewat perintah ‘next()’. Setelah mengeluarkan satu angka, fungsinya akan "tidur" lagi sampai dipanggil ulang. Cara ini bikin memori tetap aman dan ringan meskipun aliran datanya tidak terbatas.



Cara menjalankan skrip:

Pastikan berada di folder ‘case-02-iot-generator’, lalu ketik ‘python main.py’ di terminal atau tekan tombol Run di editor.



