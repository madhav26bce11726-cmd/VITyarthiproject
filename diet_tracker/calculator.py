"""Health calculation module for BMI and Calorie targets."""

from .exceptions import InvalidInputError

class BMICalculator:
    """Performs mathematical calculations for health metrics."""

    @staticmethod
    def calculate_stats(weight: float, height: float) -> tuple:
        """Calculates BMI, category, and daily target calorie intake."""
        if weight <= 0 or height <= 0:
            raise InvalidInputError("Weight and height must be strictly positive values.")

        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        bmr = (10 * weight) + (6.25 * height) - 100
        
        if bmi < 18.5:
            category = "Underweight"
            target_cal = int(bmr + 400)
        elif bmi <= 24.9:
            category = "Normal"
            target_cal = int(bmr)
        else:
            category = "Overweight"
            target_cal = int(bmr - 400)
            
        return round(bmi, 1), category, target_cal