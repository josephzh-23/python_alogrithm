package Util

import java.util.*
import kotlin.Comparator

fun main() {
    // Here are some more options
    // min heap
    val pq = PriorityQueue { a: Int, b: Int -> a - b }

    // max heap
    val pq2 = PriorityQueue { a: Int, b: Int -> b - a }


    //min heap
    val studentMinQ: PriorityQueue<Student> = PriorityQueue<Student>(Comparator<Student>
    { obj1:Student, obj2: Student -> obj1.id!! - obj2.id!! })

    // max heap
    val studentMaxQ: PriorityQueue<Student> = PriorityQueue<Student>(Comparator<Student> { obj1: Student, obj2:
    Student -> obj2.id!! - obj1.id!! })

//    studentMaxQ.add()

    val student1 = Student("Nandini", 3.2, 5)

    // Adding a student object containing fields
    // name and cgpa to priority queue

    val student2 = Student("Anmol", 3.6, 3)
    val student3 = Student("Palak", 4.0, 4)
    studentMaxQ.add(student1)
    studentMaxQ.add(student2)
    studentMaxQ.add(student3)

    println(studentMaxQ.poll())
}