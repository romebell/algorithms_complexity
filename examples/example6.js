function example6(n) {
    if (n <= 1) return;
    for (let i = 1; i <= 4; i++) {
        example6(n - 1)
    }
}

// Example with 5


//


















// notice similar, if not the same as example5.js
// O(4n)