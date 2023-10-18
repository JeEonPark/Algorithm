import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var p = priorities
    var target = location

    while true {
        if p.contains(where: { $0 > p[0]}) {
            p.append(p[0])
            p.removeFirst()
            target = !(target == 0) ? target - 1 : p.count - 1
        } else {
            if target == 0 {
                return priorities.count - p.count + 1
            }
            p.removeFirst()
            target -= 1
        }
    }
}
