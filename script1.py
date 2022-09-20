"""
run below : for starting marqo and this file.
docker rm -f marqo; #does not matter you run this or not
*docker run --name marqo -it --privileged -p 8882:8882 --add-host host.docker.internal:host-gateway marqoai/marqo:0.0.3
"""

import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

mq.index("my-first-index").add_documents([
    {
        "Title": "The Travels of Marco Polo",
        "Description": "A 13th-century travelogue describing Polo's travels"
    }, 
    {
        "Title": "Extravehicular Mobility Unit (EMU)",
        "Description": "The EMU is a spacesuit that provides environmental protection, "
                       "mobility, life support, and communications for astronauts",
        "_id": "article_591"
    }]
)

results = mq.index("my-first-index").search(
    q="What is the best outfit to wear on the moon?"
)

# pprint.pprint(results)
print(results)