def part1(entries):
    output_size = [len(output) for entry in entries for output in entry.split(' | ')[1].split()]
    uniques = {}
    for size in output_size:
        uniques[size] = uniques.get(size, 0) + 1 if size in [2, 3, 4, 7] else 0
    print(sum(uniques.values()))


def part2(entries):
    displays = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

    # Find correct profile for each letter
    correct_profiles = calculate_profile(displays)

    total_value = 0
    for entry in entries:
        signals, outputs = entry.split('|')

        # Decode signals
        observed_profiles = calculate_profile(signals.split())

        decoded_profiles = {}
        for letter, profile in observed_profiles.items():
            for correct_letter, correct_profile in correct_profiles.items():
                if profile == correct_profile:
                    decoded_profiles[letter] = correct_letter
                    break

        # Calculate outputs
        output_value = 0
        for output in outputs.split():
            fixed = "".join(sorted([decoded_profiles[letter] for letter in output]))
            output_value = output_value*10 + displays.index(fixed)
        total_value += output_value
    print(total_value)


def calculate_profile(displays):
    letter_profile = {}
    for display in displays:
        for letter in display:
            profile = letter_profile.get(letter, [0 for _ in range(8)])
            profile[len(display)] += 1
            letter_profile[letter] = profile
    return letter_profile


if __name__ == "__main__":
    with open("input/day08.data", 'r') as f:
        observations = [x for x in f.readlines()]
    part1(observations)
    part2(observations)
