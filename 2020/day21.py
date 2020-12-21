import re


def parse(filepath):
    with open(filepath, 'r') as f:
        food = []
        for line in f.readlines():
            matches = re.findall(r'([^\s,()]+)', line)
            idx = matches.index('contains')
            food.append((matches[0:idx], matches[idx+1::]))
    return food


def get_possibilities(food):
    all_ing = set()
    possible = {}
    for ingredients, allergens in food:
        all_ing.update(ingredients)
        for allergen in allergens:
            s = possible.get(allergen, set(ingredients))
            s.intersection_update(ingredients)
            possible[allergen] = s
    return all_ing, possible


def count_safe(food):
    all_ing, possible = get_possibilities(food)

    all_possible = set()
    [all_possible.update(possible[k]) for k in possible]
    excluded = all_ing.difference(all_possible)

    total = sum([int(ing in ingredients) for ing in excluded for ingredients, _ in food])
    print(total)


def get_canonical(food):
    all_ing, possible = get_possibilities(food)

    result = {}
    while len(possible) > 0:
        for allergen, possibilities in possible.items():
            if len(possibilities) == 1:
                result[allergen] = possibilities.pop()

        for allergen in result:
            possible.pop(allergen, None)
            [allergens.discard(result[allergen]) for allergens in possible.values()]

    print(','.join([result[k] for k in sorted(result.keys())]))


if __name__ == "__main__":
    food_list = parse("input/day21.data")
    count_safe(food_list)
    get_canonical(food_list)
