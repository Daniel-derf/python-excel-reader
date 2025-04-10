import csv
from concurrent.futures import ProcessPoolExecutor, as_completed

p = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
    'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

regras = [
    # Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
    {
        'nome': 'Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade',
        'H': 'infantil',
        'J': 'leites infantis',
        'L': ['formulas de rotina', 'formulas especiais']
    },
    # Mamadeiras
    {
        'nome': 'Mamadeiras',
        'H': 'infantil',
        'J': ['mamadeiras, bicos e chupetas'],
        'L': ['mamadeira']
    },
    # Bicos
    {
        'nome': 'Bicos',
        'H': 'infantil',
        'J': ['mamadeiras, bicos e chupetas'],
        'L': ['bico de mamadeira']
    },
    # Chupetas
    {
        'nome': 'Chupetas',
        'H': 'infantil',
        'J': ['mamadeiras, bicos e chupetas', 'utensílios infantis'],
        'L': ['chupeta', 'prendedor de chupeta', 'utensílios infantis'],
        'N': 'acessórios infantis',
        'R-contains': 'chup' 
    }
]

def is_blocked(row):
    valores = {col: row[p[col]].lower() for col in p}

    for regra in regras:
        match = True
        for col, valor_regra in regra.items():
            if col == 'nome':
                continue  # Ignorar a chave 'nome' durante a comparação
            valor_atual = valores.get(col, '')
            if isinstance(valor_regra, list):
                if valor_atual not in valor_regra:
                    match = False
                    break
            else:
                if valor_atual != valor_regra:
                    match = False
                    break
        if match:
            return True, regra['nome']  # Retorna o nome da regra que causou o bloqueio

    return False, None

def processar_linha_csv(row):
    # Verifica se a linha deve ser bloqueada
    is_blocked_result, regra_nome = is_blocked(row)
    
    if is_blocked_result:
        sku = row[p['P']] if len(row) > p['P'] else ""
        return f"SKU: {sku} | Regra de Bloqueio: {regra_nome}"

    return None

def extract_csv_data(caminho_csv):
    with open(caminho_csv, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f, delimiter="\t"))
        header, linhas = reader[0], reader[1:]

    total = len(linhas)
    count = 0

    with ProcessPoolExecutor() as executor, open("saida.txt", "w", encoding="utf-8") as f_out:
        futures = {executor.submit(processar_linha_csv, row): row for row in linhas}

        for future in as_completed(futures):
            resultado = future.result()
            if resultado:
                f_out.write(resultado + "\n")
            count += 1
            progresso = (count / total) * 100
            print(f"\rProcessando: {count}/{total} ({progresso:.2f}%)", end="")

    print("\nExtração finalizada com sucesso!")

if __name__ == "__main__":
    extract_csv_data("./arquivo.csv")
