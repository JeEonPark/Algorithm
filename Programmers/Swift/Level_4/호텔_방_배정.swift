import Foundation

var room:[Int64: Int64] = [:] // 원하는 방 번호 : 다음 가능한 방 번호

func solution(_ k:Int64, _ room_number:[Int64]) -> [Int64] {
    let result: [Int64] = room_number.map { findRoom($0) }
    
    return result
}

func findRoom(_ wantedNumber: Int64) -> Int64 {
    // 원하는 방에 들어갈 수 있는 경우
    if room[wantedNumber] == nil {
        room[wantedNumber] = wantedNumber + 1
        return wantedNumber
    } else { // 원하는 방에 못 들어가는 경우
        let foundRoom = findRoom(room[wantedNumber]!)
        room[wantedNumber] = foundRoom + 1

        return foundRoom
    }
}