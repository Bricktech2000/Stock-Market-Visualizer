# pip install matplotlib
# https://stackoverflow.com/questions/64729944/runtimeerror-the-current-numpy-installation-fails-to-pass-a-sanity-check-due-to
# pip install numpy==1.19.3
import matplotlib.pyplot as plt
# https://pypi.org/project/yfinance/
import yfinance as yf

import threading
import time

ticker = 'AAPL'
dataPeriod = '3d'
dataInterval = '1m'
backgroundColor = 'black'
markerStyle = 'o'
markerSize = 100
markerColor = (0.0, 0.5, 1.0)
maxMarkerOpacity = 1.0
maxZoom = 3
lineColor = (0.0, 0.5, 1.0)
lineOpacity = 0.25
lineStyle = 'solid'
percentageLineDivisions = 100
percentageLineOverflow = 1.10


def getFromTicker(ticker):
  ticker = yf.Ticker(ticker)
  data = ticker.history(period=dataPeriod, interval=dataInterval)
  # Open, High, Low, Close, Volume, Dividends, Stock Splits
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
    # https://thispointer.com/python-pandas-how-to-get-column-and-row-names-in-dataframe/
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.day.html
    if lastDay != data.index[i].day:
      lines.append(1 + (data.index[i].dayofweek == 0))
    else:
      lines.append(0)
    lastDay = data.index[i].day
  lines.append(1)
  points = []
  while len(data2) > 0:
    point = data2.pop(0)
    if not (point in data2):
      points.append(point)
  return points, lines


# https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color/23907866
fig = plt.figure()
fig.patch.set_facecolor(backgroundColor)
# https://stackoverflow.com/questions/10133478/how-to-programmatically-select-pan-zoom-in-pyqt-matplotlib-navigation
plt.get_current_fig_manager().toolbar.pan()
# https://github.com/matplotlib/mplfinance/issues/85
try:
  plt.get_current_fig_manager().window.showMaximized()
except Exception as e:
  pass

try:
  plt.get_current_fig_manager().window.state('zoomed')
except Exception as e:
  pass

oldItems = []


def visualize(points, lines):
  global fig
  global oldItems
  for item in oldItems:
    # http://matplotlib.1069221.n5.nabble.com/Removing-Markers-from-Figure-td8167.html
    item.remove()
  oldItems = []
  # https://stackoverflow.com/questions/9295026/matplotlib-plots-removing-axis-legends-and-white-spaces
  plt.axis('off')
  # https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/marker_reference.html
  # https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates-in-python-matplotlib
  # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
  oldItems.append(plt.scatter(
      [point[0] for point in points],
      [point[1] for point in points],
      marker=markerStyle,
      c=[(markerColor[0], markerColor[1], markerColor[2], min(point[2] * maxMarkerOpacity, 1)) for point in points],
      s=markerSize
  ))
  # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.vlines.html
  # https://stackoverflow.com/questions/24988448/how-to-draw-vertical-lines-on-a-given-plot-in-matplotlib
  for i in range(len(lines)):
    if(lines[i]):
      oldItems.append(plt.axvline(
          x=i,
          color=(lineColor[0], lineColor[0], lineColor[1], lineOpacity * lines[i]),
          linestyle=lineStyle
      ))
  for i in range(int(percentageLineDivisions * percentageLineOverflow + 1)):
    y = i / percentageLineDivisions * max([point[1] for point in points])
    if(y > min([point[1] for point in points]) / percentageLineOverflow):
      oldItems.append(plt.axhline(
          y=y,
          color=(lineColor[0], lineColor[0], lineColor[1], lineOpacity * (1 + (i % 10 == 0))),
          linestyle=lineStyle
      ))
  fig.tight_layout()
  return plt


updating = False


def show(plt, points, lines):
  def zoomChanged(evt):
    global updating
    if updating:
      return

    global maxMarkerOpacity
    updating = True
    xlim = evt.get_xlim()
    ylim = evt.get_ylim()
    zoom = 0
    zoom += len(lines) / (xlim[1] - xlim[0])
    zoom += (max([point[1] for point in points]) * percentageLineOverflow - min([point[1] for point in points]) / percentageLineOverflow) / (ylim[1] - ylim[0])
    zoom /= 2
    if zoom < 1:
      zoom = 1
    _maxMarkerOpacity = maxMarkerOpacity
    maxMarkerOpacity = zoom / maxZoom * _maxMarkerOpacity
    visualize(points, lines)
    maxMarkerOpacity = _maxMarkerOpacity
    updating = False

  # https://www.xspdf.com/resolution/53303696.html
  ax = plt.gca()
  zoomChanged(ax)
  plt.pause(.05)


data = getFromTicker(ticker)
dataUpdated = True


def fetchLoop():
  global data, dataUpdated
  while True:
    print('fetch')
    oldData = data
    data = getFromTicker(ticker)
    if data.shape != oldData.shape:
      dataUpdated = True
    time.sleep(0.01)


def updateLoop():
  global data, dataUpdated
  points, lines = [], []
  while True:
    if len(data) > 0:
      if dataUpdated:
        dataUpdated = False
        points, lines = compile(data)
        visualize(points, lines)
      if len(points) > 0:
        show(plt, points, lines)
    time.sleep(0.05)


thr = threading.Thread(target=fetchLoop, args=(), daemon=True)
thr.start()
# https://stackoverflow.com/questions/14694408/runtimeerror-main-thread-is-not-in-main-loop
updateLoop()
