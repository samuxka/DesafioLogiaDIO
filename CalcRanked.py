ranked = ['Iron', 'Bronze', 'Silver', 'Gold', 'Diamond', 'Master', 'Challenger']

def calcRanked(victory, defeat):
    RankedScore = victory - defeat

    if RankedScore <= 10:
        print("Seu heroi teve ", victory, " vitorias, e ", defeat, " derrotas, o seu ranking nessa temporada é ", ranked[0], "Seu score foi ", RankedScore, " pontos")
    elif RankedScore >= 11 and RankedScore <= 20:
        print("Seu heroi teve ", victory, " vitorias, e ", defeat, " derrotas, o seu ranking nessa temporada é ", ranked[1], "Seu score foi ", RankedScore, " pontos")
    elif RankedScore >= 21 and RankedScore <= 50:
        print("Seu heroi teve ", victory, " vitorias, e ", defeat, " derrotas, o seu ranking nessa temporada é ", ranked[2], "Seu score foi ", RankedScore, " pontos")
    elif RankedScore >= 51 and RankedScore <= 80:
        print("Seu heroi teve ", victory, " vitorias, e ", defeat, " derrotas, o seu ranking nessa temporada é ", ranked[3], "Seu score foi ", RankedScore, " pontos")
    elif RankedScore >= 81 and RankedScore <= 90:
        print("Seu heroi teve ", victory, " vitorias, e ", defeat, " derrotas, o seu ranking nessa temporada é ", ranked[4], "Seu score foi ", RankedScore, " pontos")
    elif RankedScore >= 91 and RankedScore <= 100:
        print("Seu heroi teve ", victory, " vitorias, e ", defeat, " derrotas, o seu ranking nessa temporada é ", ranked[5], "Seu score foi ", RankedScore, " pontos")
    else:
        print("Seu heroi teve ", victory, " vitorias, e ", defeat, " derrotas, o seu ranking nessa temporada é ", ranked[6], "Seu score foi ", RankedScore, " pontos")

victory = int(input('Vitorias: '))
defeat = int(input('Derrotas: '))

calcRanked(victory, defeat)