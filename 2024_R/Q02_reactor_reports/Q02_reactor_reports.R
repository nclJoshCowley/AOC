# Read unique input
input <- readLines("Q02_input.txt")

# Parse numeric information
input_seq <- lapply(input, function(.x) as.numeric(strsplit(.x, " ")[[1]]))

# Q02.a)
# How many "reports" such that
# * All increasing or decreasing?
# * Adjacent levels differ by 1 - 3

input_diffs <- lapply(input_seq, diff)

is_monotonic <-
  input_diffs |>
  vapply(function(.x) length(unique(sign(.x))) == 1, logical(1))

is_safe <-
  input_diffs |>
  vapply(function(.x) all(dplyr::between(abs(.x), 1, 3)), logical(1))

print(sum(is_monotonic & is_safe))
