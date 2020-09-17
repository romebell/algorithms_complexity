# Exponential - O(2^n)
def exponential_2n(n):
    if (n == 1):
        return
    exponential_2n(n - 1)
    exponential_2n(n - 1)

# If we pass in 4, we are going to double our calls every single time

# Exponential - O(3^n)
def exponential_3n(n):
    if (n == 1):
        return
    exponential_2n(n - 1)
    exponential_2n(n - 1)
    exponential_2n(n - 1)
# If we pass in 4, we are going to triple our calls every single time

# Exponential - O(2^n)
# function exponential_2n(n) {
#     if (n === 1) return;
#     exponential_2n(n - 1);
#     exponential_2n(n - 1);
# }

# Exponential - O(3^n)
# function exponential_3n(n) {
#     if (n === 1) return;
#     exponential_2n(n - 1);
#     exponential_2n(n - 1);
#     exponential_2n(n - 1);
# }