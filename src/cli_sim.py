import time
from config import SystemConfig
from process import DesalinationSystem

def main():
    config = SystemConfig()
    system = DesalinationSystem(config)
    print("Desalination System CLI Simulator")
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
    main()
