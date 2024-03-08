package Recursion.recursion_with_return

fun main(args: Array<String>) {
    val arr = intArrayOf(2, 3, 1, 4, 4, 5)
    //        System.out.println(find(arr, 4, 0));
//        System.out.println(findIndex(arr, 4, 0));
//        System.out.println(findIndexLast(arr, 4, arr.length-1));
//        findAllIndex(arr, 4, 0);
//        System.out.println(list);

        var list = ArrayList<Int>()
    var ans = findAllIndex(arr, 4, 0, list)
    System.out.println(ans)
//        System.out.println(list);
//    System.out.println(findAllIndex2(arr, 4, 0))
}
fun findAllIndex(arr: IntArray, target: Int, index: Int, list: ArrayList<Int>): ArrayList<Int> {
    if (index == arr.size) {
        return list
    }
    if (arr[index] == target) {
        list.add(index)
    }
    return findAllIndex(arr, target, index + 1, list)
}