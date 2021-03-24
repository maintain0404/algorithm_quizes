const readline = require('readline');



function distance(ax, ay, bx, by){
    return (ax - bx) * (ax - bx) + (ay - by) * (ay - by);
}

const TestCase = () => {
    let cnt = 0;
    let planet_cnt = 0;
    let obj = {};
    obj.planets = [];
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });

    rl.on('line', (line) => {
        if(cnt == 0){
            [obj.sx, obj.sy, obj.ex, obj.ey] = line.trim().split(' ').map((num) => parseInt(num));
        }else if(cnt == 1){
            planet_cnt = parseInt(line.trim());
        }else{
            if (cnt == planet_cnt + 1){
                rl.close();
            }
            let planet = {};
            [planet.x, planet.y, planet.r] = line.trim().split(' ').map((num) => parseInt(num));
            obj.planets.push(planet);
        }
        cnt++;
    })
    
    rl.on('close', () => {
        let ret = 0;
        console.log(obj)
        obj.planets.map((planet) => {
            console.log('loop')
            let dist = distance(obj.sx, obj.sy, planet.x, planet.y);
            if (dist < (planet.r * planet.r)){
                ret++;
            }
        })
        console.log('answer')
        console.log(ret);
    })
}


let N;

const rln = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

rln.on('line', (line) => {
    console.log('start')
    N = parseInt(line);
    rln.close();
    
})

rln.on('close', () => {
    for(i = 0; i < N; i++){
        TestCase();
    }
})