def slices(digits, l):
    if len(digits) < l or l <= 0:
        raise ValueError("Length doesn't fit in the series.")
    else:
        return [[int(n) for n in digits[i:i+l]] \
                 for i in range(len(digits)-l+1)]