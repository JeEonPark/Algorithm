import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var p = players
    
    var rankDict = [String: Int]()
    for (index, player) in players.enumerated() {
        rankDict[player] = index
    }

    for name in callings {
        let backIndex = rankDict[name]!
        let frontIndex = backIndex - 1

        p[backIndex] = p[frontIndex]
        p[frontIndex] = name
        
        rankDict[p[frontIndex]]! -= 1
        rankDict[p[backIndex]]! += 1
    }
    
    return p
}