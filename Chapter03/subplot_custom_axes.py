from plotly import tools
import plotly as py
import plotly.graph_objs as go


pyplt = py.offline.plot

trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                          'Plot 3', 'Plot 4'))
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)

fig['layout']['xaxis1'].update(title='xaxis 1 title')
fig['layout']['xaxis2'].update(title='xaxis 2 title', range=[10, 50])
fig['layout']['xaxis3'].update(title='xaxis 3 title', showgrid=False)
fig['layout']['xaxis4'].update(title='xaxis 4 title', type='log')

fig['layout']['yaxis1'].update(title='yaxis 1 title')
fig['layout']['yaxis2'].update(title='yaxis 2 title', range=[40, 80])
fig['layout']['yaxis3'].update(title='yaxis 3 title', showgrid=False)
fig['layout']['yaxis4'].update(title='yaxis 4 title')

fig['layout'].update(title='Customizing Subplot Axes')

pyplt(fig, filename='tmp/subplot_custom_axes.html')