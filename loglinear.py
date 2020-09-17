# Loglinear - O(n*log(n))

def loglinear(n):
    if n <= 1:
        return
    for i in range(1, n):
        # something
        pass
    loglinear(n / 2)
    loglinear(n / 2)

# 8 as input
# iterate 8 times

                 # 8                   - 8
#           |           |
#           4            4             - 8
#        |     |      |     |
#        2     2      2      2          - 8
#      |   |  |  |   |  |   |  |
#      1   1   1  1  1  1   1   1        - 8
# log2(8)

# function loglinear(n) {
#     if (n <= 1) return;
#     for (let i = 1; i <= n; i++) {
#         # something
#     }
#     loglinear(n / 2);
#     loglinear(n / 2);
# }