# P&ID Generation Prompt for Desalination System - ISO Format

## Overview
Generate a comprehensive Piping and Instrumentation Diagram (P&ID) for a reverse osmosis seawater desalination system following **ISO 14617** and **ISO 10628** standards. The system includes seawater intake, pre-treatment, RO desalination, post-treatment, and dual storage tanks with distribution.

## System Description
This is a complete seawater desalination plant with the following process flow:
**Seawater Intake → Pre-treatment → RO Membrane → Post-treatment → Ground Tank → Transfer → Roof Tank → Distribution**

---

## Equipment List with ISO Symbols

### 1. PUMPS (ISO Symbol: Circle with impeller blades)
- **P-101**: Seawater Intake Pump (Submersible)
  - Type: Centrifugal, corrosion-resistant
  - Capacity: Variable based on demand
  - Material: Duplex stainless steel
  - Drive: Electric motor with VFD capability

- **P-102**: RO High-Pressure Pump 
  - Type: Multistage centrifugal
  - Operating pressure: 50-70 bar
  - Material: Super duplex stainless steel
  - Drive: Electric motor with VFD

- **P-103**: Post-treatment Pump
  - Type: Centrifugal
  - Material: Stainless steel
  - Purpose: Transfer through post-treatment unit

- **P-104**: Transfer Pump to Ground Tank
  - Type: Centrifugal
  - Purpose: Transfer treated water to ground storage

- **P-105**: Pump to Rooftop (Booster Pump)
  - Type: Multistage centrifugal
  - Operating pressure: Up to 16 bar
  - Purpose: Elevate water to roof level

- **P-106**: Transfer Pump to Roof Tank
  - Type: Centrifugal
  - Purpose: Fill roof tank from pump room

### 2. TANKS (ISO Symbol: Rectangle/cylinder)
- **TK-101**: Ground Storage Tank
  - Type: Atmospheric storage
  - Material: HDPE/FRP
  - Capacity: 1-2 days supply
  - Design: Vertical cylindrical

- **TK-102**: Rooftop Storage Tank
  - Type: Atmospheric storage  
  - Material: HDPE/FRP
  - Capacity: Building demand based
  - Design: Horizontal/vertical cylindrical

### 3. PROCESS EQUIPMENT (Various ISO symbols)
- **F-101**: Multimedia Pre-treatment Filter
  - Type: Pressure vessel
  - Media: Sand, gravel, anthracite
  - Material: FRP or carbon steel with liner
  - Accessories: Backwash system

- **RO-101**: Reverse Osmosis Membrane Unit
  - Type: Spiral wound membrane elements
  - Configuration: 4" or 8" elements in pressure vessels
  - Recovery rate: 35-45%
  - Material: Stainless steel pressure vessels

- **F-102**: Post-treatment Filter (Remineralization)
  - Type: Pressure vessel
  - Media: Calcite/dolomite
  - Material: FRP or stainless steel

- **UV-101**: UV Disinfection Unit
  - Type: UV lamp chamber
  - Dose: 30-40 mJ/cm²
  - Material: Stainless steel

### 4. VALVES (ISO Symbols per valve type)
- **V-101**: Motorized Control Valve (seawater intake)
- **V-102**: Manual Isolation Valve (pre-treatment inlet)
- **V-103**: Backwash Control Valve (multimedia filter)
- **V-104**: RO Inlet Isolation Valve
- **V-105**: RO Concentrate Drain Valve
- **V-106**: Ground Tank Inlet Valve
- **V-107**: Roof Tank Inlet Valve
- **PRV-101**: Pressure Relief Valve (RO system protection)
- **CV-101**: Check Valve (pump discharge)
- **CV-102**: Check Valve (tank outlets)

---

## Instrumentation List with ISO Tag Numbers

### 1. PRESSURE INSTRUMENTS
- **PT-101**: RO Feed Pressure Transmitter
  - Range: 0-80 bar
  - Output: 4-20mA
  - Location: RO unit inlet

- **PT-102**: RO Permeate Pressure Transmitter  
  - Range: 0-10 bar
  - Output: 4-20mA
  - Location: RO unit outlet

- **PI-101**: Pressure Indicator (Pre-treatment)
- **PI-102**: Pressure Indicator (Post-treatment)

### 2. FLOW INSTRUMENTS
- **FT-101**: Seawater Intake Flow Transmitter
  - Type: Electromagnetic
  - Range: 0-100 m³/h
  - Output: 4-20mA

- **FT-102**: RO Permeate Flow Transmitter
  - Type: Electromagnetic  
  - Range: 0-50 m³/h
  - Output: 4-20mA

- **FI-101**: Flow Indicator (RO concentrate)

### 3. LEVEL INSTRUMENTS
- **LT-101**: Ground Tank Level Transmitter
  - Type: Ultrasonic/Hydrostatic
  - Range: 0-10 m
  - Output: 4-20mA

- **LT-102**: Roof Tank Level Transmitter
  - Type: Ultrasonic/Hydrostatic
  - Range: 0-5 m  
  - Output: 4-20mA

- **LSL-101**: Ground Tank Low Level Switch
- **LSH-101**: Ground Tank High Level Switch
- **LSH-102**: Roof Tank High Level Switch

### 4. QUALITY INSTRUMENTS
- **TU-101**: Turbidity Transmitter (Pre-treatment)
  - Range: 0-100 NTU
  - Output: 4-20mA
  - Location: Pre-treatment outlet

- **CC-101**: Conductivity Controller (RO permeate quality)
- **pH-101**: pH Transmitter (Post-treatment)

### 5. ALARM DEVICES
- **ALM-101**: General System Alarm
- **ALM-102**: High Pressure Alarm
- **ALM-103**: Low Tank Level Alarm
- **ALM-104**: Water Quality Alarm

