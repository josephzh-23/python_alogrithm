
'''

Let’s say you want to check if a substring of size k appears multiple times in a large string. Recomputing a full hash for every substring would be slow.

A rolling hash speeds this up by:
	•	Using the previous hash
	•	Removing the effect of the first character
	•	Adding the next character

This way, each hash can be computed in O(1) time after the first one


Can be used to detect duplicate substrings effciiently here

2. Check out website_requests in amazon
'''