package palindrome

// here we can't create a string, have to do it in constant time here
// If input 1221, check if can reverse the last 2 nubmbers there

// Form a palindromic number there
// And that's it

fun main() {
    var x = 12345
    IsPalindrome(x)
}

// Notice below we are doing this without creating any variable
fun IsPalindrome(x: Int): Boolean {
    // Special cases:
    // As discussed above, when x < 0, x is not a palindrome.

    // x %10 = 0 means that last digit of this is 0, meaning
    // Also if the last digit of the number is 0, in order to be a palindrome,
    // the first digit of the number also needs to be 0.
    // Only 0 satisfy this property.

    // So will not work here then
    var x = x
    if (x < 0 || x % 10 == 0 && x != 0) {
        return false
    }
    var revertedNumber = 0
    while (x > revertedNumber) {

        revertedNumber = revertedNumber * 10 + x % 10

        // If the input is 12345 this is what would happen here
        // 5    54    543
        println(revertedNumber)
        x /= 10
    }

    // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
    return x == revertedNumber || x == revertedNumber / 10
}











