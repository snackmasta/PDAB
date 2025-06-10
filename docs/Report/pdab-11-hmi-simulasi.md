# Halaman 11: HMI dan Simulasi Sistem Desalinasi (Penjelasan Teknis dan Mendalam)

## 1. Arsitektur HMI

HMI (Human Machine Interface) pada sistem ini dikembangkan menggunakan Python dengan library Tkinter, yang berfungsi sebagai antarmuka operator untuk monitoring dan kontrol sistem desalinasi secara real-time. HMI terhubung langsung ke model simulasi Python, sehingga setiap perubahan status proses langsung tercermin di tampilan HMI.

### a. Struktur Kode HMI
- **File Utama:** `src/hmi.py`
- **Kelas Utama:** `DesalinationHMI`
- **Fungsi Kunci:**
  - `_build_gui()`: Membangun seluruh elemen GUI (indikator status, tombol kontrol, tren data, dsb).
  - `update()`: Sinkronisasi tampilan dengan status proses.
  - `start_system()`, `stop_system()`, `emergency_stop()`: Kontrol utama sistem.
  - `drain_roof_tank()`: Simulasi konsumsi air dari roof tank.

### b. Fitur Teknis HMI
- **Status Real-Time:**
  - Setiap sensor (level, tekanan, turbidity) dan aktuator (pompa, valve, UV, alarm) ditampilkan dengan indikator ON/OFF dan nilai aktual.
  - Status diambil langsung dari instance `DesalinationSystem` (model simulasi).
- **Alarm & Safety:**
  - Alarm kritis (misal: tekanan di luar batas, level tangki rendah/tinggi, turbidity tinggi) ditampilkan dengan warna dan notifikasi.
  - Emergency Stop akan mematikan seluruh aktuator dan mengunci sistem hingga reset manual.
- **Trend Data:**
  - Menggunakan Matplotlib untuk menampilkan grafik tren level tangki, tekanan, dan parameter utama lain secara live.
- **User Interaction:**
  - Semua perintah (start, stop, emergency, drain) langsung memanggil method pada model simulasi.

## 2. Simulasi Proses (Process Model)

Simulasi proses dikembangkan dalam Python (`src/process.py`) dan merepresentasikan seluruh dinamika sistem desalinasi secara matematis dan logis.

### a. Struktur Model Simulasi
- **Kelas Utama:** `DesalinationSystem`
- **Parameter Kunci:**
  - Level tangki (ground & roof), tekanan RO, turbidity, status pompa/valve/UV/alarm
  - Setpoint dan batas operasi diatur di `src/config.py` (misal: GROUND_TANK_MIN/MAX, PRESSURE_MIN/MAX, TURBIDITY_MAX)
- **Fungsi Kunci:**
  - `step()`: Satu siklus simulasi, menghitung perubahan variabel proses dan status aktuator berdasarkan logika kontrol.
  - `get_status()`: Mengembalikan status lengkap untuk HMI.
  - `start()`, `stop()`, `emergency_stop()`: Mengatur state sistem sesuai perintah HMI.

### b. Logika Kontrol (Sesuai PLC)
- **PreTreatment_OK:** `pre_treatment_turbidity < TURBIDITY_MAX`
- **RO_OK:** `PreTreatment_OK and ground_tank_level > 20 and PRESSURE_MIN < ro_feed_pressure < PRESSURE_MAX`
- **Aktuator:**
  - Intake Pump (`intake_pump`): ON jika RO_OK dan ground_tank_level < GROUND_TANK_MAX
  - RO Pump (`ro_pump`): ON jika RO_OK
  - Transfer Pump (`transfer_pump`): ON jika ground_tank_level > 30 dan roof_tank_level < 90
  - P-103 s/d P-106, V-101, UV-101, PRV-101, ALM-101: Semua logika sesuai tabel I/O dan PLC (lihat `src/process.py` dan `docs/control-plan.md`)
- **Alarm:**
  - Aktif jika: turbidity > 10, tekanan < 45 atau > 75, ground_tank_level < 10, roof_tank_level > 98

### c. Interaksi HMI-Simulasi
- HMI membaca status dari model simulasi setiap update.
- Setiap aksi di HMI (start, stop, emergency, drain) langsung mengubah state di model simulasi.
- Semua perubahan status proses (misal: alarm, ON/OFF pompa) langsung tercermin di HMI.

## 3. Integrasi dan Validasi

- **Konsistensi:** Semua logika kontrol di simulasi identik dengan PLC (Structured Text) dan tabel I/O.
- **Validasi:** Simulasi digunakan untuk menguji seluruh skenario operasi, alarm, dan safety sebelum implementasi fisik.
- **Ekspansi:** Arsitektur modular memudahkan penambahan fitur baru (misal: mode manual, logging data, remote monitoring).

## 4. Diagram Integrasi

```
+-------------------+         +-------------------+
|   HMI (Tkinter)   | <-----> |  Model Simulasi   |
|  - GUI/Control    |         |  (DesalinationSys)|
|  - Trend Data     |         |  - Logika Kontrol |
|  - Alarm Display  |         |  - Dinamika Proses|
+-------------------+         +-------------------+
```

## 5. Contoh Alur Kerja
1. Operator menekan START di HMI → HMI memanggil `start()` pada model → Model mengecek precondition, mengaktifkan pompa/aktuator sesuai logika → Status ON/OFF dan nilai sensor langsung tampil di HMI.
2. Jika terjadi kondisi abnormal (misal tekanan > 75 bar), model mengaktifkan alarm → HMI menampilkan notifikasi alarm dan status merah.
3. Emergency Stop di HMI → Semua aktuator OFF, alarm aktif, sistem terkunci hingga reset.

---

Dengan pendekatan ini, seluruh proses desain, validasi, dan pelatihan dapat dilakukan secara virtual dan konsisten dengan implementasi PLC fisik.
