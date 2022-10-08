import argparse
import csv

from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer


API_KEY = 'L2C2TRRNONYXHRCO'
ENDPOINT_SCHEMA_URL  = 'https://psrc-8kz20.us-east-2.aws.confluent.cloud'
API_SECRET_KEY = 'oPoIfy34rG8E6pKnzJxR1XfQknYbHHu2/vNBM7H8VT4wcOX4BJZIYHm275kI3d6E'
BOOTSTRAP_SERVER = 'pkc-ymrq7.us-east-2.aws.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MACHENISM = 'PLAIN'
SCHEMA_REGISTRY_API_KEY = 'PQ3ZEYLENNAMRJUZ'
SCHEMA_REGISTRY_API_SECRET = 'Uiudr1jsRaaj2swDO6xQg+zhI35pAY4vsDNXj3QdcRpmk8nIJaQjWPOMDGTxMepE'

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


class Car:   
    def __init__(self,record:dict):
        for k,v in record.items():
            setattr(self,k,v)
        
        self.record=record
   
    @staticmethod
    def dict_to_car(data:dict,ctx):
        return Car(record=data)

    def __str__(self):
        return f"{self.record}"


def main(topic):

    schema_str = """
    {
  "$id": "http://example.com/myURI.schema.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "additionalProperties": false,
  "description": "Sample schema to help you get started.",
  "properties": {
    "Order Number": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "Order Date": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "Item Name": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "Quantity": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "Product Price": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "Total products": {
      "description": "The type(v) type is used.",
      "type": "number"
    }
  },
  "title": "SampleRecord",
  "type": "object"
}
    """
    json_deserializer = JSONDeserializer(schema_str,
                                         from_dict=Car.dict_to_car)

    consumer_conf = sasl_conf()
    consumer_conf.update({
                     'group.id': 'group1',
                     'auto.offset.reset': "earliest"})

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])


    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            car = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))
            
            csvFile = open('output.csv','w+',newline="")
            try:
              writer = csv.writer(csvFile)
              writer.writerow((msg.key(),car))
            finally:
              csvFile.close()
            if car is not None:
                print("User record {}: Restaurant's Order: {}\n"
                      .format(msg.key(), car))
        except KeyboardInterrupt:
            break

    consumer.close()

main("restaurent-take-away-data")