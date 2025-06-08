# Simple Python Simulation for Desalination & Rooftop Storage System
# This simulates tank levels, pump/valve states, and alarms in a time-stepped loop.

import random
import tkinter as tk
import time

# System setpoints and parameters
GROUND_TANK_MIN = 10.0
GROUND_TANK_MAX = 95.0
ROOF_TANK_MAX = 98.0
TURBIDITY_MAX = 5.0
PRESSURE_MIN = 50.0
PRESSURE_MAX = 70.0
SIM_STEPS = 30

class DesalinationSystem:
    def __init__(self):
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
        # Simulate random changes
        self.pre_treatment_turbidity += random.uniform(-0.2, 0.2)
        self.ro_feed_pressure += random.uniform(-1, 1)
        self.pre_treatment_turbidity = max(0, self.pre_treatment_turbidity)
        # Control logic
        pre_treatment_ok = self.pre_treatment_turbidity < TURBIDITY_MAX
        ro_ok = pre_treatment_ok and (self.ground_tank_level > 20) and (PRESSURE_MIN < self.ro_feed_pressure < PRESSURE_MAX)
        self.intake_pump = ro_ok and (self.ground_tank_level < GROUND_TANK_MAX)
        self.ro_pump = ro_ok
        self.transfer_pump = (self.ground_tank_level > 30) and (self.roof_tank_level < 90)
        # Simulate tank level changes
        if self.intake_pump:
            self.ground_tank_level += 1.5
        if self.ro_pump:
            self.ground_tank_level -= 1.0
        if self.transfer_pump:
            self.ground_tank_level -= 0.5
            self.roof_tank_level += 0.5
        # Clamp values
        self.ground_tank_level = min(max(self.ground_tank_level, GROUND_TANK_MIN), GROUND_TANK_MAX)
        self.roof_tank_level = min(max(self.roof_tank_level, 0), ROOF_TANK_MAX)
        # Alarms
        self.alarm = (
            self.pre_treatment_turbidity > 10 or
            self.ro_feed_pressure < 45 or self.ro_feed_pressure > 75 or
            self.ground_tank_level < GROUND_TANK_MIN or
            self.roof_tank_level > ROOF_TANK_MAX
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

# HMI/SCADA GUI
class DesalinationHMI:
    def __init__(self, root, system):
        self.root = root
        self.system = system
        self.vars = {k: tk.StringVar() for k in ['step','ground','roof','turb','press','intake','ro','transfer','alarm']}
        self.labels = {}
        self._build_gui()

    def _build_gui(self):
        self.root.title("Desalination System SCADA HMI Simulation")
        frame_tanks = tk.LabelFrame(self.root, text="Tank Levels", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_tanks.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        frame_proc = tk.LabelFrame(self.root, text="Process Values", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_proc.grid(row=2, column=0, padx=10, pady=5, sticky='ew')
        frame_pumps = tk.LabelFrame(self.root, text="Pump Status", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_pumps.grid(row=3, column=0, padx=10, pady=5, sticky='ew')
        frame_alarm = tk.LabelFrame(self.root, text="Alarm", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_alarm.grid(row=4, column=0, padx=10, pady=5, sticky='ew')
        tk.Label(self.root, textvariable=self.vars['step'], font=("Arial", 14, "bold")).grid(row=0, column=0, pady=5)
        # Tank levels
        self.labels['ground'] = tk.Label(frame_tanks, text="Ground Tank Level:", font=("Arial", 11))
        self.labels['ground'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_tanks, textvariable=self.vars['ground'], font=("Arial", 11)).grid(row=0, column=1, sticky='w')
        self.labels['roof'] = tk.Label(frame_tanks, text="Roof Tank Level:", font=("Arial", 11))
        self.labels['roof'].grid(row=1, column=0, sticky='e')
        tk.Label(frame_tanks, textvariable=self.vars['roof'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        # Process values
        self.labels['turb'] = tk.Label(frame_proc, text="Turbidity:", font=("Arial", 11))
        self.labels['turb'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_proc, textvariable=self.vars['turb'], font=("Arial", 11)).grid(row=0, column=1, sticky='w')
        self.labels['press'] = tk.Label(frame_proc, text="RO Feed Pressure:", font=("Arial", 11))
        self.labels['press'].grid(row=1, column=0, sticky='e')
        tk.Label(frame_proc, textvariable=self.vars['press'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        # Pump status
        self.labels['intake'] = tk.Label(frame_pumps, text="Intake Pump:", font=("Arial", 11))
        self.labels['intake'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['intake'], font=("Arial", 11)).grid(row=0, column=1, sticky='w')
        self.labels['ro'] = tk.Label(frame_pumps, text="RO Pump:", font=("Arial", 11))
        self.labels['ro'].grid(row=1, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['ro'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        self.labels['transfer'] = tk.Label(frame_pumps, text="Transfer Pump:", font=("Arial", 11))
        self.labels['transfer'].grid(row=2, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['transfer'], font=("Arial", 11)).grid(row=2, column=1, sticky='w')
        # Alarm
        self.labels['alarm'] = tk.Label(frame_alarm, text="Alarm:", font=("Arial", 11, "bold"))
        self.labels['alarm'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_alarm, textvariable=self.vars['alarm'], font=("Arial", 11, "bold")).grid(row=0, column=1, sticky='w')

    def set_label_color(self, label, value, normal_color, alarm_color, alarm_cond):
        label.config(fg=alarm_color if alarm_cond else normal_color)

    def update(self, step):
        status = self.system.get_status()
        self.vars['step'].set(f"Step {step+1}")
        for k in ['ground','roof','turb','press','intake','ro','transfer','alarm']:
            self.vars[k].set(status[k])
        # Color coding for alarms and status
        self.set_label_color(self.labels['ground'], status['ground'], 'black', 'red', self.system.ground_tank_level < GROUND_TANK_MIN or self.system.ground_tank_level > GROUND_TANK_MAX)
        self.set_label_color(self.labels['roof'], status['roof'], 'black', 'red', self.system.roof_tank_level > ROOF_TANK_MAX)
        self.set_label_color(self.labels['turb'], status['turb'], 'black', 'red', self.system.pre_treatment_turbidity > TURBIDITY_MAX)
        self.set_label_color(self.labels['press'], status['press'], 'black', 'red', self.system.ro_feed_pressure < PRESSURE_MIN or self.system.ro_feed_pressure > PRESSURE_MAX)
        self.set_label_color(self.labels['intake'], status['intake'], 'green', 'gray', status['intake'] == 'OFF')
        self.set_label_color(self.labels['ro'], status['ro'], 'green', 'gray', status['ro'] == 'OFF')
        self.set_label_color(self.labels['transfer'], status['transfer'], 'green', 'gray', status['transfer'] == 'OFF')
        self.set_label_color(self.labels['alarm'], status['alarm'], 'black', 'red', status['alarm'] == 'YES')
        self.root.update()

# Main simulation loop
if __name__ == "__main__":
    system = DesalinationSystem()
    root = tk.Tk()
    hmi = DesalinationHMI(root, system)
    for t in range(SIM_STEPS):
        system.step()
        hmi.update(t)
        time.sleep(0.5)
    root.mainloop()
