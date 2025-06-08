# Control System Plan and I/O Table

## 1. Control Philosophy
- The system is fully automated with manual override for all pumps and valves.
- Main control logic is based on water levels, flow, pressure, and turbidity.
- Alarms are generated for abnormal conditions (low/high level, high turbidity, low pressure, etc.).
- All critical parameters are monitored and logged.
- Local HMI/SCADA for operator interface; remote monitoring optional.
- **Architecture Update:** The system now uses a modular process and control architecture, with clear separation of sensors, logic, and actuators as shown in the updated flowcharts. PLC/SCADA or software logic group handles all process decisions and actuator commands.

## 2. Main Control Logic
- **Seawater Intake Pump**: Starts if pre-treatment and RO are ready, stops on low ground tank level or alarm.
- **Pre-treatment**: Backwash cycle triggered by high differential pressure or timer.
- **RO High-Pressure Pump**: Starts if pre-treatment is OK and ground tank has sufficient level; stops on low pressure, high pressure, or low ground tank level.
- **Post-treatment**: Disinfection and remineralization run in parallel with RO output.
- **Transfer Pump to Roof Tank**: Starts if roof tank is not full and ground tank has water; stops if roof tank is full or ground tank is low.
- **Alarms**: Any abnormal sensor reading triggers alarm and can stop relevant equipment.
- **Architecture Update:** Logic is now explicitly mapped from sensors to logic functions to actuators, as per the new flowcharts. All sensor values are routed to a central logic group (PLC or software), which then controls actuators.

## 3. I/O Table
| Tag/Name                | Type      | Description                                 | Location                |
|-------------------------|-----------|---------------------------------------------|-------------------------|
| LT-101                  | AI        | Ground Tank Level Transmitter               | Ground Tank             |
| LT-102                  | AI        | Roof Tank Level Transmitter                 | Roof Tank               |
| FT-101                  | AI        | Intake Flow Transmitter                     | Intake Line             |
| FT-102                  | AI        | RO Permeate Flow Transmitter                | RO Outlet               |
| PT-101                  | AI        | RO Feed Pressure Transmitter                | RO Feed                 |
| PT-102                  | AI        | RO Permeate Pressure Transmitter            | RO Outlet               |
| TU-101                  | AI        | Pre-treatment Turbidity Sensor              | Pre-treatment Outlet    |
| P-101                   | AO/DO     | Seawater Intake Pump Start/Stop             | Intake                  |
| P-102                   | AO/DO     | RO High-Pressure Pump Start/Stop            | RO Feed                 |
| P-103                   | AO/DO     | Post-treatment Pump Start/Stop              | Post-treatment          |
| P-104                   | AO/DO     | Transfer Pump to Ground Tank                | Post-treatment          |
| P-105                   | AO/DO     | Pump to Rooftop                             | Pump Room               |
| P-106                   | AO/DO     | Transfer Pump to Roof Tank                  | Pump Room               |
| V-101 ... V-106         | DO        | Motorized Valve Open/Close                  | Various                 |
| UV-101                  | DO        | UV Disinfection Unit On/Off                 | Post-treatment          |
| ALM-101                 | DO        | General Alarm Output                        | Control Panel           |
| HMI/SCADA               | Comm      | Operator Interface                          | Control Room            |
| PRV-101                 | DO        | Pressure Relief Valve Open/Close            | RO Membrane/Brine Line      |

**Legend:**
- AI: Analog Input
- AO: Analog Output
- DO: Digital Output
- Comm: Communication

## 4. Notes
- All analog signals are 4–20 mA.
- All pumps and valves have local/remote and manual/auto modes.
- System can be expanded for remote monitoring, data logging, and advanced diagnostics.
- **Architecture Update:** The I/O table now includes all actuators and sensors as per the new architecture, including additional pumps (P-103 to P-106) and explicit mapping to logic/PLC functions.
