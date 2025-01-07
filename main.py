def process_rover_movements(plateau, rover_start, commands):
    directions = ['N', 'E', 'S', 'W']
    move_changes = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    try:
        x, y, direction = rover_start.split()
        x, y = int(x), int(y)
    except ValueError:
        return "Invalid starting position"

    if direction not in directions:
        return "Invalid direction"

    if not (0 <= x <= plateau[0] and 0 <= y <= plateau[1]):
        return "Starting position out of bounds"

    for command in commands:
        if command == 'L':
            direction = directions[(directions.index(direction) - 1) % 4]
        elif command == 'R':
            direction = directions[(directions.index(direction) + 1) % 4]
        elif command == 'M':
            dx, dy = move_changes[direction]
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x <= plateau[0] and 0 <= new_y <= plateau[1]:
                x, y = new_x, new_y
        else:
            return "Invalid command encountered"

    return f"{x} {y} {direction}"


def main():
    print("Enter the upper-right coordinates of the plateau (e.g., '5 5'):")
    try:
        plateau_input = input()
        plateau_x, plateau_y = map(int, plateau_input.split())
        if plateau_x < 0 or plateau_y < 0:
            print("Plateau dimensions cannot be negative.")
            return
    except ValueError:
        print("Invalid plateau dimensions input.")
        return

    plateau = (plateau_x, plateau_y)
    results = []
    while True:
        print("Enter the rover's starting position (e.g., '1 2 N') or type 'STOP' to finish:")
        rover_start = input().strip()
        if rover_start.upper() == 'STOP':
            break

        print("Enter the rover's movement commands (e.g., 'LMLMLMLMM'):")
        commands = input().strip()
        result = process_rover_movements(plateau, rover_start, commands)
        results.append(result)

    print("Final positions of the rovers:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
