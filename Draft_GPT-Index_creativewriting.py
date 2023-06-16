#this is a draft

# Import necessary libraries
from llama_index import SimpleDirectoryReader, Document, SimpleNodeParser, VectorStoreIndex, StorageContext, set_global_service_context, ServiceContext
from langchain import OpenAI
from llama_index import LLMPredictor

# Load in documents
documents = SimpleDirectoryReader('./data').load_data()

# Parse the Documents into Nodes
parser = SimpleNodeParser()
nodes = parser.get_nodes_from_documents(documents)

# Construct Index
index = VectorStoreIndex(nodes)

# Define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

# Configure service context
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# Build index
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Set global service context
set_global_service_context(service_context)

# Query the index
query_engine = index.as_query_engine()
response = query_engine.query("Write a short story about a young woman named Sarah with a brilliant imagination.")

# Print the response
print(response)
