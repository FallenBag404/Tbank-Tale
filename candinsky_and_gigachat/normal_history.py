from candinsky_and_gigachat.giga import *


async def normal_history(text):
    # messages = [SystemMessage(content=('''коротко и литературно
    # перескажи следущий текст, соединяя его фрагменты;
    # тебе категорически запрещено здороваться, запрещено  представляться, запрещено искожать  факты, запрещено добавлять новое.
    # Не рассказывай ничего нового и не добавляй в текст новые фрагменты или факты'''))]
    messages = [SystemMessage(content=('''Объедините следующие сообщения в единый связный текст, 
    избегая добавления нового контента, фактов о персонажах, художественных деталей. 
    Сохраните логическую последовательность и поток истории с самого начала. НЕ здоровайтесь и не представляйтесь.
'''))]
    messages.append(HumanMessage(content=text))
    chat = init_giga()
    res = chat(messages)
    print(res.content)
    return res.content
