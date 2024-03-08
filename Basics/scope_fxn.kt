package Util

fun main() {
    val number : Int?= null
    var number2 : Int?= null
    val x = number?.let {
         number2 = it+1
        number2
    } ?: 3
    //return 3 if the number is null as indicated above that's it
    number2?.let{
        println("not null")
    }?:run{
        println("null")
    }

//    (number3 as? Int)?.let{
//        println("sec")
//    }?:run{
//        println("joseph")
//    }
    val number3 = 3

//    (number3 as? String)?.let{
//        println("run ")
//    }?:run{
//        println("not run")
//    }

    (number3 as? String)?.let{
        println("run")
    }?: run{
        println("not run")

    }
    var number4:Int = 4
//    number4.(number4 as? String)?.let{
//        println("run")
//    }?: run{
//        println(number4)
//
//    }
    number4?.let {
        println("joseph")
    }


}