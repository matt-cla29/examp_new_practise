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

def trends_menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. trends and patterns for the value of the pound (GBP) compared to other currencies")
        print("2. trends and patterns for the performance (e.g. increase/decrease in value) of a selected currency")
        print("3. trends and patterns for selected day of how a currency performed (e.g. increase/decrease in value) on it")
        print("######################################################")

        
        trends_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(trends_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(trends_choice) < 1 or int(trends_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(trends_choice)  

menu_choice = menu()

if 1 <= int(menu_choice) <= 6:
    currency = get_currency()
elif int(menu_choice) == 7:
    trends_choice = trends_menu()

    # reads the CSV files
    df = pd.read_csv("Task4a_RBSX_data.csv")

    #sort the data by dates
    df = df.sort_values("Date")

    #creates four graphs
    fig, axes = plt.subplots(2, 2, figsize = (12, 8))

if trends_choice == 1:
    #convert the date to datetime format
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    #sort the data by dates
    df = df.sort_values("Date")

    # GBP compared to EUR
    axes[0, 0].plot(df["Date"], df["GBP - EUR"])
    axes[0, 0].set_title["GBP compared to EUR"]
    axes[0, 0].set_ylabel["Euro per pound"]
    plt.show()
elif trends_choice == 2:
    print("choice selected")
elif trends_choice == 3:
    print("choice selected")
else:
    print("choice not avaliable")

sys.exit()

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