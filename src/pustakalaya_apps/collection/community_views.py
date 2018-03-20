from django.shortcuts import render
from .models import Collection
from django.conf import settings
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

def community_detail(request, community_name):
    """Community detail page"""

    client = connections.get_connection()

    # s = Search(using=client, index=settings.ES_INDEX).query("match", )

    # Query the total number of items in elastic search having the name of this community
    # es_count = Search(index="pustakalaya").using(client).query("match", communities=community_name).count()

    # Context data
    context = {}
    # print("community name =",community_name)

    community_name = " ".join(community_name.split("-"))

    # Query all the collection that contains this community_name from ORM
    collections = Collection.objects.filter(community_name=community_name)

    collection_list = []

    all_total = 0

    for collection in collections:
        # Get the total no of items having this collection name in elastic search
        # item_count_per_collection = Search(index="pustakalaya").using(client).query("match", communities=collection).count()
        item_count_per_collection = Search(index="pustakalaya").using(client).query("match", collections=collection.collection_name).count()


        all_total += item_count_per_collection

        pk = collection.pk

        # Create a list to that contain collection_name and total count
        collection_list.append({
            "collection_name": collection.collection_name,
            "total_count": all_total,
            "es_count": item_count_per_collection,
            "pk": pk,
        })

    # Implement total count

    # Sort list to display in alphabetical order.
    context["collection_list"] = collection_list
    context["community_name"] = community_name
    # print("colllist=",collection_list)
    return render(request, "collection/community_detail.html", context)
