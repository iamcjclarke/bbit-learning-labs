import pika
import os

class mqProducer(mqProducerInterface):
 def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables
        self.routing_key = routing_key
        self.exchange_name = exchange
         # Call setupRMQConnection
         
def setupRMQConnection(self) -> None:
     # Set-up Connection to RabbitMQ service
    con_params = pika.URLParameters(os.environ["AMQP_URL"])
    connection = pika.BlockingConnection(parameters=con_params)
     # Establish Channel
     channel = connection.channel()
     # Create the exchange if not already present
     self.exchange = channel.exchange_declare(exchange="Exchange Name")


  def publishOrder(self, message: str) -> None:
    # Basic Publish to Exchange
  channel.basic_publish(
    self.exchange_name,
    self.routing_key,
    body="Message",
)
    # Close Channel
    self.channel.close()
    # Close Connection
    self.connection.close()
            
            