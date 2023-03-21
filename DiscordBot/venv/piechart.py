import matplotlib.pyplot as plt
import numpy as np

def makechart():
    y = np.array([65, 25, 25, 15])

    plt.pie(y)
    plt.savefig('C:/Users/Emily Rose/source/repos/DiscordBot/countingPie.png');
