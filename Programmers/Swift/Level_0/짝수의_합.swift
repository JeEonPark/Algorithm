import Foundation

func solution(_ n:Int) -> Int {
    var answer:Int = 0
    for num in stride(from: 0, through: n, by: 2) {
        answer = answer + num
    }
    return answer
}