from datetime import datetime

test = "date"

ggle = "google search api or something"
weather = "some wearther api"

def command(cmd):
    words = [word for word in cmd.split()]

    if "exit" in words:
        return ("exit",)
    if "google" in words:
        ggle_index = words.index("google")
        return  ("google", " ".join(words[ggle_index + 1:]))
    if "time" in words:
        return ("time", str(datetime.now().time()))
    if "date" in words:
        return ("date", str(datetime.now().date()))
    if "weather" in words:
        return ("weather", "It is currently sunny and 76 degrees")
    if "translate" in words:
        return ("translate", "Translating...")
    if "location" in words:
        return ("location", "Storing your new location")
    if "stock" in words:
        return ("stock", "Gathing stock data...")
    if "order pizza":
        return ("order pizza", "Ordering pizza...")

print(command(test))

