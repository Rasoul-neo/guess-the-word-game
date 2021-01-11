word ="lion"
guess=""
guess_count=0
guess_limit=3
out_of_guess=False

while guess!=word and not (out_of_guess):
    if guess_count<guess_limit:
        guess=input("guess animal name:")
        guess_count+=1 
    else:
        out_of_guess=True
if out_of_guess:
    print("You lose!")
else:
    print("you win!")
