from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline.offline import matplotlib
# %matplotlib inline
from matplotlib.backends.backend_pdf import PdfPages
# from plotly import 1.9.0
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


class myPlot(object):
    def plot(self, X,columns, color , title, fileName ):
        print "Guardando PDF..."
        df = pd.DataFrame(X, columns=columns)
        # Doc: https://pandas.pydata.org/pandas-docs/stable/visualization.html#scatter-matrix-plot
        scatter_matrix(df, figsize=(10, 10), diagonal='hist', color=color)
        plt.suptitle(title)
        plt.show()
        pp = PdfPages(fileName + '- Grafico.pdf')
        plt.savefig(pp, format='pdf')
        pp.savefig()
        pp.close()

