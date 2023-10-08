import matplotlib.pyplot as plt

# Data for creating histograms
gene_description = ['AFFX-BioB-5_at', 'AFFX-BioB-M_at', 'AFFX-BioB-3_at', 'AFFX-BioC-5_at', 'AFFX-BioC-3_at', 'AFFX-BioDn-5_at', 'AFFX-BioDn-3_at', 'AFFX-CreX-5_at']
gene_accession_number = ['AFFX-BioB-5_at', 'AFFX-BioB-M_at', 'AFFX-BioB-3_at', 'AFFX-BioC-5_at', 'AFFX-BioC-3_at', 'AFFX-BioDn-5_at', 'AFFX-BioDn-3_at', 'AFFX-CreX-5_at']
values = [
    [-214, -153, -58, 88, -295, -558, 199, -176],
    [-139, -73, -1, 283, -264, -400, -330, -168],
    [-76, -49, -307, 309, -376, -650, 33, -367],
    # ... continue with the rest of the data
]

# Create histograms
for i in range(len(gene_description)):
    plt.figure(figsize=(8, 6))
    plt.hist(values[i], bins=20, color='skyblue', alpha=0.7)
    plt.title(f'Histogram for {gene_description[i]} ({gene_accession_number[i]})')
    plt.xlabel('Expression Values')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
