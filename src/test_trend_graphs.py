#!/usr/bin/env python3
"""
Test script for the enhanced HMI with real-time trend graphs.
This script demonstrates the trend graph functionality by running
various scenarios and showing how the graphs respond to system changes.
"""

import tkinter as tk
import time
import threading
from config import SystemConfig
from process import DesalinationSystem
from hmi import DesalinationHMI

class TrendGraphDemo:
    def __init__(self):
        self.config = SystemConfig()
        self.system = DesalinationSystem(self.config)
        self.root = tk.Tk()
        self.hmi = DesalinationHMI(self.root, self.system)
        self.demo_running = False
        
        # Add demo control buttons
        self.add_demo_controls()
        
    def add_demo_controls(self):
        """Add demo control buttons to test different scenarios"""
        demo_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        demo_frame.grid(row=4, column=0, sticky='ew', padx=5, pady=5)
        
        tk.Label(demo_frame, text="Demo Controls:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        
        tk.Button(demo_frame, text="Normal Operation", command=self.demo_normal_operation, 
                 bg="#90EE90", width=15).pack(side=tk.LEFT, padx=2)
        
        tk.Button(demo_frame, text="Pressure Variations", command=self.demo_pressure_variations,
                 bg="#87CEEB", width=15).pack(side=tk.LEFT, padx=2)
        
        tk.Button(demo_frame, text="Tank Level Changes", command=self.demo_tank_changes,
                 bg="#DDA0DD", width=15).pack(side=tk.LEFT, padx=2)
        
        tk.Button(demo_frame, text="Mixed Scenario", command=self.demo_mixed_scenario,
                 bg="#F0E68C", width=15).pack(side=tk.LEFT, padx=2)
        
        tk.Button(demo_frame, text="Stop Demo", command=self.stop_demo,
                 bg="#FFB6C1", width=10).pack(side=tk.LEFT, padx=2)
    
    def demo_normal_operation(self):
        """Demo normal system operation with gradual changes"""
        self.stop_demo()
        self.demo_running = True
        
        def normal_operation_thread():
            print("Starting Normal Operation Demo...")
            self.system.start()
            
            # Gradual startup sequence
            for i in range(30):
                if not self.demo_running:
                    break
                    
                # Gradually increase tank levels
                self.system.ground_tank_level = min(80, 20 + i * 2)
                self.system.roof_tank_level = min(70, 15 + i * 1.8)
                
                # Stable pressure with minor fluctuations
                self.system.ro_feed_pressure = 55 + (i % 5) * 2
                
                self.system.step()
                self.hmi.update(i)
                time.sleep(0.5)
            
            print("Normal Operation Demo completed.")
        
        threading.Thread(target=normal_operation_thread, daemon=True).start()
    
    def demo_pressure_variations(self):
        """Demo pressure variations to show pressure trend graph"""
        self.stop_demo()
        self.demo_running = True
        
        def pressure_variations_thread():
            print("Starting Pressure Variations Demo...")
            self.system.start()
            
            import math
            
            for i in range(50):
                if not self.demo_running:
                    break
                
                # Sinusoidal pressure variations
                base_pressure = 60
                variation = 15 * math.sin(i * 0.3)
                self.system.ro_feed_pressure = max(30, min(75, base_pressure + variation))
                
                # Keep tank levels relatively stable
                self.system.ground_tank_level = 50 + 5 * math.sin(i * 0.1)
                self.system.roof_tank_level = 45 + 5 * math.cos(i * 0.1)
                
                self.system.step()
                self.hmi.update(i)
                time.sleep(0.3)
            
            print("Pressure Variations Demo completed.")
        
        threading.Thread(target=pressure_variations_thread, daemon=True).start()
    
    def demo_tank_changes(self):
        """Demo tank level changes to show tank level trend graphs"""
        self.stop_demo()
        self.demo_running = True
        
        def tank_changes_thread():
            print("Starting Tank Level Changes Demo...")
            self.system.start()
            
            phases = [
                ("Filling Phase", lambda i: (min(90, 10 + i * 3), min(85, 5 + i * 2.8))),
                ("Draining Phase", lambda i: (max(20, 90 - i * 2.5), max(15, 85 - i * 2.3))),
                ("Refilling Phase", lambda i: (min(75, 20 + i * 2), min(70, 15 + i * 1.9)))
            ]
            
            for phase_name, level_func in phases:
                print(f"  {phase_name}...")
                for i in range(25):
                    if not self.demo_running:
                        break
                    
                    ground_level, roof_level = level_func(i)
                    self.system.ground_tank_level = ground_level
                    self.system.roof_tank_level = roof_level
                    
                    # Stable pressure
                    self.system.ro_feed_pressure = 58 + (i % 3)
                    
                    self.system.step()
                    self.hmi.update(i)
                    time.sleep(0.4)
            
            print("Tank Level Changes Demo completed.")
        
        threading.Thread(target=tank_changes_thread, daemon=True).start()
    
    def demo_mixed_scenario(self):
        """Demo mixed scenario with complex patterns"""
        self.stop_demo()
        self.demo_running = True
        
        def mixed_scenario_thread():
            print("Starting Mixed Scenario Demo...")
            self.system.start()
            
            import math
            
            for i in range(60):
                if not self.demo_running:
                    break
                
                # Complex tank level patterns
                self.system.ground_tank_level = 50 + 20 * math.sin(i * 0.2) + 10 * math.cos(i * 0.05)
                self.system.roof_tank_level = 45 + 25 * math.cos(i * 0.15) + 5 * math.sin(i * 0.08)
                
                # Complex pressure pattern with spikes
                base_pressure = 55 + 10 * math.sin(i * 0.1)
                spike = 15 if i % 20 == 0 else 0  # Pressure spikes every 20 iterations
                self.system.ro_feed_pressure = max(35, min(75, base_pressure + spike))
                
                # Clamp tank levels to valid ranges
                self.system.ground_tank_level = max(10, min(95, self.system.ground_tank_level))
                self.system.roof_tank_level = max(5, min(90, self.system.roof_tank_level))
                
                self.system.step()
                self.hmi.update(i)
                time.sleep(0.25)
            
            print("Mixed Scenario Demo completed.")
        
        threading.Thread(target=mixed_scenario_thread, daemon=True).start()
    
    def stop_demo(self):
        """Stop the current demo"""
        self.demo_running = False
        self.system.stop()
        print("Demo stopped.")
    
    def run(self):
        """Run the demo application"""
        print("=== Enhanced HMI Trend Graphs Demo ===")
        print("Use the demo control buttons to test different scenarios:")
        print("- Normal Operation: Gradual startup and steady operation")
        print("- Pressure Variations: Shows pressure trend graph with sinusoidal variations")
        print("- Tank Level Changes: Shows tank filling/draining cycles")
        print("- Mixed Scenario: Complex patterns demonstrating both graphs")
        print("\nThe trend graphs show:")
        print("- Left plot: Ground Tank (green) and Roof Tank (blue) levels (%)")
        print("- Right plot: RO Feed Pressure (red) in bar")
        print("- Time window: Last 60 seconds of data")
        print("\nStart the system and run a demo to see the trends!")
        
        # Initial update
        self.hmi.update(0)
        
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nDemo terminated by user.")
        finally:
            self.stop_demo()

if __name__ == "__main__":
    demo = TrendGraphDemo()
    demo.run()
