class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        bench_id = {_id[1]:[] for _id in students}
        for _id in students:
            bench_id[_id[1]].append(_id[0])
        if len([len(set(val)) for val in bench_id.values()]) == 0:
            return 0
        else:
            return max([len(set(val)) for val in bench_id.values()])
