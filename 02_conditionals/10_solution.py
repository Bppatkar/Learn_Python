species = "dog"  # Change this to "cat" for testing with a cat
age = 3.5  # Change this value to test different ages

if species == "dog":
    if age < 2:
        food_recommendation = "Puppy food"
    elif age < 7:
        food_recommendation = "Adult dog food"
    else:
        food_recommendation = "Senior dog food"
elif species == "cat":
    if age < 1:
        food_recommendation = "Kitten food"
    elif age < 5:
        food_recommendation = "Adult cat food"
    else:
        food_recommendation = "Senior cat food"
else:
    food_recommendation = "Unknown pet species"

print(f"Recommended food: {food_recommendation}")
