import random

from sort_modules.heap_sort import heap_sort
from sort_modules.merge_sort import merge_sort
from sort_modules.quick_sort import quick_sort


# Сравнение с другими сортировками


def test_heap_sort_against_quick_sort():
    """Сравнение heap_sort с quick_sort"""
    for _ in range(50):
        lst = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        assert heap_sort(lst.copy()) == quick_sort(lst.copy())


def test_heap_sort_against_merge_sort():
    """Сравнение heap_sort с merge_sort"""
    for _ in range(50):
        lst = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        assert heap_sort(lst.copy()) == merge_sort(lst.copy())


def test_merge_sort_against_quick_sort():
    """Сравнение quick_sort с merge_sort"""
    for _ in range(50):
        lst = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        assert merge_sort(lst.copy()) == quick_sort(lst.copy())
