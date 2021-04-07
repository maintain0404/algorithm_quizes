const readline = require('readline');

let N = 0;
let cnt = 0;
let candies = [];
const rln = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rln.on('line', (line) => {
    if(cnt === 0){
        N = parseInt(line);
    }else if(cnt < N){
        cnt++;
        candies.push(parseInt(line));
    }else{
        rln.close();
    }
})

rln.on('close', () => {
    candies.map((num) => {
        
    })
})