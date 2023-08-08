def thesaurus(names: str) -> dict:
    """

    :param names:
    :return:
    """
    names_dict: dict[str, list] = dict()
    names_list = names.split(", ")
    for name in names_list:
        key = name[0]
        if key not in names_dict:
            names_dict[key] = []
        names_dict[key].append(name)

    return names_dict





print(thesaurus('kmkm, hjijioi, kjjh'))



# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
