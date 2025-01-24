class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Length of the version strings
        len_version1, len_version2 = len(version1), len(version2)

        # Initialize pointers for each version string
        pointer1 = pointer2 = 0

        # Loop until the end of the longest version string is reached
        while pointer1 < len_version1 or pointer2 < len_version2:
            # Initialize numeric values of the current version parts
            num1 = num2 = 0

            # Parse the version number from version1 until a dot is found or end is reached
            while pointer1 < len_version1 and version1[pointer1] != '.':
                num1 = num1 * 10 + int(version1[pointer1])
                pointer1 += 1

            # Parse the version number from version2 until a dot is found or end is reached
            while pointer2 < len_version2 and version2[pointer2] != '.':
                num2 = num2 * 10 + int(version2[pointer2])
                pointer2 += 1

            # Compare the parsed numbers
            if num1 != num2:
                # If they are not equal, determine which one is larger and return -1 or 1 accordingly
                return -1 if num1 < num2 else 1

            # Move past the dot for the next iteration
            pointer1, pointer2 = pointer1 + 1, pointer2 + 1

        # If no differences were found, the versions are equal
        return 0