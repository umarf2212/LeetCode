/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    if (s.length === 0) return true;
    if (t.length === 0) return false;
    
    let i = 0; // s
    let j = 0; // t
    
    while (i < s.length) {
        
        if (j == t.length) return false;
        
        if (s[i] === t[j]) {
            i++;
        }
        
        j++;
        
    }
    
    return true;
    
};