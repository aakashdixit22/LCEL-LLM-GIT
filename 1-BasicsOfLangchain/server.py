#DEPLOY LANGSERVE RUNNABLE AND CHAIN  as API
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes#add_Routes helps to ccreate api's
from dotenv import load_dotenv
load_dotenv()

gorq_api_key=os.getenv("GORQ_API_KEY")
model=ChatGroq(model="gemma2-9b-it",groq_api_key=gorq_api_key)


##prompt templates(chat prompt template basically converting the into the list of messages)
from langchain_core.prompts import ChatPromptTemplate
generic_template="Translate the folowing into {language}:"
prompt=ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","{text}")]

)
parser=StrOutputParser()
##create chain
chain=prompt|model|parser
#APP definiton
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="Langchain server is a fastapi server that provides an api to use langchain models",
            )
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":#uvicorn is a server for python used to run applications like FastAPI
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000) #after running python server.py go to http://127.0.0.1:8000/docs to see the api's
    

