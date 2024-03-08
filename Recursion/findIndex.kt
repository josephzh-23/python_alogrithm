package Recursion

fun main(args: Array<String>) {
    val arr = intArrayOf(2, 3, 1, 4, 4, 5)
    //        System.out.println(find(arr, 4, 0));
//        System.out.println(findIndex(arr, 4, 0));
//        System.out.println(findIndexLast(arr, 4, arr.length-1));
//        findAllIndex(arr, 4, 0);
//        System.out.println(list);

//        ArrayList<Integer> list = new ArrayList<>();
//        ArrayList<Integer> ans = findAllIndex(arr, 4, 0, list);
//        System.out.println(ans);
//        System.out.println(list);
//    System.out.println(findAllIndex2(arr, 4, 0))
}
fun findIndex(arr: IntArray, target: Int, index: Int): Int {
    if (index == arr.size) {
        return -1
    }
    if (arr[index] == target) {
        return index
    } else {
        return findIndex(arr, target, index + 1)
    }
}