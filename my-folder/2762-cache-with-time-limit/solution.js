
var TimeLimitedCache = function() {
    // cache: {key: [val, time]}
    this.cache = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let exists = false
    if (this.cache[key] !== undefined) {
        exists = true;
    }

    this.cache[key] = [value, Date.now() + duration]

    return exists;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    let curTime = Date.now()
    if (this.cache[key] !== undefined) {
        if (this.cache[key][1] > curTime) {
            return this.cache[key][0];
        }
    }
    return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let curTime = Date.now()
    let count = 0
    Object.keys(this.cache).forEach(item => {
        if (this.cache[item][1] > curTime) {
            count++;
        }
    })
    return count;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
