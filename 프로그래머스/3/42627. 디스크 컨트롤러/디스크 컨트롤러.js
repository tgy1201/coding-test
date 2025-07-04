function solution(jobs) {
    var t = 0
    var len = jobs.length
    var time = []
    
    while (jobs.length !== 0) {
        let a = heapq(jobs, t)
        let b = jobs.indexOf(a)
        
        if (t>= a[0]) {
            t += a[1]
        } else {
            t = a[0] + a[1]
        }

        jobs.splice(b, 1)
        time.push(t-a[0])
    }
    
    console.log(time)
    const total = 0
    const res = time.reduce((a,b)=>a+b, total)
    
    return Math.floor(res / len)
}

function heapq(arr, time) {
    const temp = arr.filter(x=> x[0] <= time)
    
    if (temp.length === 0) {
        arr.sort((a,b)=> a[0]-b[0] || a[1]-b[1])
        return arr[0]
    } else{
        temp.sort((a,b)=> a[1]-b[1] || a[0]-b[0])
        return temp[0]
    }
}