tool_call = primeira_resposta.choices[0].message.tool_calls[0]
argumentos = json.loads(tool_call.function.arguments)
print("O modelo quer chamar:", tool_call.function.name, "com", argumentos)

resultado = consultar_estoque(**argumentos)  # aqui, e só aqui, o Python de verdade roda
print("Resultado real da função:", resultado)

messages.append(primeira_resposta.choices[0].message)
messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": str(resultado)})

resposta_final = client.chat.completions.create(model="llama3.2:3b", messages=messages, tools=tools)
print("Resposta final ao usuário:", resposta_final.choices[0].message.content)
