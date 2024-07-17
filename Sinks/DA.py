def read_file_contents(file_path: str, encoding: str = 'utf-8', mode:str = 'r',) -> str:
    """Read the contents of the file"""
    file_contents = ""
    try:
        with open(file_path, mode=mode, encoding=encoding) as file:
            file_contents = file.read()
    except UnicodeDecodeError as e:
        print(f"Error reading file {file_path}: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")

    return file_contents
    
def build_grid(file_path: str) -> list[list[str]]:
    """Build a system grid from the input file"""
    max_rows = 0
    max_cols = 0
    file_contents = read_file_contents(file_path)

    lines = file_contents.split("\n")

    # Get the grid dimensions and fill it with empty spaces
    for line in lines:
        line_parts = line.split(" ")
        max_cols = max(max_cols, int(line_parts[1]))
        max_rows = max(max_rows, int(line_parts[2]))
    
    grid = [[" " for _ in range(max_cols + 1)] for _ in range(max_rows + 1)]

    # Fill the grid with the sinks, pipes and sources
    for line in lines:
        line_parts = line.split(" ")
        item = line_parts[0]
        x = int(line_parts[1])
        y = int(line_parts[2])

        grid[y][x] = item;
    
    return grid

def get_source_position(grid: list[list[str]]) -> tuple[int, int]:
    """Get the position of the source in the grid"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "*":
                return (i, j)
    return (-1, -1)

def are_connected(cell1: str, cell2: str, dx, dy, pipe_openings) -> bool:
    """Check if two cells are connected"""
    if cell1 == ' ' or cell2 == ' ':
        return False
    if cell1 == "*" or cell2 == "*":
        return True
    if cell1.isalpha() or cell2.isalpha():
        return True
    c1_to_c2 = (dy, dx) in pipe_openings.get(cell1, [])
    c2_to_c1 = (-dy, -dx) in pipe_openings.get(cell2, [])
    return c1_to_c2 and c2_to_c1

def check_conected_sinks(file_path: str) -> str:
    """ Check all the connected sinks in the system"""

    # Build the grid from the input file
    grid = build_grid(file_path)
    print_grid(grid)

    directions = [(1, 0),(-1, 0),(0, 1), (0, -1)]
    pipe_openings = {
        '═': [(0, 1), (0, -1)],
        '║': [(1, 0), (-1, 0)],
        '╔': [(0, 1), (-1, 0)],
        '╗': [(0, -1), (-1, 0)],
        '╚': [(0, 1), (1, 0)],
        '╝': [(0, -1), (1, 0)],
        '╠': [(1, 0), (-1, 0), (0, 1)],
        '╣': [(1, 0), (-1, 0), (0, -1)],
        '╦': [(0, 1), (0, -1), (-1, 0)],
        '╩': [(0, 1), (0, -1), (1, 0)]
    }

    connected_sinks = set()
    source_pos = get_source_position(grid)

    # If there is no source, return an empty string
    if source_pos == (-1, -1):
        return "".join(connected_sinks)
    visited = set()
    queue = [source_pos]

    while queue:
        y,x = queue.pop(0)
        if (y,x) in visited:
            continue
        visited.add((y,x))

        # Check all four directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (ny, nx) not in visited:
                if are_connected(grid[y][x], grid[ny][nx], dx, dy, pipe_openings):
                    queue.append((ny, nx))
                    if grid[ny][nx].isalpha():
                        connected_sinks.add(grid[ny][nx])
    
    return "".join(connected_sinks)

def print_grid(grid):
    for row in reversed(grid):
        print(row)


if __name__ == '__main__':
    test_file = "a.txt"
    sinks = check_conected_sinks(test_file)
    print(f"Connected sinks: {sinks}")