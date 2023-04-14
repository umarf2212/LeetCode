/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    // o1 => [null, object, array] = objects
    // or non-objects like int, str, undefined, [], {}, '', true/false

    // => in case of object => recurse down
    // => in case of non-object => compare right away

    if (typeof o1 !== typeof o2) return false

    if (typeof o1 !== 'object' && typeof o2 !== 'object') {
        return o1 === o2
    }
    
    function checkObject(o1, o2) {
        if (o1 === null || o2 === null) {
            return o1 === o2
        }

        if (Object.keys(o1).length !== Object.keys(o2).length) {
            return false
        }

        if (Array.isArray(o1) || Array.isArray(o2)) {
        if (!Array.isArray(o1) || ! Array.isArray(o2))
            return false
        }

        let cur = true
        Object.keys(o1).forEach(key => {
            if (o2[key] === undefined) {
                cur = false
            }
            else if (typeof o1[key] !== typeof o2[key]) {
                cur = false
            }
            else if (typeof o1[key] === 'object') {
                cur = cur & checkObject(o1[key], o2[key])
            }
            else {
                cur = cur & (o1[key] === o2[key])
            }
        })
        return cur
    }

    return checkObject(o1, o2)

};
