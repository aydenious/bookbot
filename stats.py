def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    character_count = {}
    for char in text.lower():
       if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count


def sort_characters(character_count):
    char_list = [{"char": char , "count": count} for char, count in character_count.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)

    return char_list
