
import easyocr

reader = easyocr.Reader(['en'])


def extract_text(processed_image):

    result = reader.readtext(
        processed_image,
        detail=0
    )

    text = "\n".join(result)

    return text