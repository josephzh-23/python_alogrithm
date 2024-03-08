package Util

import java.util.*


fun main(){

    var pq = PriorityQueue<Student>(5, StudentComparator())
    val student1 = Student("Nandini", 3.2)

    // Adding a student object containing fields
    // name and cgpa to priority queue

    val student2 = Student("Anmol", 3.6)
    val student3 = Student("Palak", 4.0)
    pq.add(student1)
    pq.add(student2)
    pq.add(student3)

    while(!pq.isEmpty()){
        println(pq.poll().name)
    }

    // Inline comparator as int he code before

}

class Student    // A parameterized student constructor
(var name: String, var cgpa: Double,
var id: Int?=null)


// This would be a max queue here, student with bigger id comes out first
class StudentComparator : Comparator<Student> {
    // Overriding compare()method of Comparator
    // for descending order of cgpa
    override fun compare(s1: Student, s2: Student): Int {
        /*
        So if s1 is smaller than it will be moved to after s2
         */
        if (s1.cgpa < s2.cgpa) return 1 else if (s1.cgpa > s2.cgpa) return -1
        return 0
    }
}

// Use the following would be fine
