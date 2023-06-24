/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        let ar = new Array(functions.length)
        let completed = 0
        functions.forEach((func, i) => {
            func()
                .then(res => {
                    ar[i] = res
                    completed++

                    if (completed === functions.length) {
                        resolve(ar)
                    }
                })
                .catch(err => {
                    reject(err)
                })
        })

    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */