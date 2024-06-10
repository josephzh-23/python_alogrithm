

'''
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.


1. Init no files or directories upon installation first here

2. Use a trie in this problem here
- every node : has a trie system here

3. Files as terminal nodes

Files are represented as terminal nodes (end nodes) in the Trie with an isFile flag and contain content.


3. The insert funciton

    - takes in a file or a path, and a bool isFile (check if the path
    - splits file into paths here

    - If file insertion, set file to true here and then insert here


4. The search fucntion: the ls() function


5. Mkdir:
    mkdir calls the insert method to create directories.
    It simply calls the insert(<path>, isFile)      here this is smart here
     which instructs it to only create directories along the path if they don't exist.

6. addContentToFile:
    - user insert method to find existing file here,
    - or create a new file



5. readContentFrom a file
    - use search to get node here
    - return concatenated file here

'''
from typing import List


class TrieNode:
    def __init__(self):
        # Initialize a Trie node with the appropriate attributes
        self.name = None
        self.is_file = False
        self.content = []
        self.children = {}

    def insert(self, path: str, is_file: bool) -> 'TrieNode':
        # Insert a path into the Trie and return the final node
        node = self

        # a path here is "a/b/c" here
        # node.children will have certain parts here
        parts = path.split('/')
        for part in parts[1:]:  # Skip empty root part
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.is_file = is_file
        if is_file:
            node.name = parts[-1]
        return node


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        # List directory or file
        node = self.root.search(path)
        if node is None:
            return []
        if node.is_file:
            # If it's a file, return a list with its name
            return [node.name]
        # If it's a directory, return the sorted list of children's names
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        # Create a directory given a path
        self.root.insert(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        # Add content to a file, creating the file if it doesn't exist
        node = self.root.insert(filePath, True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        # Read content from a file
        node = self.root.search(filePath)
        if node is None or not node.is_file:
            raise FileNotFoundError(f"File not found: {filePath}")
        return ''.join(node.content)




