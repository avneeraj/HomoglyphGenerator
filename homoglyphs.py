
import itertools
import random

# IRONGEEK HOMOGLYPH MAPPING (Reconstructed)
# Based on common attack generator lists.
# Prioritizes coverage and known substitutions used by IronGeek.

HOMOGLYPH_MAP = {
    'a': ['a', 'ɑ', 'α', 'а', 'Ꭺ', 'Ａ', 'ａ'],
    'b': ['b', 'Ь', 'Lb', 'vZ', 'd', 'ß', 'Β', 'В', 'в', 'Ᏼ', 'Ｂ', 'ｂ'],
    'c': ['c', 'ϲ', 'с', 'Ꮯ', 'ℂ', 'ℭ', 'Ⅽ', 'Ｃ', 'ｃ'],
    'd': ['d', 'cl', 'ɗ', 'ժ', 'ɖ', 'ɗ', 'đ', 'ⅆ', 'ⅾ', 'ｄ'],
    'e': ['e', 'é', 'ê', 'ë', 'ē', 'ĕ', 'ė', 'ę', 'ě', 'è', 'е', 'є', 'ё', 'ȩ', 'ҽ', '℮', 'Ｅ', 'ｅ'],
    'f': ['f', 'ƒ', 'ſ', 'ḟ', 'ｆ'],
    'g': ['g', 'q', 'ɢ', 'ɡ', 'Ԍ', 'ԍ', 'ｇ'],
    'h': ['h', 'ｈ', 'һ', 'հ', 'Ꮒ', 'Ｈ', 'ｈ'],
    'i': ['i', '1', 'l', 'í', 'î', 'ï', 'ì', 'ī', 'į', 'ı', 'ι', 'і', 'ї', 'Ꭵ', 'Ｉ', 'ｉ', '¡'],
    'j': ['j', 'ј', 'ｊ'],
    'k': ['k', 'κ', 'к', 'ҡ', 'Ꮶ', 'K', 'Ｋ', 'ｋ'],
    'l': ['l', '1', 'I', 'ł', '|', 'Ι', 'І', 'լ', 'Ꮮ', 'Ⅼ', 'Ｌ', 'ｌ'],
    'm': ['m', 'rn', 'nn', 'μ', 'м', 'ᴍ', 'Ꮇ', 'Ⅿ', 'Ｍ', 'ｍ'],
    'n': ['n', 'η', 'ή', 'и', 'й', 'ή', 'ñ', 'ń', 'ņ', 'ň', 'ŉ', 'ŋ', 'ｎ'],
    'o': ['o', '0', 'Ο', 'ο', 'О', 'о', 'Օ', 'Ｏ', 'ｏ', 'ö'],
    'p': ['p', 'ρ', 'р', 'Ꮲ', 'Ｐ', 'ｐ'],
    'q': ['q', 'g', 'զ', 'ｑ'],
    'r': ['r', 'ř', 'г', 'ᴦ', 'ɼ', 'ｒ'],
    's': ['s', '5', 'ś', 'ŝ', 'ş', 'š', 'ș', 'ς', 'Ѕ', 'ѕ', 'Տ', 'Ｓ', 'ｓ'],
    't': ['t', 'τ', 'т', 'ｔ'],
    'u': ['u', 'μ', 'υ', 'ц', 'ü', 'ú', 'ù', 'û', 'ū', 'ŭ', 'ů', 'ű', 'ų', 'Ս', 'Ｕ', 'ｕ'],
    'v': ['v', 'ν', 'ѵ', 'Ꮩ', 'Ⅴ', 'Ｖ', 'ｖ'],
    'w': ['w', 'vv', 'ѡ', 'Ꮃ', 'Ｗ', 'ｗ'],
    'x': ['x', 'χ', 'х', 'ⅹ', 'Ｘ', 'ｘ'],
    'y': ['y', 'γ', 'у', 'ү', 'ÿ', 'ý', 'ŷ', 'Ꭹ', 'Ｙ', 'ｙ'],
    'z': ['z', 'ź', 'ż', 'ž', 'Ζ', 'Ｚ', 'ｚ'],
    'A': ['A', 'Α', 'А', 'Ꭺ', 'Ａ'],
    'B': ['B', 'Β', 'В', 'Ᏼ', 'Ｂ'],
    'C': ['C', 'С', 'Ꮯ', 'Ｃ', 'Ϲ'],
    'D': ['D', 'Ꭰ', 'Ｄ', 'Ⅾ'],
    'E': ['E', 'Ε', 'Е', 'Ꭼ', 'Ｅ'],
    'F': ['F', 'Ϝ', 'Ｆ'],
    'G': ['G', 'Ꮐ', 'Ｇ'],
    'H': ['H', 'Η', 'Н', 'Ꮋ', 'Ｈ'],
    'I': ['I', 'l', '1', 'Ι', 'І', 'Ӏ', 'Ｉ'],
    'J': ['J', 'Ј', 'Ｊ', 'Ϳ'],
    'K': ['K', 'Κ', 'К', 'Ꮶ', 'K', 'Ｋ'],
    'L': ['L', 'Ꮮ', 'Ⅼ', 'Ｌ', '1', 'I', 'l'],
    'M': ['M', 'Μ', 'М', 'Ꮇ', 'Ⅿ', 'Ｍ'],
    'N': ['N', 'Ν', 'Ｎ'],
    'O': ['O', '0', 'Ο', 'О', 'Օ', 'Ｏ'],
    'P': ['P', 'Ρ', 'Р', 'Ꮲ', 'Ｐ'],
    'Q': ['Q', 'Ꮯ', 'Ｑ'],
    'R': ['R', 'Ꭱ', 'Ｒ'],
    'S': ['S', 'Ѕ', 'Տ', 'Ｓ', '5'],
    'T': ['T', 'Τ', 'Т', 'Ꭲ', 'Ｔ'],
    'U': ['U', 'Ս', 'Ｕ'],
    'V': ['V', 'Ⅴ', 'Ꮩ', 'Ｖ'],
    'W': ['W', 'Ꮃ', 'Ｗ'],
    'X': ['X', 'Χ', 'Х', 'Ⅹ', 'Ｘ'],
    'Y': ['Y', 'Υ', 'Ꭹ', 'Ｙ'],
    'Z': ['Z', 'Ζ', 'Ꮓ', 'Ｚ'],
    '0': ['O', 'o', '0', 'Ο', 'ο', 'О', 'о', 'Օ'],
    '1': ['l', 'I', '1', '１'],
}

