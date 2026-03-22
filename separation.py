import time
from random import randint


def how_long_can(func):
    def wrapper(*args, **kwargs):
        print(f"Вид сортировки: {func.__name__}")
        start = time.time()
        print("Loading...")
        func(*args, **kwargs)
        end = time.time()
        time.sleep(1)
        print(f"Время выполнения: {(end - start):.10f}")
        print("--------------------------------------")

    return wrapper


@how_long_can
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


@how_long_can
def quick_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


@how_long_can
def selection_sort(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


@how_long_can
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break


@how_long_can
def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

# quick_sort()
arr = [randint(0, 100) for _ in range(10)]
quick_sort(arr)

# bubble_sort()
arr = [randint(0, 100) for _ in range(10)]
bubble_sort(arr)

# selection_sort()
arr = [randint(0, 100) for _ in range(10)]
selection_sort(arr)

# insertion_sort()
arr = [randint(0, 100) for _ in range(10)]
insertion_sort(arr)

# gnome_sort()
arr = [randint(0, 100) for _ in range(10)]
gnome_sort(arr)


# Quick Sort - Маленький массив самый быстрый
# Insertion Sort - Маленький массив самый медленный
# Selection Sort - Большой массив самый быстрый
# Bubble Sort - Стабильный, средний
# Gnome Sort - Большой массив самый медленный
