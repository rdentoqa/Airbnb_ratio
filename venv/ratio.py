# x = ratio * y
# ratio = r1/r2
#
# 4x + 4y = 2404
# 4 * ((r1/r2)y + y) = 2404
# 4 * ((r1/r2)y + (r2/r2)y) = 2404
# 4 * ((r1 + r2)y)/r2 = 2404
# (r1 + r2)y = (2404 * r2)/4
# y = ((2404 * r2) / (4 * (r1+r2))

# x = (2404 - 4y) / 4

# usd to pesos: 1usd = 19.95 pesos
# usd to euro: 1usd = 0.82 euros
peso_equiv = 19.95
euro_equiv = 0.82
doge_equiv = 2.87 # taken 5/21/2021 at 3:15pm

def calcY(total, r1, r2):
    y = (total * r2) / (4 * (r1 + r2))
    return y

def calcX(total, y):
    x = ((total - 4 * y) / 4)
    return x

def print_output(r1, r2, x, y):
    print("When Ratio = " + str(r1) + "/" + str(r2) + ",\nUSD: y = $" + str(round(y, 2)) + ", and x = $" + str(round(x, 2)))
    print("Peso: y = MX$" + str(round(y * peso_equiv, 2))  + ", and x = MX$" + str(round(x * peso_equiv, 2)))
    print("EUR: y = €" + str(round(y * euro_equiv, 2))  + ", and x = €" + str(round(x * euro_equiv, 2)))
    print("Doge: y = # " + str(y * doge_equiv)  + ", and x = # " + str(x * doge_equiv))
    print('\n')

stupid_changing_price_of_airbnb = 2403.79
r1 = 2
r2 = 3
y = calcY(stupid_changing_price_of_airbnb, r1, r2)
print_output(r1, r2, y, calcX(stupid_changing_price_of_airbnb, y))
r1 = 3.14159286
r2 = 5.000000001
y = calcY(stupid_changing_price_of_airbnb, r1, r2)
print_output(r1, r2, y, calcX(stupid_changing_price_of_airbnb, y))
