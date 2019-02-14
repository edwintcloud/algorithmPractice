# Stock Prices
Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:
```python
stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)
```
No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.

## Gotchas
You can't just take the difference between the highest price and the lowest price, because the highest price might come before the lowest price. And you have to buy before you can sell.

What if the price goes down all day? In that case, the best profit will be negative.

You can do this in O(n) time and O(1) space!

## Breakdown
To start, try writing an example value for stock_prices and finding the maximum profit "by hand." What's your process for figuring out the maximum profit?

The brute force approach would be to try every pair of times (treating the earlier time as the buy time and the later time as the sell time) and see which one is higher.
```python
  def get_max_profit(stock_prices):
    max_profit = 0

    # Go through every time
    for outer_time in xrange(len(stock_prices)):

        # For every time, go through every other time
        for inner_time in xrange(len(stock_prices)):
            # For each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # And use those to find the earlier and later prices
            earlier_price = stock_prices[earlier_time]
            later_price   = stock_prices[later_time]

            # See what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # Update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit
```
But that will take O(n^2) time, since we have two nested loops—for every time, we're going through every other time. Also, it's not correct: we won't ever report a negative profit! Can we do better?

Well, we’re doing a lot of extra work. We’re looking at every pair twice. We know we have to buy before we sell, so in our inner for loop we could just look at every price after the price in our outer for loop.

That could look like this:
```python
  def get_max_profit(stock_prices):
    max_profit = 0

    # Go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(stock_prices):

        # And go through all the LATER prices
        for later_time in xrange(earlier_time + 1, len(stock_prices)):
            later_price = stock_prices[later_time]

            # See what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # Update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit
```
What’s our runtime now?

Well, our outer for loop goes through all the times and prices, but our inner for loop goes through one fewer price each time. So our total number of steps is the sum n + (n - 1) + (n - 2) ... + 2 + 1n+(n−1)+(n−2)...+2+1, which is still O(n^2)time.

We can do better!

If we're going to do better than O(n^2), we're probably going to do it in either O(n log n) or O(n). O(n log n)comes up in sorting and searching algorithms where we're recursively cutting the list in half. It's not obvious that we can save time by cutting the list in half here. Let's first see how well we can do by looping through the list only once.

Since we're trying to loop through the list once, let's use a greedy approach, where we keep a running max_profit until we reach the end. We'll start our max_profit at $0. As we're iterating, how do we know if we've found a new max_profit?

At each iteration, our max_profit is either:

the same as the max_profit at the last time step, or
the max profit we can get by selling at the current_price
How do we know when we have case (2)?

The max profit we can get by selling at the current_price is simply the difference between the current_price and the min_price from earlier in the day. If this difference is greater than the current max_profit, we have a new max_profit.

So for every price, we’ll need to:

keep track of the lowest price we’ve seen so far
see if we can get a better profit
Here’s one possible solution:
```python
  def get_max_profit(stock_prices):
    min_price  = stock_prices[0]
    max_profit = 0

    for current_price in stock_prices:
        # Ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit
```
We’re finding the max profit with one pass and constant space!

Are we done? Let’s think about some edge cases. What if the price stays the same? What if the price goes down all day?

If the price doesn't change, the max possible profit is 0. Our function will correctly return that. So we're good.

But if the value goes down all day, we’re in trouble. Our function would return 0, but there’s no way we could break even if the price always goes down.

How can we handle this?

Well, what are our options? Leaving our function as it is and just returning zero is not a reasonable option—we wouldn't know if our best profit was negative or actually zero, so we'd be losing information. Two reasonable options could be:

return a negative profit. “What’s the least badly we could have done?”
raise an exception. “We should not have purchased stocks yesterday!”
In this case, it’s probably best to go with option (1). The advantages of returning a negative profit are:

We more accurately answer the challenge. If profit is "revenue minus expenses", we’re returning the best we could have done.
It's less opinionated. We'll leave decisions up to our function’s users. It would be easy to wrap our function in a helper function to decide if it’s worth making a purchase.
We allow ourselves to collect better data. It matters if we would have lost money, and it matters how much we would have lost. If we’re trying to get rich, we’ll probably care about those numbers.
How can we adjust our function to return a negative profit if we can only lose money? Initializing max_profit to 0 won’t work...

Well, we started our min_price at the first price, so let’s start our max_profit at the first profit we could get—if we buy at the first time and sell at the second time.
```python
min_price  = stock_prices[0]
max_profit = stock_prices[1] - stock_prices[0]
```
But we have the potential for an index out of bounds error here, if stock_prices has fewer than 2 prices.

We do want to raise an exception in that case, since profit requires buying and selling, which we can't do with less than 2 prices. So, let's explicitly check for this case and handle it:
```python
if len(stock_prices) < 2:
  raise ValueError('Getting a profit requires at least 2 prices')

min_price  = stock_prices[0]
max_profit = stock_prices[1] - stock_prices[0]
```
Ok, does that work?

No! max_profit is still always 0. What’s happening?

If the price always goes down, min_price is always set to the current_price. So current_price - min_price comes out to 0, which of course will always be greater than a negative profit.

When we’re calculating the max_profit, we need to make sure we never have a case where we try both buying and selling stocks at the current_price.

To make sure we’re always buying at an earlier price, never the current_price, let’s switch the order around so we calculate max_profit before we update min_price.

We'll also need to pay special attention to time 0. Make sure we don't try to buy and sell at time 0.

Solution
We’ll greedily ↴ walk through the list to track the max profit and lowest price so far.

For every price, we check if:

we can get a better profit by buying at min_price and selling at the current_price
we have a new min_price
To start, we initialize:

min_price as the first price of the day
max_profit as the first profit we could get
We decided to return a negative profit if the price decreases all day and we can't make any money. We could have raised an exception instead, but returning the negative profit is cleaner, makes our function less opinionated, and ensures we don't lose information.
```python
  def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit
```
Complexity
O(n) time and O(1) space. We only loop through the list once.

What We Learned
This one's a good example of the greedy ↴ approach in action. Greedy approaches are great because they're fast (usually just one pass through the input). But they don't work for every problem.

How do you know if a problem will lend itself to a greedy approach? Best bet is to try it out and see if it works. Trying out a greedy approach should be one of the first ways you try to break down a new question.

To try it on a new problem, start by asking yourself:

"Suppose we could come up with the answer in one pass through the input, by simply updating the 'best answer so far' as we went. What additional values would we need to keep updated as we looked at each item in our input, in order to be able to update the 'best answer so far' in constant time?"

In this case:

The "best answer so far" is, of course, the max profit that we can get based on the prices we've seen so far.

The "additional value" is the minimum price we've seen so far. If we keep that updated, we can use it to calculate the new max profit so far in constant time. The max profit is the larger of:
1. The previous max profit
2. The max profit we can get by selling now (the current price minus the minimum price seen so far)
```
Note: This question and solution was found on interviewcake.com
```