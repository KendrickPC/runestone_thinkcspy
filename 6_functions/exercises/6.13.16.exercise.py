'''
Write a function called myPi that will return an
approximation of PI (3.14159…). Use the Madhava
approximation.
'''

# Madhava Approximation:
def myPi(iters):
    # Calculate an approximation of PI using the Madhava
    # approximation with iters number of iterations

    #your code here
    step, total = 1, 0
    
    for i in range(iters):
        if i % 2 == 0:
            total += 4 / step
        else:
            total -= 4 / step
        
        step += 2
    
    return total

print(myPi(1000000))
