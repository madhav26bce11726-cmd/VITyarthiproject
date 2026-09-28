"""Food database and recommendation engine."""

from .exceptions import FoodNotFoundError

class FoodDatabase:
    """Manages food items, calorie lookup, and meal recommendations."""

    def __init__(self):
        self._food_dict = {
            "roti": 85,
            "dal": 150,
            "rice": 180,
            "paneer": 250,
            "egg": 75,
            "banana": 90,
            "salad": 50,
            "milk": 140,
            "apple": 80
        }
        self._diet_options = {
            "Underweight": ["Banana shake", "Paneer paratha", "Boiled eggs", "Peanut butter toast"],
            "Normal": ["Dal roti", "Mixed veg rice", "Sprouts salad", "Fresh curd"],
            "Overweight": ["Green salad", "Boiled chana", "Oats chilla", "Clear soup"]
        }

    def get_food_calories(self, item_name: str) -> int:
        """Fetch calorie count for a specific food item."""
        item = item_name.strip().lower()
        if item in self._food_dict:
            return self._food_dict[item]
        raise FoodNotFoundError(f"Item '{item_name}' not found in database.")

    def get_recommendations(self, category: str) -> list:
        """Get dietary suggestions based on BMI health status."""
        return self._diet_options.get(category, [])

    def get_available_foods(self) -> list:
        """Return list of default foods."""
        return list(self._food_dict.keys())