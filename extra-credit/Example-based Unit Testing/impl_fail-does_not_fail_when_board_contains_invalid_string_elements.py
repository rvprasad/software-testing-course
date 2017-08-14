
def find_wins_for_symbol(bc, symbol):
    ret = 0
    # rows
    tmp1 = lambda x: bc[x] == bc[x + 1] == bc[x + 2] == symbol
    ret += tmp1(0) + tmp1(3) + tmp1(6)
    
    # cols
    tmp1 = lambda x: bc[x] == bc[x + 3] == bc[x + 6] == symbol
    ret += tmp1(0) + tmp1(1) + tmp1(2)
    
    # diagonals
    ret += bc[0] == bc[4] == bc[8] == symbol
    ret += bc[2] == bc[4] == bc[6] == symbol
    
    return ret


def tic_tac_toe_check(board_config):
    if not isinstance(board_config, list):
        raise TypeError("Board configuration should be a list")
    
    if len(board_config) != 9:
        raise ValueError("Board configuration should have 9 entries")
    
    if not all(isinstance(x, str) for x in board_config):
        raise TypeError("Each element in the board configuration should be a string")
        
    #if any(x != 'x' and x != 'o' and x != '' for x in board_config):
    #    raise ValueError("Board configuration should only contain x or o symbols")

    x_wins = find_wins_for_symbol(board_config, 'x')
    o_wins = find_wins_for_symbol(board_config, 'o')
    
    if x_wins + o_wins > 1:
        raise ValueError("Multiple winning patterns")
    elif x_wins == 1:
        return 'x'
    elif o_wins == 1:
        return 'o'
