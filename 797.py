class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graphs = collections.defaultdict(list)

        for i,edges in enumerate(graph):
            self.graph[i] = edges

        res = []

        def dfs(cur_path,cur_node):
            if cur_node == len(self.graph) -1 :
                res.append(list(cur_path))
            
            for connection in self.graph[cur_node]:
                cur_path.append(connection)
                dfs(cur_path,connection)
                cur_path.pop()

        dfs([0],0)
        return res


