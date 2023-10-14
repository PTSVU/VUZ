import numpy as np
import matplotlib.pyplot as plt

apple_cost = [131.96, 121.26, 122.15, 131.46, 124.61, 136.96, 145.86, 151.83, 141.50, 149.80, 165.30, 177.57]
apple_avg = np.average(apple_cost)
apple_avg_arr = [apple_avg]*12
microsoft_cost = [231.96, 232.38, 235.77, 252.18, 249.68, 270.90, 284.91, 301.88, 281.92, 331.62, 330.59, 336.32]
microsoft_avg = np.average(microsoft_cost)
microsoft_avg_arr = [microsoft_avg]*12
google_cost = [91.37, 101.10, 103.13, 117.68, 117.84, 122.09, 134.73, 144.70, 133.68, 148.05, 141.90, 144.85]
google_avg = np.average(google_cost)
google_avg_arr = [google_avg]*12
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
plt.plot(months, apple_cost, months, apple_avg_arr)
plt.xlabel("Months")
plt.ylabel("Share price $")
plt.title("Apple")
plt.show()
plt.plot(months, microsoft_cost, months, microsoft_avg_arr)
plt.xlabel("Months")
plt.ylabel("Share price $")
plt.title("Microsoft")
plt.show()
plt.plot(months, google_cost, months, google_avg_arr)
plt.xlabel("Months")
plt.ylabel("Share price $")
plt.title("Google")
plt.show()
print("Стоимость акций Apple с начала с 1 января 2021 года по 31 декабря 2021 года выросла на", round(apple_cost[11]/(apple_cost[0]/100)-100,2),"%")
print("Стоимость акций Microsoft с начала с 1 января 2021 года по 31 декабря 2021 года выросла на", round(microsoft_cost[11]/(microsoft_cost[0]/100)-100,2),"%")
print("Стоимость акций Google с начала с 1 января 2021 года по 31 декабря 2021 года выросла на", round(google_cost[11]/(google_cost[0]/100)-100,2),"%")
#%%
