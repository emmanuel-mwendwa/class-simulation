import matplotlib.pyplot as plt
from IPython.display import Math,Latex
from IPython.core.display import Image
import seaborn as sns

from scipy.stats import expon

data_expon = expon.rvs(scale=1, loc=0, size=1000)

ax = sns.distplot(data_expon,
                 kde=True,
                 bins=100,
                 color='skyblue',
                 hist_kws={"linewidth":15, 'alpha':1})

ax.set(xlabel='Exponential Distribution', ylabel='Frequency')