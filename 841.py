class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        stack = [0]
        seen_rooms = {0}

        while stack:
            idx = stack.pop()

            for j in rooms[idx]:
                if j not in seen_rooms:
                    stack.append(j)
                    seen_rooms.add(j)
        return len(seen_rooms) == len(rooms)
