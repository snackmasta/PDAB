# Model Sistem PDAB

Model sistem PDAB dapat digambarkan sebagai rangkaian proses otomatis yang terdiri dari:
1. **Intake**: Pengambilan air baku menggunakan pompa submersible.
2. **Pra-perlakuan**: Filtrasi multi-media dan cartridge filter untuk menghilangkan partikel dan kekeruhan.
3. **RO Unit**: Proses reverse osmosis untuk memisahkan garam dan kontaminan.
4. **Pasca-perlakuan**: Remineralisasi dan desinfeksi (UV atau klorin).
5. **Penyimpanan**: Tangki ground dan rooftop.
6. **Distribusi**: Pompa transfer dan booster ke titik pemakaian.
7. **Kontrol Otomatis**: PLC/HMI menjalankan logika berdasarkan input sensor dan status aktuator.

Model ini divisualisasikan dalam flowchart dan P&ID pada dokumen proyek.

## Lampiran: Flowchart dan Arsitektur Sistem Desalinasi

### Flowchart Proses dan Kontrol

```mermaid
---
config:
  layout: elk
  theme: base
---
flowchart
    START((Start))
    STOP((Stop))
    style START fill:#b6fcb6,stroke:#2e8b57,stroke-width:3px
    style STOP fill:#ffb3b3,stroke:#c0392b,stroke-width:3px
    START --> A
    A[Seawater Intake]
    P101[P-101 Seawater Intake Pump]
    B[Pre-treatment Filtration and Sediment Removal]
    P102[P-102 RO High-Pressure Pump]
    C[RO Membrane Desalination]
    P103[P-103 Post-treatment Pump]
    D[Post-treatment Mineralization and Disinfection]
    P104[P-104 Transfer Pump to Ground Tank]
    E[Ground Tank]
    P105[P-105 Pump to Rooftop]
    F[Pump Room]
    P106[P-106 Transfer Pump to Roof Tank]
    G[Roof Tank]
    H[Consumption]
    H --> STOP
    A --> P101 --> B --> P102 --> C --> P103 --> D --> P104 --> E --> P105 --> F --> P106 --> G --> H

    %% Sensors (measure process, send signal to PLC)
    subgraph Sensors
      TU101["TU-101 Turbidity Sensor"]
      FT101["FT-101 Intake Flow Transmitter"]
      FT102["FT-102 RO Permeate Flow Transmitter"]
      PT101["PT-101 RO Feed Pressure Transmitter"]
      PT102["PT-102 RO Permeate Pressure Transmitter"]
      LT101["LT-101 Ground Tank Level Transmitter"]
      LT102["LT-102 Roof Tank Level Transmitter"]
    end
    B -.-> TU101
    A -.-> FT101
    C -.-> FT102
    C -.-> PT101
    C -.-> PT102
    E -.-> LT101
    G -.-> LT102

    %% PLC/HMI block
    PLC["PLC / HMI / SCADA"]

    %% Actuators (controlled by PLC)
    subgraph Actuators
      P101
      P102
      P103
      P104
      P105
      P106
      V101["V-101...V-106 Motorized Valves"]
      UV101["UV-101 UV Disinfection"]
      ALM101["ALM-101 General Alarm"]
      PRV101["PRV-101 Pressure Relief Valve"]
    end
    TU101 --4-20mA--> PLC
    FT101 --4-20mA--> PLC
    FT102 --4-20mA--> PLC
    PT101 --4-20mA--> PLC
    PT102 --4-20mA--> PLC
    LT101 --4-20mA--> PLC
    LT102 --4-20mA--> PLC
    PLC --DO/AO--> P101
    PLC --DO/AO--> P102
    PLC --DO/AO--> P103
    PLC --DO/AO--> P104
    PLC --DO/AO--> P105
    PLC --DO/AO--> P106
    PLC --DO--> V101
    PLC --DO--> UV101
    PLC --DO--> ALM101
    PLC --DO--> PRV101
    V101 --controls--> B
    UV101 --disinfects--> D
    ALM101 --alerts--> PLC
    C --overpressure--> PRV101
    PRV101 --to Brine/Drain--> DRAIN[Brine/Drain]
```

### Flowchart Algoritma Logika Kontrol

