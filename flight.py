class Solution(object):
    def corpFlightBookings(self, bookings, n):
        seats = [0] * (n+1)
        for i in bookings: 
            seats[i[0]-1] += i[2]
            seats[i[1]] -= i[2]
        sum = 0
        for i,j in enumerate(seats):
            sum += j
            seats[i] = sum
        seats = seats[:n]
        return seats
      
