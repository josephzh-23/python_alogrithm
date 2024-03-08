
// Using array and list
fun main() {

   val numbers: IntArray = intArrayOf(10, 20, 30, 40, 50)

   // This produces an array of 5 0s basically  and that's it
   val numbers2 = IntArray(5) { 0 }

   val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")
   var initArray = intArrayOf()
    /*

With array you can't change value but can do following
initialize first and then assign value a very good way of doing things

 */
   // Notice this one doesn't have any value will crash
   var array = intArrayOf(4)
   println(array)

   val visited = BooleanArray(2)
   // can also do the above as discussedF
   array[0] =3
   // THis will give exception as said
//   println(array[1])

   // An array initialized should have the following
   var array2= IntArray(3)
   array2.forEach { println(it) }

}