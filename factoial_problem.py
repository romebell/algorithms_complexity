# Factorial 
# DISCLAIMER: Not showing factorial solution, just an example of 
# what a factorial problem would look like

def factorial_problem(n):
    if n == 1:
        return
    for i in range(1, n):
        factorial_problem(n - 1)

# The number of times that we branch is depended on size of input
# ref Graph

# Javascript
```js
function factorialProblem(n) {
    if (n === 1) return;

    for (let i = 1; i <= n; i++) {
        factorialProblem(n - 1)
    }
}
```
