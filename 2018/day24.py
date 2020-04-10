import sys, re

class Unit(object):
    def __init__(self, units, hit, damage, attack_type, imune, weak, initiative):
        self.units = units
        self.hit = hit
        self.damage = damage
        self.attack_type = attack_type
        self.imune = imune
        self.weak = weak
        self.initiative = initiative
        self.target = None

    def attacked(self, assault):
            power = self.max_damage(assault)
            kills = power // self.hit
            self.units -= kills
    
    def max_damage(self, assault):
        power, attack_type = assault
        if(attack_type not in self.imune):
            if(attack_type in self.weak):
                power *= 2
        else:
            power = 0
        return power

    def attack(self):
        return (self.effective_power(), self.attack_type)

    def effective_power(self):
        return self.units * self.damage

def part1(filepath):
    immune, infection = parse(filepath)
    while(len(immune) > 0 and len(infection) > 0):
        immune, infection = round(immune, infection)
    print(sum([u.units for u in immune+infection]))

def part2(filepath):
    immune, infection = parse(filepath)
    boost = 1
    for unit in immune:
        unit.damage += boost
    prev_units = sum([u.units for u in immune+infection])

    while(len(infection) > 0):
        immune, infection = round(immune, infection)
        if (len(immune) == 0 or sum([u.units for u in immune+infection]) == prev_units):
            immune, infection = parse(filepath)
            boost += 1
            for unit in immune:
                unit.damage += boost
        prev_units = sum([u.units for u in immune+infection])

    print(sum([u.units for u in immune+infection]))
    print(boost)


def round(immune, infection):
    #Target choosing
    choose_targets(immune, infection)
    choose_targets(infection, immune)

    # Attack
    battle = sorted(filter(lambda u:u.target != None, immune+infection),key=lambda u:u.initiative, reverse=True)
    for unit in battle:
        if (unit.units > 0):
            unit.target.attacked(unit.attack())
            unit.target = None

    # Cleanup
    immune = filter(lambda u:u.units > 0, immune)
    infection = filter(lambda u:u.units > 0, infection)
    return immune, infection

def choose_targets(attacking, defending):
    attacking = sorted(attacking, key=lambda u:(u.effective_power(), u.initiative), reverse=True)
    for unit in attacking:
        enemies = filter(lambda u:u not in [i.target for i in attacking if i.target != None], defending)
        unit.target = None
        if (len(enemies) > 0):
            enemies = sorted(enemies, key=lambda e: (e.max_damage(unit.attack()), e.effective_power(), e.initiative), reverse=True)
            if(enemies[0].max_damage(unit.attack()) > 0):
                unit.target = enemies[0]


def parse(filepath):
    immune_system = list()
    infection = list()
    inf = False
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if(line.startswith('Infection')):
                inf = True
            res = re.match(r'(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) ([a-z]+) damage at initiative (\d+)', line)
            if res:
                types = res.group(3)
                immune = re.match(r'.*immune to ([a-z,\s]*)[\);].*', types)
                weak = re.match(r'.*weak to ([a-z,\s]*)[\);].*', types)
                if weak:
                    weak = weak.group(1).split(', ')
                else:
                    weak = []
                if immune:
                    immune = immune.group(1).split(', ')
                else:
                    immune = []
                unit = Unit(int(res.group(1)), int(res.group(2)), int(res.group(4)), res.group(5), immune, weak, int(res.group(6)))
                if(inf):
                    infection.append(unit)
                else:
                    immune_system.append(unit)

    return immune_system, infection

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])