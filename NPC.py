class NPC:

    def __init__(self, name,  spot_mod, listen_mod):
        self.name = name
        self.listen_mod = listen_mod
        self.spot_mod = spot_mod

    def __repr__(self):
        self.str_repr = self.name
        return self.str_repr


