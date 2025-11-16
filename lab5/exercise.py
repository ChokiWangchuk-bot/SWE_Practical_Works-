def linear_search_all_indices(arr, target):
    """
    Modified linear search to return all indices where target appears
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

def linear_search_with_count(arr, target):
    """
    Linear search that counts comparisons
    """
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search_insertion_point(arr, target):
    """
    Uses binary search to find insertion point for target in sorted list
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def binary_search_with_count(arr, target):
    """
    Binary search that counts comparisons
    """
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

def binary_search_recursive_with_count(arr, target, left, right, comparisons=0):
    """
    Recursive binary search that counts comparisons
    """
    comparisons += 1
    if left > right:
        return -1, comparisons
    
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive_with_count(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive_with_count(arr, target, left, mid - 1, comparisons)

def jump_search(arr, target):
    """
    Jump search algorithm
    """
    n = len(arr)
    if n == 0:
        return -1
    
    # Determine the jump size
    step = int(n ** 0.5)
    
    # Find the block where target may exist
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    
    # Linear search in the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    
    return -1

def jump_search_with_count(arr, target):
    """
    Jump search that counts comparisons
    """
    comparisons = 0
    n = len(arr)
    if n == 0:
        return -1, comparisons
    
    step = int(n ** 0.5)
    
    # Find the block
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1, comparisons
    
    # Linear search in the block
    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    
    return -1, comparisons

def compare_search_algorithms(arr, target):
    """
    Compare performance of all search algorithms
    """
    print(f"\n=== Performance Comparison (Searching for {target}) ===")
    print(f"Array size: {len(arr)}")
    
    # Linear Search
    result, comparisons = linear_search_with_count(arr, target)
    print(f"Linear Search: Found at index {result}, Comparisons: {comparisons}")
    
    # Binary Search (iterative)
    sorted_arr = sorted(arr)
    result, comparisons = binary_search_with_count(sorted_arr, target)
    print(f"Binary Search (iterative): Found at index {result}, Comparisons: {comparisons}")
    
    # Binary Search (recursive)
    result, comparisons = binary_search_recursive_with_count(sorted_arr, target, 0, len(sorted_arr) - 1)
    print(f"Binary Search (recursive): Found at index {result}, Comparisons: {comparisons}")
    
    # Jump Search
    result, comparisons = jump_search_with_count(sorted_arr, target)
    print(f"Jump Search: Found at index {result}, Comparisons: {comparisons}")

def demonstrate_all_features():
    """
    Demonstrate all the implemented features
    """
    # Test data
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
    test_list_sorted = sorted(test_list)
    
    print("Original list:", test_list)
    print("Sorted list:", test_list_sorted)
    
    # 1. Linear search returning all indices
    target = 3
    all_indices = linear_search_all_indices(test_list, target)
    print(f"\n1. All indices of {target}: {all_indices}")
    
    # 2. Binary search insertion point
    insertion_targets = [0, 5, 10]
    for target in insertion_targets:
        insertion_point = binary_search_insertion_point(test_list_sorted, target)
        print(f"2. Insertion point for {target}: {insertion_point}")
    
    # 3. Search with comparison counts
    print(f"\n3. Search with comparison counts:")
    target = 6
    result, comparisons = linear_search_with_count(test_list, target)
    print(f"   Linear Search for {target}: index={result}, comparisons={comparisons}")
    
    result, comparisons = binary_search_with_count(test_list_sorted, target)
    print(f"   Binary Search for {target}: index={result}, comparisons={comparisons}")
    
    # 4. Jump search demonstration
    print(f"\n4. Jump Search demonstration:")
    for target in [1, 6, 9, 10]:
        result = jump_search(test_list_sorted, target)
        print(f"   Jump Search for {target}: index={result}")
    
    # 5. Performance comparison
    large_list = list(range(100000))
    compare_search_algorithms(large_list, 75000)
    
    # Additional: Worst-case scenario
    print(f"\n=== Worst-case Scenario ===")
    compare_search_algorithms(large_list, 100000)  # Not in list

def main():
    """
    Main function to demonstrate all search algorithms
    """
    import random
    
    # Create test data
    test_list = [random.randint(1, 100) for _ in range(20)]
    test_list_sorted = sorted(test_list)
    
    print("=== Search Algorithms Demonstration ===")
    print("Original list:", test_list)
    print("Sorted list:", test_list_sorted)
    
    # Choose a random target
    target = random.choice(test_list)
    print(f"\nSearching for: {target}")
    
    # Demonstrate all indices feature
    all_indices = linear_search_all_indices(test_list, target)
    print(f"All indices where {target} appears: {all_indices}")
    
    # Demonstrate insertion point
    insertion_point = binary_search_insertion_point(test_list_sorted, target)
    print(f"Insertion point for {target} in sorted list: {insertion_point}")
    
    # Compare algorithms
    compare_search_algorithms(test_list, target)
    
    # Demonstrate all features
    print("\n" + "="*50)
    demonstrate_all_features()

if __name__ == "__main__":
    main()