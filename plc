// Siemens S7-1200 PLC Program (Structured Text - TIA Portal style)
// Desalination & Rooftop Storage System - Main Control Logic
// This is a simplified, modular example for reference only.

PROGRAM Main
VAR
    // Analog Inputs
    LT_101 : REAL; // Ground Tank Level
    LT_102 : REAL; // Roof Tank Level
    FT_101 : REAL; // Intake Flow
    FT_102 : REAL; // RO Permeate Flow
    PT_101 : REAL; // RO Feed Pressure
    PT_102 : REAL; // RO Permeate Pressure
    TU_101 : REAL; // Turbidity

    // Digital/Analog Outputs
    P_101 : BOOL; // Seawater Intake Pump
    P_102 : BOOL; // RO High-Pressure Pump
    P_103 : BOOL; // Transfer Pump to Roof
    V_101, V_102, V_103, V_104, V_105, V_106 : BOOL; // Valves
    UV_101 : BOOL; // UV Disinfection
    ALM_101 : BOOL; // General Alarm

    // Internal
    PreTreatment_OK : BOOL;
    RO_OK : BOOL;
    PostTreatment_OK : BOOL;
    Alarm : BOOL;
END_VAR

// Pre-treatment logic
PreTreatment_OK := (TU_101 < 5.0); // Example: turbidity < 5 NTU

// RO logic
RO_OK := PreTreatment_OK AND (LT_101 > 20.0) AND (PT_101 > 50.0) AND (PT_101 < 70.0);
P_102 := RO_OK;

// Intake pump logic
P_101 := RO_OK AND (LT_101 < 95.0);

// Post-treatment logic
PostTreatment_OK := RO_OK;
UV_101 := PostTreatment_OK;

// Transfer pump to roof tank
P_103 := (LT_101 > 30.0) AND (LT_102 < 90.0);

// Alarms
Alarm := (TU_101 > 10.0) OR (PT_101 < 45.0) OR (PT_101 > 75.0) OR (LT_101 < 10.0) OR (LT_102 > 98.0);
ALM_101 := Alarm;

// Example valve logic (open/close as needed)
V_101 := P_101;
V_102 := P_102;
V_103 := P_103;
// ... add more detailed valve logic as needed

END_PROGRAM

// Notes:
// - All setpoints (e.g., levels, pressures) should be adjusted for your system.
// - Add interlocks, manual/auto modes, and HMI/SCADA interface as required.
// - For a real project, modularize code and use function blocks for each subsystem.
