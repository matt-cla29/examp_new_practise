import pandas as pd
import matplotlib.pyplot as plt
import sys

#The menu() function generates the UI the accepts and validates user choice
def menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("7. trends and patterns over time")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-7): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 7:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(menu_choice)


#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GBP - JPY',
       '6': 'JPY - GBP'}
   
    currency = currencies.get(menu_choice)
    
    return currency

def trend_menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. trends and patterns for the value of the pound (GBP) compared to other currencies")
        print("2. trends and patterns for the performance (e.g. increase/decrease in value) of a selected currency")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        

        
        trend_choice = input("Please enter the number of your choice (1-7): ")

        try:
            int(trend_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(trend_choice) < 1 or int(trend_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(trend_choice)

menu_choice = menu()

if 1 <= int(menu_choice) <= 6:
    currency = get_currency()

elif int(menu_choice) == 7:
    trend_choice = trend_menu()

# we will need a complete dataframe for all the functions here
    df = pd.read_csv("Task4a_RBSX_data.csv")


if trend_choice == 1:
    # Read the CSV file
    df = pd.read_csv("Task4a_RBSX_data.csv")

     # Convert the Date column into datetime format
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    # Sort the data by date
    df = df.sort_values("Date")

    # Create four graphs
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

     # GBP compared to EUR
    axes[0, 0].plot(df["Date"], df["GBP - EUR"])
    axes[0, 0].set_title("GBP to EUR")
    axes[0, 0].set_ylabel("Euros per pound")

    # GBP compared to AUD
    axes[0, 1].plot(df["Date"], df["GBP - AUD"])
    axes[0, 1].set_title("GBP to AUD")
    axes[0, 1].set_ylabel("Australian dollars per pound")

    # GBP compared to JPY
    axes[1, 0].plot(df["Date"], df["GBP - JPY"])
    axes[1, 0].set_title("GBP to JPY")
    axes[1, 0].set_ylabel("Yen per pound")

     # GBP compared to USD
    axes[1, 1].plot(df["Date"], df["GBP - USD"])
    axes[1, 1].set_title("GBP to USD")
    axes[1, 1].set_ylabel("Dollars per pound")

    # Add labels and gridlines to each graph
    for ax in axes.flat:
            ax.set_xlabel("Date")
            ax.grid(True)
            ax.tick_params(axis="x", rotation=45)

    # Add a heading to the complete figure
    fig.suptitle("Value of GBP Against Other Currencies Over Time")
    plt.tight_layout()
    plt.show()

elif trend_choice == 2:
# Let the user select a currency
        print("\nWhich currency would you like to analyse?")
        print("1. Euro (EUR)")
        print("2. Australian Dollar (AUD)")
        print("3. Japanese Yen (JPY)")
        print("4. US Dollar (USD)")

        currency_choice = input("Enter your choice (1-4): ")

        # Match the choice to the correct CSV column
        currencies = {
            "1": ("EUR - GBP", "Euro (EUR)"),
            "2": ("AUD - GBP", "Australian Dollar (AUD)"),
            "3": ("JPY - GBP", "Japanese Yen (JPY)"),
            "4": ("USD - GBP", "US Dollar (USD)")
        }

        if currency_choice in currencies:
            column, currency_name = currencies[currency_choice]

            # Convert the dates and sort them
            df["Date"] = pd.to_datetime(
                df["Date"], dayfirst=True, format="mixed"
            )
            df = df.sort_values("Date")

            # Plot the selected currency
            plt.figure(figsize=(10, 6))
            plt.plot(df["Date"], df[column])

            plt.title(
                "Value of " + currency_name + " Over Time"
            )
            plt.xlabel("Date")
            plt.ylabel("Value in GBP")
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

            # Compare the first and last values
            first_value = df[column].iloc[0]
            last_value = df[column].iloc[-1]

            if last_value > first_value:
                print(currency_name, "increased in value against GBP.")
            elif last_value < first_value:
                print(currency_name, "decreased in value against GBP.")
            else:
                print(currency_name, "remained at the same value.")

        else:
            print("Invalid choice. Please select a number from 1 to 4.")

elif trend_choice == 3:
    # Let the user select a currency
        print("\nWhich currency would you like to analyse?")
        print("1. Euro (EUR)")
        print("2. Australian Dollar (AUD)")
        print("3. Japanese Yen (JPY)")
        print("4. US Dollar (USD)")
    
        currency_choice = input("Enter your choice (1-4): ")
    
        currencies = {
            "1": ("EUR - GBP", "Euro (EUR)"),
            "2": ("AUD - GBP", "Australian Dollar (AUD)"),
            "3": ("JPY - GBP", "Japanese Yen (JPY)"),
            "4": ("USD - GBP", "US Dollar (USD)")
        }
    
        if currency_choice in currencies:
            column, currency_name = currencies[currency_choice]
    
            # Convert and sort the dates
            df["Date"] = pd.to_datetime(
                df["Date"], dayfirst=True, format="mixed"
            )
            df = df.sort_values("Date").reset_index(drop=True)
    
            # Ask the user to select a date
            date_input = input(
                "Enter the date (DD/MM/YYYY): "
            )
    
            selected_date = pd.to_datetime(
                date_input, dayfirst=True, errors="coerce"
            )
    
            if pd.isna(selected_date):
                print("Invalid date format. Please use DD/MM/YYYY.")
    
            else:
                # Find the selected date in the CSV
                matching_rows = df[
                    df["Date"].dt.date == selected_date.date()
                ]
    
                if matching_rows.empty:
                    print("No exchange-rate data found for that date.")
    
                else:
                    # Get the selected day's rate
                    day_index = matching_rows.index[0]
                    current_value = df.loc[day_index, column]
    
                    # Check whether a previous available day exists
                    if day_index == 0:
                        print(
                            "There is no previous available day "
                            "to compare with."
                        )
    
                    else:
                        previous_value = df.loc[
                            day_index - 1, column
                        ]
    
                        # Calculate the change
                        difference = current_value - previous_value
                        percentage_change = (
                            difference / previous_value
                        ) * 100
    
                        print("\nCurrency performance on",
                              selected_date.strftime("%d/%m/%Y"))
                        print("Currency:", currency_name)
                        print("Previous rate:", previous_value)
                        print("Selected day's rate:", current_value)
                        print("Percentage change:",
                              round(percentage_change, 2), "%")
    
                        # Identify the trend
                        if current_value > previous_value:
                            print(
                                currency_name,
                                "increased in value against GBP."
                            )
                        elif current_value < previous_value:
                            print(
                                currency_name,
                                "decreased in value against GBP."
                            )
                        else:
                            print(
                                currency_name,
                                "remained at the same value."
                            )
    
        else:
            print("Invalid choice. Please select a number from 1 to 4.")
    
sys.exit(0)

#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_RBSX_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate

conversion_rate = get_conversion_rate()


#Accepts and validates user input for the amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the amount you wish to convert")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  

conversion_amount = float(get_amount_to_convert())

#Performs the conversion and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will receive {} in {}'.format(amount_recieved, currency[6:9]))
    
perfom_conversion()
