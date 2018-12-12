from datetime import datetime
import sys

WORKING_HOURS_IN_A_DAY = 8

def take_the_input():
    if (len(sys.argv) > 1):
        return list(map(lambda value: value.replace(",", ""), sys.argv[1:]))
    else:
        return input("Input your working periods (e.g. \"08:00, 12:00\" ): ").split(",")


worked_intervals = take_the_input()

now = datetime.now()

if not len(worked_intervals) % 2 == 0:
    worked_intervals.append("{:0>2d}:{:0>2d}".format(now.hour, now.minute))

hours = [datetime.strptime(hour.strip(), "%H:%M") for hour in worked_intervals]
hours_sum = datetime.strptime("00:00", "%H:%M")

for iteracao in range(0, len(hours), 2):
    hours_sum = hours_sum + (hours[iteracao + 1] - hours[iteracao])

print("I worked {:0>2d}:{:0>2d} hours".format(hours_sum.hour, hours_sum.minute))

if (hours_sum.hour < WORKING_HOURS_IN_A_DAY):
    regular_worked_time = datetime.strptime("08:00", "%H:%M")
    hour_left = regular_worked_time - hours_sum
    limit_hour = (datetime.now() + hour_left)
    print("I need to work util {:0>2d}:{:0>2d} to accomplish today's mission".format(limit_hour.hour, limit_hour.minute))
