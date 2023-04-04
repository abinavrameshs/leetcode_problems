# %%

dict_roman = {
"I": 1,
"V": 5,
"X": 10,
"L": 50,
"C": 100,
"D": 500,
"M": 1000
}


# %%
s = "MCMXCIV"
num_to_add = 0
i=0 
while i<len(s):
    current_letter = s[i]
    try : 
        next_letter = s[i+1]
        if dict_roman[current_letter]<dict_roman[next_letter]:
            num_to_add-=dict_roman[current_letter]
        
        elif dict_roman[current_letter]>=dict_roman[next_letter]:
            num_to_add+= dict_roman[current_letter] 
        i+=1
    except : 
        num_to_add+= dict_roman[current_letter] 
        break

    
        



# %%
num_to_add
# %%


#### LEETCODE solution

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        num_to_add = 0
        i=0 

        while i<len(s):
            current_letter = s[i]
            try : 
                next_letter = s[i+1]
                if dict_roman[current_letter]<dict_roman[next_letter]:
                    num_to_add-=dict_roman[current_letter]
                
                elif dict_roman[current_letter]>=dict_roman[next_letter]:
                    num_to_add+= dict_roman[current_letter] 
                i+=1
            except : 
                num_to_add+= dict_roman[current_letter] 
                break
        return num_to_add