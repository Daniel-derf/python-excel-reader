import pandas as pd

def generate_queries(file_path, output_file="queries.sql"):
    # Carregar o arquivo
    df = pd.read_excel(file_path, engine="odf")
    
    # Renomear colunas para facilitar o uso
    df.columns = [
        "grupo", "cod_grupo", "nivel", "cod_cat", "categoria", "cod_subcat",
        "subcategoria", "cod_marca", "desc_marca", "bl_relacionamento",
        "bl_plm_catch_all", "bl_catch_all_pers", "motivos", "acao"
    ]
    
    queries = []
    
    for _, row in df.iterrows():
        nivel = str(row["nivel"]).strip().lower()
        categoria = str(row["categoria"]).strip()
        subcategoria = str(row["subcategoria"]).strip() if pd.notna(row["subcategoria"]) else ""
        marca = str(row["desc_marca"]).strip() if pd.notna(row["desc_marca"]) else ""
        motivo = str(row["motivos"]).strip()

        if nivel == "categoria":
            query = f"""
            UPDATE products 
            SET blocked = TRUE, reason = 'Categoria: {motivo}' 
            FROM product_categories c WHERE products.product_category_id = c.id AND c.name IN ('{categoria}');
            """.strip()
        
        elif nivel == "marca":
            query = f"""
            UPDATE products
            SET blocked = TRUE, 
                reason = 'Marca: ' || b.reason
            FROM brands b, product_categories c
            WHERE products.brand_id = b.id
            AND products.product_category_id = c.id
            AND b.name = '{marca}'
            AND c.name = '{categoria}';
            """.strip()
        
        elif nivel == "subcat" and subcategoria:
            query = f"""
            UPDATE products
            SET blocked = TRUE, 
                reason = 'Subcategoria: ' || ps.reason
            FROM product_subcategory ps, product_categories c
            WHERE products.product_subcategory_id = ps.id
            AND products.product_category_id = c.id
            AND ps.name = '{subcategoria}'
            AND c.name = '{categoria}';
            """.strip()
        
        else:
            continue
        
        queries.append(query)
    
    # Salvar as queries em um arquivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(queries))
    
    print(f"✅ Queries geradas e salvas em {output_file}")

# Exemplo de uso
file_path = "./arquivo.ods"  # Altere para o caminho correto do arquivo
generate_queries(file_path)
