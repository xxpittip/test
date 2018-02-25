import matplotlib.pyplot as plt

def plotTest(x):
    plt.plot(x, color="green")
    plt.xlim(0,len(x)-1)
    plt.ylim(min(x),max(x))
    plt.show()
