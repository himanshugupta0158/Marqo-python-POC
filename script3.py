import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')


results = mq.index("my-first-index").search(
    q="Where to go today?"
)

pprint.pprint(results)