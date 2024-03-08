
import java.util.*


fun main() {
    val capitalCities: HashMap<String, String> = HashMap<String, String>()

    // This is from the network delay example as shown before
    // The following a  { 1: [1, 2] } as discussed      very good for ad
    // adjlist problem      "no interface no constructor error"
    val graph: MutableMap<Int, MutableList<IntArray>> = HashMap()

    // Add keys and values (Country, City)

    // Add keys and values (Country, City)
    capitalCities.put("England", "London")
    capitalCities.put("Germany", "Berlin")
    // In reorganizeString, the following can be used to update the string
    // that's 1 part that you can reuse
  //  counts.put(cur, counts.get(cur)!!-1)
    println("joseph ")
    capitalCities.get("England")
    capitalCities.remove("England")
    println(capitalCities)

    capitalCities

    // to loop thru the kes here
    for (i in capitalCities.keys) {
        println(i)
    }

    for (i in capitalCities.values){
        println(i)
    }

    for (i in capitalCities.entries){
        println(i)
    }

    // Get the max and min in the dicrinoaty
//    Collections.min(capitalCities)
}
