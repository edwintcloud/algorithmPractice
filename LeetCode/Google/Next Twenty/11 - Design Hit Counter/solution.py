# For this problem, I think it will be best to use a dictionary maping timestamps to hits.
# The window would be 300 (300 seconds in 5 mins), every hit update or add in the dictionary.
# When getHits is called, we can just sum the values within the window of timestamps.


class HitCounter:

    def __init__(self, window=300):
        self.window = window
        self.hits = {}

    def hit(self, time):

        # if time in hits, increment it
        # otherwise create new entry for time
        # with 1 hit
        if time in self.hits:
            self.hits[time] += 1
        else:
            self.hits[time] = 1

    def getHits(self, time):
        # return hits within time window
        return sum(v for k, v in self.hits.items() if time >= k > time-self.window)

## TEST ##
counter = HitCounter()

# hit at timestamp 1.
counter.hit(1)

# hit at timestamp 2.
counter.hit(2)

# hit at timestamp 3.
counter.hit(3)

# get hits at timestamp 4, should return 3.
print("4:", counter.getHits(4))

# hit at timestamp 300.
counter.hit(300)

# get hits at timestamp 300, should return 4.
print("300:", counter.getHits(300))

# get hits at timestamp 301, should return 3.
print("301:", counter.getHits(301))

## ADDITIONAL TESTING ##
counter.hit(300)
counter.hit(399)
counter.hit(399)
counter.hit(399)
counter.hit(401)
print("500:", counter.getHits(500)) 
print("700:", counter.getHits(700))