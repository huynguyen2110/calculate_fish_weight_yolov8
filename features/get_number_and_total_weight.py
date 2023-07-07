def get_number_and_total_weight(list, fish_array):
    if fish_array[0] == "carp":
        list["carp"]["number"] += 1
        list["carp"]["length"] += fish_array[1]
        list["carp"]["weight"] += fish_array[2]
        return list
    elif fish_array[0] == "catfish":
        list["catfish"]["number"] += 1
        list["catfish"]["length"] += fish_array[1]
        list["catfish"]["weight"] += fish_array[2]
        return list
    elif fish_array[0] == "tilapia":
        list["tilapia"]["number"] += 1
        list["tilapia"]["length"] += fish_array[1]
        list["tilapia"]["weight"] += fish_array[2]
        return list
    elif fish_array[0] == "perch":
        list["perch"]["number"] += 1
        list["perch"]["length"] += fish_array[1]
        list["perch"]["weight"] += fish_array[2]
        return list
    else:
        return list
