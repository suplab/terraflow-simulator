import numpy as np
import pandas as pd

class Ecosystem:
    def __init__(self, flora=50, fauna=50, water_level=50, human_activity=50):
        self.flora = flora
        self.fauna = fauna
        self.water_level = water_level
        self.human_activity = human_activity
        self.history = pd.DataFrame(columns=['step','flora','fauna','water_level','human_activity'])

    def step(self, intervention=None):
        self.flora += np.random.randint(-2,3) - 0.1*self.human_activity
        self.fauna += np.random.randint(-2,3) + 0.05*self.flora - 0.1*self.human_activity
        self.water_level += np.random.randint(-1,2) - 0.05*self.human_activity

        if intervention:
            self.flora += intervention.get('flora_boost',0)
            self.fauna += intervention.get('fauna_boost',0)
            self.water_level += intervention.get('water_boost',0)
            self.human_activity -= intervention.get('human_activity_reduction',0)

        self.flora = np.clip(self.flora,0,100)
        self.fauna = np.clip(self.fauna,0,100)
        self.water_level = np.clip(self.water_level,0,100)
        self.human_activity = np.clip(self.human_activity,0,100)

        self.history = pd.concat([self.history, pd.DataFrame([{
            'step': len(self.history)+1,
            'flora': self.flora,
            'fauna': self.fauna,
            'water_level': self.water_level,
            'human_activity': self.human_activity
        }])], ignore_index=True)

    def simulate(self, steps=10, interventions=None):
        for i in range(steps):
            intervention = interventions[i] if interventions and i < len(interventions) else None
            self.step(intervention)
        return self.history
