import random
from config import SystemConfig

class DesalinationSystem:
    def __init__(self, config: SystemConfig):
        self.config = config
        self.reset()
        # Architecture Update: Add new actuators and sensors as attributes
        self.p103 = False  # Post-treatment Pump
        self.p104 = False  # Transfer Pump to Ground Tank
        self.p105 = False  # Pump to Rooftop
        self.p106 = False  # Transfer Pump to Roof Tank
        self.v101 = False  # Motorized Valves (example, can be expanded)
        self.uv101 = False # UV Disinfection
        self.alm101 = False # General Alarm

    def reset(self):
        self.ground_tank_level = 50.0
        self.roof_tank_level = 50.0
        self.pre_treatment_turbidity = 2.0
        self.ro_feed_pressure = 60.0
        self.alarm = False
        self.intake_pump = False
        self.ro_pump = False
        self.transfer_pump = False
        self.running = False  # Ensure system boots in STOP condition
        self.emergency = False
        # Architecture Update: Reset new actuators
        self.p103 = False
        self.p104 = False
        self.p105 = False
        self.p106 = False
        self.v101 = False
        self.uv101 = False
        self.alm101 = False

    def step(self):
        if not getattr(self, 'running', False):
            # If not running, all pumps and actuators should be OFF
            self.intake_pump = False
            self.ro_pump = False
            self.transfer_pump = False
            self.p103 = False
            self.p104 = False
            self.p105 = False
            self.p106 = False
            self.v101 = False
            self.uv101 = False
            self.alm101 = False
            return
        c = self.config
        self.pre_treatment_turbidity += random.uniform(-0.2, 0.2)
        self.ro_feed_pressure += random.uniform(-1, 1)
        self.pre_treatment_turbidity = max(0, self.pre_treatment_turbidity)
        pre_treatment_ok = self.pre_treatment_turbidity < c.TURBIDITY_MAX
        ro_ok = pre_treatment_ok and (self.ground_tank_level > 20) and (c.PRESSURE_MIN < self.ro_feed_pressure < c.PRESSURE_MAX)
        self.intake_pump = ro_ok and (self.ground_tank_level < c.GROUND_TANK_MAX)
        self.ro_pump = ro_ok
        self.transfer_pump = (self.ground_tank_level > 30) and (self.roof_tank_level < 90)
        # Architecture Update: New actuators logic (example, can be expanded)
        self.p103 = (self.ground_tank_level > 30)  # Post-treatment pump logic
        self.p104 = (self.ro_pump and self.ground_tank_level < c.GROUND_TANK_MAX)  # Transfer to ground tank
        self.p105 = (self.ground_tank_level > 40) and (self.roof_tank_level < 95)  # Pump to rooftop
        self.p106 = (self.roof_tank_level < c.ROOF_TANK_MAX)  # Transfer to roof tank
        self.v101 = self.intake_pump or self.ro_pump  # Example: open valve if any pump is on
        self.uv101 = self.ro_pump  # UV on if RO is running
        self.alm101 = self.alarm
        if self.intake_pump:
            self.ground_tank_level += 1.5
        if self.ro_pump:
            self.ground_tank_level -= 1.0
        if self.transfer_pump:
            self.ground_tank_level -= 0.5
            self.roof_tank_level += 0.5
        self.ground_tank_level = min(max(self.ground_tank_level, c.GROUND_TANK_MIN), c.GROUND_TANK_MAX)
        self.roof_tank_level = min(max(self.roof_tank_level, 0), c.ROOF_TANK_MAX)
        self.alarm = (
            self.pre_treatment_turbidity > 10 or
            self.ro_feed_pressure < 45 or self.ro_feed_pressure > 75 or
            self.ground_tank_level < c.GROUND_TANK_MIN or
            self.roof_tank_level > c.ROOF_TANK_MAX
        )
        self.alm101 = self.alarm

    def get_status(self):
        return {
            'ground': f"{self.ground_tank_level:.1f}%",
            'roof': f"{self.roof_tank_level:.1f}%",
            'turb': f"{self.pre_treatment_turbidity:.1f} NTU",
            'press': f"{self.ro_feed_pressure:.1f} bar",
            'intake': 'ON' if self.intake_pump else 'OFF',
            'ro': 'ON' if self.ro_pump else 'OFF',
            'transfer': 'ON' if self.transfer_pump else 'OFF',
            'alarm': 'YES' if self.alarm else 'NO',
            # Architecture Update: Add new actuators to status
            'p103': 'ON' if self.p103 else 'OFF',
            'p104': 'ON' if self.p104 else 'OFF',
            'p105': 'ON' if self.p105 else 'OFF',
            'p106': 'ON' if self.p106 else 'OFF',
            'v101': 'ON' if self.v101 else 'OFF',
            'uv101': 'ON' if self.uv101 else 'OFF',
            'alm101': 'ON' if self.alm101 else 'OFF'
        }

    def start(self):
        # Simulate staged startup: clear alarm, check preconditions, then enable running
        if self.alarm:
            print("[START SEQUENCE] Alarm present. Resetting alarm...")
            self.alarm = False
        if self.ground_tank_level < 20 or self.roof_tank_level > self.config.ROOF_TANK_MAX:
            print("[START SEQUENCE] Preconditions not met. Cannot start.")
            self.running = False
            return
        print("[START SEQUENCE] System starting...")
        self.intake_pump = False
        self.ro_pump = False
        self.transfer_pump = False
        self.emergency = False
        self.running = True

    def stop(self):
        # Simulate staged shutdown: turn off all pumps and actuators, set running to False
        print("[STOP SEQUENCE] Stopping system. Turning off all pumps and actuators...")
        self.intake_pump = False
        self.ro_pump = False
        self.transfer_pump = False
        self.p103 = False
        self.p104 = False
        self.p105 = False
        self.p106 = False
        self.v101 = False
        self.uv101 = False
        self.alm101 = False
        self.running = False
        # Optionally, set alarm if needed

    def emergency_stop(self):
        # Immediate shutdown: all pumps off, alarm set, emergency lockout
        print("[EMERGENCY SEQUENCE] EMERGENCY STOP! All pumps OFF. Alarm set.")
        self.intake_pump = False
        self.ro_pump = False
        self.transfer_pump = False
        self.running = False
        self.emergency = True
        self.alarm = True

    def drain_roof_tank(self, amount=2.0):
        self.roof_tank_level = max(0, self.roof_tank_level - amount)

# Simulation loop for interactive control
def run_simulation():
    from config import SystemConfig
    import time

    config = SystemConfig()
    system = DesalinationSystem(config)
    system.running = False
    system.emergency = False

    print("Desalination System Simulation")
    print("Commands: start, stop, emergency, drain, status, exit")
    while True:
        cmd = input("Enter command: ").strip().lower()
        if cmd == "start":
            system.start()
            print("System started.")
        elif cmd == "stop":
            system.stop()
            print("System stopped.")
        elif cmd == "emergency":
            system.emergency_stop()
            print("EMERGENCY STOP activated!")
        elif cmd == "drain":
            system.drain_roof_tank()
            print("Roof tank drained (simulated usage).")
        elif cmd == "status":
            print(system.get_status())
        elif cmd == "exit":
            print("Exiting simulation.")
            break
        else:
            print("Unknown command.")
        # Run step if running and not in emergency
        if getattr(system, 'running', False) and not getattr(system, 'emergency', False):
            system.step()
            print("[Step]", system.get_status())
        time.sleep(0.5)

if __name__ == "__main__":
    run_simulation()
