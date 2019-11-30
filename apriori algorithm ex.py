from apyori import apriori 
data = [
        ['bread','milk',],
        ['bread','diaper','beer','eggs'],
        ['milk','diaper','beer','cola'],
        ['bread','milk','diaper','beer'],
        ['bread','milk','diaper','cola']
]
#minsup = 0.5
#minconf = 0.6
ap = list(apriori(data))
print(ap)
