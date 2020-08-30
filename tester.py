def hourglassSum(arr):
    counter = 0
    max_num = 0
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            counter = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if i == 0 and j ==0:
                max_num = counter
            if counter >= max_num:
                max_num = counter
    return max_num

if __name__ == "__main__":
    arr = [
        [-1,-1,0,-9,-2,-2],
        [-2,-1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1 ,-9 ,-2 ,-4 ,-4 ,-5],
        [-7 ,-3 ,-3 ,-2 ,-9 ,-9 ],
        [-7 ,-3 ,-3 ,-2 ,-9 ,-9]
    ]
    print(hourglassSum(arr))


# def get_max_profit(stock_prices):
#     #exception case:
#     if stock_prices == None:
#         raise ValueError("The input is empty")
    
#     if stock_prices[0] == max(stock_prices):
#         max_val = max(stock_prices[1:])
#         return max_val - stock_prices[0]


#     last_max_idx = len(stock_prices) - stock_prices[::-1].index(max(stock_prices)) 
#     min_val = min(stock_prices[:last_max_idx-1])
#     return max(stock_prices) - min_val



#   def get_max_profit(stock_prices):
#     if len(stock_prices) < 2:
#         raise ValueError('Getting a profit requires at least 2 prices')

#     # We'll greedily update min_price and max_profit, so we initialize
#     # them to the first price and the first possible profit
#     min_price  = stock_prices[0]
#     max_profit = stock_prices[1] - stock_prices[0]

#     # Start at the second (index 1) time
#     # We can't sell at the first time, since we must buy first,
#     # and we can't buy and sell at the same time!
#     # If we started at index 0, we'd try to buy *and* sell at time 0.
#     # This would give a profit of 0, which is a problem if our
#     # max_profit is supposed to be *negative*--we'd return 0.
#     for current_time in range(1, len(stock_prices)):
#         current_price = stock_prices[current_time]

#         # See what our profit would be if we bought at the
#         # min price and sold at the current price
#         potential_profit = current_price - min_price

#         # Update max_profit if we can do better
#         max_profit = max(max_profit, potential_profit)

#         # Update min_price so it's always
#         # the lowest price we've seen so far
#         min_price  = min(min_price, current_price)

#     return max_profit



# # Tests

# import unittest

# class Test(unittest.TestCase):

#     def test_price_goes_up_then_down(self):
#         actual = get_max_profit([1, 5, 3, 2])
#         expected = 4
#         self.assertEqual(actual, expected)

#     def test_price_goes_down_then_up(self):
#         actual = get_max_profit([7, 2, 8, 9])
#         expected = 7
#         self.assertEqual(actual, expected)

#     def test_price_goes_up_all_day(self):
#         actual = get_max_profit([1, 6, 7, 9])
#         expected = 8
#         self.assertEqual(actual, expected)

#     def test_price_goes_down_all_day(self):
#         actual = get_max_profit([9, 7, 4, 1])
#         expected = -2
#         self.assertEqual(actual, expected)

#     def test_price_stays_the_same_all_day(self):
#         actual = get_max_profit([1, 1, 1, 1])
#         expected = 0
#         self.assertEqual(actual, expected)

#     def test_error_with_empty_prices(self):
#         with self.assertRaises(Exception):
#             get_max_profit([])

#     def test_error_with_one_price(self):
#         with self.assertRaises(Exception):
#             get_max_profit([1])


# unittest.main(verbosity=2)