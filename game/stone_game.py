def stone_game(piles, stones, player=0, level=0):
    sz = len(piles)
    if sz == 1:
        player_win = stones[player] + piles[0] > stones[1-player]
        print(f"{level*4*' '}player {player} win {player_win} with stones: {stones} piles: {piles}")
        return player_win

    for i in [0, -1]:
        new_piles = piles[1:] if i == 0 else piles[:-1]
        stones[player] += piles[i]
        other_win = stone_game(new_piles, stones, 1-player, level+1)
        stones[player] -= piles[i]
        if not other_win:
            print(f"{level*4*' '}player {player} win with stones: {stones} piles: {piles}")
            return True

    print(f"{level*4*' '}player {player} lose with stones: {stones} piles: {piles}")
    return False

if __name__ == "__main__":
    piles = [5,3,4,5]
    stones = [0, 0]
    player = 0
    alex_win = stone_game(piles, stones, player)
    print(f"alex win {alex_win}")