"""Custom exceptions module for error handling."""

class DietTrackerError(Exception):
    """Base exception class for all diet tracker exceptions."""
    pass

class InvalidInputError(DietTrackerError):
    """Raised when user enters invalid numeric inputs or out-of-bounds data."""
    pass

class FoodNotFoundError(DietTrackerError):
    """Raised when a food item is not found in the pre-configured database."""
    pass