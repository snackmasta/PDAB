# 1. Pengertian Sistem PDAB

## 1.1 Definisi Umum

Sistem PDAB (Pengolahan dan Distribusi Air Bersih) adalah sistem simulasi terintegrasi yang dirancang untuk mempelajari dan memahami proses distribusi air bersih dengan fokus pada integrasi teknologi desalinasi dan sistem penyimpanan bertingkat (roof tank). Sistem ini merupakan platform pembelajaran yang menggabungkan prinsip-prinsip engineering distribusi air dengan implementasi kontrol otomatis untuk memberikan pemahaman komprehensif tentang operasi sistem distribusi air modern yang terintegrasi dengan teknologi desalinasi.

## 1.2 Konsep Dasar Sistem Distribusi Air Bersih

Sistem Pengolahan dan Distribusi Air Bersih (PDAB) merupakan sistem terintegrasi yang menggabungkan aspek pengolahan air melalui desalinasi dengan sistem distribusi yang efisien menggunakan konsep penyimpanan bertingkat. Fokus utama sistem ini adalah pada distribusi air bersih yang optimal dengan memanfaatkan teknologi desalinasi reverse osmosis sebagai sumber air dan sistem roof tank sebagai komponen kunci distribusi gravitasi.

Desalinasi dalam konteks sistem PDAB berfungsi sebagai teknologi pengolahan air untuk menghasilkan air bersih berkualitas yang kemudian didistribusikan melalui sistem penyimpanan dan distribusi yang terintegrasi. Teknologi reverse osmosis (RO) bekerja dengan memaksa air melalui membran semipermeabel menggunakan tekanan tinggi, menghasilkan air tawar yang siap untuk didistribusikan.

Sistem roof tank menjadi komponen strategis dalam distribusi air bersih karena memungkinkan distribusi gravitasi yang efisien dan menyediakan tekanan distribusi yang stabil tanpa ketergantungan kontinyu pada pompa distribusi. Konsep dual storage (ground tank dan roof tank) memberikan fleksibilitas operasional dan redundansi dalam penyediaan air bersih.

## 1.3 Komponen Utama Sistem PDAB

### 1.3.1 Tahapan Proses Sistem PDAB

Sistem PDAB terdiri dari enam tahapan proses utama yang saling terintegrasi untuk mencapai distribusi air bersih yang optimal:

- **Pengambilan Air Baku (Intake)**: Tahap awal dimana air laut diambil dari sumber dan dipompa menggunakan pompa intake (P-101) menuju sistem pengolahan. Sensor flow transmitter (FT-101) memantau laju aliran air masuk untuk memastikan supply yang memadai bagi proses distribusi.
- **Pra-perlakuan (Pre-treatment)**: Proses filtrasi awal untuk menghilangkan partikel tersuspensi dan kontaminan yang dapat mengganggu proses pengolahan dan kualitas air yang akan didistribusikan. Sensor turbidity (TU-101) memantau tingkat kekeruhan air setelah pra-perlakuan.
- **Unit Reverse Osmosis (RO)**: Komponen pengolahan air yang menghasilkan air bersih berkualitas tinggi untuk distribusi. Pompa tekanan tinggi (P-102) dan sistem monitoring (PT-101, PT-102, FT-102) memastikan produksi air bersih yang konsisten untuk kebutuhan distribusi.
- **Pasca-perlakuan (Post-treatment)**: Tahap finalisasi kualitas air yang meliputi disinfeksi menggunakan UV (UV-101) dan pompa transfer (P-103) untuk mempersiapkan air bersih sebelum masuk ke sistem distribusi.
- **Penyimpanan dan Distribusi Primer**: Ground tank dengan sensor level (LT-101) berfungsi sebagai buffer storage utama yang mengumpulkan air bersih hasil pengolahan sebelum didistribusikan ke level yang lebih tinggi.
- **Distribusi Sekunder dan Roof Tank**: Sistem pompa transfer (P-104, P-105, P-106) mengalirkan air dari ground storage ke roof tank (LT-102) yang menjadi komponen kunci distribusi gravitasi untuk melayani titik-titik konsumsi dengan tekanan yang stabil dan efisien.

### 1.3.2 Sistem Kontrol dan Instrumentasi Distribusi

Sistem PDAB menggunakan arsitektur kontrol otomatis yang dirancang khusus untuk mengoptimalkan distribusi air bersih:

- **Sensor Network**: Tujuh sensor utama (TU-101, FT-101, FT-102, PT-101, PT-102, LT-101, LT-102) yang mengumpulkan data operasional secara real-time untuk monitoring parameter kritis distribusi seperti flow, pressure, level storage, dan kualitas air yang didistribusikan.
- **Control Logic**: Sistem kontrol berbasis Python yang memproses data sensor dan mengimplementasikan algoritma kontrol untuk mengatur operasi distribusi air, termasuk logika transfer antar storage dan kontrol tekanan distribusi.
- **Human Machine Interface (HMI)**: Interface berbasis Tkinter yang menyediakan visualisasi real-time status sistem distribusi, kontrol manual pompa transfer, dan monitoring level storage untuk operator.
- **Actuator Network**: Sepuluh aktuator utama termasuk pompa distribusi (P-101 hingga P-106), valve kontrol aliran (V-101), UV disinfection (UV-101), sistem alarm (ALM-101), dan pressure relief valve (PRV-101) yang mengeksekusi strategi distribusi dari sistem kontrol.

