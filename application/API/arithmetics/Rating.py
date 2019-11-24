cameras_impact = 50.0
stolen_impact = 0.5
returned_impact = 0.8

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


def sequrityRating(cameras, stolen_rate, returned_rate):            # (100 - CI/(1+cameras))*SI^(stolen - RI*returned)
    base = 100 - cameras_impact/(1+cameras)
    returned_part = returned_rate/stolen_rate
    exp = stolen_rate*(1 - returned_impact*returned_part)
    return base * (stolen_impact**exp)
