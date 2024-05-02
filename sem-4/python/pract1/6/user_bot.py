from collections import deque


def shortest_path_to_gold(source_point, check) -> "list[str]":
    q = deque()
    reached = set()
    parents = {}
    q.append(source_point)
    while len(q):
        current = q.popleft()
        reached.add(current)
        if check("gold", current[0], current[1]):
            path_points = [current]

            while parents.get(path_points[-1], None) is not None:
                path_points.append(parents[path_points[-1]])
            path_points.reverse()
            path_commands = []

            for i, p in enumerate(path_points[1:]):
                if p[0] - path_points[i][0] == 1:
                    path_commands.append("right")
                elif p[0] - path_points[i][0] == -1:
                    path_commands.append("left")
                elif p[1] - path_points[i][1] == 1:
                    path_commands.append("down")
                elif p[1] - path_points[i][1] == -1:
                    path_commands.append("up")
                else:
                    raise Exception("don't know where to go")  # debug
            return path_commands

        adjacent_cells = [
            (current[0] + 1, current[1]),
            (current[0], current[1] + 1),
            (current[0] - 1, current[1]),
            (current[0], current[1] - 1)
        ]

        for p in adjacent_cells:
            if not check("wall", p[0], p[1]) and p not in reached:
                q.append(p)
                reached.add(p)
                parents[p] = current
    return []


def script(check, x, y):
    if check("gold", x, y) and check("player", x, y):
        return "take"
    if check("player", x, y):
        return shortest_path_to_gold((x, y), check)[0]
    return "pass"
