package Numbers.Basics

import January_3rd.Main.power

// THis is just a concept doesn't actually work please see the oter oen
// mutiplying strings here
fun main(){
    var ans = "1234"
    var carry = 0

    /*
    Basically what we are doing here is quite simple, if we have
    123
  * 456
  we actually get

  The question here
  (123 * (6 + 50 + 400))
 -> 123 * 6 + 123 * 50 + 123 * 400

 = (first # * jth digit of second number * 10 ^(index of j coming from the
 end)

     */

    var zero = '0'.code
    var sum = 0
    var j = 0
    var totalSum  = 0
    for(i in ans.toCharArray().reversed()){
        var b = '4'- '0'
        var a = i - '0'
         sum = a * b  * power(10, j)+ carry
        carry = a * b/10
        println("sum is $sum and carry is $carry")
        j++
        totalSum+= sum
    }
    println(totalSum)
}