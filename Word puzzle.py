def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1)
    ]
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                rr, cc = r, c
                matched = True
                for i in range(word_len):
                    if 0 <= rr < rows and 0 <= cc < cols:
                        if grid[rr][cc] != word[i]:
                            matched = False
                            break
                    else:
                        matched = False
                        break
                    rr += dr
                    cc += dc
                if matched:
                    return (r, c), (rr - dr, cc - dc), (dr, dc)
    return None

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def mark_word(grid, start, end, direction, mark_char='*'):
    r, c = start
    dr, dc = direction
    word_len = max(abs(end[0] - start[0]), abs(end[1] - start[1])) + 1
    for _ in range(word_len):
        grid[r][c] = mark_char
        r += dr
        c += dc

if __name__ == "__main__":
    grid = [
        list("aoxprlpenqwertyuiozxcv"),
        list("lpzxmqporangexcvbnmkj"),
        list("ewqlkjhgapleomnbvczxq"),
        list("orpxysdfghjklzxcvbnml"),
        list("nmapplepqowierutylkjh"),
        list("qwaszxorangepoiuytbnm"),
        list("lkjhgfdsmapplewqertzxc"),
        list("zxcvmnborangeklijuhytr"),
        list("plmoknijbuhvygctfrzxe"),
        list("qazwsxedcrfvtgbyhnplm"),
        list("plmoknijbuhvygctfrzxc"),
        list("qazwsxedcrfvtgbyhnplk"),
        list("plmoknijbuhvygctfrzxc"),
        list("qazwsxedcrfvtgbyhnplk"),
        list("plmoknijbuhvygctfrzxc"),
        list("qazwsxedcrfvtgbyhnplk"),
        list("plmoknijbuhvygctfrzxc"),
        list("qazwsxedcrfvtgbyhnplk"),
        list("plmoknijbuhvygctfrzxc"),
        list("qazwsxedcrfvtgbyhnplk"),
        list("mncbvaporangelyuiopsdf"),
        list("appleqwertyuiopasdfghj"),
    ]

    words_to_find = [
        'apple', 'orange', 'banana', 'grape', 'melon', 'kiwi',
        'peach', 'plum', 'cherry', 'pear', 'mango', 'lemon',
        'lime', 'apricot', 'fig', 'date', 'guava', 'papaya',
        'berry', 'coconut'
    ]

    print("Original Grid:")
    print_grid(grid)

    for word in words_to_find:
        result = find_word(grid, word)
        if result:
            start, end, direction = result
            print(f"'{word}' found from {start} to {end} in direction {direction}")
            mark_word(grid, start, end, direction)
        else:
            print(f"'{word}' not found.")

    print("\nGrid with marked words (*):")
    print_grid(grid)

