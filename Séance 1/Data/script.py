nombre_articles = 0
motcle = "Raoult"
titres = [' Bolsonaro sur le banc des accusés après les ravages du Covid à Manaus ',
 " Gilbert Deray Bilan d'étape du virus, un an après La découverte de vaccins en un temps record est un incontestable succès médico-scientifique, mais nos échecs économiques et sociétaux dans la lutte contre le Covid-19 sont évidents, souligne le médecin ",
 ' Information et pandémie Les médias traitent-ils bien les sciences ? ',
 ' Par Nicolas Berrod, Ludwig Gallet et Paméla ',
 ' Covid-19 : le docu «Hold-up» bat des records de défiance ',
 " A Marseille, la facture n'est pas passée ",
 ' Pass sanitaire|« On y mettra fin à la minute où nous le pourrons » ',
 ' Les covidosceptiques veulent faire avaler leurs pilules ',
 ' Didier Raoult, le postmodernisme en étendard ',
 " Crise sanitaire Le professeur Raoult persiste dans ses certitudes Visé par une plainte, le directeur de l'institut Méditerranée Infection prescrit toujours l'hydroxychloroquine "]
nombre_total_articles = len(titres)
if nombre_total_articles > 0:
    for i in titres:
        if motcle in i:
            print(i)
            nombre_articles+=1
else:
    print("La liste est vide")
proportion = 100*nombre_articles/nombre_total_articles
print("Proportion d'articles contenant le terme dans le titre : {} %".format(round(proportion,1)))
