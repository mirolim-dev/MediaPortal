def get_nested_list_includes_triple_lists(data:list)->list:
    """making nested list The list which is located inside of main list should include 3 objects
        because The design of webside requires that. 
        start handling neset list
    """
    list_data = []
    triple_data = []
    steps = 0
    for single_data in data: 
        steps += 1
        triple_data.append(single_data)
        if steps == 3:
            list_data.append(triple_data)
            steps = 0
            triple_data = []
    else:
        if triple_data != []:
            list_data.append(triple_data)
    return list_data