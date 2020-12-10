
#pip install matplotlib
#https://stackoverflow.com/questions/64729944/runtimeerror-the-current-numpy-installation-fails-to-pass-a-sanity-check-due-to
#pip install numpy==1.19.3
import matplotlib.pyplot as plt
#https://pypi.org/project/yfinance/
import yfinance as yf

###   CONSTANTS   ###
ticker = 'AAPL'
maxMarkerOpacity = 1
dataPeriod = '30d'
dataInterval = '5m'
backgroundColor = 'black'
markerShape = 's'
markerColor = (0, 1, 1)
markerSize = 100



###     CODE     ###
def getFromTicker(ticker):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period=dataPeriod, interval=dataInterval)
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
    fig.patch.set_facecolor(backgroundColor)
    #https://stackoverflow.com/questions/9295026/matplotlib-plots-removing-axis-legends-and-white-spaces
    plt.axis('off')
    #https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/marker_reference.html
    #https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates-in-python-matplotlib
    #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
    plt.scatter(
        [point[0] for point in points],
        [point[1] for point in points],
        marker=markerShape,
        c=[(markerColor[0], markerColor[1], markerColor[2], point[2] * maxMarkerOpacity) for point in points],
        s=markerSize
    )
    plt.show()


data = getFromTicker(ticker)
points = compile(data)
visualize(points)






















