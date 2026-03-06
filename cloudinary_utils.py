import os
import cloudinary
import cloudinary.uploader

def init_cloudinary():
    cloudinary.config(
        cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
        api_key=os.environ.get("CLOUDINARY_API_KEY"),
        api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
        secure=True,
    )

def upload_image_file(file_storage, folder=None):
    if not file_storage:
        return None

    folder = folder or os.environ.get("CLOUDINARY_FOLDER", "static/uploads")

    result = cloudinary.uploader.upload(
        file_storage,
        folder=folder,
        resource_type="image",
        transformation=[{"quality": "auto", "fetch_format": "auto"}],
    )

    return {
        "url": result.get("secure_url"),
        "public_id": result.get("public_id"),
        "width": result.get("width"),
        "height": result.get("height"),
        "format": result.get("format"),
    }

def delete_image_by_public_id(public_id: str):
    if not public_id:
        return
    cloudinary.uploader.destroy(public_id, resource_type="image")