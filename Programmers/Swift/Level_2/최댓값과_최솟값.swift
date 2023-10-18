func solution(_ s: String) -> String {
    let splited_s = s.split(separator: " ").compactMap { Int($0) }
    return "\(splited_s.min() ?? 0) \(splited_s.max() ?? 0)"
}
