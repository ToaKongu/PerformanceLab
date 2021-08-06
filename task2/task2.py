import sys


file1 = open(f'{sys.argv[1]}', 'r')
nums1 = file1.read()
file1.close()
nums1 = nums1.split()
c_x, c_y = int(nums1[0]), int(nums1[1])
r = int(nums1[2])

file2 = open(f'{sys.argv[2]}', 'r')
nums2 = file2.read()
file2.close()
nums2 = nums2.split()
for i in range(0, len(nums2), 2):
    x = int(nums2[i])
    y = int(nums2[i + 1])
    length = ((c_x - x) * (c_x - x) + (c_y - y) * (c_y - y)) ** 0.5
    if length < r:
        print(1)
    elif length > r:
        print(2)
    else:
        print(0)
