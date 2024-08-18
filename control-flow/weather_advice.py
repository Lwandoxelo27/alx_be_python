# Prompt User for Weather Input
weather = input("What is the weather like today? (sunny/cold):")
                
# Provide Clothing
if weather == "sunny":
    print("Wear a t-shirt and sunglasses")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat")
elif weather == "cold":
    print("Make sure to wear a warm coat and scarf")
else:
    print("Sorry, I don't have reccomendations for this weather")