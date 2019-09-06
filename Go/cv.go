package main

import (
        "fmt"
        "time"
)

func fib(n int) (res int) {
        if n<2{
                res = 1
        } else if n>=2{
                res = fib(n-2) + fib(n-1)
        }
        return
}
func main() {
        timetemp := time.Now()
        fmt.Println(fib(50))
        fmt.Println(time.Now().Sub(timetemp))
}