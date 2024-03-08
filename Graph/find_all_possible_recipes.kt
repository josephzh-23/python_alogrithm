package Graph

import java.util.*


fun main() {
    var recipes = arrayOf("bread", "sandwich")
    var ingredients = listOf(listOf("yeast", "flour"), listOf("bread", "meat"))
    var supplies = arrayOf("yeast", "flour", "meat")
    findAllRecipes(recipes, ingredients, supplies)
}
fun findAllRecipes(recipes: Array<String>, ingredients: List<List<String>>, supplies: Array<String>): List<String> {
    // Have a bunch of default recipes here

    var graph = mutableMapOf<String, MutableList<String>>()
    var indegree = mutableMapOf<String,Int>()

    (recipes.zip(ingredients)).forEach{
        val (recipe, ingredientsPerRecipe) = Pair(it.first, it.second)

        println("$ingredientsPerRecipe is ingredients per recipes")
     // "bread" -> 2 from ["yeast", "flour"]
        indegree[recipe] = ingredientsPerRecipe.size


        for(ingredient in ingredientsPerRecipe){
            // For a particular ingredient you will go
            // "yeast" -> "bread"
            graph.computeIfAbsent(ingredient) {ArrayList()}.add(recipe)
        }

    }

    // the grpah is
    println("graph is $graph")
    var ans = mutableListOf<String>()

    var q = LinkedList<String>()
    q.addAll(supplies)

    var recipesSet = recipes.toMutableSet()
    while(q.isNotEmpty()){
        var supply =  q.pop()

        // This is the case where "bread" contains "bread"
        if(recipesSet.contains(supply)){
            ans.add(supply)
        }

        println("supply is ${graph[supply]}")

        // "yeast":
        graph[supply]?.run {
            for (recipe in this) {
                indegree[recipe] = indegree[recipe]!! - 1

                println("The indegree of this is ${indegree[recipe]}")
                // The indegrees of that recipe is now at 0
                if(indegree[recipe] == 0){
                    q.add(recipe)
                }
            }
        }
    }
    println(ans)
    return ans
}







