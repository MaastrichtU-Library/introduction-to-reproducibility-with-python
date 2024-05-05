class HealthMetrics:
    def __init__(self):
        pass

    @staticmethod
    def height_in_meters(height, metric):
        if metric == 'cm':
            return round(height / 100, 2)
        elif metric == 'ft':
            return round(height * 0.3048, 2)
        elif metric == 'm':
            return height
        else:
            raise ValueError("Unknown metric unit")

    @staticmethod
    def calculate_bmi(weight, height):
        bmi = weight / (height ** 2)
        return round(bmi, 2)

    @staticmethod
    def calculate_bfp(fat_mass, weight):
        bfp = (fat_mass / weight) * 100
        return round(bfp, 2)