package Binary_search

/*
Use the binary search + the custom object here
what you are trying to return is a time such that

timeStamp_prev <= timeStamp as said
 */

fun main() {
    var timeStamp = TimeMap()
    timeStamp.set("foo", "bar", 1)
    timeStamp.get("foo", 1)
    print(timeStamp.get("foo", 3))
}

class TimeMap {
    class TimeValue(var time: Int, var value: String)
    var map = mutableMapOf<String, MutableList<TimeValue>>()

    operator fun set(key: String, value: String, timestamp: Int) {
        if (!map.containsKey(key)) {
            map.put(key, ArrayList<TimeValue>())
        }
        val list = map.get(key)
        list!!.add(TimeValue(timestamp, value))
    }

    fun get(key: String, timeStamp: Int): String {

        if (!map.containsKey(key)) return ""

        var list = map[key]
        var (left, right) = intArrayOf(0, list!!.size - 1)

        // A left and rgith pointer
        while (left + 1 < right) {
            var mid = (left + right) / 2
            val midTimeValue = list[mid]
            if (midTimeValue.time == timeStamp) {
                return midTimeValue.value

                // Search in the right
            } else if (midTimeValue.time < timeStamp) {
                left = mid // Search in the left here
            } else {
                right = mid
            }
        }

        /*
    THis is for if the left pointer < the right pointer here
    The reason we check the right first is b/c we want to find the
    largest right value that's greater
    and then we check the left here
     */ //
        if (list[right].time <= timeStamp) {
            return list[right].value
        } else if (list[left].time <= timeStamp) {
            return list[left].value
        } else {
            return ""
        }
    }
}