
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
    data = ticker.history(period='1d', interval='1m')
    #Open, High, Low, Close, Volume, Dividends, Stock Splits
    return data


def compile(data):
    data2 = []
    for i in range(0, len(data)):
        data2.append([i, data['Open'][i]])
        data2.append([i, data['High'][i]])
        data2.append([i, data['Low'][i]])
        data2.append([i, data['Close'][i]])
    out = []
    while len(data2) > 0:
        item = data2.pop(0)
        if not (item in data2):
            out.append(item)
    return out

def visualize(points):
    #https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/marker_reference.html
    #https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates-in-python-matplotlib
    plt.scatter([point[0] for point in points], [point[1] for point in points], marker='s')
    plt.show()


data = getFromTicker('AAPL')
print(data)
points = compile(data)
visualize(points)






















