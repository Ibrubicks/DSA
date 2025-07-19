class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []
        for num in operations:
            if num == "C":
                ops.pop()
            elif num=="D":
                ops.append(2*ops[-1])
            elif num=="+":
                ops.append(ops[-1]+ops[-2])
            else:
                ops.append(int(num))
        return sum(ops)
        
                    