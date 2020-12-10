
#pip install matplotlib
#https://stackoverflow.com/questions/64729944/runtimeerror-the-current-numpy-installation-fails-to-pass-a-sanity-check-due-to
#pip install numpy==1.19.3
import matplotlib.pyplot as plt



data = [
    [1, 10.5],
    [1, 10.2],
    [1, 10.4],
    [1, 10.5],
    [1, 10.8],
    [1, 10.4],
    [1, 10.5],
    [1, 10.2],
    [1, 10.4],
    [1, 10.4],
    [2, 10.5],
    [2, 10.2],
    [2, 10.1],
    [2, 10.0],
    [2, 10.0],
    [2, 10.8],
    [2, 10.5],
    [2, 10.3],
    [2, 10.7],
    [2, 10.2],
    [3, 10.5],
    [3, 10.8],
    [3, 10.0],
    [3, 10.0],
    [3, 10.5],
    [3, 10.2],
    [3, 10.1],
    [3, 10.3],
    [3, 10.5],
    [3, 10.7],
    [3, 10.4],
    [3, 10.9],
    [3, 10.0],
]

def visualize(points):
    #https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/marker_reference.html
    #https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates-in-python-matplotlib
    plt.scatter([point[0] for point in points], [point[1] for point in points], marker='s')
    plt.show()

def compile(data):
    return data

points = compile(data)
visualize(points)






















