import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from app.core.config import settings

channel = grpc.insecure_channel(settings.TF_SERVING_HOST + ':' + settings.TF_SERVING_PORT)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

async def generate_ai_response(prompt: str):
    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'mistral'
    request.model_spec.signature_name = 'serving_default'
    request.inputs['input'].CopyFrom(
        tf.make_tensor_proto([prompt], shape=[1]))
    
    result = stub.Predict(request, 10.0)  # 10 secs timeout
    output = tf.make_ndarray(result.outputs['output'])
    return output[0].decode('utf-8')

