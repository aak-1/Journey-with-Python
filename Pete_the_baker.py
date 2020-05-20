def cakes(recipe, available):
    # TODO: insert code
    count = 1000000000
    for i in recipe.keys():
        if i in available.keys():
            if available[i] >= recipe[i]:
                if int(available[i]/recipe[i]) <= count:
                    count = int(available[i]/recipe[i])
            else:
                return 0
        else:
            return 0
    return count