def agrupar_skus_por_regra(input_str, output_path="agrupados.txt"):
    linhas = input_str.strip().splitlines()
    agrupados = {}

    for linha in linhas:
        if not linha.strip():
            continue  # pular linhas em branco
        try:
            sku_part, regra_part = linha.split("|")
            sku = sku_part.split(":")[1].strip()
            regra = regra_part.split(":")[1].strip()
            agrupados.setdefault(regra, []).append(sku)
        except ValueError:
            print(f"Linha ignorada (formato inválido): {linha}")

    with open(output_path, "w", encoding="utf-8") as f:
        for regra, skus in agrupados.items():
            skus_com_aspas = [f"'{sku}'" for sku in skus]
            linha_formatada = f"{regra}: [{', '.join(skus_com_aspas)}]"
            f.write(linha_formatada + "\n")

    print(f"Arquivo '{output_path}' gerado com sucesso.")





# Exemplo de uso:
if __name__ == "__main__":
    input_data = """
SKU: 35348 | Regra de Bloqueio: Bicos
SKU: 35361 | Regra de Bloqueio: Bicos
SKU: 35363 | Regra de Bloqueio: Bicos
SKU: 51845 | Regra de Bloqueio: Bicos
SKU: 51848 | Regra de Bloqueio: Bicos
SKU: 62269 | Regra de Bloqueio: Bicos
SKU: 23653 | Regra de Bloqueio: Bicos
SKU: 9836 | Regra de Bloqueio: Bicos
SKU: 1151049 | Regra de Bloqueio: Bicos
SKU: 68204 | Regra de Bloqueio: Bicos
SKU: 7802 | Regra de Bloqueio: Bicos
SKU: 811618 | Regra de Bloqueio: Bicos
SKU: 811619 | Regra de Bloqueio: Bicos
SKU: 224342 | Regra de Bloqueio: Bicos
SKU: 227043 | Regra de Bloqueio: Bicos
SKU: 227018 | Regra de Bloqueio: Bicos
SKU: 227029 | Regra de Bloqueio: Bicos
SKU: 226971 | Regra de Bloqueio: Bicos
SKU: 226930 | Regra de Bloqueio: Bicos
SKU: 226629 | Regra de Bloqueio: Bicos
SKU: 3750 | Regra de Bloqueio: Bicos
SKU: 3751 | Regra de Bloqueio: Bicos
SKU: 3748 | Regra de Bloqueio: Bicos
SKU: 44771 | Regra de Bloqueio: Bicos
SKU: 44772 | Regra de Bloqueio: Bicos
SKU: 360153 | Regra de Bloqueio: Bicos
SKU: 360293 | Regra de Bloqueio: Bicos
SKU: 79679 | Regra de Bloqueio: Bicos
SKU: 65188 | Regra de Bloqueio: Bicos
SKU: 65194 | Regra de Bloqueio: Bicos
SKU: 64837 | Regra de Bloqueio: Bicos
SKU: 1247922 | Regra de Bloqueio: Bicos
SKU: 1247924 | Regra de Bloqueio: Bicos
SKU: 1247925 | Regra de Bloqueio: Bicos
SKU: 16681 | Regra de Bloqueio: Bicos
SKU: 7186 | Regra de Bloqueio: Bicos
SKU: 17778 | Regra de Bloqueio: Bicos
SKU: 66261 | Regra de Bloqueio: Bicos
SKU: 26574 | Regra de Bloqueio: Bicos
SKU: 80944 | Regra de Bloqueio: Bicos
SKU: 23044 | Regra de Bloqueio: Bicos
SKU: 26804 | Regra de Bloqueio: Bicos
SKU: 26802 | Regra de Bloqueio: Bicos
SKU: 8168 | Regra de Bloqueio: Bicos
SKU: 57500 | Regra de Bloqueio: Bicos
SKU: 357104 | Regra de Bloqueio: Bicos
SKU: 11984 | Regra de Bloqueio: Bicos
SKU: 73696 | Regra de Bloqueio: Bicos
SKU: 11985 | Regra de Bloqueio: Bicos
SKU: 11987 | Regra de Bloqueio: Bicos
SKU: 5957 | Regra de Bloqueio: Bicos
SKU: 11988 | Regra de Bloqueio: Bicos
SKU: 26839 | Regra de Bloqueio: Bicos
SKU: 5334 | Regra de Bloqueio: Bicos
SKU: 96462 | Regra de Bloqueio: Bicos
SKU: 79279 | Regra de Bloqueio: Bicos
SKU: 568571 | Regra de Bloqueio: Bicos
SKU: 568581 | Regra de Bloqueio: Bicos
SKU: 79276 | Regra de Bloqueio: Bicos
SKU: 47788 | Regra de Bloqueio: Bicos
SKU: 243521 | Regra de Bloqueio: Bicos
SKU: 243515 | Regra de Bloqueio: Bicos
SKU: 243522 | Regra de Bloqueio: Bicos
SKU: 243519 | Regra de Bloqueio: Bicos
SKU: 32090 | Regra de Bloqueio: Bicos
SKU: 3965 | Regra de Bloqueio: Bicos
SKU: 3966 | Regra de Bloqueio: Bicos
SKU: 3962 | Regra de Bloqueio: Bicos
SKU: 3964 | Regra de Bloqueio: Bicos
SKU: 21188 | Regra de Bloqueio: Bicos
SKU: 7094 | Regra de Bloqueio: Bicos
SKU: 21187 | Regra de Bloqueio: Bicos
SKU: 7093 | Regra de Bloqueio: Bicos
SKU: 63902 | Regra de Bloqueio: Bicos
SKU: 38125 | Regra de Bloqueio: Bicos
SKU: 38128 | Regra de Bloqueio: Bicos
SKU: 38124 | Regra de Bloqueio: Bicos
SKU: 38127 | Regra de Bloqueio: Bicos
SKU: 169807 | Regra de Bloqueio: Bicos
SKU: 169808 | Regra de Bloqueio: Bicos
SKU: 169809 | Regra de Bloqueio: Bicos
SKU: 61162 | Regra de Bloqueio: Chupetas
SKU: 60667 | Regra de Bloqueio: Chupetas
SKU: 60655 | Regra de Bloqueio: Chupetas
SKU: 60668 | Regra de Bloqueio: Chupetas
SKU: 33006 | Regra de Bloqueio: Chupetas
SKU: 60095 | Regra de Bloqueio: Chupetas
SKU: 60098 | Regra de Bloqueio: Chupetas
SKU: 60112 | Regra de Bloqueio: Chupetas
SKU: 60144 | Regra de Bloqueio: Chupetas
SKU: 7829 | Regra de Bloqueio: Chupetas
SKU: 7804 | Regra de Bloqueio: Chupetas
SKU: 33007 | Regra de Bloqueio: Chupetas
SKU: 60090 | Regra de Bloqueio: Chupetas
SKU: 60091 | Regra de Bloqueio: Chupetas
SKU: 7801 | Regra de Bloqueio: Chupetas
SKU: 9835 | Regra de Bloqueio: Chupetas
SKU: 64313 | Regra de Bloqueio: Chupetas
SKU: 360151 | Regra de Bloqueio: Chupetas
SKU: 360152 | Regra de Bloqueio: Chupetas
SKU: 360149 | Regra de Bloqueio: Chupetas
SKU: 360150 | Regra de Bloqueio: Chupetas
SKU: 9933 | Regra de Bloqueio: Chupetas
SKU: 922228 | Regra de Bloqueio: Chupetas
SKU: 922229 | Regra de Bloqueio: Chupetas
SKU: 1247918 | Regra de Bloqueio: Chupetas
SKU: 1247919 | Regra de Bloqueio: Chupetas
SKU: 7187 | Regra de Bloqueio: Chupetas
SKU: 7188 | Regra de Bloqueio: Chupetas
SKU: 6391 | Regra de Bloqueio: Chupetas
SKU: 6392 | Regra de Bloqueio: Chupetas
SKU: 42843 | Regra de Bloqueio: Chupetas
SKU: 26587 | Regra de Bloqueio: Chupetas
SKU: 833686 | Regra de Bloqueio: Chupetas
SKU: 833687 | Regra de Bloqueio: Chupetas
SKU: 57554 | Regra de Bloqueio: Chupetas
SKU: 3578 | Regra de Bloqueio: Chupetas
SKU: 3580 | Regra de Bloqueio: Chupetas
SKU: 64845 | Regra de Bloqueio: Chupetas
SKU: 138831 | Regra de Bloqueio: Chupetas
SKU: 138829 | Regra de Bloqueio: Chupetas
SKU: 70925 | Regra de Bloqueio: Chupetas
SKU: 70927 | Regra de Bloqueio: Chupetas
SKU: 3679 | Regra de Bloqueio: Chupetas
SKU: 3680 | Regra de Bloqueio: Chupetas
SKU: 22232 | Regra de Bloqueio: Chupetas
SKU: 138832 | Regra de Bloqueio: Chupetas
SKU: 138859 | Regra de Bloqueio: Chupetas
SKU: 60031 | Regra de Bloqueio: Chupetas
SKU: 22234 | Regra de Bloqueio: Chupetas
SKU: 60037 | Regra de Bloqueio: Chupetas
SKU: 64807 | Regra de Bloqueio: Chupetas
SKU: 64825 | Regra de Bloqueio: Chupetas
SKU: 26715 | Regra de Bloqueio: Chupetas
SKU: 54996 | Regra de Bloqueio: Chupetas
SKU: 26724 | Regra de Bloqueio: Chupetas
SKU: 54748 | Regra de Bloqueio: Chupetas
SKU: 54752 | Regra de Bloqueio: Chupetas
SKU: 4345 | Regra de Bloqueio: Chupetas
SKU: 152737 | Regra de Bloqueio: Chupetas
SKU: 152743 | Regra de Bloqueio: Chupetas
SKU: 1034048 | Regra de Bloqueio: Chupetas
SKU: 1034047 | Regra de Bloqueio: Chupetas
SKU: 43714 | Regra de Bloqueio: Chupetas
SKU: 43718 | Regra de Bloqueio: Chupetas
SKU: 57200 | Regra de Bloqueio: Chupetas
SKU: 57222 | Regra de Bloqueio: Chupetas
SKU: 64798 | Regra de Bloqueio: Chupetas
SKU: 71662 | Regra de Bloqueio: Chupetas
SKU: 58200 | Regra de Bloqueio: Chupetas
SKU: 58088 | Regra de Bloqueio: Chupetas
SKU: 43712 | Regra de Bloqueio: Chupetas
SKU: 43709 | Regra de Bloqueio: Chupetas
SKU: 57999 | Regra de Bloqueio: Chupetas
SKU: 12430 | Regra de Bloqueio: Chupetas
SKU: 111006 | Regra de Bloqueio: Chupetas
SKU: 111007 | Regra de Bloqueio: Chupetas
SKU: 117303 | Regra de Bloqueio: Chupetas
SKU: 77259 | Regra de Bloqueio: Chupetas
SKU: 117302 | Regra de Bloqueio: Chupetas
SKU: 77260 | Regra de Bloqueio: Chupetas
SKU: 20733 | Regra de Bloqueio: Chupetas
SKU: 11995 | Regra de Bloqueio: Chupetas
SKU: 11997 | Regra de Bloqueio: Chupetas
SKU: 51402 | Regra de Bloqueio: Chupetas
SKU: 77340 | Regra de Bloqueio: Chupetas
SKU: 77342 | Regra de Bloqueio: Chupetas
SKU: 542113 | Regra de Bloqueio: Chupetas
SKU: 542115 | Regra de Bloqueio: Chupetas
SKU: 542114 | Regra de Bloqueio: Chupetas
SKU: 117306 | Regra de Bloqueio: Chupetas
SKU: 117307 | Regra de Bloqueio: Chupetas
SKU: 416970 | Regra de Bloqueio: Chupetas
SKU: 416972 | Regra de Bloqueio: Chupetas
SKU: 416971 | Regra de Bloqueio: Chupetas
SKU: 7571 | Regra de Bloqueio: Chupetas
SKU: 7572 | Regra de Bloqueio: Chupetas
SKU: 417001 | Regra de Bloqueio: Chupetas
SKU: 417017 | Regra de Bloqueio: Chupetas
SKU: 417063 | Regra de Bloqueio: Chupetas
SKU: 7190 | Regra de Bloqueio: Chupetas
SKU: 12125 | Regra de Bloqueio: Chupetas
SKU: 12127 | Regra de Bloqueio: Chupetas
SKU: 12128 | Regra de Bloqueio: Chupetas
SKU: 12144 | Regra de Bloqueio: Chupetas
SKU: 63478 | Regra de Bloqueio: Chupetas
SKU: 72801 | Regra de Bloqueio: Chupetas
SKU: 117298 | Regra de Bloqueio: Chupetas
SKU: 95653 | Regra de Bloqueio: Chupetas
SKU: 34533 | Regra de Bloqueio: Chupetas
SKU: 117304 | Regra de Bloqueio: Chupetas
SKU: 117300 | Regra de Bloqueio: Chupetas
SKU: 139270 | Regra de Bloqueio: Chupetas
SKU: 139271 | Regra de Bloqueio: Chupetas
SKU: 790339 | Regra de Bloqueio: Chupetas
SKU: 790341 | Regra de Bloqueio: Chupetas
SKU: 77251 | Regra de Bloqueio: Chupetas
SKU: 77252 | Regra de Bloqueio: Chupetas
SKU: 117299 | Regra de Bloqueio: Chupetas
SKU: 77254 | Regra de Bloqueio: Chupetas
SKU: 117297 | Regra de Bloqueio: Chupetas
SKU: 77255 | Regra de Bloqueio: Chupetas
SKU: 416977 | Regra de Bloqueio: Chupetas
SKU: 416978 | Regra de Bloqueio: Chupetas
SKU: 117305 | Regra de Bloqueio: Chupetas
SKU: 77256 | Regra de Bloqueio: Chupetas
SKU: 117301 | Regra de Bloqueio: Chupetas
SKU: 77258 | Regra de Bloqueio: Chupetas
SKU: 790337 | Regra de Bloqueio: Chupetas
SKU: 417000 | Regra de Bloqueio: Chupetas
SKU: 790338 | Regra de Bloqueio: Chupetas
SKU: 790334 | Regra de Bloqueio: Chupetas
SKU: 790335 | Regra de Bloqueio: Chupetas
SKU: 790342 | Regra de Bloqueio: Chupetas
SKU: 790343 | Regra de Bloqueio: Chupetas
SKU: 72803 | Regra de Bloqueio: Chupetas
SKU: 72806 | Regra de Bloqueio: Chupetas
SKU: 77326 | Regra de Bloqueio: Chupetas
SKU: 77328 | Regra de Bloqueio: Chupetas
SKU: 417086 | Regra de Bloqueio: Chupetas
SKU: 417089 | Regra de Bloqueio: Chupetas
SKU: 416974 | Regra de Bloqueio: Chupetas
SKU: 416976 | Regra de Bloqueio: Chupetas
SKU: 416975 | Regra de Bloqueio: Chupetas
SKU: 416973 | Regra de Bloqueio: Chupetas
SKU: 72810 | Regra de Bloqueio: Chupetas
SKU: 31411 | Regra de Bloqueio: Chupetas
SKU: 31414 | Regra de Bloqueio: Chupetas
SKU: 76795 | Regra de Bloqueio: Chupetas
SKU: 53975 | Regra de Bloqueio: Chupetas
SKU: 28861 | Regra de Bloqueio: Chupetas
SKU: 28864 | Regra de Bloqueio: Chupetas
SKU: 117296 | Regra de Bloqueio: Chupetas
SKU: 542116 | Regra de Bloqueio: Chupetas
SKU: 542118 | Regra de Bloqueio: Chupetas
SKU: 542117 | Regra de Bloqueio: Chupetas
SKU: 77336 | Regra de Bloqueio: Chupetas
SKU: 77339 | Regra de Bloqueio: Chupetas
SKU: 72713 | Regra de Bloqueio: Chupetas
SKU: 51961 | Regra de Bloqueio: Chupetas
SKU: 51964 | Regra de Bloqueio: Chupetas
SKU: 51957 | Regra de Bloqueio: Chupetas
SKU: 47855 | Regra de Bloqueio: Chupetas
SKU: 47877 | Regra de Bloqueio: Chupetas
SKU: 49912 | Regra de Bloqueio: Chupetas
SKU: 243534 | Regra de Bloqueio: Chupetas
SKU: 243536 | Regra de Bloqueio: Chupetas
SKU: 243540 | Regra de Bloqueio: Chupetas
SKU: 250080 | Regra de Bloqueio: Chupetas
SKU: 243539 | Regra de Bloqueio: Chupetas
SKU: 250066 | Regra de Bloqueio: Chupetas
SKU: 1061570 | Regra de Bloqueio: Chupetas
SKU: 1061571 | Regra de Bloqueio: Chupetas
SKU: 243526 | Regra de Bloqueio: Chupetas
SKU: 243530 | Regra de Bloqueio: Chupetas
SKU: 243528 | Regra de Bloqueio: Chupetas
SKU: 250089 | Regra de Bloqueio: Chupetas
SKU: 250090 | Regra de Bloqueio: Chupetas
SKU: 3968 | Regra de Bloqueio: Chupetas
SKU: 3969 | Regra de Bloqueio: Chupetas
SKU: 16936 | Regra de Bloqueio: Chupetas
SKU: 21211 | Regra de Bloqueio: Chupetas
SKU: 21214 | Regra de Bloqueio: Chupetas
SKU: 61294 | Regra de Bloqueio: Chupetas
SKU: 61295 | Regra de Bloqueio: Chupetas
SKU: 61298 | Regra de Bloqueio: Chupetas
SKU: 154501 | Regra de Bloqueio: Chupetas
SKU: 154512 | Regra de Bloqueio: Chupetas
SKU: 154529 | Regra de Bloqueio: Chupetas
SKU: 14549 | Regra de Bloqueio: Chupetas
SKU: 54208 | Regra de Bloqueio: Chupetas
SKU: 54207 | Regra de Bloqueio: Chupetas
SKU: 75674 | Regra de Bloqueio: Chupetas
SKU: 75675 | Regra de Bloqueio: Chupetas
SKU: 154645 | Regra de Bloqueio: Chupetas
SKU: 154644 | Regra de Bloqueio: Chupetas
SKU: 13868 | Regra de Bloqueio: Chupetas
SKU: 13865 | Regra de Bloqueio: Chupetas
SKU: 154416 | Regra de Bloqueio: Chupetas
SKU: 73415 | Regra de Bloqueio: Chupetas
SKU: 154656 | Regra de Bloqueio: Chupetas
SKU: 73418 | Regra de Bloqueio: Chupetas
SKU: 154657 | Regra de Bloqueio: Chupetas
SKU: 73414 | Regra de Bloqueio: Chupetas
SKU: 790162 | Regra de Bloqueio: Chupetas
SKU: 790164 | Regra de Bloqueio: Chupetas
SKU: 62771 | Regra de Bloqueio: Mamadeiras
SKU: 75662 | Regra de Bloqueio: Mamadeiras
SKU: 10053 | Regra de Bloqueio: Mamadeiras
SKU: 110534 | Regra de Bloqueio: Mamadeiras
SKU: 62922 | Regra de Bloqueio: Mamadeiras
SKU: 62920 | Regra de Bloqueio: Mamadeiras
SKU: 65178 | Regra de Bloqueio: Mamadeiras
SKU: 7834 | Regra de Bloqueio: Mamadeiras
SKU: 811616 | Regra de Bloqueio: Mamadeiras
SKU: 65189 | Regra de Bloqueio: Mamadeiras
SKU: 65212 | Regra de Bloqueio: Mamadeiras
SKU: 71684 | Regra de Bloqueio: Mamadeiras
SKU: 811611 | Regra de Bloqueio: Mamadeiras
SKU: 811617 | Regra de Bloqueio: Mamadeiras
SKU: 7833 | Regra de Bloqueio: Mamadeiras
SKU: 65218 | Regra de Bloqueio: Mamadeiras
SKU: 65234 | Regra de Bloqueio: Mamadeiras
SKU: 811614 | Regra de Bloqueio: Mamadeiras
SKU: 62755 | Regra de Bloqueio: Mamadeiras
SKU: 110533 | Regra de Bloqueio: Mamadeiras
SKU: 65239 | Regra de Bloqueio: Mamadeiras
SKU: 7827 | Regra de Bloqueio: Mamadeiras
SKU: 2476 | Regra de Bloqueio: Mamadeiras
SKU: 35365 | Regra de Bloqueio: Mamadeiras
SKU: 65248 | Regra de Bloqueio: Mamadeiras
SKU: 227651 | Regra de Bloqueio: Mamadeiras
SKU: 228184 | Regra de Bloqueio: Mamadeiras
SKU: 227810 | Regra de Bloqueio: Mamadeiras
SKU: 228151 | Regra de Bloqueio: Mamadeiras
SKU: 228183 | Regra de Bloqueio: Mamadeiras
SKU: 227708 | Regra de Bloqueio: Mamadeiras
SKU: 227658 | Regra de Bloqueio: Mamadeiras
SKU: 227709 | Regra de Bloqueio: Mamadeiras
SKU: 227681 | Regra de Bloqueio: Mamadeiras
SKU: 227768 | Regra de Bloqueio: Mamadeiras
SKU: 227808 | Regra de Bloqueio: Mamadeiras
SKU: 228189 | Regra de Bloqueio: Mamadeiras
SKU: 228187 | Regra de Bloqueio: Mamadeiras
SKU: 228193 | Regra de Bloqueio: Mamadeiras
SKU: 228186 | Regra de Bloqueio: Mamadeiras
SKU: 58755 | Regra de Bloqueio: Mamadeiras
SKU: 65101 | Regra de Bloqueio: Mamadeiras
SKU: 3747 | Regra de Bloqueio: Mamadeiras
SKU: 44778 | Regra de Bloqueio: Mamadeiras
SKU: 44782 | Regra de Bloqueio: Mamadeiras
SKU: 44784 | Regra de Bloqueio: Mamadeiras
SKU: 44780 | Regra de Bloqueio: Mamadeiras
SKU: 360146 | Regra de Bloqueio: Mamadeiras
SKU: 360147 | Regra de Bloqueio: Mamadeiras
SKU: 360148 | Regra de Bloqueio: Mamadeiras
SKU: 922224 | Regra de Bloqueio: Mamadeiras
SKU: 922223 | Regra de Bloqueio: Mamadeiras
SKU: 65203 | Regra de Bloqueio: Mamadeiras
SKU: 1247926 | Regra de Bloqueio: Mamadeiras
SKU: 1247933 | Regra de Bloqueio: Mamadeiras
SKU: 66406 | Regra de Bloqueio: Mamadeiras
SKU: 66407 | Regra de Bloqueio: Mamadeiras
SKU: 138877 | Regra de Bloqueio: Mamadeiras
SKU: 138879 | Regra de Bloqueio: Mamadeiras
SKU: 138880 | Regra de Bloqueio: Mamadeiras
SKU: 138878 | Regra de Bloqueio: Mamadeiras
SKU: 56771 | Regra de Bloqueio: Mamadeiras
SKU: 56887 | Regra de Bloqueio: Mamadeiras
SKU: 64966 | Regra de Bloqueio: Mamadeiras
SKU: 64971 | Regra de Bloqueio: Mamadeiras
SKU: 53359 | Regra de Bloqueio: Mamadeiras
SKU: 26768 | Regra de Bloqueio: Mamadeiras
SKU: 331907 | Regra de Bloqueio: Mamadeiras
SKU: 37152 | Regra de Bloqueio: Mamadeiras
SKU: 138827 | Regra de Bloqueio: Mamadeiras
SKU: 37406 | Regra de Bloqueio: Mamadeiras
SKU: 37407 | Regra de Bloqueio: Mamadeiras
SKU: 62787 | Regra de Bloqueio: Mamadeiras
SKU: 62792 | Regra de Bloqueio: Mamadeiras
SKU: 26782 | Regra de Bloqueio: Mamadeiras
SKU: 31652 | Regra de Bloqueio: Mamadeiras
SKU: 26785 | Regra de Bloqueio: Mamadeiras
SKU: 26786 | Regra de Bloqueio: Mamadeiras
SKU: 31651 | Regra de Bloqueio: Mamadeiras
SKU: 154173 | Regra de Bloqueio: Mamadeiras
SKU: 77184 | Regra de Bloqueio: Mamadeiras
SKU: 154227 | Regra de Bloqueio: Mamadeiras
SKU: 77185 | Regra de Bloqueio: Mamadeiras
SKU: 77138 | Regra de Bloqueio: Mamadeiras
SKU: 77178 | Regra de Bloqueio: Mamadeiras
SKU: 77139 | Regra de Bloqueio: Mamadeiras
SKU: 77179 | Regra de Bloqueio: Mamadeiras
SKU: 6841 | Regra de Bloqueio: Mamadeiras
SKU: 6843 | Regra de Bloqueio: Mamadeiras
SKU: 3343 | Regra de Bloqueio: Mamadeiras
SKU: 54732 | Regra de Bloqueio: Mamadeiras
SKU: 64982 | Regra de Bloqueio: Mamadeiras
SKU: 169 | Regra de Bloqueio: Mamadeiras
SKU: 170 | Regra de Bloqueio: Mamadeiras
SKU: 54725 | Regra de Bloqueio: Mamadeiras
SKU: 3173 | Regra de Bloqueio: Mamadeiras
SKU: 2049 | Regra de Bloqueio: Mamadeiras
SKU: 2050 | Regra de Bloqueio: Mamadeiras
SKU: 26834 | Regra de Bloqueio: Mamadeiras
SKU: 54735 | Regra de Bloqueio: Mamadeiras
SKU: 152721 | Regra de Bloqueio: Mamadeiras
SKU: 152726 | Regra de Bloqueio: Mamadeiras
SKU: 152727 | Regra de Bloqueio: Mamadeiras
SKU: 152714 | Regra de Bloqueio: Mamadeiras
SKU: 152709 | Regra de Bloqueio: Mamadeiras
SKU: 152719 | Regra de Bloqueio: Mamadeiras
SKU: 152711 | Regra de Bloqueio: Mamadeiras
SKU: 1034046 | Regra de Bloqueio: Mamadeiras
SKU: 1034045 | Regra de Bloqueio: Mamadeiras
SKU: 152734 | Regra de Bloqueio: Mamadeiras
SKU: 152733 | Regra de Bloqueio: Mamadeiras
SKU: 152735 | Regra de Bloqueio: Mamadeiras
SKU: 152728 | Regra de Bloqueio: Mamadeiras
SKU: 152731 | Regra de Bloqueio: Mamadeiras
SKU: 152729 | Regra de Bloqueio: Mamadeiras
SKU: 152732 | Regra de Bloqueio: Mamadeiras
SKU: 531516 | Regra de Bloqueio: Mamadeiras
SKU: 531514 | Regra de Bloqueio: Mamadeiras
SKU: 77442 | Regra de Bloqueio: Mamadeiras
SKU: 77438 | Regra de Bloqueio: Mamadeiras
SKU: 77444 | Regra de Bloqueio: Mamadeiras
SKU: 77441 | Regra de Bloqueio: Mamadeiras
SKU: 76793 | Regra de Bloqueio: Mamadeiras
SKU: 9059 | Regra de Bloqueio: Mamadeiras
SKU: 9061 | Regra de Bloqueio: Mamadeiras
SKU: 19288 | Regra de Bloqueio: Mamadeiras
SKU: 4608 | Regra de Bloqueio: Mamadeiras
SKU: 79092 | Regra de Bloqueio: Mamadeiras
SKU: 79091 | Regra de Bloqueio: Mamadeiras
SKU: 79094 | Regra de Bloqueio: Mamadeiras
SKU: 79095 | Regra de Bloqueio: Mamadeiras
SKU: 111008 | Regra de Bloqueio: Mamadeiras
SKU: 79098 | Regra de Bloqueio: Mamadeiras
SKU: 79096 | Regra de Bloqueio: Mamadeiras
SKU: 79038 | Regra de Bloqueio: Mamadeiras
SKU: 79040 | Regra de Bloqueio: Mamadeiras
SKU: 16907 | Regra de Bloqueio: Mamadeiras
SKU: 11991 | Regra de Bloqueio: Mamadeiras
SKU: 11992 | Regra de Bloqueio: Mamadeiras
SKU: 16906 | Regra de Bloqueio: Mamadeiras
SKU: 58133 | Regra de Bloqueio: Mamadeiras
SKU: 417091 | Regra de Bloqueio: Mamadeiras
SKU: 417093 | Regra de Bloqueio: Mamadeiras
SKU: 417092 | Regra de Bloqueio: Mamadeiras
SKU: 77262 | Regra de Bloqueio: Mamadeiras
SKU: 77430 | Regra de Bloqueio: Mamadeiras
SKU: 77434 | Regra de Bloqueio: Mamadeiras
SKU: 117309 | Regra de Bloqueio: Mamadeiras
SKU: 57900 | Regra de Bloqueio: Mamadeiras
SKU: 15808 | Regra de Bloqueio: Mamadeiras
SKU: 26319 | Regra de Bloqueio: Mamadeiras
SKU: 51343 | Regra de Bloqueio: Mamadeiras
SKU: 71263 | Regra de Bloqueio: Mamadeiras
SKU: 568555 | Regra de Bloqueio: Mamadeiras
SKU: 47791 | Regra de Bloqueio: Mamadeiras
SKU: 47792 | Regra de Bloqueio: Mamadeiras
SKU: 47794 | Regra de Bloqueio: Mamadeiras
SKU: 47795 | Regra de Bloqueio: Mamadeiras
SKU: 47798 | Regra de Bloqueio: Mamadeiras
SKU: 47844 | Regra de Bloqueio: Mamadeiras
SKU: 568522 | Regra de Bloqueio: Mamadeiras
SKU: 568504 | Regra de Bloqueio: Mamadeiras
SKU: 243480 | Regra de Bloqueio: Mamadeiras
SKU: 243490 | Regra de Bloqueio: Mamadeiras
SKU: 243484 | Regra de Bloqueio: Mamadeiras
SKU: 243492 | Regra de Bloqueio: Mamadeiras
SKU: 243486 | Regra de Bloqueio: Mamadeiras
SKU: 243489 | Regra de Bloqueio: Mamadeiras
SKU: 1061587 | Regra de Bloqueio: Mamadeiras
SKU: 1061610 | Regra de Bloqueio: Mamadeiras
SKU: 61304 | Regra de Bloqueio: Mamadeiras
SKU: 61306 | Regra de Bloqueio: Mamadeiras
SKU: 21194 | Regra de Bloqueio: Mamadeiras
SKU: 21215 | Regra de Bloqueio: Mamadeiras
SKU: 21192 | Regra de Bloqueio: Mamadeiras
SKU: 54214 | Regra de Bloqueio: Mamadeiras
SKU: 54209 | Regra de Bloqueio: Mamadeiras
SKU: 54213 | Regra de Bloqueio: Mamadeiras
SKU: 75680 | Regra de Bloqueio: Mamadeiras
SKU: 169655 | Regra de Bloqueio: Mamadeiras
SKU: 169745 | Regra de Bloqueio: Mamadeiras
SKU: 3976 | Regra de Bloqueio: Mamadeiras
SKU: 169711 | Regra de Bloqueio: Mamadeiras
SKU: 169772 | Regra de Bloqueio: Mamadeiras
SKU: 3977 | Regra de Bloqueio: Mamadeiras
SKU: 79129 | Regra de Bloqueio: Mamadeiras
SKU: 79127 | Regra de Bloqueio: Mamadeiras
SKU: 79128 | Regra de Bloqueio: Mamadeiras
SKU: 62914 | Regra de Bloqueio: Mamadeiras
SKU: 62767 | Regra de Bloqueio: Mamadeiras
SKU: 62803 | Regra de Bloqueio: Mamadeiras
SKU: 72332 | Regra de Bloqueio: Mamadeiras
SKU: 74453 | Regra de Bloqueio: Mamadeiras
SKU: 71095 | Regra de Bloqueio: Mamadeiras
SKU: 71094 | Regra de Bloqueio: Mamadeiras
SKU: 71097 | Regra de Bloqueio: Mamadeiras
SKU: 71098 | Regra de Bloqueio: Mamadeiras
SKU: 34292 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 34294 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 999266 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 75290 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 34297 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 999267 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 65236 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 34298 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 5881 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 5885 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 513750 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 513751 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 5879 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 5880 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 5884 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 71777 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 72115 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 78668 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 78665 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 15451 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 3949 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 78670 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 78666 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 54526 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 3952 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 38776 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 75264 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 38777 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 75267 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2420 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2421 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 57322 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 83554 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 29108 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 20336 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 63530 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 337254 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 337255 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 62189 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 28080 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 62343 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 14343 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2766 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2769 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2762 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2765 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2768 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 499288 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 27610 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 62646 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 59826 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 499289 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 34569 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 62153 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 44770 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 70654 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 75907 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 70652 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 75909 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2543 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 30797 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 2569 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 30798 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 30795 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 56995 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 948 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 949 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 13121 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 45694 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 12686 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 1131214 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 954730 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 12595 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 58747 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 954684 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 42365 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 3220 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 50879 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 72538 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 19372 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 5071 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 44670 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 58745 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 32257 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 67235 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 3946 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 116532 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 3954 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 55612 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 3948 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 34690 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 8882 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 62219 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 116531 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 61271 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 66028 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 993469 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 35632 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 35628 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 30147 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 80449 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 9674 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 8295 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 68792 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 83999 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 60213 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 859122 | Regra de Bloqueio: Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 741314 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 223488 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 223571 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 1064146 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 250640 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 250635 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111204 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111202 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 23833 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 69427 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 55634 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 151421 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 151422 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 23977 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 23988 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 76566 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 76568 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 30145 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 39810 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 76571 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 4897 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 741050 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 6174 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 741049 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 25422 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 1154463 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 741047 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 741052 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 58221 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 29078 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 29082 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 39103 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 46682 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111734 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 865240 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 110088 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 865235 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111013 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 72071 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 865241 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 865234 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 1219530 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111735 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 8881 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 865237 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 865242 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 41843 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 42169 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 17293 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 30801 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111732 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111203 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 111201 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 68935 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 68938 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 68634 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 68638 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 68625 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 28106 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 720749 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 95305 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 47284 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 117630 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 3961 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 117628 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 59658 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 68631 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 67221 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 67352 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 8817 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 5073 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 58758 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade
SKU: 58754 | Regra de Bloqueio: Aviso - Fórmulas infantis destinadas a crianças em amamentação até os 11 meses e 29 dias de idade

"""
    agrupar_skus_por_regra(input_data)
