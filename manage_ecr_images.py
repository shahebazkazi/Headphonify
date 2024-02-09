import boto3

def list_ecr_images(repository_name):
    client = boto3.client('ecr')
    response = client.describe_images(repositoryName=repository_name)
    return response['imageDetails']

def print_ecr_images(repository_name):
    images = list_ecr_images(repository_name)
    for image in images:
        print(f"Image Digest: {image['imageDigest']}, Image Tags: {image.get('imageTags', 'None')}")

def delete_old_images(repository_name, num_to_keep):
    images = list_ecr_images(repository_name)
    images.sort(key=lambda x: x['imagePushedAt'], reverse=True)
    images_to_delete = images[num_to_keep:]
    if images_to_delete:
        client = boto3.client('ecr')
        for image in images_to_delete:
            image_digest = image['imageDigest']
            print(f"Deleting image with digest: {image_digest}")
            # Prompt for confirmation before deletion
            confirmation = input("Are you sure you want to delete this image? (yes/no): ")
            if confirmation.lower() == 'yes':
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
                print("Image deletion canceled.")
    else:
        print("No images to delete.")

if _name_ == "_main_":
    repository_name = "hedphony"  # Your repository name
    num_to_keep = 10  # Number of image versions to keep
    # First, list all ECR images
    print("Listing all ECR images:")
    print_ecr_images(repository_name)
    # Then, delete old images to keep only the specified number of latest images
    print("\nDeleting old images to keep only the latest", num_to_keep, "images:")
    delete_old_images(repository_name, num_to_keep)
