import boto3
def list_ecr_repositories():
    client = boto3.client('ecr')
    response = client.describe_repositories()
    repositories = response['repositories']
    return repositories
def list_ecr_images(repository_name):
    client = boto3.client('ecr')
    response = client.describe_images(repositoryName=repository_name)
    return response['imageDetails']
def print_ecr_images(repository_name):
    images = list_ecr_images(repository_name)
    for image in images:
        print(f"Image Digest: {image['imageDigest']}, Image Tags: {image['imageTags'] if 'imageTags' in image else 'None'}")
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
    repository_names = ["shahebaz", "ecrepo1", "ecrepo2"]  # List of repository names
    for repository_name in repository_names:
        # List all ECR repositories
        print("Listing all ECR repositories:")
        repositories = list_ecr_repositories()
        for repo in repositories:
            print(repo['repositoryName'])
            # List all ECR images for each repository
            print("\nListing all ECR images for repository:", repo['repositoryName'])
            print_ecr_images(repo['repositoryName'])
            print()  # Add a newline to separate outputs for each repository
        # Specify the repository name and the number of image versions to keep
        num_to_keep = 2  # Number of image versions to keep
        # Then, delete old images to keep only the specified number of latest images
        print("\nDeleting old images to keep only the latest", num_to_keep, "images:")
        delete_old_images(repository_name, num_to_keep)









