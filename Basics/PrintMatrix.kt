package Basics


fun printMatrix(matrix: Array<IntArray>){

    for(i in matrix.indices){
        for(j in matrix[0].indices ){
            println(matrix[i][j])
        }
    }
}