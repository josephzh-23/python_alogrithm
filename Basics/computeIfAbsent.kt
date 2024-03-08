package Util


object GFG2 {
    // Main method
    @JvmStatic
    fun main(args: Array<String>) {

        // create a HashMap and add some values
        val map = HashMap<String, Int>()
        map["key1"] = 10000
        map["key2"] = 55000
        map["key3"] = 44300
        map["key4"] = 53200

        // print map details
        println("""HashMap:
 $map""")

        // provide value for new key which is absent
        // using computeIfAbsent method
        map.computeIfAbsent("key5"
        ) { k: String? -> 2000 + 33000 }
        map.computeIfAbsent("key5"
        ) { k: String? -> 2000 + 33000 }
        map.computeIfAbsent("key6"
        ) { k: String? -> 2000 * 34 }

        // print new mapping
        println("""New HashMap:
 $map""")
    }
}