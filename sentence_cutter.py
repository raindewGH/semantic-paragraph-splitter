from langdetect import detect
#from langdetect import detect_langs
from sentence_spliter import spliter
from sentence_spliter.logic_graph_en import long_cuter_en
from sentence_spliter.automata.state_machine import StateMachine
from sentence_spliter.automata.sequence import EnSequence
from sentence_spliter.logic_graph import long_short_cuter
from sentence_spliter.automata.sequence import StrSequence

class SentenceCutter:
    def __init__(self):
        pass

    @staticmethod
    def cut_english_sentences(text):
        # 令句子长度不能小于5个单词
        long_machine_en = StateMachine(long_cuter_en(min_len=5))
        m_input = EnSequence(text)
        long_machine_en.run(m_input)
        sentences = m_input.sentence_list()
        return sentences

    @staticmethod
    def cut_chinese_sentences(text):
        # -- 初始化 状态机器 -- #
        cuter = StateMachine(long_short_cuter(hard_max=128, max_len=128, min_len=15))
        sequence = cuter.run(StrSequence(text))
        sentences = sequence.sentence_list()
        return sentences

    def cut_sentences(self, text):
        lang = detect(text)
        #print(lang)
        if lang.startswith('zh'):
            # 中文切句调用 cut_to_sentences
            sentences = self.cut_chinese_sentences(text)
        elif lang == 'en':
            # 英文切句调用 split_sentences
            sentences = self.cut_english_sentences(text)
        else:
            return []
        return sentences


if __name__ == '__main__':
    sc = SentenceCutter()
    paragraph = "today is a very nice day, i'm feeling good. how about you?"
    #paragraph = "在很久很久以前......。。... 有座山，山里有座庙啊!!!!!!!庙里竟然有个老和尚！？。。。。"
    result = sc.cut_sentences(paragraph)
    print(result)
