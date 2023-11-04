/* 
    PROMPT

    Given an integer n, return a counter function. 
    This counter function initially returns n and then returns 
    1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).

    PROMPT
*/

// Solution

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    var curr_val = n;
    var first = 0;

    return function() {
        if(first == 0)
        {
            first = 1;
            return curr_val;
        }
        curr_val += 1;
        return curr_val;
    };
};