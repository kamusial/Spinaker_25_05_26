# Import the 'os' module - provides access to operating system environment variables (e.g. API keys)
import os
# Import ImageAnalysisClient - the main "client" for communicating with Azure Vision API
from azure.ai.vision.imageanalysis import ImageAnalysisClient
# Import VisualFeatures - a list of available analysis features, e.g. TAGS, OBJECTS, READ
from azure.ai.vision.imageanalysis.models import VisualFeatures
# Import AzureKeyCredential - wraps the API key in an object that Azure recognizes as authorization
from azure.core.credentials import AzureKeyCredential



    # Get the Azure endpoint URL from the environment variable named "VISION_ENDPOINT"
endpoint = os.getenv("VISION_ENDPOINT")
    # Get the secret Azure API key from the environment variable named "VISION_KEY"
key = os.getenv("VISION_KEY")

# Create an ImageAnalysisClient object - this is what sends requests to Azure
client = ImageAnalysisClient(
    # Provide the Azure endpoint address (e.g. https://myresource.cognitiveservices.azure.com/)
    endpoint=endpoint,
    # Create an object with the API key - Azure will use it to verify we have access
    credential=AzureKeyCredential(key)
)

# Send an image analysis request for the given URL - store the result in the variable 'result'
result = client.analyze_from_url(
        # Provide the URL of the image to be analyzed by Azure
        image_url="https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png",
        # Provide the list of features to be run on the image
        visual_features=[
            # TAGS - ask Azure to return a list of keywords describing the image (e.g. "outdoor", "sky")
            VisualFeatures.TAGS,
            # OBJECTS - detect objects in the image and return their names and bounding boxes
            VisualFeatures.OBJECTS,
            # CAPTION - disabled (commented out); would return a single sentence describing the whole image
            # VisualFeatures.CAPTION,
            # DENSE_CAPTIONS - disabled; would return up to 10 descriptions for the image and individual objects
            # VisualFeatures.DENSE_CAPTIONS,
            # READ - run OCR: extract printed and handwritten text from the image
            VisualFeatures.READ,
            # SMART_CROPS - calculate coordinates of the best image crop for given aspect ratios
            VisualFeatures.SMART_CROPS,
            # PEOPLE - detect people in the image and return their bounding boxes
            VisualFeatures.PEOPLE,
        ],
        # Provide aspect ratios (width/height) for Smart Crop: 0.9 ≈ portrait, 1.33 ≈ landscape 4:3
        smart_crops_aspect_ratios=[0.9, 1.33],
        # gender_neutral_caption - disabled; would use neutral terms ("person" instead of "man"/"woman")
        # gender_neutral_caption=True,
        # Set the language of results to English - applies mainly to tags and categories
        language="en",
        # Use the latest version of the AI model on the Azure side
        model_version="latest",
    )

# Print a header - inform the user that we are starting to print the analysis results
print("Image analysis results:")

# Check if Azure returned a Caption result - may be None if it was disabled
if result.caption is not None:
    # Print the Caption section header
    print(" Caption:")
    # Print the description text and confidence level rounded to 4 decimal places
    print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

# Check if Azure returned Dense Captions results (multiple descriptions)
if result.dense_captions is not None:
    # Print the Dense Captions section header
    print(" Dense Captions:")
    # Iterate over the list of all descriptions returned by Azure
    for caption in result.dense_captions.list:
        # For each description: print the text, bounding box coordinates, and confidence level
        print(f"   '{caption.text}', {caption.bounding_box}, Confidence: {caption.confidence:.4f}")

# Check if Azure returned OCR results (text read from the image)
if result.read and result.read.blocks:
    # Print the Read (OCR) section header
    print(" Read:")
    # Iterate over lines of text in the first text block - an image can have multiple blocks
    for line in result.read.blocks[0].lines:
        # Print the full line of text and the bounding polygon describing its position on the image
        print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
        # Iterate over individual words in this line
        for word in line.words:
            # Print the word, its bounding polygon, and the recognition confidence level
            print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")

# Check if Azure returned tags (keywords describing the image)
if result.tags is not None:
    # Print the Tags section header
    print(" Tags:")
    # Iterate over the list of all tags returned by Azure
    for tag in result.tags.list:
        # Print the tag name and confidence level - closer to 1.0 means more certain detection
        print(f"   '{tag.name}', Confidence {tag.confidence:.4f}")

# Check if Azure detected any objects in the image
if result.objects is not None:
    # Print the Objects section header
    print(" Objects:")
    # Iterate over the list of detected objects
    for object in result.objects.list:
        # Print the object name (first tag), its bounding box, and detection confidence
        print(f"   '{object.tags[0].name}', {object.bounding_box}, Confidence: {object.tags[0].confidence:.4f}")

# Check if Azure detected any people in the image
if result.people is not None:
    # Print the People section header
    print(" People:")
    # Iterate over the list of detected people
    for person in result.people.list:
        # Print the person's bounding box and confidence level - does not return identity, only location
        print(f"   {person.bounding_box}, Confidence {person.confidence:.4f}")

# Check if Azure returned Smart Crop results (intelligent image crops)
if result.smart_crops is not None:
    # Print the Smart Cropping section header
    print(" Smart Cropping:")
    # Iterate over the list of crops - one for each provided aspect ratio
    for smart_crop in result.smart_crops.list:
        # Print the aspect ratio and the rectangle of the best crop for that ratio
        print(f"   Aspect ratio {smart_crop.aspect_ratio}: Smart crop {smart_crop.bounding_box}")

# Print the image height in pixels - comes from the metadata returned by Azure
print(f" Image height: {result.metadata.height}")
# Print the image width in pixels - comes from the metadata returned by Azure
print(f" Image width: {result.metadata.width}")
# Print the version of the AI model that actually analyzed the image (may differ from "latest")
print(f" Model version: {result.model_version}")