## 1.4 Prinsip Operasi Sistem Distribusi

### 1.4.1 Mode Operasi

Sistem PDAB dapat beroperasi dalam dua mode utama untuk mengoptimalkan distribusi air bersih:

- **Mode Otomatis**: Sistem beroperasi secara otomatis berdasarkan logika kontrol distribusi yang telah diprogram, dengan monitoring kontinyu terhadap level storage, pressure distribusi, dan automatic transfer air dari ground tank ke roof tank berdasarkan demand dan level setpoints.
- **Mode Manual**: Operator dapat mengambil kontrol manual melalui HMI untuk mengoperasikan pompa distribusi individual, terutama untuk keperluan maintenance sistem distribusi, testing kapasitas transfer, atau kondisi emergency dalam penyediaan air.

### 1.4.2 Safety Systems

Sistem dilengkapi dengan multiple safety features untuk melindungi infrastructure distribusi dan memastikan kontinuitas penyediaan air:

- **Alarm System**: Sistem alarm (ALM-101) yang terintegrasi memberikan warning dini terhadap kondisi abnormal dalam distribusi seperti level storage ekstrem, tekanan distribusi berlebih, atau gangguan pada sistem transfer air.
- **Pressure Relief**: Valve PRV-101 berfungsi sebagai pressure relief untuk melindungi sistem distribusi dari tekanan berlebih yang dapat merusak infrastruktur perpipaan dan storage.
- **Interlocking Logic**: Logika kontrol yang mencegah operasi berbahaya dalam sistem distribusi, seperti menjalankan pompa transfer tanpa supply air yang memadai di ground tank atau mengoperasikan sistem pada kondisi alarm aktif yang dapat mengganggu kontinuitas distribusi.

## 1.5 Tujuan Sistem Simulasi Distribusi

### 1.5.1 Pembelajaran Engineering Distribusi Air

Sistem PDAB dirancang sebagai platform pembelajaran yang memberikan pemahaman praktis tentang:
- Prinsip dasar sistem distribusi air bersih dengan teknologi desalinasi terintegrasi
- Integrasi sistem instrumentasi dan kontrol otomatis dalam distribusi air
- Design consideration untuk sistem penyimpanan bertingkat (ground tank dan roof tank)
- Operational challenges dalam sistem distribusi air dengan sumber desalinasi

### 1.5.2 Demonstrasi Teknologi Distribusi

Sistem menyediakan demonstrasi interaktif tentang:
- Control loop feedback dalam sistem distribusi air
- Human-machine interaction dalam automation sistem distribusi
- Process monitoring dan data acquisition untuk sistem storage dan transfer
- Safety system implementation dalam infrastruktur distribusi air

### 1.5.3 Pengembangan Kompetensi Distribusi Air

Platform ini memungkinkan pengembangan kompetensi dalam:
- System design dan process engineering untuk distribusi air
- Industrial automation dan control systems untuk infrastruktur air
- Process optimization dan troubleshooting sistem distribusi
- Operational management sistem distribusi air terintegrasi

## 1.6 Keunggulan Sistem PDAB

### 1.6.1 Modularitas

Desain modular memungkinkan pemahaman sistem distribusi secara bertahap, dimana setiap subsistem (intake, pengolahan, storage, distribusi) dapat dipelajari secara individual sebelum memahami integrasi keseluruhan sistem distribusi air.

### 1.6.2 Fleksibilitas Konfigurasi

Parameter operasi distribusi dapat disesuaikan melalui file konfigurasi untuk mempelajari berbagai skenario distribusi, pola konsumsi, dan condition handling dalam sistem penyediaan air.

### 1.6.3 Real-time Visualization

Interface HMI menyediakan visualisasi real-time yang memudahkan pemahaman tentang dynamic behavior sistem distribusi, level storage, dan interaksi antar komponen distribusi.

### 1.6.4 Comprehensive Monitoring

Sistem menyediakan monitoring lengkap terhadap seluruh parameter distribusi penting, memberikan insight tentang performance sistem distribusi, efisiensi transfer, dan operational efficiency.

Sistem PDAB merepresentasikan integrasi antara teknologi pengolahan air (desalinasi) dengan sistem distribusi air modern yang menggunakan konsep penyimpanan bertingkat dan kontrol otomatis, menyediakan platform pembelajaran yang komprehensif untuk memahami kompleksitas operasi sistem distribusi air bersih dalam konteks engineering yang praktis dan aplikatif.
