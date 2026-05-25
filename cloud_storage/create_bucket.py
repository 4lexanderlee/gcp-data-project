import argparse
from google.cloud import storage 

def main():
    #Linea de terminal para pasar argumentos
    parse = argparse.ArgumentParser(description="Crear un bucket de GCP")
    parse.add_argument("bucket_name", type=str, help="Nombre del bucket a crear")
    args = parse.parse_args()
    
    bucket_name = args.bucket_name
    print(f"bucket_name recibido: {bucket_name}")
    #Lógica para crear bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"
    new_bucket = storage_client.create_bucket(bucket, location="us-central1")
    print(f"Wonderful: New gcp bucket is created\nName bucket: {new_bucket.name}\nCreated in: {new_bucket.location}\nWith class: {new_bucket.storage_class}")    
    

if __name__ == "__main__":
    main()