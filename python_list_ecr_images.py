import boto3
def list_ecr_images(repository_name):
    client = boto3.client('ecr')
    response = client.describe_images(repositoryName=repository_name)
    image_details = response['imageDetails']
    for image in image_details:
        print(f"Image Digest: {image['imageDigest']}, Image Tags: {image['imageTags'] if 'imageTags' in image else 'None'}")
if __name__ == "__main__":
    repository_name = "hedphony"  # Replace with your repository name
    list_ecr_images(repository_name)
