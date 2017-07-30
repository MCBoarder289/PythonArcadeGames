import matplotlib.pyplot as plt
import random

""" 
Notes: 


# https://stackoverflow.com/questions/29045636/attributeerror-module-object-has-no-attribute-hist
# matplotlib doesn't have hist function, but matplotlib.pyplot does, fixes error above

# Good link for pyplot: https://matplotlib.org/api/pyplot_summary.html

# pyplot tutorial: https://matplotlib.org/users/pyplot_tutorial.html

"""

# Number of Iterations:
n = 10000

# Vectors:
x = []
x_sq = []
x_y = []
avg_xy = []
avg_xyz = []
avg_x2y2 = []
norm_0to10 = []
norm_14to27 = []
sq_142to351 = []
bkwd_decay = []

for i in range(n):
    rand_1 = random.uniform(0, 1)
    rand_2 = random.uniform(0, 1)
    rand_3 = random.uniform(0, 1)
    x.append(rand_1)
    x_sq.append(rand_1 ** 2)
    x_y.append(rand_1 * rand_2)
    avg_xy.append((rand_1 + rand_2) / 2)
    avg_xyz.append((rand_1 + rand_2 + rand_3) / 3)
    avg_x2y2.append(((rand_1 ** 2) + (rand_2 ** 2)) / 2)
    norm_0to10.append(avg_xyz[i] * 10)  # multiply by 10 to stretch range from 0-1 to 0-10
    norm_14to27.append((avg_xyz[i] * 13) + 14)  # multiply by 13 to stretch range from 0-1 to 0-13 then shift to 14-27 by adding 14
    sq_142to351.append((x[i] * 209) + 42)
    bkwd_decay.append((x_sq[i] * -1) + 1)


"""
To show multiple charts in one window, you need to call sub plot...

subplot(212) == subplot(2, 1, 2) == 2 total rows, 1 total column, 2nd graph

Pattern goes row by row:
1 2
3 4

"""
plt.figure("Random Number Distributions", figsize=(10, 8))

# x is square probability
plt.subplot(6, 2, 1)
plt.title("Square Probability")
plt.hist(x, bins=50)

# x_sq is sharp exponential decay
plt.subplot(6, 2, 3)
plt.title("Sharp Exponential Decay")
plt.hist(x_sq, bins=50)

# x_y is gradual exponential decay
plt.subplot(6, 2, 5)
plt.title("Gradual Exponential Decay")
plt.hist(x_y, bins=50)

# avg_xy is platykurtic normal distribution (flat)
plt.subplot(6, 2, 7)
plt.title("Platykurtic Normal Distribution (Flat) ")
plt.hist(avg_xy, bins=50)

# avg_xyz is closer to normal distribution - more random numbers makes it more leptokurtic (peaky)
plt.subplot(6, 2, 9)
plt.title("Normal Distribution (more random numbers = peaky)")
plt.hist(avg_xyz, bins=50)

# avg_x2y2 is weird - flat distribution to 0.5 then decay
plt.subplot(6, 2, 11)
plt.title("Flat to 0.5, then decay")
plt.hist(avg_x2y2, bins=50)

# normal distribution 0 - 10
plt.subplot(6, 2, 2)
plt.title("Normal Distribution (1-10)")
plt.hist(norm_0to10, bins=50)

# normal distribution 14 - 27
plt.subplot(6, 2, 4)
plt.title("Normal Distribution (14-27)")
plt.hist(norm_14to27, bins=50)

# square distribution 142-351 - 209 range
plt.subplot(6, 2, 6)
plt.title("Square Distribution (142-351) 209 range")
plt.hist(sq_142to351, bins=50)

# backwards x^2 decay
plt.subplot(6, 2, 8)
plt.title("Backwards x^2 decay")
plt.hist(bkwd_decay, bins=50)

# Make the Layout Pretty
plt.tight_layout()
plt.subplots_adjust(hspace=1)
