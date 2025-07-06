from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0     # Total gas available at all stations
        total_cost = 0    # Total cost to travel around the circuit
        tank = 0          # Current fuel in the tank
        start = 0         # Candidate starting station

        # Iterate over each gas station
        for i in range(len(gas)):
            total_gas += gas[i]      # Add gas from current station
            total_cost += cost[i]    # Add cost to reach next station
            tank += gas[i] - cost[i] # Update tank: gas gained - gas spent

            # If tank becomes negative, we can't reach the next station
            if tank < 0:
                # So, we reset the tank and set the next station as the new start
                start = i + 1
                tank = 0

        # After the loop, check if the journey is possible at all
        if total_gas < total_cost:
            return -1  # Not enough gas to travel the whole circuit

        # If possible, return the starting station index
        return start


# Input
gas = list(map(int, input("Enter gas: ").split()))
cost = list(map(int, input("Enter cost: ").split()))

sol = Solution()
print("Start index:", sol.canCompleteCircuit(gas, cost))