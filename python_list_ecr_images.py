import boto3
def list_ecr_images(repository_name):
    client = boto3.client('ecr')
    response = client.describe_images(repositoryName=repository_name)
    return response['imageDetails']
def delete_old_images(repository_name, num_to_keep):
    images = list_ecr_images(repository_name)
    images.sort(key=lambda x: x['imagePushedAt'], reverse=True)
    images_to_delete = images[num_to_keep:]
    if images_to_delete:
        client = boto3.client('ecr')
        for image in images_to_delete:
            image_digest = image['imageDigest']
            client.batch_delete_image(
                repositoryName=repository_name,
                imageIds=[
                    {
                        'imageDigest': image_digest
                    }
                ]
            )
            print(f"Deleted image with digest: {image_digest}")
    else:
        print("No images to delete.")
if __name__ == "__main__":
    repository_name = "hedphony"  # Your repository name
    num_to_keep = 5  # Number of image versions to keep
    delete_old_images(repository_name, num_to_keep)







