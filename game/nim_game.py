def nim_game(n, k):
    return n % (k+1) != 0

if __name__ == "__main__":
    n = 5
    k = 3
    print(f"Winning the game {nim_game(n, k)}")
