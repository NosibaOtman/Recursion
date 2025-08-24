from ex7_helper import *
from typing import List, Any


def mult(x: float, y: int) -> float:
    "function Which receives the number x) float (and the number y which is a non-negative integer (int,) and returns The result of the calculation of x double y"
    if y == 0:
        return 0
    else:
        return add(x, mult(x, (subtract_1(y))))



def is_even(n: int) -> bool:
    "A function that checks if the number is even"
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return (is_even(subtract_1(subtract_1(n))))




def log_mult(x: float, y: int) -> float:
    "A function that multiplies the x and y tck implementation Its must be while logarithmic running"
    if (x == 0) or (y == 0):
        return 0.0
    k = log_mult(x, divide_by_2(y))
    if not is_odd(y):
        return add(k, k)
    else:
        return add(add(k, k), x)



def reverse(s: str) -> str:
    "A function that receives a string of characters (str (s), and returns the string that contains the Same characters as s, but in reverse order"
    return reverse_helper(s)


def reverse_helper(s: str, index: int = 0, new: str = "") -> str:
    if index >= len(s):
        return new
    return reverse_helper(s, index + 1, append_to_end(new, s[-index - 1]))



def is_power_helper(b: int, x: int, c: int) -> bool:
    if b > x:
        return False
    if b == x:
        return True

    return is_power_helper(int(log_mult(b, c)), x, c)


def is_power(b: int, x: int) -> bool:
    "Test function Is there a non-negative integer n such that b to the power of n is equal to x"
    if b == x:
        return True
    if b == 1 or b == 0:
        return False
    if x == 1:
        return True
    if b > x:
        return False
    return is_power_helper(b, x, b)



def number_of_one(n: int, count: int) -> int:
    if n == 0:
        return count
    if n % 10 == 1:
        count += 1
    return number_of_one(n // 10, count)


def number_of_ones_helper(n: int, number: int) -> int:
    if n == 0:
        return number
    number += number_of_one(n, 0)
    return number_of_ones_helper(n - 1, number)


def number_of_ones(n: int) -> int:
    "Returns the number The times the digit '1' appears in all numbers from 1 to n"
    return number_of_ones_helper(n, 0)


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    "Function, solving the game Ornamental Towers"
    if n >= 1:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n - 1, temp, dst, src)
    else:
        return


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    "Receives two two-dimensional lists of numbers (all One of them is represented by a list of number lists). The function returns True if the two lists Identical dimensions in all their value"
    return helper_compare_lists(l1, l2)


def helper_compare_lists(l1: List[Any], l2: List[Any], a: int=0) -> bool:
    if a >= len(l1) or a >= len(l2):
        return len(l1) == len(l2)
    if isinstance(l1[a], list):
        return helper_compare_lists(l1[a], l2[a], 0) and helper_compare_lists(
            l1, l2, a + 1)
    return l1[a] == l2[a] and helper_compare_lists(l1, l2, a + 1)




def magic_list_helper(n: int, lst: List[Any]) -> List[Any]:
    if n == 0:
        return lst
    return_lst = magic_list_helper(n-1, lst)
    lst.append(magic_list_helper(n-1, []))
    return return_lst


def magic_list(n: int) -> List[Any]:
    """"""
    lst: List[Any] = []
    magic_list_helper(n, lst)
    return lst

