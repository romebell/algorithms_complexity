# Polynomial - O(n^2)

def quadratic(n):
    for i in range(1, n):
        for j in range(1, n):
                pass

# Polynomial - O(n^3)
def cubic(n):
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                pass

# we have to look for nested loops where both depend on the size of our input

```js
function quadratic(n) {
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= n; j++) {
            // something
        }
    }
}
```


# Polynomial - O(n^3)
```js
function cubic(n) {
    for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                for (let k = 1; k <= n; k++) {
                    // something
                }
            }
        }
}
```
