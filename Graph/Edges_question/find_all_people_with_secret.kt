import java.util.*
import java.util.stream.Collectors

/*
O( n * log n)
 */
internal class Solution32 {
    // m number of meeting
    // n number of people
    //
    // Time complexity: O(m log(m)) + O(n)
    // Space: O(n) + O(m)
    fun findAllPeople(n: Int, meetings: Array<IntArray>, firstPerson: Int): List<Int> {
        val graph: MutableMap<Int, MutableList<IntArray>> = HashMap(n)
        for (m in meetings) {
            graph.computeIfAbsent(
                m[0]
            ) { ArrayList() }.add(intArrayOf(m[1], m[2]))
            graph.computeIfAbsent(
                m[1]
            ) { ArrayList() }.add(intArrayOf(m[0], m[2]))
        }

        // Stores the person and the time here
        val secretHolder = PriorityQueue { a: IntArray, b: IntArray ->
            a[1].compareTo(b[1])
        }

        /*
        Add 0th person to time 0 and 1st person to time 0 here
         */
        secretHolder.add(intArrayOf(0, 0))
        secretHolder.add(intArrayOf(firstPerson, 0))
        val knownSet: MutableSet<Int> = HashSet()

        while (!secretHolder.isEmpty()) {
            val sh = secretHolder.remove()
            val person1 = sh[0]
            val time1 = sh[1]

            // If not contained already
            if (!knownSet.contains(person1)) {
                for (m in graph.getOrDefault(person1, mutableListOf())) {
                    val person2 = m[0]
                    val time2 = m[1]

                    /*
                    This is the key here besides this nothign else matters here
                     */
                    // meeting with person2 took place after person1 knew the secret
                    // and person2 doesnt know the secret yet
                    if (time2 >= time1 && !knownSet.contains(person2)) {
                        secretHolder.add(intArrayOf(person2, time2))
                    }
                }
            }
        }
        return knownSet.stream().collect(Collectors.toList())
    }
}