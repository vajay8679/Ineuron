import argparse

import json
from confluent_kafka import Consumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.serialization import SerializationContext, MessageField, StringDeserializer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer


API_KEY = 'MCEKJLRF3GCYSMTV'
ENDPOINT_SCHEMA_URL  = 'https://psrc-mw731.us-east-2.aws.confluent.cloud'
API_SECRET_KEY = 'Y1HNEK9VyQ/U7YBmumwe2eNHb4OXPuwgr4Sf6juBwT6Y2JowlsmYuoqgVlyttmxt'
BOOTSTRAP_SERVER = 'pkc-l7pr2.ap-south-1.aws.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MACHENISM = 'PLAIN'
SCHEMA_REGISTRY_API_KEY = 'ISAE2YTXXGNP5G6L'
SCHEMA_REGISTRY_API_SECRET = 'Hsb5k7VENtc1OfmD/qYhE4ezdapHQFDgcsxEYLaH6jkuLGMg7YV5V8Pg2ilG4PXB'


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }


class Case:   
    def __init__(self,record:dict):
        for k,v in record.items():
            setattr(self,k,v)
        
        self.record=record
   
    @staticmethod
    def dict_to_case(data:dict,ctx):
        return Case(record=data)

    def __str__(self):
        return f"{self.record}"


def main(topic):

    consumer_conf = sasl_conf()
    consumer_conf.update({
        'group.id': 'group1',
        'auto.offset.reset': "earliest"})

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])

    schema_registry_conf = schema_config()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    string_serializer = StringDeserializer('utf_8')
    my_schema = schema_registry_client.get_latest_version(topic + '-value').schema.schema_str

    json_deserializer = JSONDeserializer(my_schema,
                                         from_dict=Case.dict_to_case)


    count = 0
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            case = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))

            if case is not None:
                count += 1
                print("User record {}: car: {}\n"
                      .format(msg.key(), case))
        except KeyboardInterrupt:
            break

    consumer.close()
    print("No of values it consumed from the topic is --------> {}".format(count))

main("Test_Topic")