#!/usr/bin/pypy3
'''Benchmarking Insertion Sort

After reading the correctness proof of insertion sort during discussion for week 1,
Konstantinos is wondering how many times line 6 is performed for a given array.
He could simply count, but it took too long for big arrays, so instead he wants
you to write a faster algorithm to compute that result.
'''

def solve(N, array):
    calls = 0

    size = 1
    while size < N:
        for l in range(0, N, 2 * size):
            mid = min(l + size, N)
            r = min(mid + size, N)

            if mid == r: continue
            
            # Merge

            merged = []
            i, j = l, mid

            while i < mid and j < r:
                if array[i] < array[j]:
                    merged.append(array[i])
                    i += 1
                else:
                    merged.append(array[j])
                    j += 1
                    calls += mid - i
            
            merged += array[i: mid]
            merged += array[j: r]

            # Insert merged into array

            array[l:r] = merged

        size *= 2

    return calls

'''
def solve_inplace(N, array):
    calls = 0

    size = 1
    while size < N:
        for l in range(0, N, 2 * size):
            mid = min(l + size, N)
            r = min(mid + size, N)

            if mid == r: continue

            arr1, arr2 = array[l: mid].copy(), array[mid: r].copy()

            i, j, k = 0, 0, l

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    array[k] = arr1[i]
                    i += 1
                else:
                    array[k] = arr2[j]
                    j += 1
                    calls += mid - i - l
                k += 1

            if i < len(arr1): array[k:r] = arr1[i:]
            if j < len(arr2): array[k:r] = arr2[j:]

        size *= 2

    return calls
'''

def main():
    N = int(input())
    array = [int(i) for i in input().split()]
    solution = solve(N, array)
    print(solution)

if __name__ == '__main__':
    main()
