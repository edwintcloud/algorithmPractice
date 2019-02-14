def get_max_profit(prices):
    if len(prices) < 2:
        return None

    # set min_price to first price and max_profit to second price - first price
    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for i in range(1, len(prices)):
        
        # get the potential profit of subtracting current price from min_price
        profit = prices[i] - min_price

        # if potential profit is higher than max profit, set max profit to potential profit
        if profit > max_profit:
            max_profit = profit

        # if current price is less than min price, set min price to current price
        if prices[i] < min_price:
            min_price = prices[i]
    
    # return the max profit
    return max_profit

# test function
stock_prices = [10, 7, 5, 8, 11, 9]
result = get_max_profit(stock_prices)
print("Prices: ", stock_prices)
print("Max Profit: ", result)