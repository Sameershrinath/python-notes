from datetime import datetime

current = datetime.now()
hour = current.hour  # Extract the hour directly from the datetime object
print(f'Time is {current}')
if 3 <= hour < 12:
    print("Good Morning Sir!")
elif 12 <= hour < 16:
    print('Good Afternoon')
elif 16 <= hour < 21:
    print('Good Evening')
else:
    print("Good Night")