---

## Control System Architecture

### PLC/DCS System
- **PLC-101**: Main Process Control Unit
  - I/O capacity: Digital and analog inputs/outputs
  - Communication: Ethernet, Modbus, Profibus
  - Redundancy: Hot standby configuration

### HMI/SCADA
- **HMI-101**: Human Machine Interface
  - Type: Touch screen panel
  - Size: 15" minimum
  - Features: Trend graphs, alarm management

---

## Process Lines and Connections (ISO Line Standards)

### 1. MAIN PROCESS LINES
- **Line 1001**: Seawater Intake (DN100, PN16)
  - From: Seawater source
  - To: P-101 suction
  - Material: Duplex stainless steel

- **Line 1002**: Pre-treatment Feed (DN100, PN16)
  - From: P-101 discharge  
  - To: F-101 inlet
  - Material: Stainless steel 316L

- **Line 1003**: RO Feed (DN80, PN80)
  - From: F-101 outlet
  - To: P-102 suction
  - Material: Super duplex stainless steel

- **Line 1004**: High Pressure RO Feed (DN80, PN80)
  - From: P-102 discharge
  - To: RO-101 inlet
  - Material: Super duplex stainless steel

- **Line 1005**: RO Permeate (DN65, PN16)
  - From: RO-101 permeate outlet
  - To: F-102 inlet
  - Material: Stainless steel 316L

- **Line 1006**: Post-treatment Outlet (DN65, PN16)
  - From: F-102 outlet
  - To: UV-101 inlet
  - Material: Stainless steel 316L

- **Line 1007**: Treated Water to Ground Tank (DN65, PN16)
  - From: UV-101 outlet
  - To: TK-101 inlet
  - Material: Stainless steel 316L

- **Line 1008**: Ground Tank to Roof Transfer (DN50, PN25)
  - From: TK-101 outlet
  - To: P-105/P-106 suction
  - Material: Stainless steel 316L

- **Line 1009**: Roof Tank Feed (DN50, PN25)
  - From: P-105/P-106 discharge
  - To: TK-102 inlet
  - Material: Stainless steel 316L

### 2. UTILITY LINES
- **Line 2001**: RO Concentrate Reject (DN50, PN80)
  - From: RO-101 concentrate outlet
  - To: Waste discharge
  - Material: Super duplex stainless steel

- **Line 2002**: Filter Backwash (DN80, PN16)
  - From: F-101 backwash outlet
  - To: Waste discharge
  - Material: Stainless steel 316L

- **Line 3001**: Compressed Air (DN25, PN10)
  - Service: Instrument air
  - Material: Galvanized steel

- **Line 4001**: Electrical Power Supply
  - Voltage levels: 400V, 230V, 24VDC
  - Control: 24VDC, 4-20mA signals

---

## Drawing Requirements (ISO Standards)

### 1. TITLE BLOCK (ISO 7200)
- Drawing title: "SEAWATER DESALINATION SYSTEM P&ID"
- Drawing number: DES-PID-001
- Scale: Not to scale (typical for P&IDs)
- Date and revision tracking
- Company information and approval signatures

### 2. SYMBOL STANDARDS
- Follow ISO 14617 for equipment symbols
- Follow ISO 10628 for P&ID conventions
- Use ISA-5.1 for instrument symbols (if ISO symbols not available)
- Line weights: Process lines (thick), instrument lines (thin), utility lines (medium)

### 3. DRAWING LAYOUT
- Process flow: Left to right arrangement
- Equipment elevation: Show relative heights where critical
- Instrument connections: Dashed lines from process to instruments
- Control signals: Pneumatic (dashed), electrical (solid thin)

### 4. NOTES AND SPECIFICATIONS
- Include material specifications for all process lines
- Operating conditions: Temperature, pressure, flow rates
- Utility requirements: Power, compressed air, cooling water
- Safety devices: Pressure relief valves, emergency stops
- Environmental protection: Spill containment, overflow handling

### 5. LEGEND AND ABBREVIATIONS
- Complete symbol legend following ISO standards
- Process abbreviations dictionary
- Instrument abbreviation table (ISA-5.1 based)
- Line identification system explanation

---

## Critical Design Considerations

### 1. MATERIAL COMPATIBILITY
- Seawater exposure: Use corrosion-resistant materials
- High pressure: Ensure proper pressure ratings
- Food grade: Potable water contact materials

### 2. SAFETY SYSTEMS
- Emergency shutdown capabilities
- Pressure relief protection
- Overflow protection for tanks
- Leak detection systems

### 3. MAINTENANCE ACCESS
- Isolation valves for each major component
- Bypass lines where necessary
- Sample points for water quality testing
- Maintenance platforms and access

### 4. CONTROL PHILOSOPHY
- Automatic operation with manual override
- Cascade control for pressure and flow
- Alarm management following IEC 62682
- Batch control for cleaning cycles

---

## OUTPUT REQUIREMENTS

Generate a detailed P&ID drawing that includes:

1. **Complete process flow diagram** with all equipment properly positioned and connected
2. **All instrumentation** with proper ISO tag numbers and symbols
3. **Control system architecture** showing PLC, HMI, and field devices
4. **Utility connections** including power, air, and waste streams
5. **Safety devices** and emergency systems
6. **Material specifications** and operating conditions
7. **Proper ISO formatting** with title block, legend, and notes
8. **Revision tracking** and approval blocks

The P&ID should be suitable for:
- Construction and installation guidance
- Operations and maintenance procedures  
- Safety system verification
- Regulatory approval submissions
- Equipment procurement specifications

**Note**: Ensure all symbols, line types, and annotations strictly follow ISO 14617 and ISO 10628 standards for international compatibility and professional presentation.
