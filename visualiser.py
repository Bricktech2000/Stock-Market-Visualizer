
#pip install matplotlib
#https://stackoverflow.com/questions/64729944/runtimeerror-the-current-numpy-installation-fails-to-pass-a-sanity-check-due-to
#pip install numpy==1.19.3
import matplotlib.pyplot as plt
#https://pypi.org/project/yfinance/
import yfinance as yf



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

def getFromTicker(ticker):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period='30d', interval='5m')
    #Open, High, Low, Close, Volume, Dividends, Stock Splits
    return data


def compile(data):
    data2 = []
    for i in range(0, len(data)):
        vol = data['Volume'][i] / max(data['Volume'])
        data2.append([i, data['Open'][i],  vol])
        data2.append([i, data['High'][i],  vol])
        data2.append([i, data['Low'][i],   vol])
        data2.append([i, data['Close'][i], vol])
    out = []
    while len(data2) > 0:
        item = data2.pop(0)
        if not (item in data2):
            out.append(item)
    return out

def visualize(points):
    #https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color/23907866
    fig = plt.figure()
    fig.patch.set_facecolor('black')
    #https://stackoverflow.com/questions/9295026/matplotlib-plots-removing-axis-legends-and-white-spaces
    plt.axis('off')
    #https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/marker_reference.html
    #https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates-in-python-matplotlib
    #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
    plt.scatter([point[0] for point in points], [point[1] for point in points], marker='s', c=[(0, 1, 1, point[2] * 1) for point in points], s=100)
    plt.show()


data = getFromTicker('AAPL')
print(data)
points = compile(data)
visualize(points)






















