import random

import pytest
from sort_modules.heap_sort import heap_sort, heapify

# unit тесты


def test_heapify_work():
    """Тест функции heapify на корректность"""
    arr = [1, 3, 2]
    heapify(arr, 3, 0)
    assert arr == [3, 1, 2]


def test_duplicate_elements():
    """Тест с дубликатами"""
    assert heap_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_negative_numbers():
    """Тест с отрицательными числами"""
    assert heap_sort([-5, 3, -1, 0, 2]) == [-5, -1, 0, 2, 3]


# крайние случаи


def test_empty_list():
    """Тест пустого списка"""
    assert heap_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert heap_sort([5]) == [5]


def test_sorted_list():
    """Тест уже отсортированного списка"""
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    """Тест обратно отсортированного списка"""
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_large_list():
    """Тест большого списка"""
    lst = list(range(1000, 0, -1))
    expected = list(range(1, 1001))
    assert heap_sort(lst) == expected


# параметризованный тест


@pytest.mark.parametrize(
    "arr, expected",
    [([], []), ([5], [5]), ([3, 1], [1, 3]), ([3, 1, 5, 7], [1, 3, 5, 7])],
)
def test_heap_sort_main(arr, expected):
    assert heap_sort(arr) == expected


# property-based тесты


def test_property_idempotence():
    """Повторная сортировка не меняет результат"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        sorted_once = heap_sort(lst.copy())
        sorted_twice = heap_sort(sorted_once.copy())
        assert sorted_once == sorted_twice


def test_property_length_preservation():
    """Длина списка сохраняется"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        assert len(heap_sort(lst)) == len(lst)


def test_property_sorted_order():
    """Результат должен быть отсортирован"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(1, 100))]
        sorted_lst = heap_sort(lst)
        for i in range(1, len(sorted_lst)):
            assert sorted_lst[i - 1] <= sorted_lst[i]


def test_against_builtin_sort():
    """Сравнение со встроенной сортировкой Python"""
    for _ in range(100):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 100))]
        assert heap_sort(lst.copy()) == sorted(lst)
