
'''



Host name is url.split("/")[2]  here
'''
import collections

# def getHostName(url):

'''

Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
getUrl() : grabs all the urls for a given host name basically 

Then the expression is then O(m * l) here very good 

l = the orl length here and then x = this is one of these here 
'''
class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """

def getHostName(url):
    return url.split('/')[2]


def crawl(startUrl, htmlParser):
    visited = set()
    startHostName = getHostName(startUrl)
    def dfs(url, htmlParser):
        visited.add(url)

        for nextUrl in htmlParser.getUrl(url):
            if getHostName(nextUrl) == startHostName and nextUrl not in visited:
                dfs(nextUrl, htmlParser)


    dfs(startUrl, htmlParser)
    return visited