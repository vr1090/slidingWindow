package main

import "fmt"

func missingNumber(nums []int) int {
    var sum = 0
    
    for _, i := range nums {
        sum = sum + i
    }
    
    var shouldSum = len(nums) * ( len(nums)+ 1) /2
    
    fmt.Println(shouldSum)
    return shouldSum-sum
    
}