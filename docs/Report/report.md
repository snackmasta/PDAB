**PDAB (Penyediaan dan Distribusi Air Bersih)  
DENGAN SUMBER DESALINASI AIR LAUT DAN PENYIMPANAN ROOF TANK**

Disusun untuk Memenuhi Tugas Mata Kuliah Otomasi Gedung Komersial 2

Dosen Pengampu :

**Drs. Dwi Septiyanto , SST., M.Eng**


**DISUSUN OLEH :**

Agung Rambujana 221364002

**JURUSAN TEKNIK ELEKTRO**

**PROGRAM STUDI TEKNIK OTOMASI INDUSTRI**

**TEKNIK OTOMASI INDUSTRI**

**POLITEKNIK NEGERI BANDUNG**

**2025**

DAFTAR ISI

[**1.** **Pengertian Sistem PDAB** 4](#_Toc200437762)

[**1.1** **Konsep Dasar Sistem Distribusi Air Bersih** 4](#_Toc200437763)

[**2.** **Ruang Lingkup Sistem PDAB** 4](#_Toc200437764)

[**3.** **Elemen Dasar dan Jaringan Sistem PDAB** 5](#_Toc200437765)

[**3.1** **Sistem Instrumentasi dan Sensor** 5](#_Toc200437766)

[**3.2. Sistem Aktuator dan Kontrol** 6](#_Toc200437767)

[**4.** **Model Sistem PDAB** 7](#_Toc200437768)

[**4.1. Flowchart Algoritma Logika Kontrol** 7](#_Toc200437769)

[**4.2 Model: Fungsi dan Hubungan PLC dalam Sistem Desalinasi dan PDAB Roof Tank** 8](#_Toc200437770)

[**5.** **Mekanisme Operasi Sistem PDAB** 8](#_Toc200437771)

[**1\. Start/Stop** 8](#_Toc200437772)

[**2\. Pengambilan Air (Intake)** 8](#_Toc200437773)

[**3\. Pra-perlakuan** 8](#_Toc200437774)

[**4\. Reverse Osmosis (RO)** 9](#_Toc200437775)

[**5\. Pasca-perlakuan** 9](#_Toc200437776)

[**6\. Distribusi** 9](#_Toc200437777)

[**7\. Alarm dan Proteksi** 9](#_Toc200437778)

[**8\. Monitoring dan Kontrol** 9](#_Toc200437779)

[**6.** **Posisi Utilitas PDAB** 9](#_Toc200437780)

[**1\. Panel Kontrol** 10](#_Toc200437781)

[**2\. Pompa Intake** 10](#_Toc200437782)

[**3\. Unit Pra-perlakuan** 10](#_Toc200437783)

[**4\. Unit RO** 10](#_Toc200437784)

[**5\. Tangki Ground** 10](#_Toc200437785)

[**6\. Pompa Transfer & Booster** 10](#_Toc200437786)

[**7\. Tangki Rooftop** 11](#_Toc200437787)

[**8\. Sensor** 11](#_Toc200437788)

[**7.** **Perangkat Keras Kendali Utilitas** 11](#_Toc200437789)

[**8.** **Perangkat Lunak Jaringan Kendali** 12](#_Toc200437790)

[1\. Arsitektur HMI 12](#_Toc200437791)

[a. Struktur Kode HMI 12](#_Toc200437792)

[b. Fitur Teknis HMI 12](#_Toc200437793)

[2\. Simulasi Proses (Process Model) 13](#_Toc200437794)

[a. Struktur Model Simulasi 13](#_Toc200437795)

[b. Logika Kontrol (Sesuai PLC) 13](#_Toc200437796)

[c. Interaksi HMI-Simulasi 14](#_Toc200437797)

[3\. Integrasi dan Validasi 14](#_Toc200437798)

[4\. Diagram Integrasi 14](#_Toc200437799)

[5\. Contoh Alur Kerja 14](#_Toc200437800)

[**9.** **HMI** 17](#_Toc200437801)

1. **Pengertian Sistem PDAB**

Sistem PDAB (Pengolahan dan Distribusi Air Bersih) adalah sistem simulasi terintegrasi yang dirancang untuk mempelajari dan memahami proses distribusi air bersih dengan fokus pada integrasi teknologi desalinasi dan sistem penyimpanan bertingkat (roof tank). Sistem ini merupakan platform pembelajaran yang menggabungkan prinsip-prinsip engineering distribusi air dengan implementasi kontrol otomatis untuk memberikan pemahaman komprehensif tentang operasi sistem distribusi air modern yang terintegrasi dengan teknologi desalinasi.

## **1.1 Konsep Dasar Sistem Distribusi Air Bersih**

Sistem Pengolahan dan Distribusi Air Bersih (PDAB) merupakan sistem terintegrasi yang menggabungkan aspek pengolahan air melalui desalinasi dengan sistem distribusi yang efisien menggunakan konsep penyimpanan bertingkat. Fokus utama sistem ini adalah pada distribusi air bersih yang optimal dengan memanfaatkan teknologi desalinasi reverse osmosis sebagai sumber air dan sistem roof tank sebagai komponen kunci distribusi gravitasi.

Desalinasi dalam konteks sistem PDAB berfungsi sebagai teknologi pengolahan air untuk menghasilkan air bersih berkualitas yang kemudian didistribusikan melalui sistem penyimpanan dan distribusi yang terintegrasi. Teknologi reverse osmosis (RO) bekerja dengan memaksa air melalui membran semipermeabel menggunakan tekanan tinggi, menghasilkan air tawar yang siap untuk didistribusikan. Sistem roof tank menjadi komponen strategis dalam distribusi air bersih karena memungkinkan distribusi gravitasi yang efisien dan menyediakan tekanan distribusi yang stabil tanpa ketergantungan kontinyu pada pompa distribusi. Konsep dual storage (ground tank dan roof tank) memberikan fleksibilitas operasional dan redundansi dalam penyediaan air bersih.

1. **Ruang Lingkup Sistem PDAB**

Ruang lingkup sistem Pengolahan dan Distribusi Air Bersih (PDAB) mencakup semua aspek sistem yang dirancang untuk menghasilkan air bersih berkualitas tinggi melalui proses desalinasi. Dokumen ini menjelaskan batasan sistem secara detail, meliputi komponen fisik, operasional, dan kontrol yang tergabung dalam satu sistem distribusi air bersih.

Pentingnya mendefinisikan ruang lingkup sistem secara jelas adalah untuk memastikan semua pihak memiliki pemahaman yang sama tentang cakupan proyek, tanggung jawab masing-masing bagian sistem, dan hubungan dengan sistem luar. Ruang lingkup yang jelas akan mengurangi ketidakjelasan dalam pelaksanaan dan memudahkan proses perawatan serta pemecahan masalah.

Ruang lingkup sistem PDAB meliputi seluruh proses, mulai dari pengambilan air baku (intake), praolah (filtrasi dan penghilangan kotoran), proses utama (reverse osmosis), pascaolah (remineralisasi dan desinfeksi), penyimpanan air bersih, hingga distribusi kepada pengguna akhir. Selain itu, ruang lingkup juga mencakup sistem kontrol otomatis (PLC/HMI), pemantauan parameter proses, alarm, serta integrasi dengan sistem utilitas lain apabila diperlukan.

1. **Elemen Dasar dan Jaringan Sistem PDAB**

## **3.1 Sistem Instrumentasi dan Sensor**

1. Level Transmitter

Level transmitter digunakan untuk mengukur ketinggian air pada berbagai jenis tangki dalam sistem pengolahan air, seperti reservoir, clarifier, dan filter tank. Teknologi pengukuran yang digunakan dapat berupa ultrasonic, radar, maupun pressure-based, tergantung pada kebutuhan dan kondisi instalasi. Alat ini memiliki jangkauan pengukuran dari 0 hingga 10 meter dengan tingkat akurasi tinggi sebesar ±0.1%. Sinyal keluarannya tersedia dalam bentuk analog 4–20 mA maupun digital berbasis protokol Modbus, sehingga dapat dengan mudah diintegrasikan ke dalam sistem kontrol otomatis.

1. Flow Meter

Flow meter berfungsi untuk mengukur laju aliran air pada berbagai titik dalam sistem, termasuk air baku, air produk, dan air reject. Jenis flow meter yang digunakan adalah electromagnetic flow meter karena kemampuannya memberikan pengukuran yang akurat tanpa hambatan fisik di dalam pipa. Kapasitas pengukurannya mencapai 0–500 liter per menit dengan akurasi ±0.5%. Data dari sensor ini sangat penting untuk monitoring performa sistem secara real-time dan memastikan distribusi air berjalan sesuai perencanaan.

1. Pressure Sensor

Pressure sensor dipasang untuk memantau tekanan di berbagai bagian sistem, terutama pada membran reverse osmosis (RO), pompa, dan jaringan pipa distribusi. Sensor ini memiliki jangkauan pengukuran dari 0 hingga 10 bar dengan resolusi hingga 0.01 bar, yang memungkinkan deteksi perubahan tekanan secara akurat. Sensor ini sangat krusial karena berperan dalam melindungi membran RO dari kerusakan akibat tekanan yang berlebihan atau tidak stabil. Sistem dilengkapi dengan alarm tekanan tinggi (lebih dari 8 bar) dan tekanan rendah (kurang dari 2 bar) untuk mengantisipasi kondisi abnormal yang dapat mengganggu operasi sistem.

1. Turbidity Sensor

Sensor kekeruhan (turbidity sensor) digunakan untuk memantau kualitas air berdasarkan tingkat kekeruhannya. Alat ini memiliki rentang pengukuran dari 0 hingga 1000 NTU (Nephelometric Turbidity Units) dan dipasang pada beberapa titik penting, seperti sebelum proses pengolahan (pre-treatment), setelah proses (post-treatment), dan pada air hasil akhir (product water). Pemantauan kekeruhan merupakan aspek penting dalam pengendalian mutu air, karena standar kualitas air minum yang aman harus mengacu pada panduan dari World Health Organization (WHO).

1. Conductivity/TDS Meter

Conductivity/TDS meter digunakan untuk mengukur konduktivitas listrik dan kandungan Total Dissolved Solids (TDS) dalam air. Rentang pengukuran alat ini adalah 0–2000 µS/cm, yang cukup untuk memantau efektivitas proses desalinasi air. Sensor ini dipasang pada beberapa titik strategis seperti saluran air baku (feed water), permeate (hasil RO), dan concentrate (limbah RO), guna memastikan bahwa sistem beroperasi dengan efisien dan menghasilkan air berkualitas tinggi.

## **3.2. Sistem Aktuator dan Kontrol**

1. Sistem Pompa

Sistem ini terdiri dari beberapa jenis pompa yang berfungsi untuk mendukung proses pengambilan, pemindahan, dan distribusi air. Intake pump merupakan pompa sentrifugal berdaya 5 HP yang digunakan untuk mengambil air baku dari sumber. High pressure pump, dengan daya 15 HP, digunakan untuk memberikan tekanan tinggi pada sistem reverse osmosis. Transfer pump berdaya 3 HP bertugas memindahkan air antar tangki dalam proses pengolahan. Sementara itu, booster pump berdaya 2 HP digunakan untuk mendistribusikan air ke jaringan pengguna. Seluruh pompa dikendalikan menggunakan Variable Frequency Drive (VFD) yang memungkinkan pengaturan kecepatan motor secara fleksibel dan efisien, sekaligus menghemat energi.

1. Valve Motorized

Untuk mengatur aliran cairan dalam sistem, digunakan katup bermotor (motorized valve) dengan jenis ball valve dan butterfly valve yang dilengkapi dengan aktuator elektrik. Fungsi utama katup ini mencakup pengaturan aliran (flow control), isolasi bagian sistem, serta mendukung operasi backwash pada filter. Katup ini dapat dikendalikan melalui sinyal analog 4–20 mA maupun sinyal digital on/off. Dengan waktu respons kurang dari 30 detik untuk membuka atau menutup penuh, katup ini memastikan proses kontrol berlangsung cepat dan akurat.

1. Sistem Disinfeksi UV

Sistem disinfeksi UV bertugas mensterilisasi air dari mikroorganisme patogen yang berbahaya. Sistem ini menggunakan lampu UV berdaya 40 watt dengan intensitas iradiasi sebesar 30 mJ/cm² yang efektif untuk membunuh bakteri dan virus. Untuk menjamin performa sistem, sensor intensitas UV dipasang untuk memantau efektivitas pencahayaan, serta indikator status lampu guna mendeteksi kerusakan atau penurunan kinerja. Sistem ini juga dilengkapi dengan sistem pembersih otomatis untuk menjaga lensa UV tetap bersih dari endapan dan kotoran.

1. Sistem Alarm dan Indikasi

Untuk mendukung pengawasan sistem, digunakan sistem alarm dan indikasi yang terdiri dari beberapa media. Secara visual, sistem dilengkapi panel LED dan layar HMI untuk menampilkan status operasional secara langsung. Dalam situasi darurat, alarm suara (horn) akan menyala untuk memberikan peringatan kepada operator. Selain itu, sistem ini juga mendukung notifikasi jarak jauh melalui SMS dan email, memungkinkan respons cepat terhadap kondisi abnormal. Seluruh kejadian penting dalam sistem dicatat secara otomatis dalam bentuk log lengkap dengan penanda waktu (timestamp), sehingga dapat ditelusuri kembali untuk keperluan analisis dan audit.

1. **Model Sistem PDAB**

## ![A diagram of a flowchart


4.2 Model: Fungsi dan Hubungan PLC dalam Sistem Desalinasi dan PDAB Roof Tank**

1. **Mekanisme Operasi Sistem PDAB**

## **1\. Start/Stop**

Pengop\`erasian sistem dapat dimulai atau dihentikan melalui HMI. Operator memiliki kontrol penuh untuk melakukan start atau stop seluruh proses, baik secara manual maupun otomatis sesuai jadwal atau kondisi tertentu.

## **2\. Pengambilan Air (Intake)**

Pompa intake akan aktif secara otomatis jika level air pada tangki ground berada di bawah ambang batas minimum dan seluruh kondisi pra-perlakuan telah terpenuhi. Sistem akan memastikan bahwa air baku yang diambil memenuhi syarat untuk diproses lebih lanjut.

## **3\. Pra-perlakuan**

Pada tahap ini, air baku melewati filter untuk menghilangkan partikel kasar dan kotoran. Jika tekanan diferensial pada filter melebihi batas yang ditentukan, sistem akan menjalankan proses backwash (pencucian balik) secara otomatis untuk menjaga performa filter.

## **4\. Reverse Osmosis (RO)**

Pompa RO akan aktif jika proses pra-perlakuan selesai dan level air pada tangki cukup. Sistem akan memantau tekanan dan parameter lain secara kontinu. Jika terdeteksi tekanan abnormal atau kondisi tidak aman, pompa RO akan berhenti secara otomatis untuk mencegah kerusakan.

## **5\. Pasca-perlakuan**

Setelah proses RO, air hasil olahan akan melalui tahap remineralisasi dan desinfeksi. Kedua proses ini berjalan secara paralel dengan output RO untuk memastikan air yang dihasilkan memenuhi standar kualitas.

## **6\. Distribusi**

Pompa transfer dan booster akan aktif berdasarkan level air pada tangki rooftop. Sistem akan memastikan distribusi air ke jaringan pelanggan berjalan lancar dan tekanan tetap stabil.

## **7\. Alarm dan Proteksi**

Jika terjadi kondisi abnormal seperti tekanan berlebih, level air tidak normal, atau turbidity tinggi, sistem akan memicu alarm dan secara otomatis mematikan pompa terkait untuk mencegah kerusakan lebih lanjut.

## **8\. Monitoring dan Kontrol**

Seluruh parameter proses (tekanan, level, kualitas air, status pompa, dsb.) dapat dipantau secara real-time melalui HMI. Operator dapat melakukan penyesuaian setpoint, melihat histori alarm, dan melakukan troubleshooting jika diperlukan.

Dengan mekanisme operasi ini, sistem PDAB dapat berjalan secara otomatis, efisien, dan aman, serta memudahkan pemantauan dan pengendalian oleh operator.

1. **Posisi Utilitas PDAB**


## **1\. Panel Kontrol**

Panel kontrol ditempatkan di ruang kontrol atau dekat area proses utama. Lokasi ini dipilih agar operator mudah memantau dan mengendalikan seluruh sistem, serta memudahkan akses saat troubleshooting atau pemeliharaan.

## **2\. Pompa Intake**

Pompa intake dipasang di area sumber air (sumur atau laut) untuk memudahkan pengambilan air baku secara langsung dan mengurangi kehilangan tekanan akibat jarak distribusi.

## **3\. Unit Pra-perlakuan**

Unit pra-perlakuan ditempatkan dekat intake dan sebelum unit RO. Penempatan ini memastikan air baku yang masuk ke RO sudah melalui proses penyaringan awal, sehingga memperpanjang umur membran RO.

## **4\. Unit RO**

Unit RO berada di ruang proses utama, biasanya terpusat dengan akses mudah untuk pemantauan dan perawatan. Penempatan ini juga mempertimbangkan kebutuhan ruang dan keamanan dari paparan lingkungan luar.

## **5\. Tangki Ground**

Tangki ground diletakkan setelah unit RO dan sebelum pompa transfer. Fungsinya sebagai penampung sementara air hasil olahan sebelum didistribusikan lebih lanjut.

## **6\. Pompa Transfer & Booster**

Pompa transfer dan booster ditempatkan di ruang pompa, di antara tangki ground dan tangki rooftop. Penempatan ini memudahkan pengaturan tekanan dan aliran air ke tangki rooftop maupun ke jaringan distribusi.

## **7\. Tangki Rooftop**

Tangki rooftop dipasang di atap bangunan untuk memanfaatkan gravitasi dalam distribusi air ke seluruh jaringan pelanggan, serta sebagai cadangan saat terjadi gangguan pasokan.

## **8\. Sensor**

Sensor (level, tekanan, flow, turbidity) dipasang pada titik-titik strategis di seluruh sistem, seperti pada tangki, pipa, dan unit proses. Penempatan sensor disesuaikan dengan kebutuhan monitoring dan kontrol otomatis.


Sistem otomatisasi pengolahan air ini dikendalikan oleh PLC (Programmable Logic Controller) tipe Siemens S7-1200, yang mendukung komunikasi Modbus/TCP dan dapat diintegrasikan dengan HMI. Pengukuran level air pada tangki ground dan rooftop dilakukan oleh sensor ultrasonik (LT-101 dan LT-102) yang memiliki output analog 4–20 mA. Untuk pemantauan tekanan, digunakan sensor tekanan digital (PT-101 dan PT-102) dengan rentang 0–10 bar yang dipasang pada jalur feed dan permeate dari sistem Reverse Osmosis (RO). Laju aliran air pada intake dan output RO diukur menggunakan flowmeter elektromagnetik (FT-101 dan FT-102) dengan rentang 0–20 m³/jam. Kualitas air sebelum perlakuan lebih lanjut dipantau menggunakan sensor kekeruhan optik (TU-101) dengan rentang pengukuran 0–100 NTU.

Sistem ini juga dilengkapi dengan beberapa pompa sentrifugal untuk keperluan intake, RO, transfer, booster, dan post-treatment, yang masing-masing dilengkapi proteksi terhadap thermal dan overload. Pengaturan aliran air di berbagai jalur proses dilakukan secara otomatis oleh PLC melalui enam valve bermotor (V-101 hingga V-106) tipe on/off. Untuk proses desinfeksi, digunakan unit UV (UV-101) berkapasitas 2 m³/jam yang dipasang pada outlet air hasil RO. Sistem peringatan menggunakan alarm (ALM-101) berupa sirine dan lampu indikator untuk memberi sinyal kondisi abnormal, seperti level air rendah, tekanan tinggi, atau kegagalan pompa. Seluruh sistem dikendalikan melalui panel kontrol berbahan mild steel dengan tingkat perlindungan IP54, yang berisi PLC, relay, terminal, sistem proteksi, serta HMI touchscreen berukuran 7 inci.

1. **Perangkat Lunak Jaringan Kendali**

## 1\. Arsitektur HMI

HMI (Human Machine Interface) pada sistem ini dikembangkan menggunakan Python dengan library Tkinter, yang berfungsi sebagai antarmuka operator untuk monitoring dan kontrol sistem desalinasi secara real-time. HMI terhubung langsung ke model simulasi Python, sehingga setiap perubahan status proses langsung tercermin di tampilan HMI.

### a. Struktur Kode HMI

- **File Utama:** src/hmi.py
- **Kelas Utama:** DesalinationHMI
- **Fungsi Kunci:**
  - \_build_gui(): Membangun seluruh elemen GUI (indikator status, tombol kontrol, tren data, dsb).
  - update(): Sinkronisasi tampilan dengan status proses.
  - start_system(), stop_system(), emergency_stop(): Kontrol utama sistem.
  - drain_roof_tank(): Simulasi konsumsi air dari roof tank.

### b. Fitur Teknis HMI

- **Status Real-Time:**
  - Setiap sensor (level, tekanan, turbidity) dan aktuator (pompa, valve, UV, alarm) ditampilkan dengan indikator ON/OFF dan nilai aktual.
  - Status diambil langsung dari instance DesalinationSystem (model simulasi).
- **Alarm & Safety:**
  - Alarm kritis (misal: tekanan di luar batas, level tangki rendah/tinggi, turbidity tinggi) ditampilkan dengan warna dan notifikasi.
  - Emergency Stop akan mematikan seluruh aktuator dan mengunci sistem hingga reset manual.
- **Trend Data:**
  - Menggunakan Matplotlib untuk menampilkan grafik tren level tangki, tekanan, dan parameter utama lain secara live.
- **User Interaction:**
  - Semua perintah (start, stop, emergency, drain) langsung memanggil method pada model simulasi.

## 2\. Simulasi Proses (Process Model)

Simulasi proses dikembangkan dalam Python (src/process.py) dan merepresentasikan seluruh dinamika sistem desalinasi secara matematis dan logis.

### a. Struktur Model Simulasi

- **Kelas Utama:** DesalinationSystem
- **Parameter Kunci:**
  - Level tangki (ground & roof), tekanan RO, turbidity, status pompa/valve/UV/alarm
  - Setpoint dan batas operasi diatur di src/config.py (misal: GROUND_TANK_MIN/MAX, PRESSURE_MIN/MAX, TURBIDITY_MAX)
- **Fungsi Kunci:**
  - step(): Satu siklus simulasi, menghitung perubahan variabel proses dan status aktuator berdasarkan logika kontrol.
  - get_status(): Mengembalikan status lengkap untuk HMI.
  - start(), stop(), emergency_stop(): Mengatur state sistem sesuai perintah HMI.

### b. Logika Kontrol (Sesuai PLC)

- **PreTreatment_OK:** pre_treatment_turbidity < TURBIDITY_MAX
- **RO_OK:** PreTreatment_OK and ground_tank_level > 20 and PRESSURE_MIN < ro_feed_pressure < PRESSURE_MAX
- **Aktuator:**
  - Intake Pump (intake_pump): ON jika RO_OK dan ground_tank_level < GROUND_TANK_MAX
  - RO Pump (ro_pump): ON jika RO_OK
  - Transfer Pump (transfer_pump): ON jika ground_tank_level > 30 dan roof_tank_level < 90
  - P-103 s/d P-106, V-101, UV-101, PRV-101, ALM-101: Semua logika sesuai tabel I/O dan PLC (lihat src/process.py dan docs/control-plan.md)
- **Alarm:**
  - Aktif jika: turbidity > 10, tekanan &lt; 45 atau &gt; 75, ground_tank_level &lt; 10, roof_tank_level &gt; 98

### c. Interaksi HMI-Simulasi

- HMI membaca status dari model simulasi setiap update.
- Setiap aksi di HMI (start, stop, emergency, drain) langsung mengubah state di model simulasi.
- Semua perubahan status proses (misal: alarm, ON/OFF pompa) langsung tercermin di HMI.

## 3\. Integrasi dan Validasi

- **Konsistensi:** Semua logika kontrol di simulasi identik dengan PLC (Structured Text) dan tabel I/O.
- **Validasi:** Simulasi digunakan untuk menguji seluruh skenario operasi, alarm, dan safety sebelum implementasi fisik.
- **Ekspansi:** Arsitektur modular memudahkan penambahan fitur baru (misal: mode manual, logging data, remote monitoring).

## 4\. Diagram Integrasi

+-------------------+ +-------------------+  
| HMI (Tkinter) | &lt;-----&gt; | Model Simulasi |  
| - GUI/Control | | (DesalinationSys)|  
| - Trend Data | | - Logika Kontrol |  
| - Alarm Display | | - Dinamika Proses|  
+-------------------+ +-------------------+

## 5\. Contoh Alur Kerja

1. Operator menekan START di HMI → HMI memanggil start() pada model → Model mengecek precondition, mengaktifkan pompa/aktuator sesuai logika → Status ON/OFF dan nilai sensor langsung tampil di HMI.
2. Jika terjadi kondisi abnormal (misal tekanan > 75 bar), model mengaktifkan alarm → HMI menampilkan notifikasi alarm dan status merah.
3. Emergency Stop di HMI → Semua aktuator OFF, alarm aktif, sistem terkunci hingga reset.

| Tag/Name | Type | Description | Location | PLC Variable | HMI Display |
| --- | --- | --- | --- | --- | --- |
| LT-101 | AI  | Ground Tank Level Transmitter | Ground Tank | LT_101 | ground |
| LT-102 | AI  | Roof Tank Level Transmitter | Roof Tank | LT_102 | roof |
| FT-101 | AI  | Intake Flow Transmitter | Intake Line | FT_101 | (not displayed) |
| FT-102 | AI  | RO Permeate Flow Transmitter | RO Outlet | FT_102 | (not displayed) |
| PT-101 | AI  | RO Feed Pressure Transmitter | RO Feed | PT_101 | press |
| PT-102 | AI  | RO Permeate Pressure Transmitter | RO Outlet | PT_102 | (not displayed) |
| TU-101 | AI  | Pre-treatment Turbidity Sensor | Pre-treatment Outlet | TU_101 | turb |
| P-101 | DO  | Seawater Intake Pump Start/Stop | Intake | P_101 | intake |
| P-102 | DO  | RO High-Pressure Pump Start/Stop | RO Feed | P_102 | ro  |
| P-103 | DO  | Post-treatment Pump Start/Stop | Post-treatment | P_103 | p103 |
| P-104 | DO  | Transfer Pump to Ground Tank | Post-treatment | P_104 | p104 |
| P-105 | DO  | Pump to Rooftop | Pump Room | P_105 | p105 |
| P-106 | DO  | Transfer Pump to Roof Tank | Pump Room | P_106 | p106 |
| V-101 | DO  | Motorized Valve (Primary) | Main Process Line | V_101 | v101 |
| V-102 | DO  | RO Feed Valve | RO Feed Line | V_102 | (not displayed) |
| V-103 | DO  | Post-treatment Valve | Post-treatment Line | V_103 | (not displayed) |
| V-104 | DO  | Ground Transfer Valve | Ground Transfer Line | V_104 | (not displayed) |
| V-105 | DO  | Rooftop Pump Valve | Rooftop Line | V_105 | (not displayed) |
| V-106 | DO  | Roof Tank Transfer Valve | Roof Transfer Line | V_106 | (not displayed) |
| UV-101 | DO  | UV Disinfection Unit On/Off | Post-treatment | UV_101 | uv101 |
| ALM-101 | DO  | General Alarm Output | Control Panel | ALM_101 | alm101 |
| PRV-101 | DO  | Pressure Relief Valve Open/Close | RO Membrane/Brine Line | PRV_101 | prv101 |
| SYSTEM_RUNNING | DI/DO | System Running State | Control Logic | System_Running | step |
| EMERGENCY_STOP | DI/DO | Emergency Stop Active | Control Logic | Emergency_Stop | step |

#### System States

1. **Emergency Stop**: All actuators OFF, ALM-101 ON, System_Running = FALSE
2. **System Stopped**: All actuators OFF, System_Running = FALSE  

3. **System Running**: Normal operation logic active, System_Running = TRUE

#### Key Logic Conditions (from PLC implementation)

- **PreTreatment_OK**: TU_101 < 5.0 NTU
- **RO_OK**: PreTreatment_OK AND LT_101 > 20% AND PT_101 50-70 bar
- **P_101 (Intake)**: RO_OK AND LT_101 < 95%
- **P_102 (RO Pump)**: RO_OK
- **P_103 (Post-treatment)**: LT_101 > 30%
- **P_104 (Transfer to Ground)**: RO_OK AND LT_101 < 95%
- **P_105 (Pump to Rooftop)**: LT_101 > 40% AND LT_102 < 95%
- **P_106 (Transfer to Roof)**: LT_102 < 98%
- **UV_101**: RO_OK (UV on when RO running)
- **V_101**: P_101 OR P_102 (open when intake or RO active)
- **PRV_101**: PT_101 > 70 bar (pressure relief)
- **Alarm**: TU_101 > 10 NTU OR PT_101 &lt; 45 OR PT_101 &gt; 75 OR LT_101 &lt; 10% OR LT_102 &gt; 98%

1. **HMI**
