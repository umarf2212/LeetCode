/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {

    //  {"a":"str", "e":[1,2,3], "b":-12, "c":true, "d":null}

    if (typeof object === 'string') {
        return '"'+object+'"'
    }
    else if (typeof object !== 'object' || object === null) {
        return object
    }

    function makeString(object, str) {

        const keys = Object.keys(object)
        keys.forEach(item => {
            // concatenate key
            if (!Array.isArray(object)) {
                str.push('"' + item + '":')
            }
            
            // concatenate value
            if (typeof object[item] === 'object') {
                if (object[item] === null) {
                    str.push(null)
                }
                else if (Array.isArray(object[item])) {
                    str.push('[')
                    makeString(object[item], str)
                    str.push(']')
                } else {
                    str.push('{')
                    makeString(object[item], str)
                    str.push('}')
                }
            } 
            else if (typeof object[item] === 'string') {
                str.push('"'+object[item]+'"')
            } else {
                str.push(object[item])
            }

            if (item !== keys[keys.length-1]) {
                str.push(",")
            }
        })
    }

    const str = [];
    makeString(object, str)
    res = ''

    for (let token of str) {
        res += token
    }

    if (typeof object === 'object') {
        if (Array.isArray(object)) {
            res = "["+res+"]"
        } else {
            res = "{"+res+"}"
        }
    }

    return res
};