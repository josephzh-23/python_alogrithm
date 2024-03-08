package Stacks_Queue

import java.util.*

// https://leetcode.com/problems/simplify-path/description/
// Will then do this problem next here
fun simplifyPath(path: String): String {

    var s = Stack<String>()
    var res = StringBuilder()

    var p = path.split("/")
    // If we see a .. we pop from the name here
    // if see a name, we push into it
    for (i in 0 until p.size) {
        if (!s.isEmpty() && p[i].equals("..")) s.pop()
        else if (!p[i].equals("") && !p[i].equals(".")
            && !p[i].equals("..")
        ) {
            s.push(p[i])
        }
    }

    if (s.isEmpty()) return "/"
    while (!s.isEmpty()) {
        res.insert(0, s.pop()).insert(0, "/")
    }
    return res.toString()
}