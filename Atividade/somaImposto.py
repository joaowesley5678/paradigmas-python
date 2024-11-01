def somaImposto(taxaImposto, custo):
    taxa = 0.5
    aumento = (taxaImposto * custo)/100

    return custo + (aumento * taxa)
