
## The function which calls itself is called recursive function and the process is called as recursion

##1. PRINT NUMBERS FROM N TO 0 USING WHILE LOOP

def count_down(number):
    while number >= 0:
        print(f'counting down {number}')
        number -= 1
# count_down(5)

##2. PRINT NUMBERS FROM N TO 0 USING FOR LOOP

def CountDown(number):
    for num in range(number, -1, -1):
        print(f'counting down {num}')
# CountDown(5)

## PRINT NUMBERS FROM N TO 0 USING RECURSION

def Count_Down(number):
    ## Base Case
    if number >= 0:
        print(f'counting down {number}')
        ## Recursive Case
        Count_Down(number - 1)
# Count_Down(2)

##2. PRINT THE NUMBERS FROM 1 to 5, "START" AND "STOP" USING RECURSION

def count_up(start, stop):
    ## Base Case
    if start <= stop:
        print(f'counting up {start}')
        ## Recursive Case
        count_up(start + 1, stop)
# count_up(1, 5)

##2. PRINT THE NUMBERS FROM 1 to 5, "START" AND "STOP" USING RECURSION (NESTED FUNCTION)
## outer function should take only stop value and inner function should take only start value

##3. PRINT THE EVEN NUMBERS FROM 2 to 10, "START" AND "STOP" USING RECURSION
def fun(start, stop):
    if(start>stop):
        return 
    if start%2==0:
        print(start)
    fun(start + 1, stop)
fun(2, 10)


















