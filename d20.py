import random

class d20:

    def roll(self, collated_modifiers):
        result = random.randint(1, 20) + collated_modifiers
        return result
