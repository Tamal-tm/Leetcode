class Solution:
    def asteroidCollision(self, asteroids):
        st = []
        
        for a in asteroids:
            while st and a < 0 < st[-1] and st[-1] < -a:
                st.pop()
            
            if not st or a > 0 or st[-1] < 0:
                st.append(a)
            elif st[-1] == -a:
                st.pop()
        
        return st