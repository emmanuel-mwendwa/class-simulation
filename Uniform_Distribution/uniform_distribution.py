# %matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import Math,Latex
from IPython.core.display import Image
import seaborn as sns
# Uniform Distribution
from scipy.stats import uniform

# random numbers from uniform distribution
n = 1000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc=start, scale=width)

ax = sns.distplot(data_uniform,
                 bins=100,
                 kde=True,
                 color='skyblue',
                 hist_kws={"linewidth": 15, 'alpha':1})
ax.set(xlabel='Uniform Distribution', ylabel='Frequency')