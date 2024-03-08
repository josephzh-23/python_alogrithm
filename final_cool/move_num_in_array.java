package final_cool;

// O(n) solutino better then O(logn)
public class move_num_in_array {

    private static int[] moveZerosToLeft(int[] arr){
        int f = 0;
        int l = arr.length -1;

        int newArr[] = new int[arr.length];

        for(int i =0; i < arr.length; i++){
            if (arr[i] == 0) {
                newArr[l--] = arr[i];
            }else{
                newArr[f++] = arr[i];
            }
        }
        return newArr;
    }

}
