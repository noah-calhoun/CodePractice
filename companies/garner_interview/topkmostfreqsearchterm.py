

def topkmostfreq(terms, k):
    items = {}
    for term in terms:
        items[term] = items.get(term, 0) + 1
    result = []
    for i in range(k):
        best = max(items, key=items.get)
        result.append(best)
        items.pop(best)
    return result

if __name__ == "__main__":
    terms = ["mri","mri","ekg","xray","ekg","mri"]
    k = 2
    # Output: ["mri","ekg"]
    print(topkmostfreq(terms, k))