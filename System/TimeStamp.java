package System;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Time: set - O(1)  get - log(n)   (binary search)
// space: set - o(n)    get - O(1)
public class TimeStamp {

    private Map<String, List<Data>> map;

    // init the data structure here
    public TimeStamp(){
        map = new HashMap<>();
    }
    public void set(String key, String value, int timestamp){
        if(!map.containsKey(key)) map.put(key, new ArrayList<>());
        map.get(key).add(new Data(value, timestamp));
    }

    public String get(String key, int timestamp){
        if(!map.containsKey(key)) return "";
        List<Data> data = map.get(key);
        return findClosestValue(data, timestamp);
    }

    private String findClosestValue(List<Data> data, int timestamp){
        int l = 0, r = data.size() -1;
        while(l < r){
            int mid = (l + r + 1)/2;
            // if the one in the middle time stamp smaller then
            // move bottom to higher
            if(data.get(mid).timestamp <= timestamp) l = mid;
            else r = mid- 1;
        }
        Data closestData = data.get(l);
        return closestData.timestamp > timestamp ? "": closestData.value;
    }

    class Data{
        String value;
        int timestamp;
        public Data(String value, int timestamp){
            this.value = value;
            this.timestamp= timestamp;
        }
    }
}
