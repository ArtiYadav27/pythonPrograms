import random


options=[["Python is a ..","programming language","scripting language","local language","snake",1],
         ["new delhi is the capital of ...","India","Austrailia","UK","USA",1],
         ["father of python","guido van rossum","bill gates","mark zukerburg","no one",1],
         ["sparrows are..","dividing","multiplying","diminishing","hiding",3],
         ["RATAN TATA belongs to..","USA","Austrailia","UK","India",4],
         ["pratapgarh is the name of the ...","a country","a district","a state","a country",2]]
while(True):
    level=1
    amount=0
    ques=random.choice(options)
    print(ques[0])
    print(f"(A){ques[1]}                            (B){ques[2]}" )
    print(f"(C){ques[3]}                            (D){ques[4]}" )
    ans=int(input("Enter Correct ans option[1-4]:"))
    if(ans==ques[-1]):
        print("\t\t\t\t\t\t\t\tcorrect answer,you won 1000 for this correct answer",end="\n\n\n")
        amount=amount+level*1000
        level=level+1
    else:
        print("\t\t\t\t\t\t\t\tincorrect answer...you lost Rs.100 from total amount",end="\n\n\n")
        if(amount>=100):
            amount=amount-100
print(f"you won {amount}",end="\n\n")
