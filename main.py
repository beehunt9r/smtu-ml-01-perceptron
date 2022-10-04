from helpers import *
import random
import matplotlib.pyplot as plt

# Set seed to generate repeatable values.
random.seed(7)

# Input training dataset.
x_train = [
    (1.0, 0.1, -1.5), (1.0, 0.1, 0.0), (1.0, 0.1, 1.5),
    (1.0, 0.0, -1.5), (1.0, 0.0, 0.0), (1.0, 0.0, 1.5),
    (1.0, -0.1, -1.5), (1.0, -0.1, 0.0), (1.0, -0.1, 1.5)
]
# Output training dataset.
y_train = [-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0]

# Indexes of training data list.
index_list = list(range(len(x_train)))

# Starting weights.
weights = [0.2, -0.6, 0.25]

# Show default weights.
print(format_weights(weights))

# Fill the plot with plus and minus points.
figure, axes = plt.subplots()

print(type(axes))

axes.set_xlim(-1.6, 1.6)  # x2
axes.set_ylim(-0.11, 0.11)  # x1

for index in index_list:
    x_values = x_train[index]
    y = y_train[index]

    axes.scatter(x_values[2], x_values[1], marker='_' if y < 0 else '+', color='red' if y < 0 else 'blue')

# Train perceptron.
all_correct = False
while not all_correct:
    all_correct = True
    random.shuffle(index_list)

    for index in index_list:
        x_values = x_train[index]
        y = y_train[index]

        output = compute_output(weights, x_values)

        if output != y:
            for weightIndex in range(len(weights)):
                weights[weightIndex] += (y * 0.1 * x_values[weightIndex])

            all_correct = False

            # Show new weights.
            print(format_weights(weights))

    add_weights_line(weights, axes, 'green' if all_correct else 'red')

# Create new plot.
figure, axes = plt.subplots()

axes.set_xlim(-1.6, 1.6)  # x2
axes.set_ylim(-0.11, 0.11)  # x1

# Fill plot with calculated signatures.
for x1 in range(-100, 101, 25):
    x1 = x1 / 1000
    for x2 in range(-150, 151, 50):
        x2 = x2 / 100
        y = compute_output(weights, [1.0, x1, x2])
        axes.scatter(x2, x1, marker='_' if y < 0 else '+', color='red' if y < 0 else 'blue')

# Add final line.
add_weights_line(weights, axes, 'orange')

plt.show()
