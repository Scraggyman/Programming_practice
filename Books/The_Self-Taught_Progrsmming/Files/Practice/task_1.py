import os

way = os.path.join("Macintosh HD", "/Users", "Vadim", "Library", "Application Support",
             "Steam", "steamapps", "common", "dota 2 beta", "game",
             "bin", "sdkassettypes.txt")
way2 = os.path.join("/Volumes", "Macintosh_Vadim", "Coursera",
                    "Python for Everybody", "Course 3", "regex_sum_42.txt")
print(way)
print(way2)
with open("/Volumes/Macintosh_Vadim/Coursera/Python for Everybody/Course 3/regex_sum_42.txt",
          'r') as file:
    print(file.read())

with open(way, 'r') as fl:
    print(fl.read())
