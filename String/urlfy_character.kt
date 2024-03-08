package String

// The true length can be 13 in this case here
fun main() {

    var str = "Mr John Smith"
    val ch = CharArray(str.length)

    // Copying character by character into array
    // using for each loop

    // Copying character by character into array
    // using for each loop
    for (i in 0 until str.length) {
        ch[i] = str[i]
    }

    for(c in ch){
        print(c)
    }

}
fun solution(str: CharArray, trueLength: Int){

    // Basically with the true length then we can insert from the back
    // So here we need 2 extra characters for each space
    // %20 2 character longer than than ' ', so double this count right here
    //
    var (spaceCount, index, i) = intArrayOf(0)


    // This finds you the space ocunt here
    while (i < trueLength) {
        if (str[i] === ' ') {
            spaceCount++
        }
        i++
    }

    // %20 is 2 characters longer than ' '
    if(trueLength < str.size){
        str[trueLength] = '\\'
    }
}