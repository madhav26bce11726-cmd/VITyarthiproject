"""Main application entry point."""

from diet_tracker import (
    BMICalculator,
    FoodDatabase,
    UserProfile,
    setup_logger,
    InvalidInputError,
    FoodNotFoundError
)

logger = setup_logger()
db = FoodDatabase()

def get_positive_float(prompt: str) -> float:
    """Ensures input is a valid positive floating point number."""
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Invalid input! Please enter a number greater than 0.")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def main():
    print("====================================")
    print("     STUDENT DIET & CALORIE LOG")
    print("====================================")

    name = input("Enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter your name: ").strip()

    weight = get_positive_float("Enter weight in kg: ")
    height = get_positive_float("Enter height in cm: ")

    try:
        bmi, category, target_cal = BMICalculator.calculate_stats(weight, height)
        user = UserProfile(name, weight, height, bmi, category, target_cal)
        logger.info(f"Initialized user profile: {name}, BMI: {bmi}, Category: {category}")
    except InvalidInputError as e:
        print(f"Error initializing profile: {e}")
        logger.error(f"Failed profile creation for {name}: {e}")
        return

    print("\n------------------------------------")
    print(f"Hello, {user.name}")
    print(f"Your BMI is: {user.bmi}")
    print(f"Status: {user.category}")
    print(f"Daily Calorie Target: {user.target_cal} kcal")
    print("------------------------------------")

    print("\nRecommended food items for you:")
    for food in db.get_recommendations(user.category):
        print(f"- {food}")

    while True:
        print("\n-------- MENU --------")
        print("1. Check Remaining Calories")
        print("2. Add Food (Eat)")
        print("3. Add Exercise (Burn)")
        print("4. View Today's Log")
        print("5. Generate Final Report & Exit")
        print("----------------------")
        
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            print(f"\nTarget Calories: {user.target_cal} kcal")
            print(f"Remaining Balance: {user.balance_cal} kcal")
            if user.balance_cal < 0:
                print("Warning: You have exceeded your daily calorie intake limit!")

        elif choice == "2":
            print(f"\nAvailable pre-configured foods: {', '.join(db.get_available_foods())}")
            print("Tip: You can enter more food item(s) by using commas")
            raw_input = input("Enter food item(s): ").strip()
            if not raw_input:
                print("No food items entered")
                continue
            #Use of commas to seperate multiple food items
            items = [i.strip().lower() for i in raw_input.split(",") if i.strip()]

            for item in items:
                # asking quantity of food items
                qty = round(get_positive_float(f"How many '{item}' did you eat? "))
                try:
                    cal_per_unit = db.get_food_calories(item)
                    print(f"Found '{item}' : {cal_per_unit} kcal per unit.")
                except FoodNotFoundError:
                    print(f"'{item}' not found in database.")
                    cal_per_unit = round(
                        get_positive_float(
                            f"Enter approximate calories for 1 unit of '{item}': "
                        )
                    )

                user.log_food(item, cal_per_unit, qty)
                logger.info(
                    f"Logged intake: {qty}x {item} ({cal_per_unit * qty} kcal) "
                    f"for user {user.name}"
                )
                print(f"Item logged: {qty}x {item} ({cal_per_unit * qty} kcal).")
            print(f"All items logged successfully! Remaining Balance: {user.balance_cal} kcal")

        elif choice == "3":
            work = input("\nEnter workout/activity name: ").strip()
            burn = round(get_positive_float("Enter calories burned: "))
            user.log_workout(work, burn)
            logger.info(f"Logged activity: {work} ({burn} kcal) for user {user.name}")
            print(f"Burn logged. Updated balance: {user.balance_cal} kcal")

        elif choice == "4":
            print("\n--- Current Activity Log ---")
            if not user.history:
                print("No activities logged yet today.")
            else:
                for entry in user.history:
                    print(entry)
            print(f"Remaining calories: {user.balance_cal} kcal")

        elif choice == "5":
            print("\n" + "=" * 40)
            print("       FINAL DIET & HEALTH SUMMARY")
            print("=" * 40)
            print(f"Student Name   : {user.name}")
            print(f"BMI Score      : {user.bmi} ({user.category})")
            print(f"Daily Target   : {user.target_cal} kcal")
            print(f"Final Balance  : {user.balance_cal} kcal")
            print("-" * 40)
            print("Today's Activity Log:")
            if not user.history:
                print("  (No activities logged)")
            else:
                for entry in user.history:
                    print(f"  • {entry}")
            print("=" * 40)
            print("Thank you for using the Student Diet Tracker. Goodbye!")
            logger.info(f"Session closed for user {user.name}")
            break
        else:
            print("Invalid choice! Please select a valid option from 1 to 5.")

if __name__ == "__main__":
    main()