from concurrent import futures
import grpc
import kafka
import kafka_server_pb2
import kafka_server_pb2_grpc

class KafkaServiceServicer(kafka_server_pb2_grpc.KafkaServiceServicer):
    def __init__(self):
        self.producer = kafka.KafkaProducer(bootstrap_servers='kafka:9092')
        self.consumer = kafka.KafkaConsumer(bootstrap_servers='kafka:9092', auto_offset_reset='earliest')
    
    def ProduceMessage(self, request, context):
        self.producer.send(request.topic, request.message.encode('utf-8'))
        self.producer.flush()
        return kafka_server_pb2.ProduceResponse(success=True)
    
    def ConsumeMessages(self, request, context):
        self.consumer.subscribe([request.topic])
        for message in self.consumer:
            yield kafka_server_pb2.ConsumeResponse(message=message.value.decode('utf-8'))
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kafka_server_pb2_grpc.add_KafkaServiceServicer_to_server(KafkaServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()