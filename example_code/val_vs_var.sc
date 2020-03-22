// ~/code/scala/demo/src/val_vs_var.sc

// immutable
val x = 5

// x = 6


// mutable
var y = 2
y = 4

// This is ok
val arr = Array(1,2,3)
arr(2) = 99
arr

// But this is not allowed
arr = Array(5,6,7)

// Prefer vals, immutable objects, and methods without side effects.
// Reach for them first. Use vars, mutable objects, and methods with
// side effects when you have a specific need and justification for them.”