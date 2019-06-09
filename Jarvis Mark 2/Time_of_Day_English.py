from datetime import datetime

time = str(datetime.now().time())

hour = int(time[0:2])
minute = int(time[3:5])
second = int(time[6:8])
current_time = "%s:%s:%s" % (hour, minute, second)

username = input("My name is Jarvis. What is your name? ")

if hour >= 7 and hour < 11:
    print("Good Morning,", username, "it is", current_time)
elif hour >=11 and hour < 17:
    print("Good Afternoon,", username, "it is", current_time)
elif hour >=17 and hour < 22:
    print("Good Evening,", username, "it is", current_time)
elif hour >= 22 or hour < 7:
    print(username, ", it is", current_time + " and it is late. You should go and get some rest.")