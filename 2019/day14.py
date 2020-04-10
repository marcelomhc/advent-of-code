from collections import defaultdict

class Reaction(object):
    def __init__(self, output, amount, ingredients):
        self.output = output
        self.amount = amount
        self.ingredients = ingredients

def get_reactions(filepath):
    reactions = dict()

    with open(filepath, "r") as f:
        for line in f:
            reaction = line.split(' => ')
            result = reaction[1].split(' ')

            amount = int(result[0])
            output = result[1].strip()
            ingredients = list()

            for element in reaction[0].split(', '):
                element = element.split(' ')
                element = (element[1], int(element[0]))
                ingredients.append(element)

            reactions[output] = Reaction(output, amount, ingredients)

    return reactions

def find_ores(reactions, element, required, spares):
    if(element == 'ORE'):
        return required

    spare = spares.get(element, 0)
    #print(element + ': total need: ' + str(required))
    if (spare > 0):
        #print(element + ': using spares: ' + str(spare))
        spares[element] -= min(spare, required)
        required -= spare
        if(required <= 0):
            #print(element + ': No extra ORE required')
            return 0
    #print(element + ': still need: ' + str(required))

    reaction = reactions.get(element)
    n = required // reaction.amount
    extra = required % reaction.amount
    if (extra > 0):
        n += 1
    extra = (n * reaction.amount) - required
    #print(element + ': {0} reactions required that will leave {1} to spare'.format(n, extra))
    
    ores = 0
    for ingredient, qtd in reaction.ingredients:
        ores += find_ores(reactions, ingredient, n*qtd, spares)

    spares[element] += extra

    #print(element + ': required ores: ' + str(ores))
    return ores

def produce_fuel(available, reactions):

    total = 2390000
    spares = defaultdict(lambda: 0)
    required = find_ores(reactions, 'FUEL', total, spares)
    available -= required

    while(available > 0):
        required = find_ores(reactions, 'FUEL', 1, spares)
        available -= required
        if(available > 0):
            total += 1
        #print('Required ores for 1 fuel: ' + str(required) + ' / available: ' + str(available))

    print('Total fuels produced: ' + str(total))
    return total

if __name__ == "__main__":
    reactions = get_reactions("input/day14.data")
    print(find_ores(reactions, 'FUEL', 1, defaultdict(lambda: 0)))
    produce_fuel(1000000000000, reactions)
