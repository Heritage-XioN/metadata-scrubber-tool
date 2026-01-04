from PIL import ExifTags

from src.utils.exceptions import MetadataNotFoundError, MetadataProcessingError


class PngProcessor:
    def __init__(self):
        self.tags_to_delete = []
        self.data = {}

    def get_metadata(self, img):
        img.load()
        exif = img.getexif()
        try:
            if exif:
                # iterate through the (0th) IFD
                for tag, value in exif.items():
                    # Get the human-readable name for the tag
                    tag_name = ExifTags.TAGS.get(tag, tag)

                    # save to list and dict
                    self.tags_to_delete.append(tag)
                    self.data[tag_name] = value
                    print(f"{tag_name}: {value}")

                # terate through the (GPS) IFD
                gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)
                for tag, value in gps_ifd.items():
                    # Get the human-readable name for the tag
                    tag_name = ExifTags.GPSTAGS.get(tag, tag)

                    # save to list and dict
                    self.tags_to_delete.append(tag)
                    self.data[tag_name] = value
                    print(f"{tag_name}: {value}")

                return {"data": self.data, "tags_to_delete": self.tags_to_delete}
            else:
                raise MetadataNotFoundError("No EXIF data found in the image.")
        except MetadataNotFoundError as e:
            return f"Error: {str(e)}"

    def delete_metadata(self, img, tags_to_delete):
        img.load()
        exif = img.getexif()
        try:
            # iterate through the (0th) IFD
            for tag_id, value in exif.items():
                if tag_id in tags_to_delete:
                    del exif[tag_id]

            # terate through the (GPS) IFD
            gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)
            for tag_id, value in gps_ifd.items():
                if tag_id in tags_to_delete:
                    del gps_ifd[tag_id]

            return exif + gps_ifd
        except Exception as e:
            raise MetadataProcessingError(f"Error Processing image: {str(e)}")
