/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.cache = new Map()
    this.dll = new DLL()
    this.capacity = capacity
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (!this.cache.has(key)) {
        return -1
    }

    const cur = this.cache.get(key)
    this.dll.deleteNode(cur)
    this.dll.appendNode(cur)

    return cur.val
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.cache.has(key)) {
        this.dll.deleteNode(this.cache.get(key))
        this.cache.delete(key)
    }

    if (this.cache.size >= this.capacity) {
        const leastUsed = this.dll.head
        this.dll.deleteNode(leastUsed)
        this.cache.delete(leastUsed.key)
    }

    const newNode = this.dll.appendNode(new ListNode(value, key))
    this.cache.set(key, newNode)

};

class ListNode {
    constructor(val, key) {
        this.val = val
        this.key = key
        this.prev = null
        this.next = null
    }
}

class DLL {
    constructor() {
        this.head = null
        this.tail = null
    }
    
    appendNode(newNode) {
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            newNode.prev = this.tail
            this.tail = newNode
        }
        return newNode
    }
    
    deleteNode(node) {
        if (!node) return
        
        if (node === this.head) {
            this.head = this.head.next
            if (this.head) {
                this.head.prev = null
            } else {
                this.tail = null
            }
        }
        else if (node === this.tail) {
            this.tail = this.tail.prev
            if (this.tail) {
                this.tail.next = null
            } else {
                this.head = null
            }
        }
        else {
            node.prev.next = node.next
            node.next.prev = node.prev
        }
    }
}

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
