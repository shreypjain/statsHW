from scipy import stats
import matplotlib.pyplot as plt

males = [16,16,17,16,18,17,17,16,16,27,16,17,16,17,16,16]
females = [17,18,19,20,18,19,20,18,18,17,16,18,19,17,18]


def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.



#mean
print(sum(males) / len(males))
print(sum(females) / len(females))

#medians
print(median(males))
print(median(females))

#modes
print(stats.mode(males)[0])
print(stats.mode(females)[0])

#range
print(max(males) - min(males))
print(max(females) - min(females))

#graphs
#stem and leaf
plt.scatter(females,range(15))
plt.show()
plt.scatter(males,range(16))
plt.show()
#MY PLOTS ARE OFF^^^^

#recalculating the without the outlier:
outlier = [16,16,17,16,18,17,17,16,16,16,17,16,17,16,16]
print(sum(outlier) / len(outlier))
print(median(outlier))
print(stats.mode(outlier)[0])
print(max(outlier) - min(outlier))