def detect_anagrams(word, candidate_anagrams):
    standardized_word = word.lower()
    test_word = sorted(list(standardized_word))
    return [wd for wd in candidate_anagrams if wd.lower() != standardized_word and sorted(list(wd.lower())) == test_word]
