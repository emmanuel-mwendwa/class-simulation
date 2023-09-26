import matplotlib.pyplot as plt
from IPython.display import Math,Latex
from IPython.core.display import Image
import seaborn as sns

from scipy.stats import gamma
data_gamma = gamma.rvs(a=5, size=10000)
ax = sns.distplot(data_gamma,
                 kde=True,
                 bins=100,
                 color='skyblue',
                 hist_kws={"linewidth":15, 'alpha': 1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')

plt.show()