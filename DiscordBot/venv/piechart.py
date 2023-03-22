import matplotlib.pyplot as plt
import numpy as np
import os

def makechart(numList, userList):

    ny = numList.copy()
    su = userList.copy()

    nu = [su for _, su in sorted(zip(ny, su))]
    
    ny.sort()
    y = np.array(ny)

    for i in range(len(nu)):
        nu[i] = nu[i]+ " - "+str(y[i])

    p, tx, autotexts = plt.pie(y, autopct="", radius=.8)

    tempU = nu.copy()
    tempU.reverse()

    tempP = p.copy()
    tempP.reverse()

    plt.legend(tempP, tempU, loc='best', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
    plt.axis('equal')
    plt.title("Counting contributions up to " + str(sum(numList)))



    strFile = 'C:/Users/Emily Rose/source/repos/DiscordBot/countingPie.png'

    if os.path.isfile(strFile):
        os.system("del "+strFile)   # Opt.: os.system("rm "+strFile)
    plt.savefig(strFile, bbox_inches='tight');
    
    plt.close()
