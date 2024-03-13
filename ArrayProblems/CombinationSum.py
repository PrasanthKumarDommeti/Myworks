class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # This can be solved by using backtracking approache
        def backtrack(start, target, path):
            if target == 0:
                # This can be the First/Starting Path
                result.append(path)
                return
            # If the target has a negative value then it returns nothing 
            if target < 0:
                return
            for i in range(start, len(candidates)):
                # recursive approaches to call the paths
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result
        