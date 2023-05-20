class EventEmitter {
    constructor() {
        this.callbacks = {}
    }

    subscribe(event, cb) {
        if (this.callbacks[event] === undefined) {
            this.callbacks[event] = new Set()
        }

        this.callbacks[event].add(cb)

        return {
            unsubscribe: () => {
                this.callbacks[event].delete(cb)
                return undefined
            }
        };
    }

  emit(event, args = []) {
      if (this.callbacks[event] === undefined) {
          return []
      }
      
      let results = []
      for (let f of this.callbacks[event]) {
          results.push( f.apply(null, args) )
      }
      return results
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */