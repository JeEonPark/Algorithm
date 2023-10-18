import Foundation

func solution(_ n:Int) -> Int {
    for index in 2...n-1 {
        if ((n-1) % index == 0) {
            return index
        }
    }
    return 0
}