internal class Solution33q1 {
    // Hash table that takes care of the mappings.
    private val mappings: HashMap<Char, Char>

    // Initialize hash map with mappings. This simply makes the code easier to read.
    init {
        mappings = HashMap()
        mappings[')'] = '('
        mappings['}'] = '{'
        mappings[']'] = '['
    }
}