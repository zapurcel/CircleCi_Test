# This file is for testing code from scratch
# Attempting to create an app to automatically turn on and off lights as people leave and enter rooms
# Not exactly sure how to code this, but it would require a motion sensor and counter
# Will start by creating a dataset of "people" and simulate them entering and leaving a room

data = [1, 4, 6, 2, 5, 3, 7]  # Each number repersents an amount of people entering a room
totalinroom = 0
for i in data:
    totalinroom = totalinroom + i  # Summing the total people in entering the room

while totalinroom > 1:
    totalinroom = totalinroom - 1

if totalinroom > 1:
    light = 'ON'
else:
    light = 'OFF'

print(light)

