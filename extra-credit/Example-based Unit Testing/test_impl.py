import impl
import pytest

FULL_BOARD_CONFIG = 'xoxoxxoxo'

def test_tic_tac_toe_check_x_based_winning_pattern():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[6] = 'x'
    assert impl.tic_tac_toe_check(tmp1) ==  'x', "fails to recognize x based winning pattern"

    
def test_tic_tac_toe_check_o_based_winning_pattern():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[2] = 'o'
    tmp1[5] = 'o'
    assert impl.tic_tac_toe_check(tmp1) ==  'o', "fails to recognize x based winning pattern"


def test_tic_tac_toe_check_no_winning_pattern():
    tmp1 = list(FULL_BOARD_CONFIG)
    assert impl.tic_tac_toe_check(tmp1) ==  None, "fails to return None when there is no winner"


def test_tic_tac_toe_check_partial_board():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[0] = ''
    assert impl.tic_tac_toe_check(tmp1) ==  None, "fails to return None when there is no winner"
    
    
def test_tic_tac_toe_check_multiple_winning_patterns1():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[8] = 'x'
    tmp1[0] = 'o'
    with pytest.raises(ValueError, message="does not flag multiple winning patterns"):
        impl.tic_tac_toe_check(tmp1)

def test_tic_tac_toe_check_multiple_winning_patterns2():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[8] = 'x'
    tmp1[3] = 'x'
    with pytest.raises(ValueError, message="does not flag multiple x winning patterns"):
        impl.tic_tac_toe_check(tmp1)

def test_tic_tac_toe_check_multiple_winning_patterns3():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[0] = 'o'
    tmp1[7] = 'o'
    with pytest.raises(ValueError, message="does not flag multiple o winning patterns"):
        impl.tic_tac_toe_check(tmp1)

    
def test_tic_tac_toe_check_not_x():
    tmp1 = list(FULL_BOARD_CONFIG.replace('x', 'm'))
    with pytest.raises(ValueError, message="does not flag invalid symbols"):
        impl.tic_tac_toe_check(tmp1)


def test_tic_tac_toe_check_not_o():
    tmp1 = list(FULL_BOARD_CONFIG.replace('o', 'd'))
    with pytest.raises(ValueError, message="does not flag invalid symbols"):
        impl.tic_tac_toe_check(tmp1)
    

def test_tic_tac_toe_check_not_empty_string():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[0] = ' '
    with pytest.raises(ValueError, message="does not flag invalid empty position string"):
        impl.tic_tac_toe_check(tmp1)
    

def test_tic_tac_toe_check_multiple_symbols():
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[0] = 'y'
    with pytest.raises(ValueError, message="does not flag invalid symbols"):
        impl.tic_tac_toe_check(tmp1)
    

def test_tic_tac_toe_check_invalid_symbol_type1():
    with pytest.raises(TypeError, message="does not flag invalid arg type"):
        impl.tic_tac_toe_check([1] * 9)
    with pytest.raises(TypeError, message="does not flag invalid arg type"):
        impl.tic_tac_toe_check([None] * 9)
    tmp1 = list(FULL_BOARD_CONFIG)
    tmp1[0] = 1
    with pytest.raises(TypeError, message="does not flag invalid arg type"):
        impl.tic_tac_toe_check(tmp1)


def test_tic_tac_toe_check_incorrect_board_size1():
    with pytest.raises(ValueError, message="does not flag invalid board size"):
        impl.tic_tac_toe_check(list('oxo'))


def test_tic_tac_toe_check_incorrect_board_size2():
    with pytest.raises(ValueError, message="does not flag invalid board size"):
        impl.tic_tac_toe_check(list('oxxooxxoooxx'))
    

def test_tic_tac_toe_check_incorrect_board_type1():
    with pytest.raises(TypeError, message="does not flag invalid arg type"):
        impl.tic_tac_toe_check(None)


def test_tic_tac_toe_check_incorrect_board_type2():
    with pytest.raises(TypeError, message="does not flag invalid arg type"):
        impl.tic_tac_toe_check(3)

