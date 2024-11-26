from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

# from request import get_response
from request import get_gpt_response

router = Router()


print("Bot is ready")
answ = '''
В C++ лямбда-функции могут захватывать переменные из окружающего контекста с помощью механизма "capture". Вот пример лямбда-функции с захватом переменной:

```cpp
#include <iostream>

int main() {
    int x = 10;

    // Лямбда-функция, захватывающая переменную x по значению
    auto lambda = [x]() {
        std::cout << "Значение x: " << x << std::endl;
    };

    lambda(); // Вызов лямбда-функции

    // Изменим x
    x = 20;

    // Лямбда-функция, захватывающая переменную x по ссылке
    auto lambdaByRef = [&x]() {
        std::cout << "Значение x: " << x << std::endl;
    };

    lambdaByRef(); // Вызов лямбда-функции

    return 0;
}
```

В этом примере:

1. Первая лямбда-функция захватывает переменную `x` по значению, поэтому при вызове функции она будет использовать значение `10`, даже если `x` изменится позже.        
2. Вторая лямбда-функция захватывает `x` по ссылке, поэтому при вызове она будет использовать текущее значение `x`, которое равно `20` после изменения.

Вы можете использовать разные способы захвата, такие как `[&]` для захвата всех переменных по ссылке или `[=]` для захвата всех переменных по значению.'''
@router.message(Command("start"))
async def start_handler(msg:Message):
  # soup = BeautifulSoup(markdown.markdown(get_response()), "html.parser")
  # for i in soup.find_all("p"):
  #   result = f"{i.text}\n"

  await msg.answer("Бот отвечает на любой вопрос.")


@router.message()
async def get_request(msg:Message):
  try:
    last_message = await msg.answer("Подождите, идет обработка запроса...")
    # print(f"id is: {msg.from_user.id}")
    msg_from = f"Message from {msg.from_user.username}: {msg.text}"
    print("_" * len(msg_from))
    print(msg_from)
    bot_ans = get_gpt_response(msg.text)
    print(f"\nBot answer: {bot_ans}\n")
    # print(f"Длина: {len(bot_ans)}")
    await msg.answer(bot_ans,parse_mode=ParseMode.MARKDOWN)
    await last_message.delete()
    # test = '*' * 1000
    # await msg.answer(test)
  except:
    await msg.answer("Что то пошло не так. Повторите запрос.")