# merge QA pair
# merge according to dictionary
# merge according to grammar dependency

# 如果一句话中出现以下词语, 则向上合并
MERGE_DICT = ["因此", "因为", "并且", "所以", "但是", "而且", "然而", "可是", "另外"]


class SentenceMerger:
    def __init__(self):
        pass

    @staticmethod
    def merge_by_dict(sentences):
        merged_sentences = []
        current_sentence = sentences[0]

        for i in range(1, len(sentences)):
            sentence = sentences[i]
            if any(word in sentence for word in MERGE_DICT):
                current_sentence += " " + sentence
            else:
                merged_sentences.append(current_sentence)
                current_sentence = sentence

        merged_sentences.append(current_sentence)

        return merged_sentences


if __name__ == '__main__':
    sm = SentenceMerger()
    sentences = ["今天天气很好", "但是没有风", "我很开心", "心情也不错", "因为我不想吹风"]
    print(sm.merge_by_dict(sentences))
