# System setpoints and parameters for Desalination System
class SystemConfig:
    GROUND_TANK_MIN = 10.0
    GROUND_TANK_MAX = 95.0
    ROOF_TANK_MAX = 98.0
    TURBIDITY_MAX = 5.0
    PRESSURE_MIN = 50.0
    PRESSURE_MAX = 70.0
    SIM_STEPS = 30
    # Architecture Update: Add setpoints for all new actuators and sensors as per new architecture
    # Additional pumps and actuators (P-103 to P-106, V-101...V-106, UV-101, ALM-101) can be configured here if needed
    # Example:
    # POST_TREATMENT_PUMP_MIN = ...
    # TRANSFER_PUMP_GROUND_MIN = ...
    # PUMP_TO_ROOFTOP_MIN = ...
    # TRANSFER_PUMP_ROOF_MIN = ...
    # Add more as required for expanded architecture
