import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = 0
    for strNum in String(n) {
        answer += Int(String(strNum))!
    }
    
    return answer
}