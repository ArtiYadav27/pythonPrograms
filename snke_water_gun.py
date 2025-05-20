import random
print("S=Snake\nW=Water \nG=Gun")
mat=[['DRAW','WIN','LOSE'],['LOSE','DRAW','WIN'],['WIN','LOSE','DRAW']]
options={'S':0,'W':1,'G':2}
while(True):
    choices=options[input("Enter any one option[S-W-G]:")]
    comp=random.choice(list(options.values()))
##    print("Computer Choice:" ,options[comp])
    print(f"YOU {mat[comp][choices]}")
