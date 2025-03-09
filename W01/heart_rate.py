"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

user_age = int(input('Please enter your age: '))
maximum_heart_rate = 220
maximum_heart_rate -= user_age

min_heart_rate = (65/100) * maximum_heart_rate
max_heart_rate = (85/100) * maximum_heart_rate

print(f'When you exercise to strengthen your heart, you should \nkeep your heart rate between {min_heart_rate:.0f} and {max_heart_rate:.0f} \nbeats per minute.')