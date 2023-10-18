func solution(_ s:String) -> String {
    
    var flag: Bool = true
    var answer: String = ""
    for word in s {
        if word == " " {
            answer += String(word)
            flag = true
        } else {
            if flag {
                answer += word.uppercased()
                flag = false
            } else {
                answer += word.lowercased()
            }
        }
    }
    
    return answer
}