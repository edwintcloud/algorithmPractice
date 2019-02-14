class NXT:

    def __init__(self, time):
        '''
        @param time: 
                    input time string of format "00:00"'''
        self.memo = []
        self.time = time

    def next_closest_time(self):
        '''
        @return:
                    next closest time formed from the input time digits'''
        # strip : out of time
        self.time = self.time.replace(":", "")

        # get posible valid permutations of digits
        perms = self.get_permutations()

        # initialize result to min time in perms
        result = min(perms)

        # construct a list of any perms greater than time
        gt = [i for i in perms if i > int(self.time)]

        # if there are times greater than time, update result
        # to min perm that is greater than time
        if len(gt) > 0:
            result = min(gt)

        # convert result to string so we can format it
        result = str(result)

        # return closest time formatted properly
        return "{}:{}".format(result[:2], result[2:])

    def get_permutations(self, perm=""):
        '''get_permutations recursively generates valid time permutations from time'''

        # if permutation is a 4 digit invalid time, return
        if len(perm) == 4 and (int(perm) >= 2400 or int(perm[2:]) >= 60):
            return self.memo

        # once permutation reaches 4 digits, append the
        # permutation to list of permutations and return
        if len(perm) == 4:
            self.memo.append(int(perm))
            return self.memo

        # otherwise recursively build the permutation digit by digit
        for i in range(4):
            self.get_permutations(perm+self.time[i])

        # return the list of permutations when we are done
        return self.memo


## TEST ##
tests = [
    "19:34",
    "23:59",
    "14:46",
    "11:11",
    "18:12"
]
for time in tests:
    print("Time:", time)
    nxt = NXT(time)
    print("Next Closest Time:", nxt.next_closest_time())
