import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import scipy
from FileLoader import FileLoader as loader

import matplotlib.pyplot as plt


class MyPlotLib:

    NUMERICS = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    @staticmethod
    def histogram(data, features):
        tmp = (data[features]
               .select_dtypes(include=MyPlotLib.NUMERICS)
               .drop_duplicates())
        for ft in tmp:
            hist = data[ft].plot.hist()
            hist.set_xlabel(ft)
            plt.figure()
            hist.plot()
        plt.show()


    @staticmethod
    def density(data, features):
        pass

    @staticmethod
    def pair_plot(data, features):
        pass

    @staticmethod
    def box_plot(data, features):
        pass