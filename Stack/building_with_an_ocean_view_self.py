



heights = [4,2,3, 1]
def solution(heights):
    st = []
    for (i, c) in enumerate(heights):

        # While stack is not empty AND top of stack is more than the current element
        while st and st[-1][1] < c:
            # Pop the top element from the stack
            st.pop()
        # Push the current element into the stack
        st.append((i, c))

    print(st)

solution(heights)
