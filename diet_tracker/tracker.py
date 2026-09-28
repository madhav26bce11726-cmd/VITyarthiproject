"""Session logging and state management module."""

class UserProfile:
    """Tracks user health state, calorie consumption, and exercise history."""

    def __init__(self, name: str, weight: float, height: float, bmi: float, category: str, target_cal: int):
        self.name = name
        self.weight = weight
        self.height = height
        self.bmi = bmi
        self.category = category
        self.target_cal = target_cal
        self.balance_cal = target_cal
        self.history = []

    def log_food(self, item_name: str, calories: int, quantity: int = 1):
        """Logs consumed food item with quantity and updates balance."""
        total_calories = calories * quantity
        self.balance_cal -= calories
        if quantity > 1:
            self.history.append(f"Eaten: {quantity}x {item_name} (-{total_calories} kcal)")
        else:
            self.history.append(f"Eaten:  {item_name} (-{total_calories} kcal)")

    def log_workout(self, workout_name: str, calories_burned: int):
        """Logs workout activity and updates balance."""
        self.balance_cal += calories_burned
        self.history.append(f"Workout: {workout_name} (+{calories_burned} kcal)")