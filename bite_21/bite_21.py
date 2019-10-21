"""
Bite 21 Query a nested data structure
"""
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    if "Jeep" in cars:
        jeeps = ", ".join([j for j in cars["Jeep"]])
        return jeeps
    return ""


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    result = []
    for car_types in cars:
        if cars[car_types]:
            result.append(cars[car_types][0])
    return result


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    result = []
    for car_types in cars:
        for model in cars[car_types]:
            if grep.lower() in model.lower():
                result.append(model)
    return sorted(result)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    result = {}
    for car_types in cars:
        if cars[car_types]:
            result[car_types] = sorted(cars[car_types])
    return result

