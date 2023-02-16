import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

fig = go.Figure()

# Add traces
# fig.add_trace(go.Scatter(x=random_x, y=random_y0,
#                     mode='markers',
#                     name='markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='lines+markers',
                    name='lines+markers'))
# fig.add_trace(go.Scatter(x=random_x, y=random_y2,
#                     mode='lines',
#                     name='lines'))

fig.show()

# from bokeh.plotting import figure, output_file, show
# from bokeh.layouts import row
# from bokeh.models.widgets import Slider
# output_file('layout.html')
# p = figure(width=400,height=200) # 建立圖表
# p.line([1,2,3,4,5],[5,4,3,2,1])
# slide = Slider()                 # 建立 Slider
# layout = row(p,slide)          # 將圖表與 Slider 利用 hplot 排版
# show(layout)