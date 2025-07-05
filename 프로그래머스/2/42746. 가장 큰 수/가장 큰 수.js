function solution(numbers) {
    var answer = '';
    
    const arr = numbers.map((e,i)=> {
        let s = e.toString()
        let ss = ""
        if(s.length === 1) {
            ss = s.repeat(12)
        } else if(s.length === 2) {
            ss = s.repeat(6)
        } else if(s.length === 3) {
            ss = s.repeat(4)
        } else {
            ss = s.repeat(3)
        }
        
        return [ss,i]
    })
    
    arr.sort((a,b)=> b[0]-a[0])
    
    arr.forEach(e=>{
        answer += numbers[e[1]].toString()
    })
    return answer[0] === "0" ? "0": answer
}