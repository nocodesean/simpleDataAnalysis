import pandas as pd
import matplotlib.pyplot as plt

# Load COVID-19 data
url = 'covid19_test_data.csv'
data = pd.read_csv(url)

# Preprocess data
data['date'] = pd.to_datetime(data['date'])
data = data.groupby(['date', 'country']).sum().reset_index()

# Analyze and plot data
country = 'USA'
usa_data = data[data['country'] == country]

plt.figure(figsize=(10, 6))
plt.plot(usa_data['date'], usa_data['cases'], label='Cases')
plt.plot(usa_data['date'], usa_data['deaths'], label='Deaths')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(f'COVID-19 Trends in {country}')
plt.legend()
plt.show()
