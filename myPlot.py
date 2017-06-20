from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


class myPlot(object):
    def plot(self, X,columns, color , title, fileName ):
        df = pd.DataFrame(X, columns=columns)
        # Doc: https://pandas.pydata.org/pandas-docs/stable/visualization.html#scatter-matrix-plot
        scatter_matrix(df, figsize=(10, 10), diagonal='hist', color=color)
        plt.suptitle(title)
        # plt.show()
        pp = PdfPages(fileName + '- Grafico.pdf')
        plt.savefig(pp, format='pdf')
        pp.savefig()
        pp.close()
