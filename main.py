
x = int(input("What is your birth year: "))
if x < 1900:
    print("You are from Lost Generation.")
elif x < 1927:
    print("You are from Greatest Generation.")
elif x < 1945:
    print("You are from Silent Generation.")
elif x < 1964:
    print("You are from Baby boomers.")
elif x < 1980:
    print("You are from Generation X.")
elif x < 1996:
    print("You are from Millennials.")
elif x < 2012:
    print("You are from Generation Z.")
else:
    print("You are from Generation Alpha.")

    