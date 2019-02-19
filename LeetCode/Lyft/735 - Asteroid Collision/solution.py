def asteroid_collision(asteroids):

    # initialize an empty list we will use as a stack
    stack = []

    # iterate through the list of asteroids
    for asteroid in asteroids:

        # while there are asteroids in the stack and 
        # the current asteroid is less than 0 and 
        # the top item (last appended item) is greater
        # than 0, loop
        while stack and asteroid < 0 < stack[-1]:

            # if the absolute value of the current asteroid is less
            # than the top item in the stack break from the loop.
            # OR pop the top item from the stack and break if the 
            # absolute value of the current asteroid is equal to the
            # item popped, otherwise continue the loop
            if abs(asteroid) < stack[-1] or abs(asteroid) == stack.pop():
                break

        # otherwise add the asteroid to the top
        # of the stack
        else:
            stack.append(asteroid)

    # return stack which will contain asteroids
    # that haven't collided
    return stack