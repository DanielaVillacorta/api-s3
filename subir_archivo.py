import boto3
import base64

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']      
    nombre_archivo = event['body']['nombre_archivo'] 
    contenido_base64 = event['body']['contenido_base64']

    if not directorio.endswith('/'):
        directorio += '/'

    key = directorio + nombre_archivo

    # Proceso
    contenido_bytes = base64.b64decode(contenido_base64)

    s3 = boto3.client('s3')
    response = s3.put_object(Bucket=nombre_bucket, Key=key, Body=contenido_bytes)

    # Salida
    return {
        'statusCode': 200,
        'mensaje': f'Archivo {key} subido correctamente al bucket {nombre_bucket}'
    }
