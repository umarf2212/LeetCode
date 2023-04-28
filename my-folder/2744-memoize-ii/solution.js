/**
 * @param {Function} fn
 */
function memoize(fn) {
    const cache = new Map()
    const RES = Symbol()
    return function(...args) {
        let curCache = cache;
        for (let arg of args) {
            if (!curCache.has(arg)) {
                curCache.set(arg, new Map())
            }
            curCache = curCache.get(arg)
        }

        if (curCache.has(RES)) {
            return curCache.get(RES)
        }

        const result = fn.apply(this, args)
        curCache.set(RES, result)
        return result
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
