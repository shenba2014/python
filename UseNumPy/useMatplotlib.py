import matplotlib.pyplot as plt
year = [1990, 2000, 2010, 2020]
poplutaion = [2.56, 3.89, 5.89, 6.34]
plt.fill_between(year, poplutaion, 0, color='green')
# plt.scatter(year, population)
plt.xlabel('year')
plt.ylabel('population')
plt.title('just a figure')
plt.yticks([0, 2, 4, 6], ['0B', '2B', '4B', '6B'])
plt.show()