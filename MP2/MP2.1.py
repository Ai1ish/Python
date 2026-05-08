month = input("Enter birth month: ").lower()
day = int(input("Enter birth day: "))

if (month == "december" and day >= 22) or (month == "january" and day <= 19):
    zodiac = "Capricorn"

elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
    zodiac = "Aquarius"

elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
    zodiac = "Pisces"

elif (month == "march" and day >= 21) or (month == "april" and day <= 19):
    zodiac = "Aries"

elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
    zodiac = "Taurus"

elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
    zodiac = "Gemini"

elif (month == "june" and day >= 21) or (month == "july" and day <= 22):
    zodiac = "Cancer"

elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
    zodiac = "Leo"

elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
    zodiac = "Virgo"

elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
    zodiac = "Libra"

elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
    zodiac = "Scorpio"

else:
    zodiac = "Sagittarius"

print("Your zodiac sign is", zodiac)
