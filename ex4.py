import pandas as pd


data = {
    'Date': ['2025-01-07', '2025-01-14', '2025-01-21', '2025-02-01',
             '2025-01-07', '2025-01-14', '2025-01-21', '2025-02-01'],
    'City': ['CityA', 'CityA', 'CityA', 'CityA', 'CityB', 'CityB', 'CityB', 'CityB'],
    'Temperature': [20, 21, 19, 22, 25, 26, 24, 23]
}

df = pd.DataFrame(data)


df['Date'] = pd.to_datetime(df['Date'])


df['Month'] = df['Date'].dt.strftime('%B')  
total_temp_by_city = df.groupby('City')['Temperature'].sum().reset_index()
print("Total Temperature by City:\n", total_temp_by_city)


monthly_summary = df.pivot_table(values='Temperature', index='City', columns='Month', aggfunc='sum', fill_value=0)
print("\nMonth-wise Summary Table:\n", monthly_summary)


hottest_city = total_temp_by_city.loc[total_temp_by_city['Temperature'].idxmax()]
print(f"\nCity with Highest Total Temperature: {hottest_city['City']} ({hottest_city['Temperature']}°)")
