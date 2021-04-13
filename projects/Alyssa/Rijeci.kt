fun buttonPress(n: Int) {
    
    var a = 1
    var b = 0
    var temp = 0
    
    for (i in 1..n) {
        
        temp = b
        b = b + a
        a = temp
        
    }
    
    println("$a $b")
    
}

fun main(args: Array<String>) {
    
    buttonPress(1)
    buttonPress(4)
    buttonPress(10)
   
