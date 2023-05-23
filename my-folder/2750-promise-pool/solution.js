/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    
    const results = []
    let i = 0

    function next() {

        // this is the base case to stop recursing further, simple empty settled promise
        if (i >= functions.length){
            return Promise.resolve()
        }

        const p = functions[i++]()

        // this returns the Promise of the current function
        return p.then(res => {
            results.push(res)

            // this return is responsible for creating a Promise Chain
            // the next function's promise is return through this and outer
            // return
            return next()
        })
    }


    // initializing only n promises ensures that at any given moment,
    // only n promises will execute at most, one after another
    const promises = []
    for (let i=0; i < Math.min(n, functions.length); i++) {
        promises.push(next())
    }

    return Promise.all(promises).then(() => results)

    

    // let next=()=>functions[n++]?.().then(next);
    // return Promise.all(functions.slice(0,n).map(f=>f().then(next)));
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
