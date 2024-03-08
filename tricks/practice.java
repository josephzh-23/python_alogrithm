package tricks;

import java.util.Arrays;

public class practice {

    public static void main(String[] args) {
        String arr[];    //declaring array
        arr = new String[]{"joseph", "jose", "ee"};
        Arrays.sort(arr, (a, b)->Integer.compare(a.length(), b.length()));

    }
}
