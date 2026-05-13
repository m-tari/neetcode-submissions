class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks_idx = [[enqT, procT, i] for i, [enqT, procT] in enumerate(tasks)]
        tasks_idx.sort()

        heap = []  # Heap tracks current available tasks for CPU in a (procT, idx) pair
        i, time = 0, tasks_idx[0][0]
        res = []

        while heap or i < n:
            # If no task available, jump time forward
            if not heap and time < tasks_idx[i][0]:
                time = tasks_idx[i][0]

            # Add all available tasks by this time
            while i < n and tasks_idx[i][0] <= time:
                heapq.heappush(heap, [tasks_idx[i][1], tasks_idx[i][2]])
                i += 1

            # Process next task
            procT, idx = heapq.heappop(heap)
            time += procT
            res.append(idx)

        return res