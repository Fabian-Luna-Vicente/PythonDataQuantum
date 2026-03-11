from langchain_core.runnables import RunnableLambda,RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
import json
from dotenv import load_dotenv

load_dotenv()

Key=load_dotenv("GOOGLE_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

def preprocess_text(text):
    return text.strip()[:5000]

preprocessor=RunnableLambda(preprocess_text)

def generate_summary(text):
    prompt=f"genera un resumen en una sola oracion de: {text}"
    response=llm.invoke(prompt)
    return response.content

summary_branch=RunnableLambda(generate_summary)

def analyzer_sentiment(text):
    prompt=f"""Analiza los sentimientos del siguiente texto.
    Responde solo en formato JSON valido:
    {{"sentimiento":"positivo|negativo|neutro","razon":"justificacion breve"}}
    Texto:{text}
    
    """
    response=llm.invoke(prompt)
    content=response.content.strip()

    content=content.replace("```json","").replace("```","").strip()
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        print(e)
        print(content)
        return{"sentimiento":"neutro","razon":"Error al analisis"}

sentiment_branch=RunnableLambda(analyzer_sentiment)

def merge_results(data):
    return{
        "resumen":data["resumen"],
        "sentimiento":data["sentimiento_data"]["sentimiento"],
        "razon":data["sentimiento_data"]["razon"]
    }

merger=RunnableLambda(merge_results)

parallel_analysis=RunnableParallel({
    "resumen":summary_branch,
    "sentimiento_data":sentiment_branch
})

chain= preprocessor|parallel_analysis|merger

result=chain.invoke("El servicio estaba bien solo que estaba sucio el hotel con manchas blancas raras")
print(result)


