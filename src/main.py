import time
import tkinter as tk
from config import SystemConfig
from process import DesalinationSystem
from hmi import DesalinationHMI

if __name__ == "__main__":
    config = SystemConfig()
    system = DesalinationSystem(config)
    root = tk.Tk()
    hmi = DesalinationHMI(root, system)
    for t in range(config.SIM_STEPS):
        system.step()
        hmi.update(t)
        time.sleep(0.5)
    root.mainloop()
