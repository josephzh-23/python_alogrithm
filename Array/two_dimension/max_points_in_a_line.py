''''
Greatest common divisor here

GCD of 10 and 15 is 5 here


We find the gcd between each point with a double for loop
2. If the gcd has been seen before add to map if not keep increasing?
3. Check the max # of times for a particular gcp here



'''
from collections import Counter


# an important function here
class Solution:
    def maxPoints(self, points):
        """
        Calculates the maximum number of points that lie on a straight line.

        :param points: A list of point coordinates [x, y].
        :type points: List[List[int]]
        :return: The maximum number of points on a straight line.
        :rtype: int
        """

        def calculate_gcd(a, b):
            return a if b == 0 else calculate_gcd(b, a % b)

        num_points = len(points)
        max_points_on_line = 1  # A single point is always on a line.

        for i in range(num_points):
            x1, y1 = points[i]
            slopes = Counter()  # Counter to track the number of points for each slope
            for j in range(i + 1, num_points):
                x2, y2 = points[j]
                delta_x = x2 - x1
                delta_y = y2 - y1
                gcd_value = calculate_gcd(delta_x, delta_y)

                # Reduce the slope to its simplest form to count all equivalent slopes together.
                slope = (delta_x // gcd_value, delta_y // gcd_value)

                # Increment the count for this slope and update the maximum if needed.
                slopes[slope] += 1
                max_points_on_line = max(max_points_on_line, slopes[slope] + 1)

        return max_points_on_line
