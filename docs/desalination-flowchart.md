# Desalination System Flowchart (Mermaid)

```mermaid
flowchart LR
    A[Seawater Intake] -->|P-101, FT-101| B[Pre-treatment\nFiltration and Sediment Removal]
    B -->|P-102| C[RO Membrane\nDesalination]
    C -->|P-103| D[Post-treatment\nMineralization and Disinfection]
    D -->|P-104| E[Ground Tank]
    E -->|P-105| F[Pump to Rooftop]
    F --> G[Roof Tank]
    G -->|LT-102| H[Consumption]

    %% Sensors and valves
    A -.->|Valve V-101| B
    B -.->|Valve V-102| C
    C -.->|Valve V-103| D
    D -.->|Valve V-104| E
    E -.->|Valve V-105| F
    F -.->|Valve V-106| G
```

*Legend:*
- **P-101 ... P-106**: Pumps
- **FT**: Flow Transmitter
- **LT**: Level Transmitter
- **TU**: Turbidity Sensor
- **PT**: Pressure Transmitter
- **V-101 ... V-106**: Valves

# Control System Flowchart (Mermaid)

```mermaid
flowchart TD
    Start(["System Start"]) --> CheckSource{Seawater Available?}
    CheckSource -- No --> AlarmSource[Alarm: No Source]
    CheckSource -- Yes --> PreTreat[Start Pre-treatment]
    PreTreat --> CheckTurbidity{Turbidity OK?}
    CheckTurbidity -- No --> AlarmTurb[Alarm: High Turbidity]
    CheckTurbidity -- Yes --> RO[Start RO Pump]
    RO --> CheckPressure{Pressure OK?}
    CheckPressure -- No --> AlarmPressure[Alarm: Low Pressure]
    CheckPressure -- Yes --> PostTreat[Start Post-treatment]
    PostTreat --> CheckGroundLevel{Ground Tank Level OK?}
    CheckGroundLevel -- Low --> StopAll[Stop System]
    CheckGroundLevel -- OK --> PumpToRoof[Start Pump to Roof]
    PumpToRoof --> CheckRoofLevel{Roof Tank Full?}
    CheckRoofLevel -- Yes --> StopRoofPump[Stop Roof Pump]
    CheckRoofLevel -- No --> Continue[Continue Pumping]
    StopAll --> End(["System Stop"])
    StopRoofPump --> End
    AlarmSource --> End
    AlarmTurb --> End
    AlarmPressure --> End

    %% Sensors: Level, Flow, Pressure, Turbidity
    %% Actuators: Pumps, Valves
```

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
