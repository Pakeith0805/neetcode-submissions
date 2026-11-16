class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        for p in s:
            p = ord(p)
            s_list.append(p)
        for q in t:
            q = ord(q)
            t_list.append(q)
        s_list.sort()
        t_list.sort()
        if s_list == t_list:
            return True
        else:
            return False