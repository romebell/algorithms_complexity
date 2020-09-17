// Keep in mind that this input is a string
function example7(str) {
    if (str.length <= 1) return; 

    let midIdx = Math.floor(str.length / 2);
    let left = str.slice(0, midIdx);
    let right = str.slice(midIdx);

    example7(left);
    example7(right);
}

// Big O?

// When consider Big O, we should bare in mind the Big O for any hidden methods
// of methods used in the logic.

// Math.floor() is a constant operation
// str.slice() is a linear because you don't know the length of the string making it (n)












// O(nlog(n))














