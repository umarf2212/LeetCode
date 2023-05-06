/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let counts = init;
    return {
        increment: function() {
            return ++counts
        },
        decrement: function() {
            return --counts
        },
        reset: function() {
            counts = init
            return counts
        }

    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
