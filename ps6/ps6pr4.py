# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
# Computer Science 111
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
# Partner: None

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print("(3) Find the average price")
    print("(4) Find the max price and its day")
    print("(5) Find the min single-day change and its day")
    print("(6) Test a threshold")
    print("(7) Your investment plan")
    print('(8) Quit')


def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list


def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])


def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(prices):
    """takes a list of 1 or more prices and
    computes and returns the average price"""

    sum_lst = 0
    for price in prices:
        sum_lst += price

    avg = sum_lst / len(prices)
    return avg


def max_day(prices):
    """takes a list of 1 or more prices and computes and
    returns the day (i.e., the index) of the maximum price"""

    curr_index = 0
    curr_num = 0

    for i in range(len(prices)):
        if prices[i] > curr_num:
            curr_num = prices[i]
            curr_index = i

    return curr_index


def min_change_day(prices):
    """takes a list of 2 or more prices and computes and returns the
    day (i.e., the index) of the minimum single-day absolute change in price"""

    lst_changes = []

    for i in range(len(prices)):
        if i + 1 < len(prices):
            lst_changes += [abs(prices[i] - prices[i + 1])]
        else:
            break

    curr_index = 0
    curr_diff = 0

    for i in range(len(lst_changes)):
        if i + 1 < len(lst_changes):
            if lst_changes[i] > lst_changes[i + 1]:
                curr_diff = lst_changes[i+1]
                curr_index = i + 1
        else:
            break

    return curr_index + 1


def any_above(prices, num):
    """takes a list of 1 or more prices and an integer threshold, and uses a loop
    to determine if there are any prices above that threshold. The function should
    return True if there are any prices above the threshold, and False otherwise"""

    for i in range(len(prices)):
        if num < prices[i]:
            return True

    return False


def find_tts(prices):
    """takes a list of 2 or more prices, and that uses one or more loops to find the best days
    on which to buy and sell the stock whose prices are given in the list of prices. The buy and
    sell days that you determine should maximize the profit earned, but the sell day must be
    greater than the buy day. The function should return a list containing three integers"""

    highest_price = prices[max_day(prices)]
    lowest_price = prices[0]
    buy_day = 0

    for i in range(len(prices)):
        if i + 1 < len(prices):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
                buy_day = i
        else:
            break

    new_price_lst = []
    for i in prices[buy_day:]:
        new_price_lst += [i]

    buy_price = new_price_lst[0]
    sell_price = buy_price
    sell_index = 0

    for i in range(len(new_price_lst)):
        if new_price_lst[i] > sell_price:
            sell_price = new_price_lst[i]
            sell_index = i

    sell_day = buy_day + sell_index
    profit = prices[sell_day] - prices[buy_day]

    return [buy_day, sell_day, profit]



def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            print(f"The average price is {avg_price(prices)}")
        elif choice == 4:
            print(f"The max price is {prices[max_day(prices)]} on day {max_day(prices)}")
        elif choice == 5:
            print(f"The min single-day occurs on day {min_change_day(prices)}\nwhen the price goes from "
                  f"{prices[min_change_day(prices)-1]} to {prices[min_change_day(prices)]}")
        elif choice == 6:
            threshold_price = int(input("Enter the threshold: "))
            result = any_above(prices, threshold_price)
            if result == True:
                print(f"There is at least one price above {threshold_price}")
            elif result == False:
                print(f"There are no prices above {threshold_price}")
        elif choice == 7:
            results = find_tts(prices)
            print(f"Buy on day {results[0]} at price {prices[results[0]]}\n"
                  f"Sell on day {results[1]} at price {prices[results[1]]}\nTotal profit: {results[2]}")
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')


tts()
