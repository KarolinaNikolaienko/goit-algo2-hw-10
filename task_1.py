import random
import statistics
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо випадковий індекс для опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо середній індекс для опорного елемента
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

if __name__ == "__main__":
    test_arr_sizes = [10000, 50000, 100000, 500000]
    results_rand = {}
    results_determ = {}

    for size in test_arr_sizes:
        test_arr = []
        for _ in range(size):
            test_arr.append(random.randint(-size, size))

        rand_sort_times = []
        determ_sort_times = []
        for _ in range(5):
            start = time.time()
            rand_sorted_arr = randomized_quick_sort(test_arr)
            rand_sort_time = time.time() - start
            rand_sort_times.append(rand_sort_time)

            start = time.time()
            determ_sorted_arr = randomized_quick_sort(test_arr)
            determ_sort_time = time.time() - start
            determ_sort_times.append(determ_sort_time)


        results_rand[size] = statistics.fmean(rand_sort_times)
        results_determ[size] = statistics.fmean(determ_sort_times)

    for size in test_arr_sizes:
        print(f"\nРозмір масиву: {size}")
        print(f"\tРандомізований QuickSort: {results_rand[size]} секунд"
              f"\n\tДетермінований QuickSort: {results_determ[size]} секунд")

    fig, ax = plt.subplots()

    ax.plot(test_arr_sizes, results_rand.values(), 'o-', linewidth=2, label="Рандомізований QuickSort")
    ax.plot(test_arr_sizes, results_determ.values(), 'o-', linewidth=2, color="orange", label="Детермінований QuickSort")

    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого і детермінованого QuickSort")

    ax.legend(loc='upper left')

    plt.show()