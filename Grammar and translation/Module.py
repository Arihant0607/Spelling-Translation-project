import language_tool_python
from googletrans import Translator


class SpellCheck:
    def correct_spelling(self, text):
        tool = language_tool_python.LanguageTool("en-US")
        check = tool.check(text)
        correct_word = language_tool_python.utils.correct(text, check)
        return correct_word


class Trans:
    def translate_text(self, text, lang):
        translator = Translator()
        lang = lang.lower()
        Result = translator.translate(text, dest=lang)
        return Result.text


if __name__ == "__main__":
    obj = Trans()
    msg = "hello"
    lang = "es"
    print(obj.translate_text(msg, lang))
