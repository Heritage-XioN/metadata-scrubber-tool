import shutil
from pathlib import Path
from typing import Optional

import piexif
from PIL import Image

from src.services.metadata_handler import MetadataHandler
from src.utils.jpeg_metadata import JpegProcessaor
from src.utils.png_metadata import PngProcessor


class ImageHandler(MetadataHandler):
    def __init__(self, filepath: str):
        super().__init__(filepath)
        self.processors = {
            ".jpeg": JpegProcessaor(),
            ".jpg": JpegProcessaor(),
            ".png": PngProcessor(),
        }
        self.tags_to_delete = []

    def read(self):
        """Extracts metadata into a standard dictionary."""
        with Image.open(Path(self.filepath)) as img:
            extension = Path(self.filepath).suffix
            processor = self.processors.get(extension)

            if not processor:
                raise ValueError(f"Unsupported format: {extension}")

            self.metadata = processor.get_metadata(img)["data"]
            self.tags_to_delete = processor.get_metadata(img)["tags_to_delete"]
            return self.metadata

    def wipe(self) -> None:
        """Wipes internal metadata state."""
        with Image.open(Path(self.filepath)) as img:
            extension = Path(self.filepath).suffix
            processor = self.processors.get(extension)

            if not processor:
                raise ValueError(f"Unsupported format: {extension}")

            self.processed_metadata = processor.delete_metadata(
                img, self.tags_to_delete
            )

    def save(self, output_path: Optional[str] = None) -> None:
        """Writes the changes to a copy of the original file."""
        destination_dir = Path(output_path or "/archive/")

        # creates the destination directory if it doesn't exist
        destination_dir.mkdir(parents=True, exist_ok=True)
        destination_file_path = (
            destination_dir / f"processed_{Path(self.filepath).name}"
        )

        # copies the original file to the destination directory
        shutil.copy2(self.filepath, destination_file_path)

        # writes the processed metadata to the image in the destination directory
        with Image.open(destination_file_path) as img:
            exif_bytes = piexif.dump(self.processed_metadata)
            img.save(destination_file_path, exif=exif_bytes)


test = ImageHandler(r"C:\Users\Xheri\development\testimage\20221201_090615.jpg")
test.read()
test.wipe()
test.save()
