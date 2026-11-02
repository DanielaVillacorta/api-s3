import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']  # ej: "imagenes-chicas/2026/"

    # Asegurar que termine en "/"
    if not directorio.endswith('/'):
        directorio += '/'

    # Proceso
    # En S3 no existen carpetas reales; se simulan con un objeto "vacío" cuya Key termina en "/"
    s3 = boto3.client('s3')
    response = s3.put_object(Bucket=nombre_bucket, Key=directorio)

    # Salida
    return {
        'statusCode': 200,
        'mensaje': f'Directorio {directorio} creado en el bucket {nombre_bucket}'
    }
