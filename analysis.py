import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

revenue = pd.read_csv("/Users/camerondavison/Downloads/revenue_decay.csv")

rev = revenue.groupby("months_since_signup")["cohort_revenue"].mean()

plt.figure()
rev.plot()
plt.title("Revenue Decay Over Time")
plt.xlabel("Months Since Signup")
plt.ylabel("Average Cohort Revenue")
plt.show()

ltv_avg = revenue.groupby("months_since_signup")["ltv_per_user"].mean()

plt.figure()
ltv_avg.plot()
plt.title("Customer Lifetime Value (LTV) Over Time")
plt.xlabel("Months Since Signup")
plt.ylabel("Average LTV Per User")
plt.show()