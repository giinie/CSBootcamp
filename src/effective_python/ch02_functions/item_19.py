def remainder(number, divisor):
    return number % divisor


print(remainder(20, 7) == 6)

print(remainder(20, 7))
print(remainder(20, divisor=7))
print(remainder(number=20, divisor=7))
print(remainder(divisor=7, number=20))

print('-' * 50)
#
# import logging
#
# try:
#     # This will not compile
#     source = """remainder(number=20, 7)"""
#     eval(source)
# except:
#     logging.exception('Expected')
# else:
#     assert False
#
# print('-' * 50)
#
# try:
#     remainder(20, number=7)
# except:
#     logging.exception('Expected')
# else:
#     assert False
#
# print('-' * 50)


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('{:.3f} kg per second'.format(flow))

print('-' * 50)


def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


print(flow_rate(weight_diff, time_diff, 1))

print('-' * 50)


def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print('{:.3f} kg per second'.format(flow_per_second))
print('{:.1f} kg per hour'.format(flow_per_hour))

print('-' * 50)


def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1.0):
    return ((weight_diff * units_per_kg) / time_diff) * period


flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
pounds_per_hour = flow_rate(weight_diff, time_diff, period=3600, units_per_kg=2.2)
pounds_per_hour_2 = flow_rate(weight_diff, time_diff, 3600, 2.2)
print('{:.1f} kg per hour'.format(flow_per_hour))
print('{:.1f} pounds per hour'.format(pounds_per_hour))
print('{:.1f} pounds per hour'.format(pounds_per_hour_2))

print('-' * 50)


