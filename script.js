maxGeneration = 50;
population = 10;
diminsionSize = 30; // 2D
absorption = 1.0; // gamma absorption coefficient [0.1, 100]
randomness = 0.2; // alpha
attractiveness = 1; // beta at 0 distance
epsilon = 0.1 // between [-0.5, 0.5]
topLimit = 100;
downLimit = -100;

//-----------------------//
populationMap = [];
distanceArray = [];
lightIntensityR = [];
attractivenessR = [];


function generateFireflies() {
    for (i = 0; i < population; i++) {
        var x = [];
        for (j = 0; j < diminsionSize; j++) {
            x[j] = getRandomInteger(topLimit, downLimit);
        }
        populationMap.push({
            id: "firefly_" + i,
            locationStr: "(" + x.join(', ') + ")",
            location: x,
            lightIntensity: 0
        });
    }

    // generate random values
    function getRandomInteger(min, max) {
        return Math.floor(Math.random() * (max - min + 1) ) + min;
    }

    
}

function objectiveFunction() {
    for (i = 0; i < population; i++) {
        var sum = 0;
        for (j = 0; j < diminsionSize; j++) {
            sum += Math.pow(populationMap[i].location[j], 2);
            // sum +=  Math.pow(populationMap[i].location[j], 2);
        }
        // sum = 150 - Math.sqrt(sum);
        populationMap[i].lightIntensity = sum;
    }
}

function lightIntensityAndAttractiveness() {
    for (i = 0; i < population; i++) {
        lightIntensityR[i] = [];
        attractivenessR[i] = [];
        for (j = 0; j < population; j++) {
            var lightIntensity = 0;
            var attraction = 0;
            if ( i == j) {
                lightIntensity = 0;
                attraction = 0;
            } else {
                lightIntensity = populationMap[i].lightIntensity * Math.exp((-1 * absorption * Math.pow(distanceArray[i][j], 2)));
                attraction = attractiveness / (1 + absorption * Math.pow(distanceArray[i][j], 2));
            }
            lightIntensityR[i][j] = lightIntensity;
            attractivenessR[i][j] = attraction;
        }
    }
}

function calcDistance() {    
    //        
    for (i = 0; i < population; i++) {
        distanceArray[i] = [];
        for (j = 0; j < population; j++) {
            var distance = 0;
            if ( i == j) {
                distance = 0;
            } else {
                for (k = 0; k < diminsionSize; k++) {
                    distance += Math.pow((populationMap[i].location[k] - populationMap[j].location[k]), 2);
                }
                distance = Math.sqrt(distance);
            }
            distanceArray[i][j] = distance;
        }
    }
}

function moveTowards(id1, id2) {
    var location1 = populationMap[id1].location;
    var location2 = populationMap[id2].location;
    
    for (i = 0; i < diminsionSize; i++) {
        populationMap[id1].location[i] = location1[i] + (attractivenessR[id2][id1] * (location2[i] - location1[i])) + (randomness * epsilon);
    }
    populationMap[id1].locationStr =  "(" + populationMap[id1].location.join(', ') + ")";
    
}

function moveRandomly(id) {    
    for (i = 0; i < diminsionSize; i++) {
        populationMap[id].location[i] = populationMap[id].location[i] + (randomness * epsilon);
    }
}




//---------------------------------------------//

function test() {
    populationMap = [];
    generateFireflies();
    objectiveFunction();
    console.table(populationMap);
    console.log("Table1: populationMap");
    calcDistance();
    console.table(distanceArray);
    console.log("Table2: distanceArray");
    lightIntensityAndAttractiveness();
    console.table(lightIntensityR);
    console.log("Table3: lightIntensityR");
    console.table(attractivenessR);
    console.log("Table4: attractivenessR");
}


function run() {
    for (index = 0; index < population; index++) {
        var hasMoved = false;
        for (j = 0; j < population; j++) {
            if (populationMap[index].lightIntensity < lightIntensityR[index][j]) {
            // if (populationMap[index].lightIntensity < populationMap[j].lightIntensity) {
                moveTowards(index, j);
                hasMoved = true;
            }
        }
        if (hasMoved == false) {
            moveRandomly(index);
        }
    }
    objectiveFunction();
    lightIntensityAndAttractiveness();
    
    console.table(populationMap);
    console.log("Table1: populationMap");
    calcDistance();
    lightIntensityAndAttractiveness();
}

function loop() {
    var delay = 200; // 1000ms = 1s
    var i = 1; 
    myLoop ()
    function myLoop () {
        
        startTime = new Date();
        setTimeout(function () {
            run();
            i++;
            if (i < maxGeneration) {
                console.log("Generation: " + (i + 1));
                myLoop();
            }
        // }, delay)
        })
    }
    
}