```mermaid
flowchart TD
    Start(["System Start"]) --> Init["Initialize Variables"]
    Init --> CheckSource{Seawater Available?}
    CheckSource -- No --> AlarmSource["Alarm: No Source"]
    AlarmSource --> End
    CheckSource -- Yes --> PreTreat["Start Pre-treatment"]
    PreTreat --> CheckTurbidity{Turbidity < Max?}
    CheckTurbidity -- No --> AlarmTurb["Alarm: High Turbidity"]
    AlarmTurb --> End
    CheckTurbidity -- Yes --> RO["Start RO Pump"]
    RO --> CheckPressure{Pressure in Range?}
    CheckPressure -- No --> AlarmPressure["Alarm: Pressure Fault"]
    AlarmPressure --> End
    CheckPressure -- Yes --> PostTreat["Start Post-treatment"]
    PostTreat --> CheckGroundLevel{Ground Tank Level OK?}
    CheckGroundLevel -- Low --> StopAll["Stop System"]
    StopAll --> End
    CheckGroundLevel -- OK --> PumpToRoof["Start Transfer Pump to Roof"]
    PumpToRoof --> CheckRoofLevel{Roof Tank Full?}
    CheckRoofLevel -- Yes --> StopRoofPump["Stop Transfer Pump"]
    StopRoofPump --> End
    CheckRoofLevel -- No --> Continue["Continue Pumping"]
    Continue --> CheckGroundLevel
```

### Hardware Siteplan

```mermaid
flowchart LR
    Intake["Seawater Intake Structure"] --"Raw Seawater"--> Pretreat["Pre-treatment Unit"] 
    Pretreat --"Filtered Water"--> RO["RO Desalination Unit"]
    RO --"Permeate (Fresh Water)"--> Post["Post-treatment Unit"]
    Post --"Treated Fresh Water"--> Ground["Ground Storage Tank"]
    Ground --"Water Transfer"--> Pump["Pump Room"]
    Pump --"Pressurized Water"--> Roof["Rooftop Storage Tank"]
    Roof --"Distribution"--> Building["Building/Distribution"]
    
    %% Waste streams
    RO -.->|"Brine/Concentrate"| Waste["Waste Discharge"]
    
    style Intake fill:#b3d1ff,stroke:#333,stroke-width:2px
    style Pretreat fill:#e6ffe6,stroke:#333,stroke-width:2px
    style RO fill:#fff2cc,stroke:#333,stroke-width:2px
    style Post fill:#ffe6e6,stroke:#333,stroke-width:2px
    style Ground fill:#d9d9d9,stroke:#333,stroke-width:2px
    style Pump fill:#f2e6ff,stroke:#333,stroke-width:2px
    style Roof fill:#d1e0e0,stroke:#333,stroke-width:2px
    style Building fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Waste fill:#ffcccc,stroke:#333,stroke-width:2px
```

*Diagram siteplan ini menampilkan hubungan antar unit utama pada sistem desalinasi sesuai layout fisik dan alur proses air.*

### Flowchart Model: Fungsi dan Hubungan PLC dalam Sistem Desalinasi

