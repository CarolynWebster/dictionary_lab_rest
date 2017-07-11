"""Restaurant rating lister."""

rated_restaurants = {}
# put your code here
def get_restaurant_rating(rated_restaurants):
    user_action = raw_input("Would you like to add a restaurant or view all restaurants "
    "Type 'A' to add, Type 'V' to view, or Type 'Q' to quit ")
    if user_action.upper() == "A":
        user_rest = raw_input("Please enter restaurant name ")
        user_rating = raw_input("Please enter rating for restaurant "
        "1 = Terrible 5 = Out of this world ")
        try:
            if int(user_rating) > 5 or int(user_rating) < 1:
                print """Restaurant rating is out of range\n"""
                user_rating = raw_input("Please enter rating for restaurant ")
        except:
            print """You clearly don't know what a number is. Try that one again.\n"""
            user_rating = raw_input("Please enter rating for restaurant ")

        rated_restaurants[user_rest] = user_rating
    elif user_action.upper() == "V":
        rest_scores = open("scores.txt")
        for line in rest_scores:
            line = line.rstrip()
            line = line.split(":")
            restaurant, rating = line
            rated_restaurants[restaurant] = rating
        sorted_restaurants = sorted(rated_restaurants.items())
        for restaurant in sorted_restaurants:
            print "{} is rated at {}.".format(restaurant[0], restaurant[1])
    elif user_action.upper() == "Q":
        print """You have quit!\n"""
        return "Quit"
    else:
        print """That's not an option.\n"""

restaurant_return = None
while restaurant_return != "Quit":
    restaurant_return = get_restaurant_rating(rated_restaurants)
