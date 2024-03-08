package final_cool
// To sort this here
fun sortColors(arr: IntArray){
    // #1 to do
    var l = 0
    var cur = 0
    var r = arr.size -1

    while(cur <=r){
        // Then swap
        if(arr[cur]==0){
//            swap(arr, l, r)
            l++
            cur+=1


        }else if(arr[cur] ==2){
//            swap(arr, l, r)
            r-=1

        }else{
            cur+=1
        }
    }
}











