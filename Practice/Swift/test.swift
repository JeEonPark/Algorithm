import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var clothesCountDict: [String:Int] = [:]
    for cloth in clothes {
        if clothesCountDict.keys.contains(cloth[1]) {
            clothesCountDict[cloth[1]]? += 1
        } else {
            clothesCountDict[cloth[1]] = 1
        }
    }

    var answer: Int = 1

    for value in clothesCountDict.values {
        answer *= (value + 1)
    }

    return answer - 1
}