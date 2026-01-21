listCloud=["aws","azure","gcp"]

print(listCloud)

listCloud.append("salesforce")
listCloud.append("IBM")

print(listCloud)

listCloud.insert(2,"Heroku")

print(listCloud)

for cloud in listCloud:
    print(" ")
    print(cloud)


for i in range(1,7):
    print("Good morning")