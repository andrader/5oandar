import numpy as np
from scipy.stats import pearsonr, spearmanr, kendalltau
import matplotlib.pyplot as plt
import seaborn as sns

def plot_corr(df, ax=None):

    if not ax:
        fig, ax = plt.subplots()

    corr = df.corr().iloc[1:, :-1]
    pval = df.corr(method=lambda x, y: pearsonr(x, y)[1]).iloc[1:, :-1]
    mask = np.triu(np.ones_like(corr, dtype=bool), 1)
    asterisks = pval.applymap(
        lambda x: "*" * sum([x <= level for level in [0.01, 0.05, 0.1]])
    )
    annot = corr.applymap(lambda x: f"{x:.2f}") + asterisks

    sns.heatmap(
        corr,
        mask=mask,
        cmap="vlag",
        vmin=-1,
        vmax=1,
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.6},
        annot=annot,
        fmt="",
        ax=ax,
    )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha="right")



# g = df.set_index('variable').sort_index().groupby('month')

# fig, axs = plt.subplots((g.ngroups+1)//2, 2, figsize=(16,10))
# axs = axs.flatten()

# for (name, x), ax, in zip(g, axs):
#     x.value.plot.barh(ax=ax)


# def plot_funnel(x,y, ax=None):
#     # y = [5,4,3,2,1]
#     # x = [80,73,58,42,23]
#     labels = ['Hot Leads', 'Samples Sent', 'Quotes', 'Negotiations', 'Sales']
#     x_max = np.max(x)
#     x_min = np.min(x)
#     x_range = x_max - x_min
#     if not ax:
#         fig, ax = plt.subplots(1, figsize=(12,10))

#     for idx, (xi, yi) in enumerate(zip(x,y)):
#         left = (x_range - xi)/2
#         ax.barh(xi, label, left = left, edgecolor='black')
#         # label
#         ax.text(50, y, labels[idx], ha='center', fontsize=16, color='#2A2A2A')
#         # value
#         #ax.text(50, y[idx]-0.3, x[idx], ha='center', fontsize=16, color='#2A2A2A')
        
#     ax.set_xlim(x_min, x_max)
#     #plt.axis('off')
#     ax.set_title('Beskar Forging Services Inc.', loc='center', fontsize=24, color='#2A2A2A')


# plot_funnel([5,4,3,2,1], [80,73,58,42,23], ax=None)