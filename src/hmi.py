import tkinter as tk
from process import DesalinationSystem
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from collections import deque
import time

class DesalinationHMI:
    def __init__(self, root, system: DesalinationSystem):
        self.root = root
        self.system = system
        self.vars = {k: tk.StringVar() for k in ['step','ground','roof','turb','press','intake','ro','transfer','alarm','p103','p104','p105','p106','v101','uv101','alm101','prv101','production_rate','total_produced','efficiency']}
        self.labels = {}
        self.status_indicators = {}
        
        # Trend data storage
        self.max_trend_points = 50  # Keep last 50 data points
        self.trend_data = {
            'time': deque(maxlen=self.max_trend_points),
            'ground_level': deque(maxlen=self.max_trend_points),
            'roof_level': deque(maxlen=self.max_trend_points),
            'pressure': deque(maxlen=self.max_trend_points)
        }
        self.start_time = time.time()
        
        self._build_gui()

    def _build_gui(self):
        import tkinter.ttk as ttk
        self.root.title("Desalination System - Compact SCADA HMI")
        self.root.configure(bg="#e6e6e6")

        # --- System Control Bar ---
        ctrl_frame = tk.Frame(self.root, bg="#e6e6e6", pady=5)
        ctrl_frame.grid(row=0, column=0, sticky='ew', padx=5)
        status_lbl = tk.Label(ctrl_frame, textvariable=self.vars['step'], font=("Arial", 14, "bold"), bg="#e6e6e6", fg="#003366", width=22, anchor='w')
        status_lbl.pack(side=tk.LEFT, padx=(5, 10))
        self.start_btn = tk.Button(ctrl_frame, text="START", width=8, command=self.start_system, bg="#d9ead3", font=("Arial", 10, "bold"))
        self.start_btn.pack(side=tk.LEFT, padx=2)
        tk.Button(ctrl_frame, text="STOP", width=8, command=self.stop_system, bg="#f4cccc", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=2)
        self.emergency_btn = tk.Button(ctrl_frame, text="E-STOP", width=8, command=self.emergency_stop, bg="#ea9999", font=("Arial", 10, "bold"))
        self.emergency_btn.pack(side=tk.LEFT, padx=2)
        tk.Button(ctrl_frame, text="Drain Roof Tank", width=15, command=self.drain_roof_tank, bg="#cfe2f3").pack(side=tk.LEFT, padx=10)
        # Mode checkboxes (placeholders)
        tk.Checkbutton(ctrl_frame, text="Auto Mode", bg="#e6e6e6").pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(ctrl_frame, text="Maintenance", bg="#e6e6e6").pack(side=tk.LEFT, padx=5)        # --- System Overview ---
        overview = tk.Frame(self.root, bg="#f9f9f9", pady=5, padx=5, relief=tk.GROOVE, bd=2)
        overview.grid(row=1, column=0, sticky='ew', padx=5, pady=(0,5))
        
        tk.Label(overview, text="Production Rate", font=("Arial", 10, "bold"), bg="#f9f9f9").grid(row=0, column=0, padx=10)
        self.production_rate_lbl = tk.Label(overview, textvariable=self.vars['production_rate'], font=("Arial", 10), fg="#009933", bg="#f9f9f9")
        self.production_rate_lbl.grid(row=1, column=0)
        
        tk.Label(overview, text="Total Produced", font=("Arial", 10, "bold"), bg="#f9f9f9").grid(row=0, column=1, padx=10)
        self.total_produced_lbl = tk.Label(overview, textvariable=self.vars['total_produced'], font=("Arial", 10), fg="#009933", bg="#f9f9f9")
        self.total_produced_lbl.grid(row=1, column=1)
        
        tk.Label(overview, text="Ground Tank", font=("Arial", 10, "bold"), bg="#f9f9f9").grid(row=0, column=2, padx=10)
        tk.Label(overview, textvariable=self.vars['ground'], font=("Arial", 10), fg="#009933", bg="#f9f9f9").grid(row=1, column=2)
        
        tk.Label(overview, text="RO Pressure", font=("Arial", 10, "bold"), bg="#f9f9f9").grid(row=0, column=3, padx=10)
        tk.Label(overview, textvariable=self.vars['press'], font=("Arial", 10), fg="#009933", bg="#f9f9f9").grid(row=1, column=3)
        
        tk.Label(overview, text="Efficiency", font=("Arial", 10, "bold"), bg="#f9f9f9").grid(row=0, column=4, padx=10)
        self.efficiency_lbl = tk.Label(overview, textvariable=self.vars['efficiency'], font=("Arial", 10), fg="#009933", bg="#f9f9f9")
        self.efficiency_lbl.grid(row=1, column=4)

        # --- Main Content (Components, Alarms, Process Data) ---
        main_content = tk.Frame(self.root, bg="#e6e6e6")
        main_content.grid(row=2, column=0, sticky='ew', padx=5)
        # Components (left)
        comp_frame = tk.LabelFrame(main_content, text="Components", font=("Arial", 11, "bold"), bg="#e6e6e6", fg="#003366", padx=8, pady=5)
        comp_frame.grid(row=0, column=0, sticky='n', padx=(0,10), pady=2)
        # Pumps
        pumps_frame = tk.LabelFrame(comp_frame, text="Pumps", font=("Arial", 10, "bold"), bg="#e6e6e6", fg="#003366", padx=5, pady=2)
        pumps_frame.pack(fill='x', pady=2)
        actuators = [
            ('intake', "Intake"),
            ('ro', "RO"),
            ('transfer', "Transfer"),
            ('p103', "Post-treat"),
            ('p104', "To Ground"),
            ('p105', "To Rooftop"),
            ('p106', "To Roof Tank")
        ]
        for idx, (key, label) in enumerate(actuators):
            tk.Label(pumps_frame, text=label, font=("Arial", 10), bg="#e6e6e6").grid(row=idx, column=0, sticky='e')
            tk.Label(pumps_frame, textvariable=self.vars[key], font=("Arial", 10), bg="#e6e6e6").grid(row=idx, column=1, sticky='w')
        # Tanks
        tanks_frame = tk.LabelFrame(comp_frame, text="Tanks", font=("Arial", 10, "bold"), bg="#e6e6e6", fg="#003366", padx=5, pady=2)
        tanks_frame.pack(fill='x', pady=2)
        tk.Label(tanks_frame, text="Ground Tank", font=("Arial", 10), bg="#e6e6e6").grid(row=0, column=0, sticky='e')
        self.ground_pb = ttk.Progressbar(tanks_frame, length=120, maximum=100)
        self.ground_pb.grid(row=0, column=1, padx=5)
        self.ground_val_lbl = tk.Label(tanks_frame, textvariable=self.vars['ground'], font=("Arial", 10), bg="#e6e6e6", width=7, anchor='w')
        self.ground_val_lbl.grid(row=0, column=2, sticky='w', padx=(5,0))
        tk.Label(tanks_frame, text="Roof Tank", font=("Arial", 10), bg="#e6e6e6").grid(row=1, column=0, sticky='e')
        self.roof_pb = ttk.Progressbar(tanks_frame, length=120, maximum=100)
        self.roof_pb.grid(row=1, column=1, padx=5)
        self.roof_val_lbl = tk.Label(tanks_frame, textvariable=self.vars['roof'], font=("Arial", 10), bg="#e6e6e6", width=7, anchor='w')
        self.roof_val_lbl.grid(row=1, column=2, sticky='w', padx=(5,0))        # System Alarms (center)
        alarm_frame = tk.LabelFrame(main_content, text="System Alarms", font=("Arial", 11, "bold"), bg="#e6e6e6", fg="#990000", padx=8, pady=5)
        alarm_frame.grid(row=0, column=1, sticky='n', padx=(0,10), pady=2)
        
        # Store alarm checkboxes for updating
        self.alarm_checkboxes = {}
        
        alarms = [
            ("Emergency Stop", 'emergency'),
            ("Low Tank Level", 'low_tank'),
            ("RO Pressure Fault", 'pressure_fault'),
            ("System Leak", 'system_leak'),
            ("High Tank Level", 'high_tank'),
            ("Pump Fault", 'pump_fault'),
            ("Water Quality", 'water_quality'),
            ("General Alarm", 'general_alarm')
        ]
        
        for idx, (label, key) in enumerate(alarms):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(alarm_frame, text=label, variable=var, bg="#e6e6e6", 
                               state='disabled', disabledforeground="#666666")
            cb.grid(row=idx, column=0, sticky='w')
            self.alarm_checkboxes[key] = {'var': var, 'widget': cb}
        
        # Active alarms summary
        self.active_alarms_lbl = tk.Label(alarm_frame, text="Active: None", font=("Arial", 10, "italic"), 
                                         fg="#009933", bg="#e6e6e6")
        self.active_alarms_lbl.grid(row=len(alarms), column=0, sticky='w', pady=(5,0))

        # Process Data (right)
        proc_frame = tk.LabelFrame(main_content, text="Process Data", font=("Arial", 11, "bold"), bg="#e6e6e6", fg="#003366", padx=8, pady=5)
        proc_frame.grid(row=0, column=2, sticky='n', pady=2)
        tk.Label(proc_frame, text="Water Quality", font=("Arial", 10, "bold"), bg="#e6e6e6").grid(row=0, column=0, sticky='w')
        tk.Label(proc_frame, text="Turbidity:", font=("Arial", 10), bg="#e6e6e6").grid(row=1, column=0, sticky='e')
        tk.Label(proc_frame, textvariable=self.vars['turb'], font=("Arial", 10), bg="#e6e6e6").grid(row=1, column=1, sticky='w')
        tk.Label(proc_frame, text="RO Pressure:", font=("Arial", 10), bg="#e6e6e6").grid(row=2, column=0, sticky='e')
        tk.Label(proc_frame, textvariable=self.vars['press'], font=("Arial", 10), bg="#e6e6e6").grid(row=2, column=1, sticky='w')        # --- Real-Time Trends ---
        trends_frame = tk.LabelFrame(self.root, text="Real-Time Trends", font=("Arial", 12, "bold"), fg="#003366", bg="#1a2634", padx=10, pady=5)
        trends_frame.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
        
        # Create matplotlib figure for trends
        self.trend_fig = Figure(figsize=(14, 4), dpi=80, facecolor='#1a2634')
        
        # Create subplots for tank levels and pressure
        self.tank_level_ax = self.trend_fig.add_subplot(121)
        self.pressure_ax = self.trend_fig.add_subplot(122)
        
        # Configure tank level plot
        self.tank_level_ax.set_title('Tank Levels (%)', color='white', fontsize=10, fontweight='bold')
        self.tank_level_ax.set_ylabel('Level (%)', color='white', fontsize=9)
        self.tank_level_ax.set_xlabel('Time (s)', color='white', fontsize=9)
        self.tank_level_ax.set_facecolor('#0d1117')
        self.tank_level_ax.tick_params(colors='white', labelsize=8)
        self.tank_level_ax.grid(True, alpha=0.3, color='white')
        self.tank_level_ax.set_ylim(0, 100)
        
        # Configure pressure plot
        self.pressure_ax.set_title('RO Feed Pressure (bar)', color='white', fontsize=10, fontweight='bold')
        self.pressure_ax.set_ylabel('Pressure (bar)', color='white', fontsize=9)
        self.pressure_ax.set_xlabel('Time (s)', color='white', fontsize=9)
        self.pressure_ax.set_facecolor('#0d1117')
        self.pressure_ax.tick_params(colors='white', labelsize=8)
        self.pressure_ax.grid(True, alpha=0.3, color='white')
        self.pressure_ax.set_ylim(0, 80)
        
        # Initialize empty line plots
        self.ground_line, = self.tank_level_ax.plot([], [], 'g-', linewidth=2, label='Ground Tank')
        self.roof_line, = self.tank_level_ax.plot([], [], 'b-', linewidth=2, label='Roof Tank')
        self.pressure_line, = self.pressure_ax.plot([], [], 'r-', linewidth=2, label='RO Pressure')
        
        # Add legends
        self.tank_level_ax.legend(loc='upper right', fontsize=8, facecolor='#1a2634', edgecolor='white', labelcolor='white')
        self.pressure_ax.legend(loc='upper right', fontsize=8, facecolor='#1a2634', edgecolor='white', labelcolor='white')
        
        # Embed plots in tkinter
        self.trend_canvas = FigureCanvasTkAgg(self.trend_fig, trends_frame)
        self.trend_canvas.get_tk_widget().pack(fill='both', expand=True)
        self.trend_canvas.draw()

        # Save references for update
        self.comp_frame = comp_frame
        self.tanks_frame = tanks_frame
        self.alarm_frame = alarm_frame
        self.proc_frame = proc_frame
        self.trends_frame = trends_frame

    def set_label_color(self, label, value, normal_color, alarm_color, alarm_cond):
        label.config(fg=alarm_color if alarm_cond else normal_color)
        # Also update status indicator if present
        key = None
        for k, v in self.labels.items():
            if v == label:
                key = k
                break
        if key and hasattr(self, 'status_indicators') and key in self.status_indicators:
            canvas, indicator = self.status_indicators[key]
            color = alarm_color if alarm_cond else normal_color
            # Map to SCADA-like colors
            if color == 'green':
                fill = '#00cc44'
            elif color == 'gray':
                fill = '#cccccc'
            elif color == 'red':
                fill = '#ff3333'
            elif color == 'black':
                fill = '#222222'
            else:
                fill = color
            canvas.itemconfig(indicator, fill=fill)

    def update(self, step):
        status = self.system.get_status()
        # Set a more meaningful title
        if getattr(self.system, 'emergency', False):
            self.vars['step'].set("SYSTEM STOPPED - EMERGENCY")
        elif getattr(self.system, 'running', False):
            self.vars['step'].set("SYSTEM RUNNING")
        else:
            self.vars['step'].set("SYSTEM STOPPED")
        for k in self.vars:
            if k != 'step':
                self.vars[k].set(status.get(k, 'OFF'))
        c = self.system.config
        # Update progress bars for tanks (parse percentage from string like '54.2%')
        try:
            ground_str = status.get('ground', '0')
            ground_val = float(ground_str.replace('%','').strip())
            self.ground_pb['value'] = max(0, min(100, ground_val))
        except Exception:
            self.ground_pb['value'] = 0
            
        try:
            roof_str = status.get('roof', '0')
            roof_val = float(roof_str.replace('%','').strip())
            self.roof_pb['value'] = max(0, min(100, roof_val))
        except Exception:
            self.roof_pb['value'] = 0
              # Update alarm indicators
        self._update_alarm_indicators()
        # Update production metric label colors based on status
        self._update_production_colors()
        # Update trend data and plots
        self._update_trends()
        
        self.root.update()

    def _update_alarm_indicators(self):
        """Update alarm indicator checkboxes based on system status"""
        c = self.system.config
        active_alarms = []
        
        # Emergency Stop
        emergency_active = getattr(self.system, 'emergency', False)
        self.alarm_checkboxes['emergency']['var'].set(emergency_active)
        if emergency_active:
            active_alarms.append("Emergency")
            self.alarm_checkboxes['emergency']['widget'].config(fg="#ff0000")
        else:
            self.alarm_checkboxes['emergency']['widget'].config(fg="#666666")
            
        # Low Tank Level
        low_tank = self.system.ground_tank_level < c.GROUND_TANK_MIN
        self.alarm_checkboxes['low_tank']['var'].set(low_tank)
        if low_tank:
            active_alarms.append("Low Tank")
            self.alarm_checkboxes['low_tank']['widget'].config(fg="#ff6600")
        else:
            self.alarm_checkboxes['low_tank']['widget'].config(fg="#666666")
            
        # RO Pressure Fault
        pressure_fault = (self.system.ro_feed_pressure < c.PRESSURE_MIN or 
                         self.system.ro_feed_pressure > c.PRESSURE_MAX)
        self.alarm_checkboxes['pressure_fault']['var'].set(pressure_fault)
        if pressure_fault:
            active_alarms.append("Pressure")
            self.alarm_checkboxes['pressure_fault']['widget'].config(fg="#ff6600")
        else:
            self.alarm_checkboxes['pressure_fault']['widget'].config(fg="#666666")
            
        # System Leak (using ALM101)
        system_leak = getattr(self.system, 'alm101', False)
        self.alarm_checkboxes['system_leak']['var'].set(system_leak)
        if system_leak:
            active_alarms.append("Leak")
            self.alarm_checkboxes['system_leak']['widget'].config(fg="#ff3300")
        else:
            self.alarm_checkboxes['system_leak']['widget'].config(fg="#666666")
            
        # High Tank Level
        high_tank = self.system.roof_tank_level > c.ROOF_TANK_MAX
        self.alarm_checkboxes['high_tank']['var'].set(high_tank)
        if high_tank:
            active_alarms.append("High Tank")
            self.alarm_checkboxes['high_tank']['widget'].config(fg="#ff6600")
        else:
            self.alarm_checkboxes['high_tank']['widget'].config(fg="#666666")
            
        # Pump Fault (any critical pump off when it should be on)
        pump_fault = (getattr(self.system, 'running', False) and 
                     not self.system.ro_pump and 
                     self.system.ground_tank_level > 20)
        self.alarm_checkboxes['pump_fault']['var'].set(pump_fault)
        if pump_fault:
            active_alarms.append("Pump Fault")
            self.alarm_checkboxes['pump_fault']['widget'].config(fg="#ff6600")
        else:
            self.alarm_checkboxes['pump_fault']['widget'].config(fg="#666666")
            
        # Water Quality
        water_quality = self.system.pre_treatment_turbidity > c.TURBIDITY_MAX
        self.alarm_checkboxes['water_quality']['var'].set(water_quality)
        if water_quality:
            active_alarms.append("Water Quality")
            self.alarm_checkboxes['water_quality']['widget'].config(fg="#ff9900")
        else:
            self.alarm_checkboxes['water_quality']['widget'].config(fg="#666666")
            
        # General Alarm
        general_alarm = getattr(self.system, 'alarm', False)
        self.alarm_checkboxes['general_alarm']['var'].set(general_alarm)
        if general_alarm:
            active_alarms.append("General")
            self.alarm_checkboxes['general_alarm']['widget'].config(fg="#ff0000")
        else:
            self.alarm_checkboxes['general_alarm']['widget'].config(fg="#666666")
            
        # Update summary
        if active_alarms:
            alarm_text = f"Active: {', '.join(active_alarms)}"
            self.active_alarms_lbl.config(text=alarm_text, fg="#ff0000")
        else:
            self.active_alarms_lbl.config(text="Active: None", fg="#009933")
    
    def _update_production_colors(self):
        """Update production metric label colors based on performance"""
        # Production Rate colors
        if self.system.production_rate > 4.0:
            self.production_rate_lbl.config(fg="#009933")  # Good production
        elif self.system.production_rate > 2.0:
            self.production_rate_lbl.config(fg="#ff9900")  # Moderate production
        else:
            self.production_rate_lbl.config(fg="#ff3300")  # Low/no production
            
        # Efficiency colors
        if self.system.efficiency > 80:
            self.efficiency_lbl.config(fg="#009933")  # High efficiency
        elif self.system.efficiency > 60:
            self.efficiency_lbl.config(fg="#ff9900")  # Moderate efficiency
        else:
            self.efficiency_lbl.config(fg="#ff3300")  # Low efficiency
            
        # Total produced is informational, keep it neutral
        self.total_produced_lbl.config(fg="#009933")

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

    def _update_trends(self):
        """Update trend data and refresh the trend plots"""
        # Add current time and data points
        current_time = time.time() - self.start_time
        self.trend_data['time'].append(current_time)
        self.trend_data['ground_level'].append(self.system.ground_tank_level)
        self.trend_data['roof_level'].append(self.system.roof_tank_level)
        self.trend_data['pressure'].append(self.system.ro_feed_pressure)
        
        # Convert deques to lists for matplotlib
        times = list(self.trend_data['time'])
        ground_levels = list(self.trend_data['ground_level'])
        roof_levels = list(self.trend_data['roof_level'])
        pressures = list(self.trend_data['pressure'])
        
        # Update tank level plot
        self.ground_line.set_data(times, ground_levels)
        self.roof_line.set_data(times, roof_levels)
        
        # Update pressure plot  
        self.pressure_line.set_data(times, pressures)
        
        # Adjust x-axis limits to show a rolling window
        if times:
            # Show last 60 seconds of data
            max_time = max(times)
            min_time = max(0, max_time - 60)
            
            self.tank_level_ax.set_xlim(min_time, max_time)
            self.pressure_ax.set_xlim(min_time, max_time)
            
            # Auto-scale y-axis if needed
            if ground_levels or roof_levels:
                all_levels = ground_levels + roof_levels
                level_min = max(0, min(all_levels) - 5)
                level_max = min(100, max(all_levels) + 5)
                self.tank_level_ax.set_ylim(level_min, level_max)
            
            if pressures:
                pressure_min = max(0, min(pressures) - 5)
                pressure_max = min(80, max(pressures) + 5)
                self.pressure_ax.set_ylim(pressure_min, pressure_max)
        
        # Refresh the canvas
        self.trend_canvas.draw_idle()

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
