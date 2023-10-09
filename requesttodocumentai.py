from google.api_core.client_options import ClientOptions
from google.cloud import documentai

# Creating the options (location), client instance, and name (where to find the processor)
opts = ClientOptions(api_endpoint="us-documentai.googleapis.com")
client = documentai.DocumentProcessorServiceClient(client_options=opts)
name = client.processor_path('250193706', 'us', '293114145e64a069')

# Read the file
with open('testpassport.png', "rb") as image:
    image_content = image.read()

# Load raw file data
raw_document = documentai.RawDocument(content=image_content, mime_type='image/png')

# Request creation, specifying the processor to query and the document
request = documentai.ProcessRequest(
    name=name, raw_document=raw_document
)

# Getting the result
result = client.process_document(request=request)

# Getting the document portion of the response
document = result.document

# Read the output
print("Results:")
print(document.entities[0])
