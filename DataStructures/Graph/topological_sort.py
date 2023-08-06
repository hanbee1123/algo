"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

"""

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        if len(prerequisites)==0:
            return True

        courses = defaultdict(list)
        indegrees = [0]*numCourses

        for i,j in prerequisites:
            courses[i].append(j)
            indegrees[j] += 1
        
        counter = 0
        q = deque()

        for k in range(len(indegrees)):
            if indegrees[k] == 0:
                q.append(k)

        while q:
            val = q.popleft()
            counter += 1
            for k in courses[val]:
                indegrees[k] -= 1
                if indegrees[k] == 0:
                    q.append(k)



        return counter == numCourses