def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
      rows = file.readlines()
      for row in rows:
        row_list = row.strip().split('\t')
        codon  = row_list[0]
        amino_acid = row_list[2]
        print(codon, amino_acid)
        codon_dict[codon] = amino_acid
    return codon_dict
