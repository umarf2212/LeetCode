/**
 * @param {Object} obj
 * @return {Object}
 */
/*
{ 
    a: 1, 
    b:'b', 
    c: [
        1, 
        2, 
        {ac:1}
    ], 
    d: {
        do: 1, 
        da: [3,4]
    } 
}
*/
var compactObject = function(obj) { 
    if (typeof obj === 'object') {
        let newObj;
        if (Array.isArray(obj)) {
            newObj = []
            for (let val of obj) {
                if (Boolean(val)) {
                    newObj.push(compactObject(val))
                }
            }
            return newObj
        } else {
            newObj = {}
            Object.keys(obj).forEach(key => {
                if (Boolean(obj[key])) {
                    newObj[key] = compactObject(obj[key])
                }
            })
            return newObj
        }
    } else {
        return obj
    }
};
