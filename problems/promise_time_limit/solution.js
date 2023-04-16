/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    /**
        Promise.race is the highlight of this problem.
    */

    // This promise is solely for rejection after time limit
    const timeout = new Promise((resolve, reject) => {
        setTimeout(() => {
            reject("Time Limit Exceeded")
        }, t)
    })

    return function(...args) {
        return Promise.race([
            new Promise(resolve => {resolve(fn(...args))}), 
            timeout
        ])
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */