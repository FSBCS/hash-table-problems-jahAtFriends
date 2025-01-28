def group_anagrams(words):
    groups = {}
    
    for wrd in words:
        key = ''.join(sorted(wrd))

        if key in groups:
            groups[key].append(wrd)
        else:
            groups[key] = [wrd]
    
    return list(groups.values())