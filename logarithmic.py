# Logarithmic - O(log(n))
def logarithmic(n):
    if n <= 1:
        return
    logarithmic(n / 2)

# If a pass in 8, my input keeps dividing 4
# We not really solving problems, but rather than getting a framework
# of how the problems will look like


# Javascript
```js
function logarithmic(n) {
    if (n <= 1) return
    logarithmic(n / 2)
}
```
