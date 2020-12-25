def encryption_step(value, subject):
    return (value * subject) % 20201227


def encrypt(subject, loop):
    value = 1
    for _ in range(loop):
        value = encryption_step(value, subject)
    return value


def find_loop(subject, public_key):
    value = 1
    i = 0
    while value != public_key:
        i += 1
        value = encryption_step(value, subject)
    return i


def handshake(card_pk, door_pk):
    card_loop = find_loop(7, card_pk)
    door_loop = find_loop(7, door_pk)

    print(encrypt(card_pk, door_loop))
    print(encrypt(door_pk, card_loop))


if __name__ == '__main__':
    handshake(10943862, 12721030)
