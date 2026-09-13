class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq.keys():
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        freq_sorted = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        res = []
        for key in freq_sorted.keys():
            if (len(res) == k): return res
            res.append(key)

        return res