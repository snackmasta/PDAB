# Perangkat Keras Kendali Utilitas Dalam Sistem PDAB

Perangkat keras utama pada sistem PDAB (Pengolahan & Distribusi Air Bersih) meliputi:
- **PLC (Programmable Logic Controller)**: Mengendalikan seluruh proses otomatisasi pengolahan air.
- **Sensor Level (LT-101, LT-102)**: Mengukur ketinggian air pada tangki ground dan rooftop.
- **Sensor Tekanan (PT-101, PT-102)**: Memantau tekanan pada feed RO dan permeate.
- **Sensor Flow (FT-101, FT-102)**: Mengukur laju aliran air pada intake dan output RO.
- **Sensor Turbidity (TU-101)**: Memantau kekeruhan air pada outlet pra-perlakuan.
- **Pompa**: Intake, RO, transfer, booster, dan post-treatment.
- **Valve Motorized (V-101 s/d V-106)**: Mengatur aliran air pada berbagai jalur proses.
- **Unit UV Disinfection (UV-101)**: Desinfeksi air hasil RO.
- **Alarm (ALM-101)**: Indikasi kondisi abnormal.
- **Panel Kontrol**: Tempat pemasangan PLC, relay, terminal, proteksi, dan HMI.

---

## Lampiran: Spesifikasi Hardware Sistem PDAB

(Lihat detail pada dokumen hardware-spec.md untuk spesifikasi lengkap pompa, filter, sensor, dan panel kontrol yang digunakan pada sistem PDAB.)

---

*Catatan: Semua perangkat keras di atas telah diintegrasikan dan dikendalikan secara otomatis melalui PLC dan HMI sesuai dengan dokumentasi dan program pada project ini.*
