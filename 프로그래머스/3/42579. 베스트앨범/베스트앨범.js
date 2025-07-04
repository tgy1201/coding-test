function solution(genres, plays) {
    var answer = [];
    const temp = new Map()
    
    for (let i = 0; i < genres.length; i++) {
        if (temp.has(genres[i])) {
            temp.get(genres[i]).cnt += plays[i]
            temp.get(genres[i]).arr.push([plays[i],i])
        } else {
            temp.set(genres[i], {cnt: plays[i], arr: [[plays[i],i]]})
        }
    }

    const newMap = new Map([...temp.entries()].sort((a, b)=> b[1].cnt - a[1].cnt))
    
    console.log(newMap)
    
    newMap.forEach(e=> {
        e.arr.sort((a,b)=> {
            if (a[0] > b[0]) {
                return -1
            } else if (a[0] < b[0]) {
                return 1
            } else {
                if (a[1] > b[1]) {
                    return 1
                } else {
                    return -1
                }
            }
        })
       
        
        for (let i = 0; i < e.arr.length; i++) {
            if (i == 2) {
                break
            }
            answer.push(e.arr[i][1])
        }
    })
    
    return answer;
}