import random

# Define the deck of 52 cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]


def is_four_of_a_kind(hand):
    rank_counts = {}
    for card in hand:
        rank = card['rank']
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    return 4 in rank_counts.values()


N = 1000000  # Number of experiments
success_count = 0

for _ in range(N):
    # Shuffle the deck and draw 5 cards
    random.shuffle(deck)
    hand = random.sample(deck, 5)

    if is_four_of_a_kind(hand):
        success_count += 1

# Calculate the probability of success
probability_of_success = success_count / N

print(f"Number of successes: {success_count}")
print(f"Probability of getting 4 of a kind: {probability_of_success:.6f}")
