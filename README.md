Ringkasan Perubahan v10.0 → v10.1

# Perubahan Manfaat
1 16 search sources dengan fallback berantai Jika GitHub/DDG gagal, otomatis lanjut ke sumber berikutnya
2 Helper _http_get + _clean_html SSL verification aktif, decode entity HTML
3 _search_stackexchange(site) generik SO, Unix SE, AskUbuntu, ServerFault, SuperUser
4 Google / Bing / Reddit / Yandex / Brave scraping Alternatif saat GitHub & DDG down
5 Arch Wiki API Solusi Linux dokumenter berkualitas
6 Searx (4 instance), Mojeek, Marginalia (deep web) Sumber independen non-Google
7 extract_commands diperluas Regex untuk sudo, code-fence, lebih banyak command
8 Body POST wajib dibaca di /fix/start Cegah koneksi menggantung
9 Guard isinstance di learning DB Cegah TypeError dari cache lama
10 ThreadingTCPServer Handle banyak koneksi SSE bersamaan
11 BrokenPipe handling di SSE Tidak crash saat client disconnect
12 Fallback ke /tmp jika /var/log read-only Bisa jalan di container tanpa root

🚀 Cara Pakai

```bash
# Mode web
python3 autofixdetect.py --web
# → http://localhost:8080

# Mode CLI
python3 autofixdetect.py
```

⚠️ Catatan

· "Deep web" di sini = search engine independen (Marginalia, Mojeek, Searx) — bukan onion/Tor. Untuk Tor asli butuh stem + requests[socks] + daemon tor.
· try_fix menjalankan perintah dari internet dengan shell=True — jangan jalankan sebagai root tanpa whitelist di environment produksi.
· Google/Bing/Brave scraping bisa kena rate-limit; cache mencegah spam berulang.
