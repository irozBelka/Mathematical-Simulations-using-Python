import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()



# Definintion Of The The Bernoulli(p) Probability Distribution Derived From U~Uniform(0,1)
def Bernoulli(p):
    U = rng.random()
    return (U < p)


# N Tosses
n = 1000

toss = [Bernoulli(0.6) for _ in range(n)]

# avg is a list where each element is the number of heads divided by the number of tosses(i of n)
avg = [sum(toss[:i])/i for i in range(1, n+1)] 

plt.xlabel("Number of coin tosses")
plt.ylabel("Proportion of Heads")

plt.title("Proportion of Heads in 1000 Coin Tosses")

#    1|__
#     |  |_____
#     |
#  1/2|
#     |
#     |
#     |________________
#     0               n

plt.axis([0, n+1, 0, 1])



plt.plot(range(1, n+1), avg)

plt.show()