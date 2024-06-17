'''
Think about how to solve this question right here


'''
from Heap.max_heap import MinHeap

# ladders allow us to know how many are avaialble here this is also very important here
def furthestBuilding(heights, bricks, ladders):

# A priority queue (min heap) to store the heights that we have used ladders for
# used only for the ladders here
    hp = MinHeap()


    for i in range(len(heights) - 1):
        current_height = heights[i]
        next_height = heights[i + 1]
        # Calculate the height difference between the current building and the next one.
        height_diff = next_height - current_height

        # Only if the next building is higher than the current one do we need ladders or bricks
        if height_diff > 0:
            # We use a ladder and add the height difference to the heap.
            # heappush(height_diffs_heap, height_diff)
            hp.push(height_diff)

            # If we have used more ladders than available, we must replace one ladder with bricks.
            if len(hp) > ladders:
                bricks -= hp.pop()  # Replace the ladder for the smallest height diff.

                # If at any point we do not have enough bricks, we cannot move to the next building.
                if bricks < 0:
                    return i

    # and this is the answer here
    # If we can climb all the buildings with the given bricks and ladders, return the last building index.
    return len(heights) - 1