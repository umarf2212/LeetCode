/**
 * @param {Function} fn
 */
function memoize(fn) {
    /**
        This cache variable is stored in the memory because
        it is being used inside the returned function and 
        a closure is being formed.
     */
    let cache = {}
    return function(...args) {
        if (cache[args] === undefined) {
            // ...args above creates an array args so we need to
            // spread it again below in the fn call.
            let res = fn(...args)
            cache[args] = res
            return res
        } else {
            return cache[args]
        }
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