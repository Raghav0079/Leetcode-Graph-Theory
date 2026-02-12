class Solution(object):

    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        adj = collections.defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)

        q = deque([(headID, 0)])
        res = 0
        while q:
            id, time = q.popleft()
            res = max(res, time)

            for emp in adj[id]:
                q.append((emp, time + informTime[id]))
        return res
