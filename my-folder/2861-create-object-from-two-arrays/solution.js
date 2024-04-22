/**
 * @param {Array} keysArr
 * @param {Array} valuesArr
 * @return {Object}
 */
var createObject = function(keysArr, valuesArr) {
    const result = {}
    for (let i=0; i<keysArr.length; i++) {
        const key = String(keysArr[i])
        if (!result.hasOwnProperty(key)) {
            result[key] = valuesArr[i]
        }
    }
    return result
};
