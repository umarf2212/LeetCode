class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:        

        # robots = list(map(list, zip(positions, healths, [i for i in directions], [i for i in range(len(positions))])))

        n = len(positions)
        robots = []
        for i in range(n):
            robots.append( [ positions[i], healths[i], directions[i], i ] )

        robots.sort(key=lambda x:x[0])
        
        survivors = []
        stack = []
        for robot in robots:
            pos, health, direction, ind = robot

            if not stack:
                # The peaceful ones, never fought
                if direction == 'L':
                    survivors.append(robot)
                    continue

                # The ones ready to take on a fight
                stack.append(robot)
            
            # Frontline soldier
            elif direction == 'R':
                stack.append(robot)

            # Incoming lefties
            elif direction == 'L':
                # L lost to the frontline soldier
                if stack and stack[-1][1] > robot[1]:
                    stack[-1][1] -= 1
                    continue

                # L takes on the existing ones
                while stack and stack[-1][1] < robot[1]:
                    stack.pop()
                    robot[1] -= 1
                
                # L defeated all of 'em
                if not stack:
                    survivors.append(robot)
                
                # L fought an equivalent
                elif stack[-1][1] == robot[1]:
                    stack.pop()
                else:
                    # L lost to the frontline soldier
                    stack[-1][1] -= 1

        stack += survivors

        stack.sort(key=lambda x:x[3])

        return [robot[1] for robot in stack]
            
