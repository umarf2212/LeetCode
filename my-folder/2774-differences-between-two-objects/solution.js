/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */

obj1 = {
    'a': 1,
    'obj': {
        'obj_a': 11,
        'obj_b': 23
    },
    'ar': [null, 1, {'a':1}, 5]
}

obj2 = {
    'a': 2,
    'obj': {
        'obj_a': 11,
    },
    'ar': [undefined, '1', {'a':1, 'b': 4}]
}

result = {
    'a': [1, 2],
    'obj': {
        'obj_a': [23, 11]
    },
    'ar': {
        '0': [null, undefined],
        '1': [1, '1'],
        '2': {} // empty object is ultimately ignore
    }
}

// 1. If both values are equal, ignore them
// 2. If a key exists only in one of them, ignore it
// 3. If one of them is null, create difference array
// 4. If both are different, create difference array
// 5. If both are pure objects, recurse and save in resultant object
// 6. If both are arrays, recurse and save in resultant object


function objDiff(obj1, obj2) {
    // both are equal, ignore them
    if (obj1 === obj2) return {}

    // if only one of them is null
    if (obj1 === null || obj2 === null) return [obj1, obj2]

    // if only one of them is an Array  
    if (Array.isArray(obj1) !== Array.isArray(obj2)) return [obj1, obj2]

    // if only one of them is an object
    if (typeof obj1 !== 'object' || typeof obj2 !== 'object') return [obj1, obj2]

    const resultObject = {}
    for (const key in obj1) {
        if (key in obj2) {
            let recursiveResult = objDiff(obj1[key], obj2[key])
            if (Object.keys(recursiveResult).length > 0) {
                resultObject[key] = recursiveResult
            }
        }
    }
    return resultObject

};


