from NPC import *

class PC(NPC):
    def __init__(self, name, spot_mod, listen_mod, sneak_mod, hide_mod, speed):
        super().__init__(name, spot_mod, listen_mod)
        self.sneak_mod = sneak_mod
        self.hide_mod = hide_mod
        self.speed = speed

    def __repr__(self):
        self.str_repr = self.name
        return self.str_repr
