from package_program import hello as h
h.hel()
def fun(n1,n2):
    if n1==n2:
        print("both won")
    elif(n1>n2):
        print("first player won")
    else:
        print("second player won")
    play_again=input("play again?(y/n)")
    if play_again=='y':
        n1 = int(input("enter a choice of player1:"))
        n2 = int(input("enter a choice of player2:"))
        fun(n1, n2)
    else:
        exit(0)

n1 = int(input("enter a choice of player1:"))
n2 = int(input("enter a choice of player2:"))
fun(n1,n2)