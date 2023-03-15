import wolframalpha
query='what'
if 'what' in query or 'solve' in query:
  app_id = ['GE8LH7-7YTEQWAGE2']
  client = wolframalpha.Client(app_id)
  res = client.query(query)
  answer = next(res.results).text
  print(answer)
