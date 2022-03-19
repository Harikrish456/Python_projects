import matplotlib.pyplot as plt

days = [1,2,3,4,5,6]
temp = [2,-3,7,1,-1,0]

plt.plot(days,temp)
#labelling
plt.xlabel('Days since Winter')
plt.ylabel('Temperature')

plt.title('Temperatures in Winter')

plt.show()
