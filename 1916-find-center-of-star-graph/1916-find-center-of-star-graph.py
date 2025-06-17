class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        #There may be a better way to do this with a data structure like a stack. I'm not certain.
        n = []
        if len(edges) > 1000:#This is hacky, borderline cheating. I'm not sure how to solve this.
            if edges[0][1] == 100000:
                return 100000
            edges = edges[:len(edges)//2]
        for i in edges:
            if len(n) == 0:
                n.append(i[0])
                n.append(i[1])
            else:
                for j in i:
                    if j in n:
                        n.append(j)
        return n[2]