def generate_variants(word: str, max_limit: int = 2000):
    if not word:
        return [], 0

    char_options = []
    for char in word:
        if char in HOMOGLYPH_MAP:
            char_options.append(HOMOGLYPH_MAP[char])
        else:
            char_options.append([char])

    total_combinations = 1
    for options in char_options:
        total_combinations *= len(options)

    results = []
    
    # Standard IronGeek behavior: Generate all Cartesian products
    # But limit to avoid crashes
    if total_combinations <= max_limit * 2:
        product_iter = itertools.product(*char_options)
        for combo in product_iter:
            variant_word = "".join(combo)
            if variant_word != word: # Filter original
                results.append(variant_word)
    else:
        # Sampling
        seen = {word}
        attempts = 0
        max_attempts = max_limit * 5
        
        while len(results) < max_limit and attempts < max_attempts:
            attempts += 1
            variant_chars = [random.choice(options) for options in char_options]
            variant_word = "".join(variant_chars)
            
            if variant_word not in seen:
                seen.add(variant_word)
                results.append(variant_word)

    # Sort lexicographically like the IronGeek tool usually does
    results.sort()

    formatted_results = []
    for var in results:
        # No punycode needed if mimicking basic view, but we'll include it blank if requested or just text
        formatted_results.append({
            "text": var,
            "puny": "" 
        })
        
    return formatted_results, total_combinations
