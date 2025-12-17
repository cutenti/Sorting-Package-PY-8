import random

import pytest
from sort_modules.quick_sort import quick_sort, partition

# unit тесты


def test_partition_work():
    """Тест функции partition на корректность"""
    arr = [3, 1, 2, 4]

    pivot_index = partition(arr, 0, 3)
    pivot_value = arr[pivot_index]

    for i in range(0, pivot_index):
        assert arr[i] <= pivot_value  # все элементы слева от pivot <= чем pivot
    for i in range(pivot_index + 1, 4):
        assert arr[i] >= pivot_value  # все элементы справа от pivot >= чем pivot


def test_duplicate_elements():
    """Тест с дубликатами"""
    assert quick_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_negative_numbers():
    """Тест с отрицательными числами"""
    assert quick_sort([-5, 3, -1, 0, 2]) == [-5, -1, 0, 2, 3]


# крайние случаи


def test_empty_list():
    """Тест пустого списка"""
    assert quick_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert quick_sort([5]) == [5]


def test_sorted_list():
    """Тест уже отсортированного списка"""
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    """Тест обратно отсортированного списка"""
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_large_list():
    """Тест большого списка"""
    lst = list(range(1000, 0, -1))
    expected = list(range(1, 1001))
    assert quick_sort(lst) == expected


# параметризованный тест


@pytest.mark.parametrize(
    "arr, expected",
    [([], []), ([5], [5]), ([3, 1], [1, 3]), ([3, 1, 5, 7], [1, 3, 5, 7])],
)
def test_quick_sort_main(arr, expected):
    assert quick_sort(arr) == expected


# property-based тесты


def test_property_idempotence():
    """Повторная сортировка не меняет результат"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        sorted_once = quick_sort(lst.copy())
        sorted_twice = quick_sort(sorted_once.copy())
        assert sorted_once == sorted_twice


def test_property_length_preservation():
    """Длина списка сохраняется"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        assert len(quick_sort(lst)) == len(lst)


def test_property_sorted_order():
    """Результат должен быть отсортирован"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(1, 100))]
        sorted_lst = quick_sort(lst)
        for i in range(1, len(sorted_lst)):
            assert sorted_lst[i - 1] <= sorted_lst[i]


def test_against_builtin_sort():
    """Сравнение со встроенной сортировкой Python"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        assert quick_sort(lst.copy()) == sorted(lst)
