
from datetime import datetime


name = input("Enter your name: ")

hour =  datetime.now().hour

if hour < 12:
    wish = 'Good Morning, ' + name
elif hour >= 12 and hour < 16:
    wish = 'Good Afternoon, ' + name
elif hour >= 16 and hour < 20:
    wish = 'Good Evening, ' + name
else:
    wish = 'Good Night, ' + name

print(wish)

