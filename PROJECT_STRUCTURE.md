# Desalination System Project Structure

src/
    config.py         # System configuration and setpoints
    process.py        # Process logic (DesalinationSystem class)
    hmi.py            # SCADA HMI (Tkinter GUI)
    main.py           # Main simulation entry point

plc/
    main.st           # PLC program (Structured Text)

docs/
    desalination-flowchart.md  # Flowcharts and diagrams
    hardware-spec.md           # Hardware specifications
    control-plan.md            # Control logic and I/O mapping

simulate.py           # Deprecated, see src/main.py

.git/                 # Git repository
README.md             # Project overview and instructions
