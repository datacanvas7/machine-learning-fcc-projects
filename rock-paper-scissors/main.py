from strategies import play, mrugesh, abbey, quincy, kris
from RPS import player

# Test against each bot
print("Testing against Quincy:")
play(player, quincy, 1000, verbose=False)

print("\nTesting against Abbey:")
play(player, abbey, 1000, verbose=False)

print("\nTesting against Kris:")
play(player, kris, 1000, verbose=False)

print("\nTesting against Mrugesh:")
play(player, mrugesh, 1000, verbose=False)