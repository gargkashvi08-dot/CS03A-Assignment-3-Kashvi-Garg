# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 3 - Question 3
# /* Student Name: Kashvi Garg
# /* SID: 20744788
# /*****************************************************/

def reverseDisplay(value):
    print(value%10,end='')
    if value//10!=0:
        reverseDisplay(value//10)

def run():
    n=int(input('Enter an integer: '))
    reverseDisplay(n)
    print()

if __name__=='__main__':
    run()
