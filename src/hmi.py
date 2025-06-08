import tkinter as tk
from process import DesalinationSystem

class DesalinationHMI:
    def __init__(self, root, system: DesalinationSystem):
        self.root = root
        self.system = system
        self.vars = {k: tk.StringVar() for k in ['step','ground','roof','turb','press','intake','ro','transfer','alarm','p103','p104','p105','p106','v101','uv101','alm101']}
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
        # Add control buttons
        frame_ctrl = tk.LabelFrame(self.root, text="Controls", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_ctrl.grid(row=5, column=0, padx=10, pady=10, sticky='ew')
        tk.Label(self.root, textvariable=self.vars['step'], font=("Arial", 14, "bold")).grid(row=0, column=0, pady=5)
        self.labels['ground'] = tk.Label(frame_tanks, text="Ground Tank Level:", font=("Arial", 11))
        self.labels['ground'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_tanks, textvariable=self.vars['ground'], font=("Arial", 11)).grid(row=0, column=1, sticky='w')
        self.labels['roof'] = tk.Label(frame_tanks, text="Roof Tank Level:", font=("Arial", 11))
        self.labels['roof'].grid(row=1, column=0, sticky='e')
        tk.Label(frame_tanks, textvariable=self.vars['roof'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        self.labels['turb'] = tk.Label(frame_proc, text="Turbidity:", font=("Arial", 11))
        self.labels['turb'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_proc, textvariable=self.vars['turb'], font=("Arial", 11)).grid(row=0, column=1, sticky='w')
        self.labels['press'] = tk.Label(frame_proc, text="RO Feed Pressure:", font=("Arial", 11))
        self.labels['press'].grid(row=1, column=0, sticky='e')
        tk.Label(frame_proc, textvariable=self.vars['press'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        self.labels['intake'] = tk.Label(frame_pumps, text="Intake Pump:", font=("Arial", 11))
        self.labels['intake'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['intake'], font=("Arial", 11)).grid(row=0, column=1, sticky='w')
        self.labels['ro'] = tk.Label(frame_pumps, text="RO Pump:", font=("Arial", 11))
        self.labels['ro'].grid(row=1, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['ro'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        self.labels['transfer'] = tk.Label(frame_pumps, text="Transfer Pump:", font=("Arial", 11))
        self.labels['transfer'].grid(row=2, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['transfer'], font=("Arial", 11)).grid(row=2, column=1, sticky='w')
        # Architecture Update: Add new actuators to HMI
        self.labels['p103'] = tk.Label(frame_pumps, text="Post-treatment Pump:", font=("Arial", 11))
        self.labels['p103'].grid(row=3, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['p103'], font=("Arial", 11)).grid(row=3, column=1, sticky='w')
        self.labels['p104'] = tk.Label(frame_pumps, text="Transfer Pump to Ground:", font=("Arial", 11))
        self.labels['p104'].grid(row=4, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['p104'], font=("Arial", 11)).grid(row=4, column=1, sticky='w')
        self.labels['p105'] = tk.Label(frame_pumps, text="Pump to Rooftop:", font=("Arial", 11))
        self.labels['p105'].grid(row=5, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['p105'], font=("Arial", 11)).grid(row=5, column=1, sticky='w')
        self.labels['p106'] = tk.Label(frame_pumps, text="Transfer Pump to Roof Tank:", font=("Arial", 11))
        self.labels['p106'].grid(row=6, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['p106'], font=("Arial", 11)).grid(row=6, column=1, sticky='w')
        self.labels['v101'] = tk.Label(frame_pumps, text="Motorized Valve V101:", font=("Arial", 11))
        self.labels['v101'].grid(row=7, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['v101'], font=("Arial", 11)).grid(row=7, column=1, sticky='w')
        self.labels['uv101'] = tk.Label(frame_pumps, text="UV Disinfection:", font=("Arial", 11))
        self.labels['uv101'].grid(row=8, column=0, sticky='e')
        tk.Label(frame_pumps, textvariable=self.vars['uv101'], font=("Arial", 11)).grid(row=8, column=1, sticky='w')
        self.labels['alm101'] = tk.Label(frame_alarm, text="General Alarm:", font=("Arial", 11, "bold"))
        self.labels['alm101'].grid(row=1, column=0, sticky='e')
        tk.Label(frame_alarm, textvariable=self.vars['alm101'], font=("Arial", 11, "bold")).grid(row=1, column=1, sticky='w')
        self.labels['alarm'] = tk.Label(frame_alarm, text="Alarm:", font=("Arial", 11, "bold"))
        self.labels['alarm'].grid(row=0, column=0, sticky='e')
        tk.Label(frame_alarm, textvariable=self.vars['alarm'], font=("Arial", 11, "bold")).grid(row=0, column=1, sticky='w')
        # Add control buttons
        frame_ctrl = tk.LabelFrame(self.root, text="Controls", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_ctrl.grid(row=5, column=0, padx=10, pady=10, sticky='ew')
        tk.Button(frame_ctrl, text="Start", width=10, command=self.start_system).grid(row=0, column=0, padx=5)
        tk.Button(frame_ctrl, text="Stop", width=10, command=self.stop_system).grid(row=0, column=1, padx=5)
        tk.Button(frame_ctrl, text="Emergency", width=10, command=self.emergency_stop).grid(row=0, column=2, padx=5)
        tk.Button(frame_ctrl, text="Drain Roof Tank", width=15, command=self.drain_roof_tank).grid(row=0, column=3, padx=5)

    def set_label_color(self, label, value, normal_color, alarm_color, alarm_cond):
        label.config(fg=alarm_color if alarm_cond else normal_color)

    def update(self, step):
        status = self.system.get_status()
        self.vars['step'].set(f"Step {step+1}")
        for k in self.vars:
            if k in status:
                self.vars[k].set(status[k])
        c = self.system.config
        self.set_label_color(self.labels['ground'], status['ground'], 'black', 'red', self.system.ground_tank_level < c.GROUND_TANK_MIN or self.system.ground_tank_level > c.GROUND_TANK_MAX)
        self.set_label_color(self.labels['roof'], status['roof'], 'black', 'red', self.system.roof_tank_level > c.ROOF_TANK_MAX)
        self.set_label_color(self.labels['turb'], status['turb'], 'black', 'red', self.system.pre_treatment_turbidity > c.TURBIDITY_MAX)
        self.set_label_color(self.labels['press'], status['press'], 'black', 'red', self.system.ro_feed_pressure < c.PRESSURE_MIN or self.system.ro_feed_pressure > c.PRESSURE_MAX)
        self.set_label_color(self.labels['intake'], status['intake'], 'green', 'gray', status['intake'] == 'OFF')
        self.set_label_color(self.labels['ro'], status['ro'], 'green', 'gray', status['ro'] == 'OFF')
        self.set_label_color(self.labels['transfer'], status['transfer'], 'green', 'gray', status['transfer'] == 'OFF')
        self.set_label_color(self.labels['alarm'], status['alarm'], 'black', 'red', status['alarm'] == 'YES')
        # Architecture Update: Add color logic for new actuators if needed
        self.root.update()

    def start_system(self):
        self.system.start()
        self._run_loop()

    def stop_system(self):
        self.system.stop()

    def emergency_stop(self):
        self.system.emergency_stop()
        self.update(-1)

    def drain_roof_tank(self):
        self.system.drain_roof_tank()
        self.update(-1)

    def _run_loop(self):
        if getattr(self.system, 'running', False) and not getattr(self.system, 'emergency', False):
            self.system.step()
            self.update(getattr(self, '_step', 0))
            self._step = getattr(self, '_step', 0) + 1
            self.root.after(500, self._run_loop)
        else:
            self.update(getattr(self, '_step', 0))

if __name__ == "__main__":
    from config import SystemConfig
    from process import DesalinationSystem
    import tkinter as tk
    config = SystemConfig()
    system = DesalinationSystem(config)
    root = tk.Tk()
    hmi = DesalinationHMI(root, system)
    hmi.update(0)
    root.mainloop()
