def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        list_to_remove_elements.remove (5)
        list_to_remove_elements.remove (4)
        list_to_remove_elements.remove (0)
        return [list_to_remove_elements]
    elif 2 < len(list_to_remove_elements) < 6:
        list_to_remove_elements.remove (4)
        list_to_remove_elements.remove (0)
        return [list_to_remove_elements]
    else:
        list_to_remove_elements.remove (0)
        return [list_to_remove_elements]


def add_elements(list_to_add_elements):
    list_to_add_elements.insert (0, "Pink")
    list_to_add_elements.insert (-1, "Yellow")
    return [list_to_add_elements]


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) and len(list_to_compare2) > 3 and list_to_compare1 [2] == list_to_compare2 [2]:
        return True
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify [0][0]
    list_of_lists_to_modify [0][1]
    list_of_lists_to_modify [1][1]
    list_of_lists_to_modify [1][2]
    list_of_lists_to_modify [1][3]
    list_of_lists_to_modify [2][-1]
    list_of_lists_to_modify [2][-1]
    return list_of_lists_to_modify
