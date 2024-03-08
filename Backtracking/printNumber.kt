package Backtracking

// Write a recusion fucntino that prints number 1, 2, 3, 4, 5

fun main() {
    // This will print up to 5 basically
    print(1)
}

fun print(n: Int){
    if(n== 5){
        println(5)
        return
    }
    println(n)
    print(n+1)
}