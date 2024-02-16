import pandas as pd
from matplotlib import pyplot as plt


pd.options.display.max_rows = 200
pd.options.display.max_columns = 10


def printRowsAndColsNumber(df):
    num_rows, num_cols = df.shape
    print("Number of rows:", num_rows)
    print("Number of columns:", num_cols)


def printFirstAndLastRows(df):
    K = 32

    firstCount = K + 7
    print(f"\nFirst {firstCount} rows:")
    print(df.head(firstCount))

    lastCount = 5 * K - 3
    print(f"\nLast {lastCount} rows:")
    print(df.tail(lastCount))


def printFieldsDataTypes(df):
    print("\nData types of each field:")
    print(df.dtypes)


def convertSalesRelatedFields(df):
    sales_fields = ['Total Sales New', 'Total Sales Used']
    for field in sales_fields:
        withoutDollarSign = df[field].str.replace('$', '')
        df[field] = pd.to_numeric(withoutDollarSign)


def createNewFields(df):
    df['Total'] = df['New'] + df['Used']
    df['Total Sales'] = df['Total Sales New'] + df['Total Sales Used']
    df['Difference'] = df['New'] - df['Used']


def changeColumnOrder(df):
    return df[["Year", "Month", "Total Sales", "Total Sales New", "Total Sales Used",
               "Total", "New", "Used", "Difference"]]


def task8(df):
    print("\nSubtask A")
    print(df[(df['Difference'] < 0)][["Year", "Month"]])

    print("\nSubtask B")
    min_total_sales_index = df['Total Sales'].idxmin()
    print("Year:", df.loc[min_total_sales_index, 'Year'])
    print("Month:", df.loc[min_total_sales_index, 'Month'])

    print("\nSubtask C")
    min_total_sales_index = df['Used'].idxmax()
    print("Year:", df.loc[min_total_sales_index, 'Year'])
    print("Month:", df.loc[min_total_sales_index, 'Month'])


def task9(df):
    print("\nSubtask A")
    print(df.groupby('Year')['Total Sales'].sum())

    print("\nSubtask B")
    M = "JUN"
    june_data = df[df['Month'] == M]
    print(june_data['Total Sales Used'].mean())


def task10(df):
    year = 2000 + (17 - 6)
    df = df[df["Year"] == year]

    plt.bar(df['Month'], df['New'])
    plt.title('Sales Volume of New Cars in 2011')
    plt.xticks(rotation=45)
    plt.show()


def task11(df):
    yearly_sales = df.groupby('Year')['Total Sales'].sum()

    # Plot the data as a pie chart
    plt.figure(figsize=(8, 8))  # Set the figure size
    plt.pie(yearly_sales, labels=yearly_sales.index, autopct='%1.1f%%', startangle=90)
    plt.title('Total Sales Volume for Each Year')
    plt.show()


def task12(df):
    yearly_sales_new = df.groupby('Year')['Total Sales New'].sum()
    yearly_sales_used = df.groupby('Year')['Total Sales Used'].sum()

    plt.figure(figsize=(10, 6))

    plt.plot(yearly_sales_new.index, yearly_sales_new.values, label='New Cars')
    plt.plot(yearly_sales_used.index, yearly_sales_used.values, label='Used Cars')

    plt.ylabel('Total Sales')
    plt.title('Total Income from Sales of New and Used Cars by Year')
    plt.legend()

    plt.grid(True)
    plt.show()


def main():
    # 1
    data_frame = pd.read_csv("Vehicle_Sales.csv")

    # 2
    printRowsAndColsNumber(data_frame)

    # 3
    # printFirstAndLastRows(data_frame)

    # 4
    # printFieldsDataTypes(data_frame)

    # 5 (necessary for next tasks)
    # convertSalesRelatedFields(data_frame)
    # printFieldsDataTypes(data_frame)

    # 6 (necessary for next tasks)
    # createNewFields(data_frame)

    # 7
    # data_frame = changeColumnOrder(data_frame)

    # 8
    # task8(data_frame)
    
    # 9
    # task9(data_frame)

    # 10
    # task10(data_frame)

    # 11
    # task11(data_frame)

    # 12
    # task12(data_frame)


if __name__ == '__main__':
    main()

