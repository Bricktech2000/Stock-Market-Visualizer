
#pip install matplotlib
#https://stackoverflow.com/questions/64729944/runtimeerror-the-current-numpy-installation-fails-to-pass-a-sanity-check-due-to
#pip install numpy==1.19.3
import matplotlib.pyplot as plt
#https://pypi.org/project/yfinance/
import yfinance as yf

###   CONSTANTS   ###
ticker = 'AAPL'
dataPeriod = '10d'
dataInterval = '5m'
backgroundColor = 'black'
markerStyle = 'o'
markerSize = 100
markerColor = (0.0, 0.5, 1.0)
maxMarkerOpacity = 1.0
lineColor = (0.0, 0.5, 1.0)
lineOpacity = 0.5
lineStyle = 'solid'
percentageLineDivisions = 100
percentageLineOverflow = 1.05



###     CODE     ###
def getFromTicker(ticker):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period=dataPeriod, interval=dataInterval)
    #Open, High, Low, Close, Volume, Dividends, Stock Splits
    return data


def compile(data):
    data2 = []
    lines = []
    lastDay = 0
    for i in range(0, len(data)):
        vol = data['Volume'][i] / max(data['Volume'])
        data2.append([i, data['Open'][i],  vol])
        data2.append([i, data['High'][i],  vol])
        data2.append([i, data['Low'][i],   vol])
        data2.append([i, data['Close'][i], vol])
        #https://thispointer.com/python-pandas-how-to-get-column-and-row-names-in-dataframe/
        #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.day.html
        if lastDay != data.index[i].day: lines.append(1)
        else: lines.append(0)
        lastDay = data.index[i].day
    lines.append(1)
    points = []
    while len(data2) > 0:
        point = data2.pop(0)
        if not (point in data2):
            points.append(point)
    return points, lines

def visualize(points, lines):
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
        marker=markerStyle,
        c=[(markerColor[0], markerColor[1], markerColor[2], point[2] * maxMarkerOpacity) for point in points],
        s=markerSize
    )
    #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.vlines.html
    #https://stackoverflow.com/questions/24988448/how-to-draw-vertical-lines-on-a-given-plot-in-matplotlib
    for i in range(len(lines)):
        if(lines[i]):
            plt.axvline(
                x=i,
                color=(lineColor[0], lineColor[0], lineColor[1], lineOpacity),
                linestyle=lineStyle
            )
    for i in range(percentageLineDivisions):
        y = i / percentageLineDivisions * max([point[1] for point in points]) * percentageLineOverflow
        if(y > min([point[1] for point in points]) / percentageLineOverflow):
            plt.axhline(
                y=y,
                color=(lineColor[0], lineColor[0], lineColor[1], lineOpacity),
                linestyle=lineStyle
            )
    plt.show()


data = getFromTicker(ticker)
points, lines = compile(data)
visualize(points, lines)






















