import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

ames_csv_path = '../data/AmesHousing.csv'


def run():
    matplotlib.style.use('default')

    df = pd.read_csv(ames_csv_path)

    print('\n=== head ===')
    print(df.head())

    print('\n=== column info ===')
    df.info()

    print('\n=== unique values in each column ===')
    print_columns_unique_values(df)

    print('\n=== total sales price by year ===')
    plot_total_sales_price_by_year(df)

    plt.show()


def print_columns_unique_values(df):
    column_names = df.columns.values.tolist()
    for column_name in column_names:
        print(column_name + ": " + str(pd.unique(df[column_name])))


def plot_total_sales_price_by_year(df):
    total_sales_price_by_year = df \
        .groupby(['Yr Sold']) \
        .agg({'SalePrice': 'sum'}) \
        .reset_index(level=[0])
    print(total_sales_price_by_year)

    yr_sold = total_sales_price_by_year['Yr Sold']
    sale_price = total_sales_price_by_year['SalePrice']

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(yr_sold, sale_price, color='green', marker='o')
    ax.set(xlabel='Year', ylabel='Total of Sales Prices',
           title='Total Sales Price by Year')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid()

    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda value, p: "{:,} k".format(value * 1e-3).replace(".0", "")))

    for x, y in zip(yr_sold, sale_price):
        ax.annotate("{:,}".format(y), xy=(x + 0.05, y), textcoords='data')


run()
