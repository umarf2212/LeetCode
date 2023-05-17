/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let waitingID;
    let storedArgs;

    const timeoutFunction = () => {
        if (!storedArgs) {
            waitingID = null;
        } else {
            fn.apply(this, storedArgs);
            storedArgs = null
            setTimeout(timeoutFunction, t)
        }
    }

    return function(...args) {
        if (!waitingID) {
            fn.apply(this, args);
            waitingID = setTimeout(timeoutFunction, t);
        } else {
            storedArgs = args;
        }
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */