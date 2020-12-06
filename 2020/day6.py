def get_answers(filepath):
    with open(filepath, 'r') as f:
        answers = []
        groups = f.read().split('\n\n')

        for group in groups:
            answer = dict()
            answer['#'] = 1
            for letter in group:
                if 'a' <= letter <= 'z':
                    answer[letter] = answer.get(letter, 0) + 1
                elif letter == '\n':
                    answer['#'] += 1

            answers.append(answer)
    return answers


def count_any(answers):
    total = 0
    for answer in answers:
        total += len(answer.keys()) - 1
    print(total)


def count_all(answers):
    total = 0
    for answer in answers:
        persons = answer.pop('#')
        for key in answer.keys():
            if answer[key] == persons:
                total += 1
    print(total)


if __name__ == "__main__":
    data = get_answers("input/day6.data")
    count_any(data)
    count_all(data)
