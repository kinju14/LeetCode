class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        maxHeap = [[-cnt, ch] for ch, cnt in Counter(s).items()]
        prev = None
        heapq.heapify(maxHeap)

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, ch = heapq.heappop(maxHeap)
            res += ch
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, ch]
        return res

        '''
        countCh = defaultdict(int)
        maxHeap = []

        for ch in s:
            countCh[ch] += 1

        for ch in countCh:
            heapq.heappush(maxHeap, [-countCh[ch], ch])

        print(maxHeap)
        while len(maxHeap) > 1:
            ch1 = heapq.heappop(maxHeap) 
            ch2 = heapq.heappop(maxHeap)
            res += ch1[1] + ch2[1]
            ch1[0] += 1
            ch2[0] += 1
            if ch1[0] != 0:
                heapq.heappush(maxHeap, ch1)
            if ch2[0] != 0:
                heapq.heappush(maxHeap, ch2)
            print(maxHeap)
        
        if not len(maxHeap):
            return res
        elif abs(maxHeap[0][0]) == 1 :
            return res + maxHeap[0][1]
        else:
            return ''
        '''
