import os
import pandas as pd


data_folder = os.path.join('C:\\dev', 'data')
sales_train_validation_file = os.path.join(data_folder, 'sales_train_validation.csv')
sell_prices_file = os.path.join(data_folder, 'sell_prices.csv')
calendar_file = os.path.join(data_folder, 'calendar.csv')


def read_sales() -> pd.DataFrame:
    return pd.read_csv(sales_train_validation_file)


def read_sell_prices() -> pd.DataFrame:
    return pd.read_csv(sell_prices_file)


def read_calendar() -> pd.DataFrame:
    return pd.read_csv(calendar_file)


if __name__ == '__main__':
    sales = read_sales()
    sell_prices_file = read_sell_prices()
    calendar = read_calendar()
    pass
