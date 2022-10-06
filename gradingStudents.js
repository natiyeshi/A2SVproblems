
/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

function gradingStudents(grades) {
    let Return = [];
    for(let itr of grades){ 
        if(itr < 38){
            Return.push(itr.toString())
            continue;
        }
        let round = itr;
        while(round % 5 != 0)
            round++;
        if(round - itr < 3)
            Return.push(round.toString());
        else 
            Return.push(itr.toString());
    }
    return Return;
}
