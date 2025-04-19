

intervals = [[1, 2],[1, 3] , [1, 4]]

# and then this will become
# start : [1, 1, 1] so this is rule #1 here 
# end: [1, 1, 4]
start = [i[0] for i in intervals]
end = [i[1] for i in intervals]