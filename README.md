Project 1: Import & Clean Retail Sales Data to PostgreSQL

Deskripsi
Proyek ini bertujuan untuk mengimpor data penjualan dari file CSV, melakukan pembersihan data, lalu menyimpannya ke PostgreSQL menggunakan Python.

Alur Proses
1. Membuat tabel `staging_sales` di PostgreSQL (DDL)
2. Membaca file CSV menggunakan pandas
3. Membersihkan data:
   - Merapikan nama kolom
   - Konversi format tanggal
   - Menghapus duplikat
   - Menghapus data null
   - Memfilter quantity 0
4. Mengimpor data ke tabel `staging_sales` di PostgreSQL

Struktur Folder
project_1_import_sales/
│── data/
│ └── Superstore.csv
│── import_sales.py
│── requirements.txt
│── README.md

Tools & Library
- Python 3.x
- PostgreSQL
- pandas
- psycopg2
- SQLAlchemy

Instalasi
1. Clone repository ini:
```bash
git clone https://github.com/ikhramfahrezi/project_1_staging_saless.git#
