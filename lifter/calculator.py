from datetime import datetime

now = datetime.now()

worked_intervals = input("Input your working periods (e.g. \"08:00, 12:00\" ): ").split(",")

if (not len(worked_intervals) % 2 == 0):
    worked_intervals.append("{:0>2d}:{:0>2d}".format(now.hour, now.minute))


hours = [datetime.strptime(hour.strip(), "%H:%M") for hour in worked_intervals]
hours_sum = datetime.strptime("00:00", "%H:%M")

for iteracao in range(0, len(hours), 2):
    hours_sum = hours_sum + (hours[iteracao + 1] - hours[iteracao])

print("I worked {:0>2d}:{:0>2d}".format(hours_sum.hour, hours_sum.minute))

