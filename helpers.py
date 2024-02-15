def capitalize_after_space(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

def is_cyrillic_or_latin(text):
    cyrillic_range = (0x0400, 0x04FF)
    latin_range = (0x0041, 0x007A)

    for char in text:
        char_code = ord(char)
        if cyrillic_range[0] <= char_code <= cyrillic_range[1]:
            return "Cyrillic"
        elif latin_range[0] <= char_code <= latin_range[1]:
            return "Latin"
    return "Unknown"