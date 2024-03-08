package Search


// This will allow us to get the # of days until a billino users
fun numberOfDaysUntilOneBillionUsers(growthRates: FloatArray):Int{

    // We will then start here
    var target = 1000000000.0
    var start = 0
    var end = 2000      // end will then assigned by the interviewed
    while (start <= end) {
        var total = 0.0

        val mid = start + (end - start) / 2

        // The middle is what we will pass in to calculate the
        // user growth rate and all that

        for(growthRate in growthRates){
            total+= getUserPerDay(growthRate, mid)
        }


        if (total < target) {
            start = mid + 1
        } else if (total> target) {
            end = mid
            // Yeah you can have that condition here
        } else if (total == target) {
            return mid
        }
    }
    return start
}

fun getUserPerDay(rate: Float, day: Int): Double {
    return Math.pow(rate.toDouble(), day.toDouble())
}
