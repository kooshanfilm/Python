# Given a non-empty array of integers,
# every element appears twice except for one. Find that single one.

# [1,2,1,2,3]
def are_all_elements_unique(l):
    seen = set()
    for x in l:
        if x in seen:
            return False
        seen.add(x)
    return True
print are_all_elements_unique([1,2,1])