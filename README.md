# Unbiased-Decision-Maker
This Python script randomly decides whether to 'Go' or 'Don't Go' to an event using multiple algorithms.
# Random Decision Generator

This script uses a variety of algorithms to randomly decide whether to 'Go' or 'Don't Go' to an event. By combining multiple methods, it ensures an unbiased and highly randomized decision.

## Features

- **Dijkstra's Algorithm**: Determines the shortest path in a graph.
- **Bellman-Ford Algorithm**: Handles graphs with negative weights for shortest path calculation.
- **Monte Carlo Simulation**: Uses random sampling to make decisions based on probability distribution.
- **Random Walk**: A stochastic process to decide based on random steps.
- **Simulated Annealing**: A probabilistic technique for approximating the global optimum of a function.
- **Genetic Algorithm**: Mimics natural selection to optimize decision-making.
- **Weighted Random Choice**: Ensures unbiased random selection between 'Go' and 'Don't Go'.

## How It Works

The script creates a complex decision-making process by using multiple algorithms. The results from these algorithms are combined to provide a final decision, ensuring high randomness and lack of bias.

## Usage

### Prerequisites

- Python 3.x
- Required Libraries: `numpy`, `networkx`

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/tanmoysaha31/Unbiased-Decision-Maker.git
    cd your-repo-name
    ```

2. **Install Dependencies**:
    ```bash
    pip install numpy networkx
    ```

### Running the Script

1. **Execute the Script**:
    ```bash
    python Unbiased Decision Maker (6 Algorithms).py
    ```

2. **User Input**:
    - Enter `yes` or `y` to trigger the decision-making process.
    - Enter `no` or `n` to decline and exit.

### Example Output

```plaintext
You have an invitation today, which is not so important to you.
Because if it was important to you,
Then you wouldn't write 70 lines of code to generate an unbiased opinion!!
Now say, Should I proceed with further operation?
Please input only yes/no or y/n: yes
Decision: Go
```

## Code Overview

### Dijkstra's Shortest Path Decision

Calculates the shortest path in a graph and decides based on the path length.

```python
def dijkstra_decision(graph, start, end):
    try:
        path = nx.dijkstra_path(graph, start, end)
        return 'Go' if len(path) % 2 == 0 else "Don't Go"
    except nx.NetworkXNoPath:
        return "Don't Go"
```

### Bellman-Ford Shortest Path Decision

Handles graphs with negative weights to determine the shortest path.

```python
def bellman_ford_decision(graph, start, end):
    try:
        length, path = nx.single_source_bellman_ford(graph, start)
        return 'Go' if len(path[end]) % 2 == 0 else "Don't Go"
    except (nx.NetworkXNoPath, nx.NetworkXUnbounded):
        return "Don't Go"
```

### Monte Carlo Simulation

Uses random sampling to decide based on probability distribution.

```python
def monte_carlo_simulation(trials):
    go_count = 0
    no_go_count = 0
    for _ in range(trials):
        if random.random() < 0.5:
            go_count += 1
        else:
            no_go_count += 1
    return 'Go' if go_count > no_go_count else "Don't Go"
```

### Random Walk

A stochastic process that decides based on random steps.

```python
def random_walk(steps):
    position = 0
    for _ in range(steps):
        step = random.choice([-1, 1])
        position += step
    return 'Go' if position > 0 else "Don't Go"
```

### Weighted Random Choice

Unbiased random selection between 'Go' and 'Don't Go'.

```python
def weighted_random_choice():
    choices = ['Go', 'Don\'t Go']
    weights = [0.5, 0.5]
    return random.choices(choices, weights=weights, k=1)[0]
```

### Simulated Annealing

A probabilistic technique for decision-making.

```python
def simulated_annealing():
    current_state = random.choice(['Go', "Don't Go"])
    temperature = 1.0
    cooling_rate = 0.03

    while temperature > 0.01:
        next_state = random.choice(['Go', "Don't Go"])
        delta_e = 1 if next_state == 'Go' else -1

        if delta_e > 0 or random.uniform(0, 1) < np.exp(delta_e / temperature):
            current_state = next_state

        temperature *= 1 - cooling_rate

    return current_state
```

### Genetic Algorithm

Mimics natural selection to optimize decision-making.

```python
def genetic_algorithm():
    population = ['Go', "Don't Go"] * 50
    fitness = lambda x: 1 if x == 'Go' else 0
    generations = 100

    for _ in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        next_generation = population[:10]

        for _ in range(45):
            parent1 = random.choice(next_generation)
            parent2 = random.choice(next_generation)
            child = parent1 if random.random() > 0.5 else parent2
            next_generation.append(child)

        population = next_generation

    return random.choice(population)
```

### Combining All Algorithms

Combines results from all algorithms to ensure a highly randomized decision.

```python
def complex_decision():
    graph = nx.gnp_random_graph(10, 0.5, directed=True)
    start_node = random.choice(list(graph.nodes))
    end_node = random.choice(list(graph.nodes))
    dijkstra_result = dijkstra_decision(graph, start_node, end_node)
    bellman_ford_result = bellman_ford_decision(graph, start_node, end_node)

    monte_carlo_result = monte_carlo_simulation(1000)
    random_walk_result = random_walk(100)
    simulated_annealing_result = simulated_annealing()
    genetic_algorithm_result = genetic_algorithm()
    weighted_random_result = weighted_random_choice()

    results = [
        dijkstra_result,
        bellman_ford_result,
        monte_carlo_result,
        random_walk_result,
        simulated_annealing_result,
        genetic_algorithm_result,
        weighted_random_result
    ]
    final_decision = random.choice(results)
    return final_decision
```

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are always welcome!

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact [tanmoysaha2003@gmail.com](mailto:your.email@example.com).

---

Happy coding! 😊
```
