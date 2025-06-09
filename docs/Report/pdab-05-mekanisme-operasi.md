# Mekanisme Operasi Sistem PDAB

Mekanisme operasi sistem PDAB berjalan secara otomatis berdasarkan logika kontrol pada PLC:
- **Start/Stop**: Sistem dapat dijalankan atau dihentikan melalui HMI.
- **Pengambilan air**: Pompa intake aktif jika level tangki ground rendah dan kondisi pra-perlakuan terpenuhi.
- **Pra-perlakuan**: Filter melakukan backwash otomatis jika tekanan diferensial tinggi.
- **RO**: Pompa RO aktif jika kondisi pra-perlakuan dan level air cukup, berhenti jika tekanan abnormal.
- **Pasca-perlakuan**: Remineralisasi dan desinfeksi berjalan paralel dengan output RO.
- **Distribusi**: Pompa transfer dan booster aktif sesuai level tangki rooftop.
- **Alarm**: Sistem akan memicu alarm dan mematikan pompa jika terjadi kondisi abnormal (tekanan, level, turbidity, dsb).
- **Monitoring**: Semua parameter dan status dapat dipantau melalui HMI.
