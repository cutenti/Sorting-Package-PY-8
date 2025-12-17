import random

import pytest
from sort_modules.merge_sort import merge_sort

# unit тесты


def test_duplicate_elements():
    """Тест с дубликатами"""
    assert merge_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_negative_numbers():
    """Тест с отрицательными числами"""
    assert merge_sort([-5, 3, -1, 0, 2]) == [-5, -1, 0, 2, 3]


# крайние случаи


def test_empty_list():
    """Тест пустого списка"""
    assert merge_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert merge_sort([5]) == [5]


def test_sorted_list():
    """Тест уже отсортированного списка"""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    """Тест обратно отсортированного списка"""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_large_list():
    """Тест большого списка"""
    lst = list(range(1000, 0, -1))
    expected = list(range(1, 1001))
    assert merge_sort(lst) == expected


# параметризованный тест


@pytest.mark.parametrize(
    "arr, expected",
    [([], []), ([5], [5]), ([3, 1], [1, 3]), ([3, 1, 5, 7], [1, 3, 5, 7])],
)
def test_merge_sort_main(arr, expected):
    assert merge_sort(arr) == expected


# property-based тесты


def test_property_idempotence():
    """Повторная сортировка не меняет результат"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        sorted_once = merge_sort(lst.copy())
        sorted_twice = merge_sort(sorted_once.copy())
        assert sorted_once == sorted_twice


def test_property_length_preservation():
    """Длина списка сохраняется"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        assert len(merge_sort(lst)) == len(lst)


def test_property_sorted_order():
    """Результат должен быть отсортирован"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(1, 100))]
        sorted_lst = merge_sort(lst)
        for i in range(1, len(sorted_lst)):
            assert sorted_lst[i - 1] <= sorted_lst[i]


def test_against_builtin_sort():
    """Сравнение со встроенной сортировкой Python"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        assert merge_sort(lst.copy()) == sorted(lst)
