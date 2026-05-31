from aether.core.aether_core import AETHER1

entity = AETHER1()
for i in range(5):
    result = entity.tick_step()
    print(result)
entity.act("Explore new environment")