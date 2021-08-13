/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var ar = [];
    
    for (let i=1; i<=n; i++) {
        if (i%3 === 0 && i%5 === 0) {
            ar.push('FizzBuzz');
        }
        else if (i%3 === 0) {
            ar.push('Fizz');
        }
        else if (i%5 === 0) {
            ar.push('Buzz');
        }
        else {
            ar.push(i.toString());
        }
    }
    return ar;
};
