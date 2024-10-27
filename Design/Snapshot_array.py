'''

A very interesting problem here

The array is of a given legnth here and then set to 0 here


To solve this problem, we need a way to efficiently record the changes to each element of the
array over time—this is done so th
at we can later query the value of an element as it was at any snapshot point.

'''
from bisect import bisect_right
from cmath import inf
from collections import defaultdict


class SnapshotArray:
    def __init__(self, length: int):
        # Initialize an index counter for snapshots and a default dictionary
        # to store values with their corresponding snapshot indices.
        self.snapshot_index = 0
        self.array_data = defaultdict(list)

    '''
    
    The logic behind here 
    1. we append a tuple to the list at that index containing the current snap_id and the new value. This way, 
    we are effectively recording a timeline of values for each index.
    
    '''

    def set(self, index: int, val: int) -> None:
        """
        Set the value at a particular index to the specified value
        within the latest snapshot.
        """
        # Append the current snapshot index and val to the list at the given index.
        self.array_data[index].append((self.snapshot_index, val))

    '''
    Increment the snap id used to track the snapshots and return the previous id here 
    
    '''

    def snap(self) -> int:
        """
        Take a snapshot of the array, incrementing the snapshot index.
        """
        # Increment the snapshot index and return the ID of the snapshot taken.
        self.snapshot_index += 1
        return self.snapshot_index - 1


    '''
        o retrieve a value from a past snapshot, we use binary search (bisect_right) to find the first tuple where the snap_id is greater than the requested snap_id. We then take the previous tuple as it will have the value of the array at the time of the snapshot. If there is no such tuple (i.e., if the index was never set before the snap_id), we return 0.
    '''
    def get(self, index: int, snap_id: int) -> int:
        """
        Get the value at the specified index at the time of the given snapshot.
        """
        # Retrieve the list of value-snapshot index pairs for the given index.
        value_snapshots = self.array_data[index]
        # Find the rightmost value such that it's snapshot index is less than or equal to snap_id.
        i = bisect_right(value_snapshots, (snap_id, inf)) - 1
        # Return 0 if no such index is found, otherwise return the value at that index.
        return 0 if i < 0 else value_snapshots[i][1]
