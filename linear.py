# Linear - O(n)

def linear_1(n):
    for i in range(0, n):
        print(i)

# iterative linear function

def linear_2(n):
    if (n == 1): 
        return
    linear_2(n - 1)

# pass in 10
# 10 -> 9 -> 8 -> 7 -> 6 ...

# JavaScript
```js
function linear_1(n) {
    for (let i = 1; i <= n; i++) {
        something
    }
}

function linear_2(n) {
    if (n === 1) {
        return;
    }

    linear_2(n - 1);
}
```

