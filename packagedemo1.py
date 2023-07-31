import world.asia.country as asia
import world.europe.country as europe
countries = asia.get_countries()
print("Asian country name")
print("_"*100)
for country in countries:
    print(country)
print("_"*100)
    
countries = europe.get_countries()
print("European country name")
print("_"*100)
for country in countries:
    print(country)
print("_"*100)
