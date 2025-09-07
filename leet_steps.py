##https://leetcode.com/problems/climbing-stairs/description/

##there are two possible ways of climbing stairs per pair of steps
def count_possibilities(n):
    counter_possibilities = 0
    while n > 0:
        if n % 2 == 0:
            counter_possibilities += 2
            n -= 2
        elif n % 2 != 0:
            counter_possibilities = 1
            n -= 1
    return counter_possibilities

##apply constraint: & <= <= 45
def check_stair(n):
    while n < 1 or n > 45:
        try:
            n = int(input("1 to 45 only!"))
        except ValueError:
            print("Now, now, numbers only.")
    return n

##declare steps stair number

stair_steps = int(input("Please enter how long the stair is: from 1 to 45 only!"))

check_stair(stair_steps)

print(count_possibilities(stair_steps))
