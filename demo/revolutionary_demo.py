from aether.core.aether_core import AETHER1
import time

def run_revolutionary_demo():
    print("=== AETHER-1 PUBLIC REVOLUTIONARY DEMO ===")
    entity = AETHER1("AETHER-Public-Demo")
    for i in range(30):
        result = entity.tick_step({"world": "public_demo_input"})
        if i % 5 == 0:
            entity.act("Demonstrating autonomous goal pursuit")
        time.sleep(0.3)
    print("Demo complete. AETHER-1 is alive and evolving.")

if __name__ == "__main__":
    run_revolutionary_demo()