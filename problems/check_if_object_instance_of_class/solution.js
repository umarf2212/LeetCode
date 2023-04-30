/**
 * @param {any} object
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    /**
        This is a good knowledge based problem to understand how
        OOP Classes are internally implemented using prototypes.
        This mainly shows the prototypal chain of sub-classes that extend
        parent/super classes.
     */

    if (obj === null || obj === undefined) {
        return false
    }
    
    // console.log(classFunction.constructor.name)

    let proto = obj
    while (proto != null) {
        if (proto.constructor === classFunction) {
            return true
        }
        proto = Object.getPrototypeOf(proto)
    }

    return false
     
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */