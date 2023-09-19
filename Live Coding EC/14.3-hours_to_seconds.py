import math

seconds = int(input())
hours = math.floor(seconds / 3600)
seconds = seconds % 3600
# modulo division gives remaining non-hour seconds
minutes = seconds // 60
seconds = seconds % 60

print(f'Hours: {hours}')
print(f'Minutes: {minutes}')
print(f'Seconds: {seconds}')
