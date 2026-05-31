import time
from aether.core.aether_core import AETHER1

def run_continuous_demo(duration_seconds: int = 60):
    """Run AETHER-1 in continuous always-active mode."""
    entity = AETHER1()
    print("=== AETHER-1 Continuous Living Demo Started ===")
    start = time.time()
    while time.time() - start < duration_seconds:
        result = entity.tick_step({"sensor": "simulated_input"})
        if result["tick"] % 20 == 0:
            entity.consolidate_memory()
            entity.evolve()
        time.sleep(0.5)  # Simulate real-time ticking
    print("=== Demo Complete ===")

if __name__ == "__main__":
    run_continuous_demo(30)