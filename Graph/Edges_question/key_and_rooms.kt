package Graph.Basics

import java.util.*


fun main() {

    var arr = listOf(listOf(1), listOf(2), listOf(3), listOf())

    canVisitAllRooms2(arr)
}
fun canVisitAllRooms2(rooms: List<List<Int>>): Boolean {
    val seen = BooleanArray(rooms.size)
    seen[0] = true
    val stack: Stack<Int> = Stack()
    stack.push(0)

    //At the beginning, we have a todo list "stack" of keys to use.
    //'seen' represents at some point we have entered this room.
    while (!stack.isEmpty()) { // While we have keys...
        val node = stack.pop() // Get the next key 'node'

        // Here is a little different
        for (nei in rooms[node])  // For every key in room # 'node'...
            if (!seen[nei]) { // ...that hasn't been used yet
                seen[nei] = true // mark that we've entered the room
                stack.push(nei) // add the key to the todo list
            }
    }
    for (v in seen)  // Everything should have bene visited already if not then
        // sth would be returned here
        if (!v) return false
    return true
}