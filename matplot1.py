import matplotlib.pyplot as plt

acid = [2.4, 3.2, 4, 4.8, 5.5]
massdiff = [0.072, 0.064, 0.058, 0.058, 0.06]


#the b means blue, - means solid, o means a circular data point
plt.plot(acid, massdiff, 'b-o', label='Mass Difference')

#the .3f means 3 decimal points, the acid[i] and massdiff[i] means that the e.g. first acid coordinate corresponds
#to the first massdiff ccoordinate, "offset points" gives the label for each plot, xytext gives the spacing.
for i, txt in enumerate(massdiff):
    plt.annotate(f'{txt:.3f}', (acid[i], massdiff[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.ylabel('Difference in Mass of Synthetic Rubber')
plt.xlabel('Acid pH')
plt.title("Acid Mass Difference")
plt.grid(True)

plt.legend()
plt.savefig("rubber_plot.png")
plt.show()

#I use this plot because it is very useful to visualise the effects of acid on creating a mass difference on synthetic rubber.