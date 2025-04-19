'''


The tough part of this problem doing the rmmovel in O(1) time here
Remove()
- might have to shift elements here
After swapping the element to be removed and then the current element here
- no shifting of the elements here

'''
from random import choice


class RandomizedSet:
    def __init__(self):
        self.index_dict = {}  # Mapping of values to their indices in the array
        self.values_list = []  # Dynamic array to hold the values

    def insert(self, val: int) -> bool:
        # Insert the value into the set if it's not already present, returning True if successful
        if val in self.index_dict:
            return False  # Value already exists
        self.index_dict[val] = len(self.values_list)  # Map value to its index in the array
        self.values_list.append(val)  # Add value to the array
        return True  # Insertion successful

    def remove(self, val: int) -> bool:
        # Remove the value from the set if present, returning True if successful
        if val not in self.index_dict:
            return False  # Value does not exist
        index_to_remove = self.index_dict[val]  # Get the index of the value to remove
        last_element = self.values_list[-1]  # Get the last element in the array

        self.values_list[index_to_remove] = last_element  # Move the last element to the 'removed' position
        self.index_dict[last_element] = index_to_remove  # Update the last element's index
        self.values_list.pop()  # Remove the last element
        del self.index_dict[val]  # Remove the value from the dictionary
        return True  # Removal successful

    def getRandom(self) -> int:
        # Return a random value from the set
        # Using the random randomly generates an iteger here
        return choice(self.values_list)  # Randomly select and return a value from the array

# Example usage:
# randomized_set = RandomizedSet()
# param_1 = randomized_set.insert(val)
# param_2 = randomized_set.remove(val)
# param_3 = randomized_set.getRandom()
