#PROBLEM 2570   Merge Two 2D Arrays by Summing Values

def mergeArrays(self, nums1, nums2):
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            a, b = nums1[i], nums2[j]
            if a[0] == b[0]:
                res.append((a[0], a[1] + b[1]))  
                i += 1
                j += 1
            elif a[0] < b[0]:
                res.append(a)
                i += 1
            else:
                res.append(b)
                j += 1

        while i < len(nums1):
            res.append(nums1[i])
            i += 1

        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return res
