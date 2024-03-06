from sps import SemanticParagraphSplitter
from sentence_cutter import SentenceCutter
from passage_merger import PassageMerger


class ParagraphCutter:
    def __init__(self):
        self.semantic_paragraph_splitter = SemanticParagraphSplitter()
        self.sentence_cutter = SentenceCutter()
        self.passage_merger = PassageMerger()
        pass

    def cut_paragraph(self, text):
        sentences = self.sentence_cutter.cut_sentences(text)
        passages = self.passage_merger.merge_by_dict(sentences)
        chunks = self.semantic_paragraph_splitter.split_passages(passages)
        return chunks


if __name__ == '__main__':
    pc = ParagraphCutter()
    paragraph = "today is a very nice day, i'm feeling good. how about you?"
    result = pc.cut_paragraph(paragraph)
    print(result)