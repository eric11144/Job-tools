import sys
from math import log
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QSlider, QWidget, 
    QHBoxLayout, QVBoxLayout)

import pyqtgraph as pg
import numpy as np

class LabelSlider(QWidget):
    def __init__(self, *args, **kwargs):
        super(LabelSlider, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        # IMPORTANT! QStyles sometimes create *huge* margins (6-10 pixels) around
        # layout contents; we don't really need those in here
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel()
        layout.addWidget(self.label, alignment=Qt.AlignHCenter)
        # use an arbitrary text for the minimum width to minimize size flickering
        # on value changes
        self.label.setMinimumWidth(self.fontMetrics().width("8.8888e+88"))
        self.label.setAlignment(Qt.AlignCenter)

        layout.addSpacing(10)

        self.slider = QSlider()
        # when adding a QSlider to a QLayout and specifying an alignment, the
        # opposite of the orientation *has* to be omitted to ensure that it's
        # centered in the other direction
        layout.addWidget(self.slider, alignment=Qt.AlignHCenter)
        # set the slider "transparent" for mouse events, so that the user will
        # still see it as enabled but won't be able to interact with it
        self.slider.setAttribute(Qt.WA_TransparentForMouseEvents)

        #set a range high enough to limit rounding errors
        self.slider.setMaximum(100000)

        # expose the basic slider signal/methods for transparency, so that
        # this LabelSlider will have a similar interface to that of a QSlider
        self.value = self.slider.value
        self.valueChanged = self.slider.valueChanged

    def setValue(self, value, xLimit):
        sliderValue = self.slider.maximum() - value * self.slider.maximum()
        self.slider.setValue(sliderValue)

        xLimitMin, xLimitMax = xLimit
        limitRange = xLimitMax - xLimitMin
        floatValue = xLimitMin + (value * limitRange / (limitRange)) * (
            limitRange)
        self.label.setText("{0:.4g}".format(floatValue))
        # ensure that the widget is resized to fit the label contents too;
        # sizeHint will be called afterwards
        self.updateGeometry()

    def sizeHint(self):
        hint = super(LabelSlider, self).sizeHint()
        # adjust the minimum hint width to accomodate the label contents
        if hint.width() < self.label.width():
            hint.setWidth(self.label.width())
        return hint


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.horizontalLayout = QHBoxLayout(self)

        self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.horizontalLayout.addWidget(self.win)
        self.p6 = self.win.addPlot(title="My Plot")
        x = np.arange(1e5)
        self.y1 = np.random.randn(x.size)
        self.p6.plot(self.y1, pen="r")
        self.p6.setMouseEnabled(x=True, y=False)
        self.p6.setXRange(0,300)
        # set a minimum x range for the plot
        # this value *HAS* to be > 0
        self.p6.setLimits(xMin=0, xMax=len(self.y1), minXRange=1)

        self.p6.sigRangeChanged.connect(self.update_plot)

        self.slider = LabelSlider()
        self.horizontalLayout.addWidget(self.slider)

    def update_plot(self):
        state = self.p6.getViewBox().state

        # get the limits of the plot's ViewBox
        limits = state["limits"]
        minZoom, maxZoom = xLimit = limits["xLimits"]
        xRangeMin, xRangeMax = limits["xRange"]

        # if the minimum x range is set, use that instead
        if xRangeMin is not None:
            minZoom = xRangeMin
        # ensure that the minimum x range is > 0
        minZoom = max(1, minZoom)
        if xRangeMax is not None:
            maxZoom = xRangeMax
        xMin, xMax = self.p6.getAxis("bottom").range
        diff = xMax - xMin

        # get the possible minimum and maximum values based on the wheel factor
        factor = abs(state["wheelScaleFactor"])
        minimum = log(maxZoom / 100000., factor)
        maximum = log(minZoom / 100000., factor)
        value = log(diff / 100000., factor)

        # adjust the factor to a 0.0-1.0 range according to the possible zoom
        realValue = (value - minimum) / (maximum - minimum)

        # set the slider value according to the above value
        self.slider.setValue(realValue, xLimit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())