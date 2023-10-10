#import libraries, set plots to display in notebook
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plots
#allows currency formatting
import locale 
locale.setlocale(locale.LC_ALL, '')

#Plot Five Points on a Graph
def plotFive():
    # Plot first five simulated portfolios 
    plots.plot(sim[first_five])
    plots.show()

#Calculate MarketReturn
def calculate_MarketReturn(expected_return, volatility):
    market_return = np.random.normal(expected_return, volatility)
    return market_return

#Calculate Future_Value
def calculate_FutureValue(pv, market_return, annual_addition):
    fv = pv * (1 + market_return) + annual_addition
    return fv

#Calculate End
def calculate_end(pv, expected_return, volatility, annual_investment):
    end = round(pv * (1 + np.random.normal(expected_return, volatility)) + annual_investment, 2)
    return end

#Calculate Probability
def calculate_Probability(endingvalue):
    endingvalue = len(endingvalue)
    return endingvalue

#Calculate Range
def getRange(endingvalue):
    endingvalue = len(sim.loc[29][(sim.loc[29] > 80000) & (sim.loc[29] < 1100000)]) /len(sim.loc[29])
    return endingvalue

#Calculate ComprehensiveTablePercentile
def comprehensiveTablePrecentile(endingvalue):
    endingvalue = np.percentile(sim.loc[29],[5, 10, 15, 25, 75, 85, 90, 95])
    return endingvalue

#Calculate pTileLength
def getpTileLength(pTiles):
    length = len(pTiles)
    return length

# Generating one possible future value based on market history; I will use 9% expected return with 18% volatility
pv = 10000
expected_return = .09
volatility = .18
time_horizon = 30
annual_addition = 10000

print("\tReturn", "\t\tEnding Value".rjust(18))
for year in range(time_horizon):
    market_return = calculate_MarketReturn(expected_return, volatility)
    fv = calculate_FutureValue(pv, market_return, annual_addition)
    print("\t{}".ljust(10).format(round(market_return,4)), "\t{}".rjust(10).format(locale.currency(fv, grouping=True)))
    pv = fv

# Simulate portfolio ending market values
sim = DataFrame()
iteration = 5000

for x in range(iteration):
    expected = 0.9
    volatility = .18
    time_horizon = 30
    pv = 10000
    annual_investment = 10000
    stream = []
    for i in range(time_horizon):
        end = calculate_end(pv, expected, volatility, annual_investment)
        stream.append(end)
        pv = end
    sim[x] = stream

first_five = list(range(5))
sim[first_five]

#Call plotFive to plot points on a graph
plotFive()

# Generate Summary Statistics with numpy functions
print("Count: ", len(sim.loc[29]))
print("Mean: ", locale.currency(np.mean(sim.loc[29]), grouping = True))
print("SD: ", locale.currency(np.std(sim.loc[29]), grouping = True))
print("Max: ", locale.currency(np.max(sim.loc[29]), grouping = True))
print("Min: ", locale.currency(np.min(sim.loc[29]), grouping = True))

# Get a visualization of the distribution of ending values
plots.hist(sim.loc[29], bins=100)
plots.show()

# Calculate probability of seeing a specific ending_value or less, 
# for example get close to the 75%ile, or #1,000,000

calculate_Probability(sim.loc[29])

# You can't really get a point estimate, but you can get a range q
getRange(sim.loc[29])

# You can get a more comprehensive table of percentiles easily using numpy's percentile function
p_tiles = comprehensiveTablePrecentile(sim.loc[29])
l = [5, 10, 15, 25, 75, 85, 90, 95]
for p in range(getpTileLength(p_tiles)):
    print("{}%-file: ".format(l[p]).rjust(15),"{}".format(locale.currency(p_tiles[p], grouping = True)))