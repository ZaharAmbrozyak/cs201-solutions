def task_12(inp='input.txt', output='summary.txt') -> None:
    with open(inp, 'r') as f:
        data = f.read()

    characters = f"Characters: {len(data)}"
    lines = f"Lines: {data.count('\n') + 1}"
    words = f"Words: {data.count(' ')}"
    out = '\n'.join((characters, lines, words))

    with open(output, 'w') as f:
        f.write(out)

task_12()