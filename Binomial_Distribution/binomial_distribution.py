import matplotlib.pyplot as plt
from IPython.display import Math,Latex
from IPython.core.display import Image
import seaborn as sns

from scipy.stats import binom

data_binom = binom.rvs(n=10, p=0.8, size=10000)
ax = sns.distplot(data_binom,
                 kde=False,
                 color='skyblue',
                 hist_kws={"linewidth": 15, "alpha": 1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')