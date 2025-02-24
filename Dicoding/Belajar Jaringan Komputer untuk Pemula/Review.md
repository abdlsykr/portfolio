# Hasil Proyek Akhir: Proyek Membangun Web Server 

Dalam proyek ini, **NGINX dikonfigurasi sebagai reverse proxy** untuk mengarahkan lalu lintas ke **server Node.js**, serta menerapkan **rate limiting** guna meningkatkan keamanan dan mencegah penyalahgunaan layanan.  

## **Hasil Implementasi**  
- **Reverse Proxy Berhasil**: NGINX berhasil meneruskan permintaan dari **port 3000 ke 8000**.  
- **Rate Limiting Berfungsi**: Permintaan dari satu IP dibatasi **6 request per menit**, melindungi server dari akses berlebihan.  
- **Server Node.js Berjalan dengan Baik**: Saat diakses melalui NGINX, server merespons dengan **"Hello world!"**.  

## **Kesimpulan**  
Dengan konfigurasi ini, **NGINX mampu berfungsi sebagai reverse proxy** untuk mengelola lalu lintas ke backend **Node.js**, sekaligus **meningkatkan keamanan melalui pembatasan jumlah request per IP**.  
Konfigurasi ini dapat diterapkan dalam **lingkungan produksi** untuk memastikan performa optimal serta melindungi server dari serangan DoS ringan.  

---

## **Capaian Utama**  
✔ **Menyiapkan web server dengan NGINX dan Node.js**  
✔ **Mengonfigurasi NGINX sebagai reverse proxy**  
✔ **Menerapkan rate limiting untuk meningkatkan keamanan**  
