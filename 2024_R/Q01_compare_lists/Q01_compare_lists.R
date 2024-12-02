# Read unique input
input <- utils::read.table("Q01_input.txt")

# Sort both lists for comparison
input$V1 <- sort(input$V1)
input$V2 <- sort(input$V2)

# Q1.a) Total distance between sorted lists
all_distances <- abs(input$V1 - input$V2)
print(sum(all_distances))

# Q1.a) Similarity scores
n_matches <-
  vapply(input$V1, function(.x) sum(.x == input$V2), numeric(1))

print(sum(n_matches * input$V1))
