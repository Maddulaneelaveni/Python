# 1. Transpose of a Matrix
# Convert rows into columns and columns into rows.

matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose=list(map(list, zip(*matrix)))
print("Transpose:", transpose)
# zip(*matrix) groups elements column-wise
# map(list, ) converts each tuple into a list

# output:
# Transpose: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]



# 2.Rotate a List by K Positions (Right Rotation)
# Shift elements right by k places.

nums=[1, 2, 3, 4, 5]
k=2
rotated=nums[-k:] + nums[:-k]
print("Rotated List:", rotated)
# nums[-k:] → last k elements [4.5]
# nums[:-k] → first n-k elements (elements before last k)

# output:
# Rotated List: [4, 5, 1, 2, 3]



# 3.Chunk a List into Smaller Sublists
# Break list into equal parts (size = k).

nums=[1, 2, 3, 4, 5, 6, 7, 8]
k=3
chunks=[]
for i in range(0, len(nums), k):
    chunks.append(nums[i:i+k])
print("Chunks:", chunks)
# range(0, len(nums), k) → generates indices 0, 3, 6
# nums[i:i+k] → slice of k elements at a time

# output:
# Chunks: [[1, 2, 3], [4, 5, 6], [7, 8]]






