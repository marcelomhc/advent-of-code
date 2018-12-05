import sys
import re

class Record(object):
    def __init__(self, date, hour, minute, action):
        self.date = date
        self.hour = int(hour)
        self.minute = int(minute)
        self.action = action
        self.id = -1

        if(action.startswith("Guard")):
            self.id = int(re.match(r'Guard #(\d+) begins shift', action).group(1))
            self.awake = True
        elif(action.startswith("falls")):
            self.awake = False
        elif(action.startswith("wakes")):
            self.awake = True
        else:
            print("Error with id: " + self.date + self.action)

class Guard(object):
    def __init__(self, id):
        self.id = id
        self.sleep_total = 0
        self.minutes = [0 for i in range(60)]
        self.minute_sleep = 0
        self.minute = -1

def main(filepath):
    records = parse_input(filepath)
    records = sorted(records, key=lambda obj: (obj.date, obj.hour, obj.minute))
    get_sleep_time(records)

def get_sleep_time(records):
    guards = dict()
    for record in records:
        if(not record.id == -1):
            guard = guards.setdefault(record.id, Guard(record.id))
        elif(record.awake):
            for i in range(begin, record.minute):
                sleep_minute = guard.minutes[i] + 1
                guard.sleep_total += 1
                guard.minutes[i] = sleep_minute
                if (guard.minute_sleep < sleep_minute):
                    guard.minute_sleep = sleep_minute
                    guard.minute = i
        elif(not record.awake):
            begin = record.minute

    guards = sorted(guards.values(), key=lambda obj: (obj.sleep_total), reverse=True)
    guard = guards[0]
    print("Guard id: #" + str(guard.id))
    print("Minutes slept: " + str(guard.sleep_total))
    print("Most slept minute: " + str(guard.minute))
    print("Slept for: " + str(guard.minute_sleep) + " minutes")
    print("Id * minute: " + str(guard.id*guard.minute))
    print("###########")

    guards = sorted(guards, key=lambda obj: (obj.minute_sleep), reverse=True)
    guard = guards[0]
    print("Guard id: #" + str(guard.id))
    print("Minutes slept: " + str(guard.sleep_total))
    print("Most slept minute: " + str(guard.minute))
    print("Slept for: " + str(guard.minute_sleep) + " minutes")
    print("Id * minute: " + str(guard.id*guard.minute))


def parse_input(filepath):
    records = []
    with open(filepath, "r") as f:
        for line in f:
            result = re.match(r'\[(.+) (\d\d):(\d\d)\] (.+)', line)
            record = Record(result.group(1), result.group(2), result.group(3), result.group(4))
            records.append(record)
    return records

if __name__ == "__main__":
    main(sys.argv[1])