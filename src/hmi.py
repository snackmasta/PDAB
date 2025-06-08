import tkinter as tk
from process import DesalinationSystem

class DesalinationHMI:
    def __init__(self, root, system: DesalinationSystem):
        self.root = root
        self.system = system
        self.vars = {k: tk.StringVar() for k in ['step','ground','roof','turb','press','intake','ro','transfer','alarm','p103','p104','p105','p106','v101','uv101','alm101','prv101']}
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
        self.start_btn = tk.Button(frame_ctrl, text="Start", width=10, command=self.start_system)
        self.start_btn.grid(row=0, column=0, padx=5)
        tk.Button(frame_ctrl, text="Stop", width=10, command=self.stop_system).grid(row=0, column=1, padx=5)
        self.emergency_btn = tk.Button(frame_ctrl, text="Emergency", width=10, command=self.emergency_stop)
        self.emergency_btn.grid(row=0, column=2, padx=5)
        tk.Button(frame_ctrl, text="Drain Roof Tank", width=15, command=self.drain_roof_tank).grid(row=0, column=3, padx=5)
        # Add PRV101 label only if not already present
        if 'prv101' not in self.labels:
            self.labels['prv101'] = tk.Label(frame_pumps, text="Pressure Relief Valve PRV101:", font=("Arial", 11))
            self.labels['prv101'].grid(row=9, column=0, sticky='e')
            tk.Label(frame_pumps, textvariable=self.vars['prv101'], font=("Arial", 11)).grid(row=9, column=1, sticky='w')

    def set_label_color(self, label, value, normal_color, alarm_color, alarm_cond):
        label.config(fg=alarm_color if alarm_cond else normal_color)

    def update(self, step):
        status = self.system.get_status()
        # Set a more meaningful title
        if getattr(self.system, 'emergency', False):
            self.vars['step'].set("SYSTEM STOPPED - EMERGENCY")
        elif getattr(self.system, 'running', False):
            self.vars['step'].set("SYSTEM RUNNING")
        else:
            self.vars['step'].set("Desalination System Ready")
        for k in self.vars:
            if k != 'step':
                self.vars[k].set(status.get(k, 'OFF'))
        c = self.system.config
        # Only set label color if label exists
        for label_key in self.labels:
            if label_key in status:
                if label_key == 'alarm':
                    self.set_label_color(self.labels[label_key], status.get(label_key,'OFF'), 'black', 'red', status.get(label_key,'OFF') == 'YES')
                elif label_key == 'prv101':
                    self.set_label_color(self.labels[label_key], status.get(label_key,'OFF'), 'green', 'gray', status.get(label_key,'OFF') == 'OFF')
                elif label_key in ['ground','roof','turb','press']:
                    # Use process value logic
                    continue
                else:
                    self.set_label_color(self.labels[label_key], status.get(label_key,'OFF'), 'green', 'gray', status.get(label_key,'OFF') == 'OFF')
        self.set_label_color(self.labels['ground'], status.get('ground','OFF'), 'black', 'red', self.system.ground_tank_level < c.GROUND_TANK_MIN or self.system.ground_tank_level > c.GROUND_TANK_MAX)
        self.set_label_color(self.labels['roof'], status.get('roof','OFF'), 'black', 'red', self.system.roof_tank_level > c.ROOF_TANK_MAX)
        self.set_label_color(self.labels['turb'], status.get('turb','OFF'), 'black', 'red', self.system.pre_treatment_turbidity > c.TURBIDITY_MAX)
        self.set_label_color(self.labels['press'], status.get('press','OFF'), 'black', 'red', self.system.ro_feed_pressure < c.PRESSURE_MIN or self.system.ro_feed_pressure > c.PRESSURE_MAX)
        self.root.update()

    def start_system(self):
        # Prevent start if emergency is active
        if getattr(self.system, 'emergency', False):
            return
        self.system.start()
        self._run_loop()

    def stop_system(self):
        self.system.stop()

    def emergency_stop(self):
        self.system.emergency_stop()
        # Explicitly set all actuator status variables to OFF in the GUI
        for key in [
            'intake', 'ro', 'transfer', 'p103', 'p104', 'p105', 'p106',
            'v101', 'uv101', 'alm101', 'prv101'
        ]:
            self.vars[key].set('OFF')
        # Also forcibly set the underlying process attributes to False
        self.system.intake_pump = False
        self.system.ro_pump = False
        self.system.transfer_pump = False
        self.system.p103 = False
        self.system.p104 = False
        self.system.p105 = False
        self.system.p106 = False
        self.system.v101 = False
        self.system.uv101 = False
        self.system.alm101 = False
        self.system.prv101 = False
        self.update(-1)
        # Disable Start button until emergency is cleared
        self.start_btn.config(state='disabled')
        self.emergency_btn.config(text='Reset Emergency', width=18, command=self.reset_emergency)
        self.vars['step'].set("SYSTEM STOPPED - EMERGENCY")

    def reset_emergency(self):
        # Clear emergency and alarm, re-enable Start button
        self.system.alarm = False
        self.system.emergency = False
        self.update(-1)
        self.start_btn.config(state='normal')
        self.emergency_btn.config(text='Emergency', width=10, command=self.emergency_stop)
        # Restore title to normal
        self.vars['step'].set("Desalination System Ready")

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
