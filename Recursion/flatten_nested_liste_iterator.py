'''

Using this you get the following here

Appraoch 1: Using recursion


define function flattenList(nestedList):
    for nestedInteger in nestedList:
        if nestedInteger.isInteger():
            append nestedInteger.getInteger() to integers
        else:
            recursively call flattenList on nestedInteger.getList()
'''

'''
O(n)
O(n + L)

'''
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self._integers.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList())

        self._integers = []

        # use this to keep track of the pointer here
        self._position = -1  # Pointer to previous returned.
        flatten_list(nestedList)

    def next(self) -> int:
        self._position += 1
        return self._integers[self._position]

    def hasNext(self) -> bool:
        return self._position + 1 < len(self._integers)



