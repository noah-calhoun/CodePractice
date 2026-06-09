def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    # collect all positions where s and goal differ
    diff_positions = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_positions.append(i)

    # more than 2 differences means no single swap can fix it
    if len(diff_positions) > 2:
        return False

    # exactly 2 differences -- check if swapping those two chars in s gives us goal
    if len(diff_positions) == 2:
        i = diff_positions[0]
        j = diff_positions[1]

        # for a swap to work:
        # the char at i in s must equal the char at i in goal after the swap
        # meaning s[i] needs to move to position j, so s[i] == goal[j]
        # and s[j] needs to move to position i, so s[j] == goal[i]
        s_char_at_i = s[i]
        s_char_at_j = s[j]
        goal_char_at_i = goal[i]
        goal_char_at_j = goal[j]

        if s_char_at_i == goal_char_at_j and s_char_at_j == goal_char_at_i:
            return True
        else:
            return False

    # zero differences means s == goal already
    # we can only return True if there's a duplicate character in s
    # because then we can swap the two duplicates and the string stays the same
    if len(diff_positions) == 0:
        seen_chars = set()
        for char in s:
            if char in seen_chars:
                return True  # found a duplicate, valid swap exists
            seen_chars.add(char)
        return False  # no duplicates, any swap would change the string

    # this handles the len == 1 case, which can never be fixed with one swap
    return False

if __name__ == "__main__":
    s = "abcd" 
    goal = "cbad"
    print(buddyStrings(s, goal))