```mermaid
---
config:
  layout: elk
  theme: base
---
flowchart
    START((Start))
    STOP((Stop))
    style START fill:#b6fcb6,stroke:#2e8b57,stroke-width:3px
    style STOP fill:#ffb3b3,stroke:#c0392b,stroke-width:3px
    START --> A
    A[Seawater Intake]
    P101[P-101 Seawater Intake Pump]
    B[Pre-treatment Filtration and Sediment Removal]
    P102[P-102 RO High-Pressure Pump]
    C[RO Membrane Desalination]
    P103[P-103 Post-treatment Pump]
    D[Post-treatment Mineralization and Disinfection]
    P104[P-104 Transfer Pump to Ground Tank]
    E[Ground Tank]
    P105[P-105 Pump to Rooftop]
    F[Pump Room]
    P106[P-106 Transfer Pump to Roof Tank]
    G[Roof Tank]
    H[Consumption]
    H --> STOP
    A --> P101 --> B --> P102 --> C --> P103 --> D --> P104 --> E --> P105 --> F --> P106 --> G --> H

    %% Sensors (measure process, send signal to logic group)
    subgraph Sensors
      TU101["TU-101 Turbidity Sensor"]
      FT101["FT-101 Intake Flow Transmitter"]
      FT102["FT-102 RO Permeate Flow Transmitter"]
      PT101["PT-101 RO Feed Pressure Transmitter"]
      PT102["PT-102 RO Permeate Pressure Transmitter"]
      LT101["LT-101 Ground Tank Level Transmitter"]
      LT102["LT-102 Roof Tank Level Transmitter"]
    end
    B -.-> TU101
    A -.-> FT101
    C -.-> FT102
    C -.-> PT101
    C -.-> PT102
    E -.-> LT101
    G -.-> LT102

    %% Logic group (PLC/Control Logic)
    subgraph Logic["PLC / Control Logic"]
      F_TU101["If TU-101 < Max → P101 ON"]
      F_FT101["If FT-101 > Min → P101 ON"]
      F_PT101["If PT-101, FT102, PT102 in Range → P102, P104, P105, P106 ON"]
      F_LT101["If LT-101 > Min → P103 ON"]
      F_LT102["If LT-102 < Max → P106 ON"]
      F_ALARM["If any alarm → ALM101 ON"]
      F_UV["If D active → UV101 ON"]
      F_VALVE["If B active → V101 ON"]
      F_PRV["If PT-101 > Max or Fault → PRV101 OPEN"]
    end
    TU101 --value--> F_TU101
    TU101 --value--> F_ALARM
    FT101 --value--> F_FT101
    FT101 --value--> F_ALARM
    PT101 --value--> F_PT101
    PT101 --value--> F_ALARM
    PT101 --value--> F_PRV
    FT102 --value--> F_PT101
    FT102 --value--> F_ALARM
    PT102 --value--> F_PT101
    PT102 --value--> F_ALARM
    LT101 --value--> F_LT101
    LT101 --value--> F_ALARM
    LT102 --value--> F_LT102
    LT102 --value--> F_ALARM
    D --state--> F_UV
    B --state--> F_VALVE
    F_TU101 --logic--> P101
    F_FT101 --logic--> P101
    F_PT101 --logic--> P102
    F_PT101 --logic--> P104
    F_PT101 --logic--> P105
    F_PT101 --logic--> P106
    F_LT101 --logic--> P103
    F_LT102 --logic--> P106
    F_ALARM --logic--> ALM101
    F_UV --logic--> UV101
    F_VALVE --logic--> V101
    F_PRV --logic--> PRV101

    %% Actuators (controlled by logic)
    subgraph Actuators
      P101
      P102
      P103
      P104
      P105
      P106
      V101["V-101...V-106 Motorized Valves"]
      UV101["UV-101 UV Disinfection"]
      ALM101["ALM-101 General Alarm"]
      PRV101["PRV-101 Pressure Relief Valve"]
    end
    V101 --controls--> B
    UV101 --disinfects--> D
    ALM101 --alerts--> F_VALVE
    PRV101 --relieves pressure--> C
    PRV101 --to Brine/Drain--> DRAIN[Brine/Drain]
```

*Flowchart ini menjelaskan hubungan antara sensor, PLC (logic group), dan aktuator dalam sistem desalinasi. Semua sinyal sensor diproses oleh PLC untuk mengaktifkan/mematikan aktuator sesuai logika kontrol yang telah diprogram.*

### Flowchart Model: Fungsi dan Hubungan PLC untuk Algoritma Logika Kontrol

```mermaid
---
config:
  layout: elk
  theme: base
---
flowchart
    START((Start))
    STOP((Stop))
    style START fill:#b6fcb6,stroke:#2e8b57,stroke-width:3px
    style STOP fill:#ffb3b3,stroke:#c0392b,stroke-width:3px
    START --> INIT["Initialize Variables"]
    INIT --> CheckSource{Seawater Available?}
    CheckSource -- No --> AlarmSource["Alarm: No Source"]
    AlarmSource --> STOP
    CheckSource -- Yes --> PreTreat["Start Pre-treatment"]
    PreTreat --> CheckTurbidity{Turbidity < Max?}
    CheckTurbidity -- No --> AlarmTurb["Alarm: High Turbidity"]
    AlarmTurb --> STOP
    CheckTurbidity -- Yes --> RO["Start RO Pump"]
    RO --> CheckPressure{Pressure in Range?}
    CheckPressure -- No --> AlarmPressure["Alarm: Pressure Fault"]
    AlarmPressure --> STOP
    CheckPressure -- Yes --> PostTreat["Start Post-treatment"]
    PostTreat --> CheckGroundLevel{Ground Tank Level OK?}
    CheckGroundLevel -- Low --> StopAll["Stop System"]
    StopAll --> STOP
    CheckGroundLevel -- OK --> PumpToRoof["Start Transfer Pump to Roof"]
    PumpToRoof --> CheckRoofLevel{Roof Tank Full?}
    CheckRoofLevel -- Yes --> StopRoofPump["Stop Transfer Pump"]
    StopRoofPump --> STOP
    CheckRoofLevel -- No --> Continue["Continue Pumping"]
    Continue --> CheckGroundLevel
```

*Flowchart ini menggambarkan algoritma logika kontrol utama pada sistem desalinasi, dengan node Start berwarna hijau dan Stop berwarna merah untuk memperjelas status awal dan akhir proses.*
