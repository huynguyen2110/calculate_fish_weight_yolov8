def calculate_weight(fish):
    if fish[0] == "carp":
        weight = 0.0146 * fish[1] ** 3.014
        return round(weight, 1)
    elif fish[0] == "catfish":
        weight = 0.0194 * fish[1] ** 2.971
        return round(weight, 1)
    elif fish[0] == "tilapia":
        weight = 0.0114 * fish[1] ** 2.980
        return round(weight, 1)
    elif fish[0] == "perch":
        weight = 0.0153 * fish[1] ** 2.958
        return round(weight, 1)
    else:
        return 0

