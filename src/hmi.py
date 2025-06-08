import tkinter as tk
from process import DesalinationSystem

class DesalinationHMI:
    def __init__(self, root, system: DesalinationSystem):
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
        c = self.system.config
        self.set_label_color(self.labels['ground'], status['ground'], 'black', 'red', self.system.ground_tank_level < c.GROUND_TANK_MIN or self.system.ground_tank_level > c.GROUND_TANK_MAX)
        self.set_label_color(self.labels['roof'], status['roof'], 'black', 'red', self.system.roof_tank_level > c.ROOF_TANK_MAX)
        self.set_label_color(self.labels['turb'], status['turb'], 'black', 'red', self.system.pre_treatment_turbidity > c.TURBIDITY_MAX)
        self.set_label_color(self.labels['press'], status['press'], 'black', 'red', self.system.ro_feed_pressure < c.PRESSURE_MIN or self.system.ro_feed_pressure > c.PRESSURE_MAX)
        self.set_label_color(self.labels['intake'], status['intake'], 'green', 'gray', status['intake'] == 'OFF')
        self.set_label_color(self.labels['ro'], status['ro'], 'green', 'gray', status['ro'] == 'OFF')
        self.set_label_color(self.labels['transfer'], status['transfer'], 'green', 'gray', status['transfer'] == 'OFF')
        self.set_label_color(self.labels['alarm'], status['alarm'], 'black', 'red', status['alarm'] == 'YES')
        self.root.update()
