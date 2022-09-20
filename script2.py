"""
run below : for starting marqo and this file.
docker rm -f marqo; #does not matter you run this or not
*docker run --name marqo -it --privileged -p 8882:8882 --add-host host.docker.internal:host-gateway marqoai/marqo:0.0.3



Now run marqo docker image
docker run marqo
"""

import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

mq.index("my-first-index").add_documents([
    {
        "name": "Sam",
        "Description": "he travels to the New York City"
    },
    {
        "name": "Jack",
        "Description": "he travels to the Tokyo."
    },
    {
        "name": "James",
        "Description": "he travels to the some where in Europe"
    },
    {
        "name": "kale",
        "Description": "she travel to nowhere just sitting home."
    },
    ]
)

results = mq.index("my-first-index").search(
    q="Who travel to Tokyo?"
)

pprint.pprint(results)