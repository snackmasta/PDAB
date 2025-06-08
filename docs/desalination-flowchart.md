# Desalination System Process and Control Architecture

```mermaid
---
config:
  layout: elk
  theme: base
---
flowchart
    START((Start))
    STOP((Stop))
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
    V101 --controls--> B
    UV101 --disinfects--> D
    ALM101 --alerts--> PLC
```

# Desalination System Flowchart (Detailed Control & Logic)

```mermaid
---
config:
  layout: elk
  theme: base
---
flowchart
    START((Start))
    STOP((Stop))
    START --> A
    A[Seawater Intake]
    P101[P-101 Seawater Intake Pump]
    B[Pre-treatment\nFiltration and Sediment Removal]
    P102[P-102 RO High-Pressure Pump]
    C[RO Membrane\nDesalination]
    P103[P-103 Post-treatment Pump]
    D[Post-treatment\nMineralization and Disinfection]
    P104[P-104 Transfer Pump to Ground Tank]
    E[Ground Tank]
    P105[P-105 Pump to Rooftop]
    F[Pump Room]
    P106[P-106 Transfer Pump to Roof Tank]
    G[Roof Tank]
    H[Consumption]
    H --> STOP

    %% Connect process flow through actuator blocks
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

    %% Logic group (replaces PLC)
    subgraph Logic["Control Logic"]
      F_TU101["If TU-101 < Max → P101 ON"]
      F_FT101["If FT-101 > Min → P101 ON"]
      F_PT101["If PT-101 in Range → P102 ON"]
      F_LT101["If LT-101 > Min → P103 ON"]
      F_LT102["If LT-102 < Max → P106 ON"]
      F_ALARM["If any alarm → ALM101 ON"]
      F_UV["If D active → UV101 ON"]
      F_VALVE["If B active → V101 ON"]
    end
    TU101 --value--> F_TU101
    FT101 --value--> F_FT101
    PT101 --value--> F_PT101
    LT101 --value--> F_LT101
    LT102 --value--> F_LT102
    FT102 --value--> F_PT101
    PT102 --value--> F_PT101
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
    end
    V101 --controls--> B
    UV101 --disinfects--> D
    ALM101 --alerts--> Logic

```

*Legend (based on I/O Table):*
- **Sensors**: Measure process variables, send values to logic group
- **Control Logic**: Functions that connect sensor outputs to actuator inputs
- **Actuators**: Shown as blocks in the process pipeline, receive commands from logic
- **Dashed arrows**: Sensor measurement points (from process to sensor)
- **Solid arrows**: Water/process flow
- **Arrows labeled value/logic**: Signal and logic direction

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
