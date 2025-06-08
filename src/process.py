import random
from config import SystemConfig

class DesalinationSystem:
    def __init__(self, config: SystemConfig):
        self.config = config
        self.reset()

    def reset(self):
        self.ground_tank_level = 50.0
        self.roof_tank_level = 50.0
        self.pre_treatment_turbidity = 2.0
        self.ro_feed_pressure = 60.0
        self.alarm = False
        self.intake_pump = False
        self.ro_pump = False
        self.transfer_pump = False

    def step(self):
        c = self.config
        self.pre_treatment_turbidity += random.uniform(-0.2, 0.2)
        self.ro_feed_pressure += random.uniform(-1, 1)
        self.pre_treatment_turbidity = max(0, self.pre_treatment_turbidity)
        pre_treatment_ok = self.pre_treatment_turbidity < c.TURBIDITY_MAX
        ro_ok = pre_treatment_ok and (self.ground_tank_level > 20) and (c.PRESSURE_MIN < self.ro_feed_pressure < c.PRESSURE_MAX)
        self.intake_pump = ro_ok and (self.ground_tank_level < c.GROUND_TANK_MAX)
        self.ro_pump = ro_ok
        self.transfer_pump = (self.ground_tank_level > 30) and (self.roof_tank_level < 90)
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

    def get_status(self):
        return {
            'ground': f"{self.ground_tank_level:.1f}%",
            'roof': f"{self.roof_tank_level:.1f}%",
            'turb': f"{self.pre_treatment_turbidity:.1f} NTU",
            'press': f"{self.ro_feed_pressure:.1f} bar",
            'intake': 'ON' if self.intake_pump else 'OFF',
            'ro': 'ON' if self.ro_pump else 'OFF',
            'transfer': 'ON' if self.transfer_pump else 'OFF',
            'alarm': 'YES' if self.alarm else 'NO'
        }
