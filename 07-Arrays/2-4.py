# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   meals = ''
   for i, meal in enumerate(meal_plan[day_number]):
      meals += meal
      if i+1 < len(meal_plan[day_number]):
         meals += ', '
   return meals

# Prints weekly meal plan
print("WEEKLY MEAL PLAN")
print("==========================")
print("Monday: ",day_meal_plan(meal_plan, 0))
print("Tuesday: ",day_meal_plan(meal_plan, 1))
print("Wednesday: ",day_meal_plan(meal_plan, 2))
print("Thursday: ",day_meal_plan(meal_plan, 3))
print("Friday: ",day_meal_plan(meal_plan, 4))
print("Saturday: ",day_meal_plan(meal_plan, 5))
print("Sunday: ",day_meal_plan(meal_plan, 6))