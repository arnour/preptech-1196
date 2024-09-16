from pytest import mark


def insertion_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


def selection_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        lowest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]


def bubble_sort(arr: list[int]) -> None:
    any_swaps = False
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                any_swaps = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not any_swaps:
            return


def heap_sort(arr: list[int]) -> None:
    def build_heap(arr: list[int]) -> None:
        # comeca da metade para o inicia para garantir as propriedades
        # da heap: Arr[Pai] >= Arr[Filho]
        # i:= N/2 até N são folhas, por isso não precisam ser checadas,
        # serao avaliadas na recursao a partir de seus pais
        for i in range(len(arr) // 2, -1, -1):
            heapfy(arr, len(arr), i)

    def heapfy(arr: list[int], n: int, i: int) -> None:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        # seleciona o no de maior valor entre o pai e seus filhos
        if left < n and arr[left] > arr[i]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        # se o no de maior valor nao for o pai, precisa troca-los
        # e recomecar o heapfy a partir da posicao filho que foi trocada
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapfy(arr, n, largest)

    if len(arr) < 2:
        return

    build_heap(arr)

    # Sort
    # Coloca o maior valor (no raiz) no final do array
    # E aplica o heapfy no novo array de tamanho N = N-1
    for k in range(len(arr), 0, -1):
        arr[0], arr[k - 1] = arr[k - 1], arr[0]
        heapfy(arr, k - 1, 0)


def merge_sort(arr: list[int]) -> None:
    def split(arr: list[int], left: int, right: int) -> None:
        if left < right:
            middle = left + (right - left) // 2
            split(arr, left, middle)
            split(arr, middle + 1, right)
            merge(arr, left, middle, right)
            return

    def merge(arr: list[int], left: int, middle: int, right: int) -> None:
        left_size = middle - left + 1
        right_size = right - middle
        left_arr = [0] * left_size
        right_arr = [0] * right_size
        for i in range(left_size):
            left_arr[i] = arr[left + i]
        for i in range(right_size):
            right_arr[i] = arr[middle + 1 + i]
        i, j, k = 0, 0, left
        while i < left_size and j < right_size:
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < left_size:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < right_size:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    split(arr, 0, len(arr) - 1)


def quick_sort(arr: list[int]) -> None:
    def find_pivot_position(arr: list[int], left: int, right: int):
        pivot = arr[left]
        i = left + 1
        j = right
        while i <= j:
            # while elements to the right are greater-equal than pivot, decrement j
            while i <= j and arr[j] >= pivot:
                j -= 1
            # while elements to the left are lesser than pivot increment i
            while i <= j and arr[i] <= pivot:
                i += 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[left], arr[j] = arr[j], arr[left]
        return j

    def sort(arr: list[int], left: int, right: int) -> None:
        if left < right:
            partition = find_pivot_position(arr, left, right)
            sort(arr, left, partition - 1)
            sort(arr, partition + 1, right)

    sort(arr, 0, len(arr) - 1)


def counting_sort(arr: list[int]) -> None:
    if len(arr) < 2:
        return
    max_value = max(arr)
    frequency = [0] * (max_value + 1)
    for i in arr:
        frequency[i] += 1
    for i in range(1, len(frequency)):
        frequency[i] += frequency[i - 1]
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        result[frequency[arr[i]] - 1] = arr[i]
        frequency[arr[i]] -= 1

    for i in range(0, len(arr)):
        arr[i] = result[i]


# #######################
# Tests
# #######################


@mark.parametrize(
    "arr, expected",
    [
        ([9, 8, 7, 1, 2, 6], [1, 2, 6, 7, 8, 9]),
        ([0, 0, 0], [0, 0, 0]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_sort_using_insertion_sort(arr, expected) -> None:
    insertion_sort(arr)
    assert arr == expected


@mark.parametrize(
    "arr, expected",
    [
        ([9, 8, 7, 1, 2, 6], [1, 2, 6, 7, 8, 9]),
        ([0, 0, 0], [0, 0, 0]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_sort_using_selection_sort(arr, expected) -> None:
    selection_sort(arr)
    assert arr == expected


@mark.parametrize(
    "arr, expected",
    [
        ([9, 8, 7, 1, 2, 6], [1, 2, 6, 7, 8, 9]),
        ([0, 0, 0], [0, 0, 0]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_sort_using_buble_sort(arr, expected) -> None:
    bubble_sort(arr)
    assert arr == expected


@mark.parametrize(
    "arr, expected",
    [
        ([9, 8, 7, 1, 2, 6], [1, 2, 6, 7, 8, 9]),
        ([0, 0, 0], [0, 0, 0]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 1, 2], [1, 2, 3, 4, 5]),
        ([1, 9, 8, 5, 3, 7, 4], [1, 3, 4, 5, 7, 8, 9]),
        ([1, 8, 5, 3, 7, 4, 9], [1, 3, 4, 5, 7, 8, 9]),
    ],
)
def test_sort_using_heap_sort(arr, expected) -> None:
    heap_sort(arr)
    assert arr == expected


@mark.parametrize(
    "arr, expected",
    [
        ([4, 1], [1, 4]),
        ([4, 1, 3, 2, 5], [1, 2, 3, 4, 5]),
        ([], []),
        ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]),
    ],
)
def test_sort_using_merge_sort(arr, expected) -> None:
    merge_sort(arr)
    assert arr == expected


@mark.parametrize(
    "arr, expected",
    [
        ([5, 9, 8, 1, 3, 7, 4], [1, 3, 4, 5, 7, 8, 9]),
        ([4, 1], [1, 4]),
        ([4, 1, 3, 2, 5], [1, 2, 3, 4, 5]),
        ([], []),
        ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]),
    ],
)
def test_sort_using_quick_sort(arr, expected) -> None:
    quick_sort(arr)
    assert arr == expected


@mark.parametrize(
    "arr, expected",
    [
        ([5, 9, 8, 1, 3, 7, 4], [1, 3, 4, 5, 7, 8, 9]),
        ([4, 1], [1, 4]),
        ([4, 1, 3, 2, 5], [1, 2, 3, 4, 5]),
        ([], []),
        ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]),
    ],
)
def test_sort_using_counting_sort(arr, expected) -> None:
    counting_sort(arr)
    assert arr == expected
