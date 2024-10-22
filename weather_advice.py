def main():
    """
    This function asks the user for the weather and provides clothing recommendations._
    """
    
    weather = input("Whats the weather like today? (sunny/rainy/cold):")
    
    if weather.lower() ==  "sunny":
        print("wear a t-shirt and sunglasses.")
    elif weather.lower() == "rainy":
        print("Dont forget your umbrella and a raincoat")
    elif weather.lower() == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("sorry, i dont have recommendations for this weather.")
        
    if  __name__  == "__main__":
        main()
        
    