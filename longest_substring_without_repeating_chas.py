# %%


s = "pwwkew"

longest_sub = 0
left =0
right = 1
d= dict()
while right > left and right<len(s) : 
    d[s[right]]
    if s[right]!=s[left]:
        right+=1
        longest_sub = right -left
        
    else : 
        right = right +1 
        longest_sub = right -left




            


    



# %%

# importing "collections" for deque operations
import collections

de = collections.deque()
de.append(1)
# %%
