package String;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/*
The window size here would be n - k + 1
 */
public class DistinctElements {

    public static List<Integer> distinctElements(int[] arr, int k) {
        List<Integer> results = new ArrayList<>();
        Map<Integer, Integer> elemCountMap = new HashMap<>();

        int len = arr.length;

        // Create a first window nad put all the elements and its count of this window
        // in a hashmap here
        for (int j = 0; j < k; j++) {
            elemCountMap.put(arr[j], elemCountMap.getOrDefault(arr[j], 0) + 1);
        }

        results.add(elemCountMap.size());

        for (int j = 1; j <= len - k; j++) {

            int removeElem = arr[j - 1];
            int addElem = arr[j + k - 1];

            // remove elem from the map
            removeElemFromMap(elemCountMap, removeElem);

            // Add elem from the map here
            elemCountMap.put(addElem, elemCountMap.getOrDefault(addElem, 0) + 1);

            results.add(elemCountMap.size());
        }
        return results;
    }


    // Either decrease the count by 1 or remove completely here
    private static void removeElemFromMap(Map<Integer, Integer> elemCountMap, int elem) {

        Integer count = elemCountMap.get(elem);
        if (count != null && count > 1) {
            elemCountMap.put(elem, count - 1);
        } else {
            elemCountMap.remove(elem);
        }

    }
}
