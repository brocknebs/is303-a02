"""
Brock Nebeker
IS 303- A02

Meal Recommender
This program suggests a meal based on the time of day, dietary preference, and budget

Inputs:
- Time of day
- Dietary Preference
- Budget

Processes:
- List of foods for every meal
- List of foods for every diet
- List of foods for every budget
- Check if the meal, diet, or budget is a valid option (check from lists)
- First filter by time of day, then by diet, then by budget

Outputs:
- Time of day and the recommended meal
- Print error message if invalid input
"""
# Inputs
time_of_day = input("Time of Day: ").lower()
diet = input("Diet: ").lower()
budget = input("Budget: ").lower()

# Processes
time_types = ["breakfast", "lunch", "dinner"]
diet_types = ["vegetarian", "vegan", "none"]
budget_types = ["low", "medium", "high"]

# Outputs
if time_of_day in time_types:
    if diet in diet_types:
        if budget in budget_types:
            print("---")
            if time_of_day == "breakfast":
                if diet == "vegan":
                    if budget == "low":
                        print(f"{time_of_day}: Frozen Hashbrowns")
                    elif budget == "medium":
                        print(f"{time_of_day}: Precooked Hashbrowns")
                    else:
                        print(f"{time_of_day}: Steamed Hashbrowns")
                elif time_of_day == "vegetarian":
                    if budget == "low":
                        print(f"{time_of_day}: Oatmeal")
                    elif budget == "medium":
                        print(f"{time_of_day}: Eggs")
                    else:
                        print(f"{time_of_day}: Avacado Toast")
                else:
                    if budget == "low":
                        print(f"{time_of_day}: Eggs")
                    elif budget == "medium":
                        print(f"{time_of_day}: Eggs and Hashbrowns")
                    else:
                        print(f"{time_of_day}: Eggs, Hashbrowns, and Bacon")
            elif time_of_day == "lunch":
                if diet == "vegan":
                    if budget == "low":
                        print(f"{time_of_day}: Frozen Hashbrowns")
                    elif budget == "medium":
                        print(f"{time_of_day}: Precooked Hashbrowns")
                    else:
                        print(f"{time_of_day}: Steamed Hashbrowns")
                elif time_of_day == "vegetarian":
                    if budget == "low":
                        print(f"{time_of_day}: Eggs")
                    elif budget == "medium":
                        print(f"{time_of_day}: Grilled Cheese Sandwich")
                    else:
                        print(f"{time_of_day}: Grilled Cheese with Tomato Soup")
                else:
                    if budget == "low":
                        print(f"{time_of_day}: Turkey Sandwich")
                    elif budget == "medium":
                        print(f"{time_of_day}: Grilled Cheese with Tomato Soup")
                    else:
                        print(f"{time_of_day}: BLT")
            else:
                if diet == "vegan":
                    if budget == "low":
                        print(f"{time_of_day}: Frozen Hashbrowns")
                    elif budget == "medium":
                        print(f"{time_of_day}: Precooked Hashbrowns")
                    else:
                        print(f"{time_of_day}: Steamed Hashbrowns")
                elif time_of_day == "vegetarian":
                    if budget == "low":
                        print(f"{time_of_day}: Rice and Beans")
                    elif budget == "medium":
                        print(f"{time_of_day}: Impossible Burger with Fries")
                    else:
                        print(f"{time_of_day}: Cheese Pizza")
                else:
                    if budget == "low":
                        print(f"{time_of_day}: Tacos")
                    elif budget == "medium":
                        print(f"{time_of_day}: Burgers")
                    else:
                        print(f"{time_of_day}: Alfredo")

        else:
            print("Error: Budget must be low, medium, or high.")

    else:
        print("Error: Diet must be vegan, vegetarian, or none.")
else:
    print("Error: Time of day must be breakfast, lunch, or dinner.")
