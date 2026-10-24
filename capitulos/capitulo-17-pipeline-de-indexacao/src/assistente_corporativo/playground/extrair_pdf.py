from pypdf import PdfReader

leitor = PdfReader("exemplo.pdf")
paginas = [pagina.extract_text() or "" for pagina in leitor.pages]
texto_completo = "\n\n".join(paginas)

print(f"O PDF tem {len(leitor.pages)} páginas e {len(texto_completo)} caracteres de texto extraído.")
print(texto_completo[:500])
