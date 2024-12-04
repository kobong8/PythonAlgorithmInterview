# %%
import collections
from typing import List, Dict

# %%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

# %%
default_dict = collections.defaultdict(int)
default_dict

# %%
default_dict["key1"]
default_dict["key2"] = 1
default_dict

# %%
default_dict_list = collections.defaultdict(list)
default_dict_list

# %%
default_dict_list["key1"]
default_dict_list["key2"].append(1)
default_dict_list

# %%
default_dict_list["key3"].append(2)
print(default_dict_list)
print(default_dict_list.values())

# %%
test_dict: Dict[str, int] = {"key1": 0}
test_dict["key2"] = 1
# test_dict["key3"] # KeyError: 'key3'
test_dict

# %%
print(sorted("eat"))
print(sorted("tea"))
print(sorted("ate"))
print()

print("".join(sorted("eat")))

# %%
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"] 
    print(strs)
    
    soln = Solution()
    ret = soln.groupAnagrams(strs)
    print(ret)


