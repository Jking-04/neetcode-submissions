class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet_stack = []

        cars = list(zip(position,speed))
        cars.sort(reverse=True)

        for car in cars:
            time = (target-car[0])/car[1]

            if not fleet_stack or time > fleet_stack[-1]:
                fleet_stack.append(time)

        return(len(fleet_stack))
        