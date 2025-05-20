import os
##for i in range(1,10):
##    if(not os.path.exists(f"day{i}")):
##       os.mkdir(f"/python programs/day{i}")

# os.rename("day1/new.txt","day1/100.txt")

files=os.listdir("day1")
i=1
for file in files:
    if file.endswith(".jpg"):
        os.rename(f"day1/{file}",f"day1/{i}.png")
        i =i+1