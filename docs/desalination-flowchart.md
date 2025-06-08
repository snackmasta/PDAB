# Desalination System Flowchart (Mermaid)

```mermaid
flowchart LR
    %% Main process flow
    A[Seawater Intake] -->|P-101| B[Pre-treatment\nFiltration and Sediment Removal]
    B -->|P-102| C[RO Membrane\nDesalination]
    C -->|P-103| D[Post-treatment\nMineralization and Disinfection]
    D -->|P-104| E[Ground Tank]
    E -->|P-103| F[Pump Room]
    F -->|P-105| G[Roof Tank]
    G --> H[Consumption]

    %% Sensors (measure process, send signal to PLC)
    subgraph Sensors
      TU101["TU-101\nTurbidity Sensor"]
      FT101["FT-101\nIntake Flow Transmitter"]
      FT102["FT-102\nRO Permeate Flow Transmitter"]
      PT101["PT-101\nRO Feed Pressure Transmitter"]
      PT102["PT-102\nRO Permeate Pressure Transmitter"]
      LT101["LT-101\nGround Tank Level Transmitter"]
      LT102["LT-102\nRoof Tank Level Transmitter"]
    end
    TU101 --4-20mA--> PLC
    FT101 --4-20mA--> PLC
    FT102 --4-20mA--> PLC
    PT101 --4-20mA--> PLC
    PT102 --4-20mA--> PLC
    LT101 --4-20mA--> PLC
    LT102 --4-20mA--> PLC

    %% PLC/HMI block
    PLC["PLC / HMI / SCADA"]

    %% Actuators (controlled by PLC)
    subgraph Actuators
      P101["P-101\nSeawater Intake Pump"]
      P102["P-102\nRO High-Pressure Pump"]
      P103["P-103\nTransfer Pump to Roof"]
      P104["P-104\n(Spare/Unused)"]
      P105["P-105\nPump to Rooftop"]
      V101["V-101...V-106\nMotorized Valves"]
      UV101["UV-101\nUV Disinfection"]
      ALM101["ALM-101\nGeneral Alarm"]
    end
    PLC --DO/AO--> P101
    PLC --DO/AO--> P102
    PLC --DO/AO--> P103
    PLC --DO/AO--> P104
    PLC --DO/AO--> P105
    PLC --DO--> V101
    PLC --DO--> UV101
    PLC --DO--> ALM101

    %% Sensors measure process points (flipped arrows)
    B -.-> TU101
    A -.-> FT101
    C -.-> FT102
    C -.-> PT101
    C -.-> PT102
    E -.-> LT101
    G -.-> LT102
```

*Legend (based on I/O Table):*
- **Sensors**: Measure process variables, send 4–20 mA signals to PLC
- **PLC/HMI/SCADA**: Receives sensor inputs, controls actuators
- **Actuators**: Receive commands from PLC (DO/AO)
- **Dashed arrows**: Sensor measurement points (from process to sensor)
- **Solid arrows**: Water/process flow
- **Arrows labeled 4-20mA/DO/AO**: Signal direction

*Notes:*
- AI: Analog Input, AO: Analog Output, DO: Digital Output, Comm: Communication
- Arrows with solid lines represent main process flow.
- Dashed arrows represent valve actuation or sensor signal paths.
- Each label corresponds to a device or instrument in the I/O table.

# Logic Algorithm Flowchart (Mermaid)

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
    
    %% Decision and process logic only, not I/O wiring
```

*This flowchart represents the main logic algorithm for the desalination control system, focusing on process decisions and actions rather than I/O wiring.*

# Hardware Siteplan (Mermaid)

```mermaid
block-beta
  columns 3
  SeawaterIntake["Seawater Intake Structure"] PreTreatment["Pre-treatment Unit"] ROUnit["RO Desalination Unit"]
  GroundTank["Ground Storage Tank"] PostTreatment["Post-treatment Unit"] PumpRoom["Pump Room"]
  RoofTank["Rooftop Storage Tank"] Building["Building/Distribution"]
  
  SeawaterIntake --> PreTreatment
  PreTreatment --> ROUnit
  ROUnit --> PostTreatment
  PostTreatment --> GroundTank
  GroundTank --> PumpRoom
  PumpRoom --> RoofTank
  RoofTank --> Building
  
  style SeawaterIntake fill:#b3d1ff,stroke:#333,stroke-width:2px
  style PreTreatment fill:#e6ffe6,stroke:#333,stroke-width:2px
  style ROUnit fill:#fff2cc,stroke:#333,stroke-width:2px
  style PostTreatment fill:#ffe6e6,stroke:#333,stroke-width:2px
  style GroundTank fill:#d9d9d9,stroke:#333,stroke-width:2px
  style PumpRoom fill:#f2e6ff,stroke:#333,stroke-width:2px
  style RoofTank fill:#d1e0e0,stroke:#333,stroke-width:2px
  style Building fill:#f9f9f9,stroke:#333,stroke-width:2px
```

# Hardware Specifications are now in [hardware-spec.md](./hardware-spec.md)
