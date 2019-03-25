import heapq


LEFT = 0
RIGHT = 1
HEIGHT = 2


def flat_building_positions(buildings):
    positions = []
    for b_id, b in enumerate(buildings):
        left, right, height = b
        positions.append((left, LEFT, height, b_id))
        positions.append((right, RIGHT, height, b_id))
    return sorted(positions)


def skyline(buildings):
    positions = flat_building_positions(buildings)
    print(f"buildings' positions: {positions}")

    heap = []
    def_height = 0
    def_building = -1
    active_builds = set()

    heapq.heappush(heap, (def_height, def_building))
    active_builds.add(def_building)
    prev_height = def_height

    r = []
    for p in positions:
        x, l_or_r, height, b_id = p
        if l_or_r == LEFT:
            heapq.heappush(heap, (-height, b_id))
            active_builds.add(b_id)
        else:
            active_builds.remove(b_id)

        while True:
            max_height, b_id = heap[0]
            if b_id not in active_builds:
                heapq.heappop(heap)
            else:
                break

        print(f"heap: {heap}, active builds: {active_builds}")
        max_height = -max_height
        if max_height != prev_height:
            r.append((x, max_height))
            prev_height = max_height
    return r


if __name__ == "__main__":
    builds = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    r = skyline(builds)
    print(f"skyline is {r}")