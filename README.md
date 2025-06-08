# Desalination System Simulation

This project simulates and documents a modular desalination and rooftop storage system, including process logic, HMI/SCADA, PLC code, and hardware specifications.

## Project Structure

- `src/` — Python simulation and HMI code
- `plc/` — PLC program (Structured Text)
- `docs/` — Documentation (flowcharts, hardware, control plan)
    - `desalination-flowchart.md`: Process/control flowcharts, logic diagrams, siteplan
    - `control-plan.md`: Control philosophy, main logic, I/O table (fully matches simulator and PLC code)
    - `hardware-spec.md`: Hardware and instrumentation specifications
- `simulate.py` — Deprecated, see `src/main.py`

## How to Run the Simulation

1. Open a terminal in the `src/` directory.
2. Run: `python main.py`

## Documentation Highlights

- **Flowcharts & Diagrams:** See `docs/desalination-flowchart.md` for detailed process, control, and logic diagrams (Mermaid format).
- **I/O Table:** See `docs/control-plan.md` for a complete mapping of all sensors, actuators, and control logic, including PRV-101 (Pressure Relief Valve).
- **Hardware Specs:** See `docs/hardware-spec.md` for all pumps, tanks, sensors, and control panel details.
- **PLC Code:** See `plc/` for a Siemens S7-1200 Structured Text program that matches the simulator logic and I/O table.

---

For more details, see `PROJECT_STRUCTURE.md`.
