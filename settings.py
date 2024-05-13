class Settings:

    def __init__(self):
        self.scale = 50
        self.bg_color = (158, 179, 184)
        self.rain_speed = 10

        self.choices = list(range(11, 31))
        self.probability = []

        for i in range(1, 21):
            self.probability.append(round(((5.625 - i * 0.25) / 60), 2))
