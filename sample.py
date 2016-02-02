# data: use JSON with
# {
#
#
# label of packages
packages = (
    "WP 1-1", "WP 1-2",
    "WP 2-1", "WP 2-2", "WP 2-3", "WP 2-4",
    "WP 3-1", "WP 3-2", "WP 3-3",
)

# offset
start = [
    0, 2,
    3, 6, 7, 8,
    2, 4, 6
]

# width of bar
end   = [
    2, 4,
    5, 8, 9, 9,
    6, 8, 12
 ]

# miles stones are optial
mileStones = {
    "WP 1-1": [2],
    "WP 1-2": [3, 4],
    "WP 2-1": [5],
    "WP 2-2": [8],
    "WP 2-3": [8],
    "WP 2-4": [9],
    "WP 3-1": [4,6],
    "WP 3-2": [8],
    "WP 3-3": [11.9] # 12 is not good to read
}

title = r" Sample GANTT for  \textbf{myProject}"
xlabel = "time (weeks)"
xticks = [2,4,6,8,10,12]