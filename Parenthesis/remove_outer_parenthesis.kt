package Parenthesis



import java.util.*


/*
1. We push the elements of the
 expression one by one onto the stack until we get a closing bracket )

 2.  Then we pop the elements from the stack one by one and evaluate the expression on-the-go.
  This is done till we find the corresponding ( opening bracket.
 */

fun main() {

    var s = "(()())(())"
    solution(s)
}

fun solution(str: String) {
    var s = Stack<Char>()
    var sb = StringBuilder()

    for(c in str.toCharArray()){
        if(c == '('){
            if(s.size>0){
                sb.append(c)
            }
            s.push(c)
        }

        //with the closing parenthesis
        else{
            s.pop()
            if(s.size> 0){
                sb.append(c)
            }
        }
    }
    println(sb)
}
