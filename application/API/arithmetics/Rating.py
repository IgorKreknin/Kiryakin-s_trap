class Rating:
    current_rating = 0
    number_of_rates = 0
    
    def get():
        return current_rating
    
    def ratings_count():
        return number_of_rates
    
    def add_rating(new_rating):
        temp = current_rating*number_of_rates
        temp += new_rating
        number_of_rates += 1
        current_rating = temp/number_of_rates
