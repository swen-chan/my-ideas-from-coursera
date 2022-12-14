#Unfinished work
#I have test this code for some randomly relative big numbers and still can't pass the coursera check,
#so I'm still wonder what's the really problem in there?Wish you can help me!
'''
Convert array into heap


Problem Description
Task. The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the
way, did you know that algorithms based on Heaps are widely used for external sort, when you need
to sort huge files that donβt fit into memory of a computer?
Your task is to implement this first step and convert a given array of integers into a heap. You will
do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
elements ππ and ππ of the array π for some π and π. You will need to convert the array into a heap using
only π(π) swaps, as was described in the lectures. Note that you will need to use a min-heap instead
of a max-heap in this problem.

Input Format. The first line of the input contains single integer π. The next line contains π space-separated
integers ππ

Constraints. 1 β€ π β€ 100 000; 0 β€ π, π β€ π β 1; 0 β€ π0, π1, . . . , ππβ1 β€ 109
. All ππ are distinct.

Output Format. The first line of the output should contain single integer π β the total number of swaps.
π must satisfy conditions 0 β€ π β€ 4π. The next π lines should contain the swap operations used
to convert the array π into a heap. Each swap is described by a pair of integers π, π β the 0-based
indices of the elements to be swapped. After applying all the swaps in the specified order the array
must become a heap, that is, for each π where 0 β€ π β€ π β 1 the following conditions must be true:
1. If 2π + 1 β€ π β 1, then ππ < π2π+1.
2. If 2π + 2 β€ π β 1, then ππ < π2π+2.
Note that all the elements of the input array are distinct. Note that any sequence of swaps that has
length at most 4π and after which your initial array becomes a correct heap will be graded as correct.

Time Limits. C: 1 sec, C++: 1 sec, Java: 3 sec, Python: 3 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 3
sec, Ruby: 3 sec, Scala: 3 sec.

Memory Limit. 512MB.
'''


# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
  
