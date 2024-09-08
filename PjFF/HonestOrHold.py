import numpy as np
from collections import Counter

# Define the updated payoff matrix
payoff_matrix = {
    ('honest', 'honest'): (3, 3),
    ('honest', 'hold'): (1, 2),
    ('honest', 'lie'): (-1, 4),
    ('hold', 'honest'): (2, 1),
    ('hold', 'hold'): (0, 0),
    ('hold', 'lie'): (1, 3),
    ('lie', 'honest'): (4, -1),
    ('lie', 'hold'): (3, 1),
    ('lie', 'lie'): (-2, -2)
}

# List of all strategies
strategies_A = ['honest', 'hold', 'lie']
strategies_B = ['honest', 'hold', 'lie']
all_strategies = [(a, b) for a in strategies_A for b in strategies_B]

# Initialize the starting strategy profile
current_strategy = ('hold', 'hold')

def payoff_A(strategy):
    return payoff_matrix[strategy][0]

def payoff_B(strategy):
    return payoff_matrix[strategy][1]

# Create the transition matrices for both players
def create_transition_matrix(player_payoff_func):
    transition_matrix = np.zeros((len(all_strategies), len(all_strategies)))
    
    for i, strategy_i in enumerate(all_strategies):
        for j, strategy_j in enumerate(all_strategies):
            if strategy_i != strategy_j:
                payoff_i = player_payoff_func(strategy_i)
                payoff_j = player_payoff_func(strategy_j)
                transition_matrix[i, j] = np.exp(payoff_j - payoff_i)
        
        # Normalize to form a probability distribution
        transition_matrix[i, :] /= np.sum(transition_matrix[i, :])
    
    return transition_matrix

transition_matrix_A = create_transition_matrix(payoff_A)
transition_matrix_B = create_transition_matrix(payoff_B)

def proposal_distribution(current_strategy, transition_matrix):
    current_index = all_strategies.index(current_strategy)
    proposed_index = np.random.choice(len(all_strategies), p=transition_matrix[current_index])
    return all_strategies[proposed_index]

def metropolis_hastings(iterations):
    strategy_profile = current_strategy
    history = []

    for _ in range(iterations):
        # Alternate between Player A and Player B for proposing new strategies
        if np.random.rand() < 0.5:
            proposed_strategy = proposal_distribution(strategy_profile, transition_matrix_A)
        else:
            proposed_strategy = proposal_distribution(strategy_profile, transition_matrix_B)
        
        current_payoff_A = payoff_A(strategy_profile)
        proposed_payoff_A = payoff_A(proposed_strategy)
        current_payoff_B = payoff_B(strategy_profile)
        proposed_payoff_B = payoff_B(proposed_strategy)
        
        acceptance_ratio_A = np.exp(proposed_payoff_A - current_payoff_A)
        acceptance_ratio_B = np.exp(proposed_payoff_B - current_payoff_B)
        
        acceptance_ratio = acceptance_ratio_A * acceptance_ratio_B
        
        if np.random.rand() < acceptance_ratio:
            strategy_profile = proposed_strategy
        
        history.append(strategy_profile)
    
    return history

# Run the Metropolis-Hastings algorithm
history = metropolis_hastings(10000)

# Analyze the results
strategy_counts = Counter(history)
print(strategy_counts)
