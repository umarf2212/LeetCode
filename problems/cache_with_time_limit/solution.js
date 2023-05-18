
var TimeLimitedCache = function() {
    // value: [value, timeout]
    this.cache = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let exists = false;
    if (this.cache[key] !== undefined) {
        exists = true;
        clearTimeout(this.cache[key][1])
    }

    timeout = setTimeout(() => {
        delete this.cache[key]
    }, duration)
    
    this.cache[key] = [value, timeout];

    return exists;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache[key] !== undefined) {
        return this.cache[key][0]
    }
    return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.cache).length
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */