"""Min and max heap sorting algorithm"""


def max_heap(array, size, root):
    """
    Heap a binary tree such that the root of the tree has the largest element.

    Given a binary tree with a root, find if the root is the largest or if
    the left or right branch is larger. If so then respectively replace it
    with the root.

    Args:
        array: A list of integers representing the array and tree to be heaped.
        size: Size of the array represented as an integer.
        root: The root of the tree to be heaped represented as an integer indicating the position
            in the array.

    Returns:
        None. Instead it modifies the array that is inputted into the heap function.
    """
    largest = root  # assume the root of tree is already the largest
    left = 2 * root + 1  # left branch will be at this position in array
    right = 2 * root + 2  # right branch will be at this position in array

    # check whether the left branch is larger than the root,
    # if so then reference it as largest
    if left < size and array[largest] < array[left]:
        largest = left

    # check whether the right branch is larger than the root,
    # if so then reference it as largest
    if right < size and array[largest] < array[right]:
        largest = right

    # change the root to the correct largest if necessary
    if largest != root:
        (array[root], array[largest]) = (array[largest], array[root])

        # run the heap recursively for the root
        max_heap(array, size, largest)


def max_heap_sort(array):
    """
    Will sort an array into a max heap.

    Given an unordered array, the function will recursively heap the trees of the array and then
    remove the largest element, moving it to the end of the array, and continue heaping the array.

    Args:
        array: A list of integers representing the array and tree to be heaped.

    Returns:
        array: A max sorted heap of the original array provided.
    """
    # store size of array
    size = len(array)

    # start at the lowest root in the tree at size // 2 and move up
    for i in range(size // 2, -1, -1):
        max_heap(array, size, i)

    # one by one remove the largest element in the tree and move it to the end
    for i in range(size - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])
        max_heap(array, i, 0)

    return array


def min_heap(array, size, root):
    """
    Heap a binary tree such that the root of the tree has the smallest element.

    Given a binary tree with a root, find if the root is the smallest or if
    the left or right branch is smaller. If so then respectively replace it
    with the root.

    Args:
        array: A list of integers representing the array and tree to be heaped.
        size: Size of the array represented as an integer.
        root: The root of the tree to be heaped represented as an integer indicating the position
            in the array.

    Returns:
        None. Instead it modifies the array that is inputted into the heap function.
    """
    smallest = root  # assume the root of tree is already the smallest
    left = 2 * root + 1  # left branch will be at this position in array
    right = 2 * root + 2  # right branch will be at this position in array

    # check whether the left branch is smaller than the root,
    # if so then reference it as smallest
    if left < size and array[smallest] > array[left]:
        smallest = left

    # check whether the right branch is smaller than the root,
    # if so then reference it as smallest
    if right < size and array[smallest] > array[right]:
        smallest = right

    # change the root to the correct smallest if necessary
    if smallest != root:
        (array[root], array[smallest]) = (array[smallest], array[root])

        # run the heap recursively for the root
        min_heap(array, size, smallest)


def min_heap_sort(array):
    """
    Will sort an array into a min heap.

    Given an unordered array, the function will recursively heap the trees of the array and then
    remove the smallest element of the array, moving it to the beginning of the array,
    and continue heaping the array.

    Args:
        array: A list of integers representing the array and tree to be heaped.

    Returns:
        array: A min sorted heap of the original array provided.
    """
    # store size of array
    size = len(array)

    # start at the lowest root in the tree at size // 2 and move up
    for i in range(size // 2, -1, -1):
        min_heap(array, size, i)

    # one by one remove the smallest element in the tree and move it to the end
    for i in range(size - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])
        min_heap(array, i, 0)

    return array


arr = [4, 10, 3, 5, 1]
print("Input Unordered Array: ", arr)
max_heap_sort(arr)
print("Max Heap Sorted Array: ", max_heap_sort(arr))
min_heap_sort(arr)
print("Min Heap Sorted Array: ", min_heap_sort(arr))
