def sort_ratings(businesses):
    """Sorts a list of ratings"""

    # loop through the list of dictionaries
    # create a list of tuples with the format (id, rating)
    # use pythons built in sorted method with labmda to sort the items by index 1, the rating
    # re-create the ordered list of dictionaries with the sorted data

    rating_tuples = []
    sorted_ratings = []

    for business in businesses:
        business_id = business["id"]
        rating = business["rating"]

        rating_tuples.append((business_id, rating))


    sorted_by_rating = sorted(rating_tuples, key=lambda x: x[1], reverse=True)

    for business in sorted_by_rating:
        sorted_info = {"id": business[0], "rating": business[1]}
        sorted_ratings.append(sorted_info)

    return sorted_ratings

