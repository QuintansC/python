import pandas as pd

# Dados do cronograma semanal de estudo de inglês
data = {
    "Semana": ["1-4", "5-8", "9-12", "13-16", "17-20", "21-24", "25-28", "29-32", "33-36", "37-40", "41-44", "45-48", "49-52"],
    "Segunda-feira": ["Gramática", "Conversação", "Leitura", "Vocabulário", "Audição", "Escrita", "Leitura", "Gramática", "Conversação", "Audição", "Escrita", "Leitura", "Conversação"],
    "Terça-feira": ["Vocabulário", "Leitura", "Escrita", "Gramática", "Conversação", "Audição", "Vocabulário", "Conversação", "Leitura", "Escrita", "Audição", "Vocabulário", "Gramática"],
    "Quarta-feira": ["Conversação", "Gramática", "Conversação", "Audição", "Escrita", "Leitura", "Gramática", "Vocabulário", "Audição", "Leitura", "Gramática", "Conversação", "Audição"],
    "Quinta-feira": ["Leitura", "Vocabulário", "Audição", "Conversação", "Leitura", "Gramática", "Escrita", "Audição", "Vocabulário", "Gramática", "Conversação", "Audição", "Vocabulário"],
    "Sexta-feira": ["Escrita", "Audição", "Gramática", "Leitura", "Vocabulário", "Conversação", "Audição", "Escrita", "Gramática", "Conversação", "Leitura", "Escrita", "Vocabulário"],
    "Sábado": ["Audição", "Escrita", "Vocabulário", "Escrita", "Gramática", "Vocabulário", "Conversação", "Leitura", "Escrita", "Vocabulário", "Vocabulário", "Gramática", "Leitura"],
    "Domingo": ["Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática", "Revisão e Prática"]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Caminho para salvar o arquivo
file_path = "Cronograma_Semanal_Para_Aprender_Ingles.xlsx"

# Exportar para um arquivo Excel
df.to_excel(file_path, index=False)

print(f"Planilha exportada com sucesso para {file_path}")