#Decision Maker
import random
import numpy as np
import networkx as nx

# Function for Dijkstra's shortest path decision
def dijkstra_decision(graph, start, end):
    try:
        path = nx.dijkstra_path(graph, start, end)
        return 'Go' if len(path) % 2 == 0 else "Don't Go"
    except nx.NetworkXNoPath:
        return "Don't Go"

# Function for Bellman-Ford's shortest path decision
def bellman_ford_decision(graph, start, end):
    try:
        length, path = nx.single_source_bellman_ford(graph, start)
        return 'Go' if len(path[end]) % 2 == 0 else "Don't Go"
    except (nx.NetworkXNoPath, nx.NetworkXUnbounded):
        return "Don't Go"

# Monte Carlo simulation for random decision based on probability distribution
def monte_carlo_simulation(trials):
    go_count = 0
    no_go_count = 0
    for _ in range(trials):
        if random.random() < 0.5:
            go_count += 1
        else:
            no_go_count += 1
    return 'Go' if go_count > no_go_count else "Don't Go"

# Random walk for decision making
def random_walk(steps):
    position = 0
    for _ in range(steps):
        step = random.choice([-1, 1])
        position += step
    return 'Go' if position > 0 else "Don't Go"

# Weighted random choice for unbiased decision
def weighted_random_choice():
    choices = ['Go', 'Don\'t Go']
    weights = [0.5, 0.5]
    return random.choices(choices, weights=weights, k=1)[0]

# Simulated Annealing for decision making
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

# Genetic Algorithm for decision making
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

# Combining all algorithms for final decision
def complex_decision():
    # Create a random graph for shortest path algorithms
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

# Main execution
print('You have an invitation today, which is not so important to you.')
print("Because if it was important to you,")
print("Then you wouldn't write 70 lines of code to generate an unbiased opinion!!")
print("Now say, Should I proceed with further operation?")
ansdao = input("Please input only yes/no or y/n: ").strip().lower()

if ansdao in ["yes", "y"]:
    # Generate the decision
    decision = complex_decision()
    print("Decision:", decision)
elif ansdao in ["no", "n"]:
    print("I know you do know Python!!")
    print("But I'm not your girlfriend!!!")
    print("Please take your decision on your own, NOW!!")
    print("You are a big ass mofo!!")
    print("Boring Devs!!!!!")
    print("Bye!!!")
else:
    print("Invalid input! Please enter yes/no or y/n.")
