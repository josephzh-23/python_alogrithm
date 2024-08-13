
class CodeC:

    # and then added

    def __init__(s):
        s.encodeMap = {}
        s.decodeMap = {}
        s.base = "http://tinyUrl.com"

        #and this is the minimum here
        # this is the macos mode
        # and then using the code here we have a much better chance of success
    # and then that's it here 
    def encodeUrl(s, longUrl):

        # and here is the solutino that you rpobably wanted
        # and then here the code becomes
        # check if this is in the map or not very important here
        if longUrl not in s.encodeMap:
            shortUrl = s.base + str(len(s.encodeMap) + 1)



            # and then here we have the code
            s.encodeMap[longUrl] = shortUrl
            s.decodeMap[shortUrl] = longUrl

        return s.encodeMap[longUrl]


    def decode(s, shortUrl)-> str:
        return s.decodeMap[shortUrl]