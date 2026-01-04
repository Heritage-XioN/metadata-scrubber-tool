import piexif  # pyright: ignore[reportMissingTypeStubs]

from src.utils.exceptions import MetadataNotFoundError, MetadataProcessingError


class JpegProcessaor:
    def __init__(self):
        self.tags_to_delete = []
        self.data = {}

    def get_metadata(self, img):
        try:
            if "exif" in img.info:
                exif_dict = piexif.load(img.info["exif"])
                for ifd, value in exif_dict.items():
                    # this exclude thumbnail IFD (its the thumbnails blob data. it can be removed but the image will take a couple more seconds to load)
                    if not isinstance(exif_dict[ifd], dict):
                        continue

                    # iterate through the IFD
                    for tag, tag_value in exif_dict[ifd].items():
                        tag_info = piexif.TAGS[ifd].get(tag, {})

                        # Get the human-readable name for the tag
                        tag_name = (
                            tag_info.get("name", "Unknown Tag")
                            if tag_info
                            else "Unknown Tag"
                        )

                        # exculudes tags that are necessary for image display integrity
                        if (
                            tag_name == "Orientation"
                            or tag_name == "ColorSpace"
                            or tag_name == "ExifTag"
                        ):
                            continue

                        # save to list and dict
                        self.tags_to_delete.append(tag)
                        self.data[tag_name] = tag_value
                return {"data": self.data, "tags_to_delete": self.tags_to_delete}
            else:
                raise MetadataNotFoundError("No EXIF data found in the image.")
        except MetadataNotFoundError as e:
            return f"Error: {str(e)}"

    def delete_metadata(self, img, tags_to_delete):
        try:
            exif_dict = piexif.load(img.info["exif"])
            for ifd, value in exif_dict.items():
                # exclude thumbnail IFD (its the thumbnails blob data so i dont wanna deal with that)
                if not isinstance(exif_dict[ifd], dict):
                    continue

                # iterate through and delete tags
                for tag in list(exif_dict[ifd]):
                    if tag in tags_to_delete:
                        del exif_dict[ifd][tag]

            return exif_dict
        except Exception as e:
            raise MetadataProcessingError(f"Error Processing: {str(e)}")
