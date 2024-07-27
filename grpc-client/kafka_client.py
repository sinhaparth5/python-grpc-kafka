import grpc
import kafka_service_pb2
import kafka_service_pb2_grpc

def run():
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = kafka_service_pb2_grpc.KafkaServiceStub(channel)

    # Produce a message
    response = stub.ProduceMessage(kafka_service_pb2.ProduceRequest(topic='test', message='Hello, Kafka!'))
    print(f"ProduceMessage success: {response.success}")

    # Consume messages
    response_iterator = stub.ConsumeMessages(kafka_service_pb2.ConsumeRequest(topic='test'))
    for response in response_iterator:
        print(f"Consumed message: {response.message}")

if __name__ == '__main__':
    run()
