
# words,word_to_id,classList,cat_to_id
def get_words_cat_dir():
    words = []
    with open('data/vacab5186.txt', encoding="UTF-8") as f:
        words.extend(f.readlines())
        words = [i.strip() for i in words]
        print(words)
        print(len(words))

    word_to_id = dict(zip(words, range(len(words))))
    print(word_to_id)
    classList = ['phone', 'weather', 'translation', 'playcontrol', 'volume', 'FM',
                 'limitLine', 'alarm', 'schedule', 'music', 'story',
                 'news', 'collect', 'musicinfo', 'healthAI', 'calculator', 'cookbook',
                 'dictionary', 'joke', 'forex', 'stock', 'other']
    cat_to_id = dict(zip(classList, range(len(classList))))
    print(cat_to_id)
    return words,word_to_id,classList,cat_to_id


