import java.util.*

fun main(){

    val list = intArrayOf(3, 6, 5, 9, 4)
    val results = sortZigzagList(list)

    // results.forEach{
    //   println(it)
    // }
}

fun swap(cArray:IntArray, i: Int, j: Int): IntArray{

    // Swap the first one
    var temp = cArray[i]
    cArray[i] = cArray[j]
    cArray[j] = temp
    return cArray

}



fun sortZigzagList(arr: IntArray):IntArray{


    var big  =0
    Arrays.sort(arr)
    big = arr.last()
    for(i in  0 until arr.size-1){


        //

        if(arr[i] >arr[i+1]&& i%2 ==0){
            swap(arr, i , i+1)
        }
        println("$arr[i] , $arr[i+1]")
        // else if (arr[i] < arr[i+1]&& i%2 !=0){
        //   swap(arr, i , i+1)
        // }


    }


    // arr[1] = arr.last
    //   swap(arr, arr.size-1, 1)
    //   for(i in  2 until arr.size-1){

    //   if(arr[i] >arr[i+1]&& i%2 ==0){
    //       swap(arr, i , i+1)
    //   }else if (arr[i] < arr[i+1]&& i%2 !=0){
    //     swap(arr, i , i+1)
    //   }
    //   }

    return arr

}
