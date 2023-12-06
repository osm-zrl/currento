import random
from datetime import datetime, timedelta
from dbconfig import insert_many

def generate_exchange_data(start_date, end_date):
    base_currency = 'EUR'
    currencies = ['MAD', 'USD']

    current_date = start_date
    data = []

    while current_date <= end_date:
        mad_rate = round(random.uniform(11, 12), 4)
        usd_rate = round(random.uniform(1, 1.2), 4)

        rates = {'MAD': mad_rate, 'USD': usd_rate}
        data.append({
            'success': True,
            'timestamp': int(current_date.timestamp()),
            'base': base_currency,
            'date': current_date.strftime('%Y-%m-%d'),
            'rates': rates
        })

        current_date += timedelta(hours=1)

    return data

# Set the start and end date for generating hourly data for one day
start_time = datetime(2023, 11, 10, 0, 0, 0)  # Year, Month, Day, Hour, Minute, Second
end_time = datetime(2023, 11, 19, 23, 0, 0)  # Year, Month, Day, Hour, Minute, Second

generated_data = generate_exchange_data(start_time, end_time)

# Example output for the first entry
insert_many(generated_data)
print(generated_data)
