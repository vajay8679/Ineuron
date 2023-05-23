#Data Indexing in Elasticsearch

from elasticsearch import Elasticsearch

# Set up Elasticsearch connection
es = Elasticsearch()

# Transform the processed data into Elasticsearch index format
elasticsearch_data = aggregated_data.rdd.map(lambda row: {
    "url": row.url,
    "country": row.country,
    "unique_users": row.unique_users,
    "avg_time_spent": row.avg_time_spent,
    "clicks": row.clicks
})

# Index the data in Elasticsearch
for data in elasticsearch_data.collect():
    es.index(index='clickstream_index', doc_type='_doc', body=data)
