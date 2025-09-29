# Mad Libs with Enhanced Conditionals

print("Welcome to Mad Libs Zoo Adventure!")
print("Let's create a story together!\n")

# Get user inputs
weather = input("What type of weather was it? (Sunny/Windy/Cloudy/Rainy): ")
color = input("What color was the monkey? (Black/White/Brown/Golden): ")
gender = input("What gender was the lion? (Male/Female): ").strip().title()
feeling = input("What was the experience like? (Awesome/Sad/Exciting/Scary): ")
animal_name = input("Give the monkey a name: ").strip()
time_of_day = input("What time of day was it? (Morning/Afternoon/Evening): ")

# 1. WEATHER CONDITIONALS - Multiple variations
if weather == "Sunny":
    weather_description = "It's a bright and beautiful day! The sun is shining brilliantly."
elif weather == "Windy":
    weather_description = "Hold onto your hat, it's quite breezy! Leaves are dancing in the air."
elif weather == "Cloudy":
    weather_description = "The sky is overcast, but it's still a nice day for adventure!"
elif weather == "Rainy":
    weather_description = "Gentle raindrops are falling, making everything fresh and clean."
else:
    weather_description = f"The weather is {weather} - quite unusual for a zoo visit!"

# 2. MONKEY BEHAVIOR CONDITIONALS - Based on color
if color == "Black":
    monkey_behavior = f"{animal_name} the {color.lower()} monkey is swinging dramatically from branch to branch like a shadow in the trees"
elif color == "White":
    monkey_behavior = f"{animal_name} the {color.lower()} monkey is gracefully leaping through the trees like a fluffy cloud"
elif color == "Brown":
    monkey_behavior = f"{animal_name} the {color.lower()} monkey is playfully tumbling around like a furry acrobat"
elif color == "Golden":
    monkey_behavior = f"{animal_name} the {color.lower()} monkey is majestically moving through the trees like a precious treasure"
else:
    monkey_behavior = f"{animal_name} the {color.lower()} monkey is energetically jumping up and down in its tree"

# 3. LION DESCRIPTION CONDITIONALS - Based on gender
if gender == "Male":
    lion_description = "a majestic male lion with a magnificent mane lounging proudly in the sun"
elif gender == "Female":
    lion_description = "an elegant female lioness resting gracefully in the warm sunlight"
else:
    lion_description = f"a {gender.lower()} lion relaxing peacefully in the sun"

# 4. TIME-BASED CONDITIONALS - Different story elements based on time
if time_of_day == "Morning":
    time_context = "As the morning sun rose higher in the sky"
elif time_of_day == "Afternoon":
    time_context = "In the warm afternoon heat"
elif time_of_day == "Evening":
    time_context = "As the golden evening light began to fade"
else:
    time_context = f"During the {time_of_day.lower()}"

# 5. EXPERIENCE CONDITIONALS - Different endings based on feeling
if feeling == "Awesome":
    story_ending = "What an absolutely incredible and unforgettable adventure! I can't wait to come back!"
elif feeling == "Sad":
    story_ending = "Even though I felt a bit melancholy, seeing the animals brought joy to my heart."
elif feeling == "Exciting":
    story_ending = "My heart was racing with excitement throughout the entire visit! What a thrill!"
elif feeling == "Scary":
    story_ending = "Despite feeling a bit frightened, it was an adventure I'll never forget!"
else:
    story_ending = f"The whole experience was simply {feeling.lower()} in every way possible!"


# Build and display the complete story
print(weather_description)
print(f"\n{time_context}, I decided to visit the local zoo.")
print(f"I saw {monkey_behavior}.")
print(f"He didn't have a care in the world!")
print(f"\nThen I spotted {lion_description}.")

print(f"\n{story_ending}")

