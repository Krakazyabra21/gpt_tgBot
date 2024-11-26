# import requests
import g4f.Provider
import openai
import g4f
token:str = "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"
# token:str = "sk-OsMMq65tXdfOIlTUYtocSL7NCsmA7CerN77OkEv29dODg1EA"

openai.api_key = token

# def get_gpt_response(content:str):
#   try:
#     result = ""
#     response = g4f.ChatCompletion.create(
#       model=g4f.models.gpt_4,
#       messages=[
#         {"role": "user", "content": content},
#       ]
#     )
#     for i in response:
#       result += i
#     return result
#   except:
#     return "Произошла ошибка, повторите запрос."


def get_gpt_response(content:str):
  result = ""
  response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[
      {"role": "user", "content": content},
    ]
  )
  # print(type(response))
  for i in response:
    # print(i)
    result += i
  # print(result)
  
  return result

