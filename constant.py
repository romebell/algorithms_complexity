# Constant - O(1)

def constant_1(n):
    return n * 2 + 1
# T(2) => O(1)

def constant_2(n):
    for i in range(0, 1000):
        print(i)
# T(100) => O(1)


```js
function constant_2(n) {
    for (let i = 1; i <= 100, i++) {
      console.log(i)
    }
}

function constant_1(n) {
   return n * 2 + 1
}

```
