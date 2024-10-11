/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    // pajshdgfwwkew
    // pajshdgfhwkew

    if (s.length === 0) {
        return 0
    }
    
    charSet = new Set()

    let i = 0
    let j = 0
    let ans = -Infinity
    while (j < s.length) {
        if (!charSet.has(s[j])) {
            charSet.add(s[j])
            ans = Math.max(ans, charSet.size)
            j++
            continue
        }

        while (i < j && charSet.has(s[j])) {
            charSet.delete(s[i])
            i++
        }
    }

    return ans
};
