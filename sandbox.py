import matplotlib.pyplot as plt
from dbconfig import daily_average


result = list(daily_average())



dates = [entry['_id'] for entry in result]
mad_rates = [entry['MAD'] for entry in result]
usd_rates = [entry['USD'] for entry in result]

# Plotting the chart
plt.figure(figsize=(10, 6))
plt.plot(dates, mad_rates, marker='o', linestyle='-', label='MAD Rates')
plt.plot(dates, usd_rates, marker='o', linestyle='-', label='USD Rates')
plt.title('MAD and USD Rates Over Time')
plt.xlabel('Date')
plt.ylabel('Rate')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.tight_layout()


# Show the plot
plt.show()
