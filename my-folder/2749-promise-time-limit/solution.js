/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {

    // If function completes withing time limit, resolve with result
    // If time limit expires, 
    // reject the function with string "time limit exceeded"

    const timeoutPromise = new Promise((resolve, reject) => {
        setTimeout(() => {
            reject("Time Limit Exceeded")
        }, t)
    })
    
    return async function(...args) {
        return Promise.race([
            new Promise(resolve => resolve(fn(...args))),
            timeoutPromise
        ])        
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
