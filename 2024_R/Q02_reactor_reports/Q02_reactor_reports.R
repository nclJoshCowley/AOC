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

# Q02.b)
# Introduction of problem dampener
# (If removing 1 element makes sequence safe, it's safe!)

# Brute force approach. Iterative looping unlikely to be quick

# Function to implement logic from part a)
is_report_safe <- function(x) {
  x_diff <- diff(x)

  is_monotonic <- length(unique(sign(x_diff))) == 1
  is_safe_jump <- all(dplyr::between(abs(x_diff), 1, 3))

  return(is_monotonic & is_safe_jump)
}

# Function to implement new logic from part b)
is_report_dampened_safe <- function(x) {
  if (is_report_safe(x)) return(TRUE)

  for (i in seq_along(x)) {
    if (is_report_safe(x[-i])) return(TRUE)
  }

  return(FALSE)
}

# Apply to all inputs
output <- vapply(input_seq, is_report_dampened_safe, logical(1))

print(sum(output))
