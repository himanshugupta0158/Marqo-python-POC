import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')




pprint.pprint(mq.index("my-first-index").get_stats())
pprint.pprint(mq.index("my-first-index").refresh())


results = mq.index("my-first-index").search(
    q="Sam"
)

pprint.pprint(results)