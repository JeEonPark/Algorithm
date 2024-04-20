import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    var ans = 0
    let sortedA = A.sorted()
    let sortedB = B.sorted(by: >)

    for index in 0..<A.count {
        ans += sortedA[index] * sortedB[index]
    }

    return ans
}