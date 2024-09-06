/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = {}

    return function(...args) {
        let argsStr = JSON.stringify(args)
        if (cache[argsStr] === undefined) {
            let result = fn.apply(this, args)
            cache[argsStr] = result
            return result
        }
        return cache[argsStr]
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
