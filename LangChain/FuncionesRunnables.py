from langchain_core.runnables import RunnableLambda

paso1=RunnableLambda(lambda x:f"numero {x}")

def duplicate(text):
    return [text]*2

paso2=RunnableLambda(duplicate)

cadena=paso1 | paso2

resultado=cadena.invoke(45)

print(resultado)
