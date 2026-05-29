# Introductie tot Artificial Intelligence

Wanneer we het hebben over Artificial Intelligence, hebben we het eigenlijk over een erg breed gebied. Dat is grotendeels op te delen in 3 delen:

## Artificial Intelligence

De code waarmee het begon. Hieronder vallen recursieve functies, megamax-strategieën om spellen te spelen, graph search algoritmes en logic programming. Voordat computers de rekenkracht hadden die ze nu hebben werd dit soort code gebruikt om computers slimmer te maken. Ze verschillen echter met wat we nu als "Artificial Intelligence" beschouwen in die zin dat ze niet leren van hun fouten. Het algoritme is maar zo slim als wij het programmeren.

## Machine learning

Het idee dat aan de basis lag van machine learning is dat we niet langer zelf de intelligentie van het systeem zouden programmeren, maar dat we een systeem maken dat zelf op basis van een paar voorbeelden een programma gaat schrijven. Bijvoorbeeld: we geven het programma een lijst met de punten van onze studenten in het eerste jaar voor de voorbije 12 jaar, samen met een indicatie of ze afstudeerden of niet. Op basis hiervan zorgt een algoritme ervoor dat we op basis van de punten van de studenten dit jaar weten of ze gaan afstuderen of niet.

"Een paar voorbeelden" is dus een understatement. We moeten het algoritme voeden met zoveel mogelijk data. Binnen het domein van machine learning is die data altijd in tabelvorm. We hebben het dan over getallen of tekst die in records zijn opgedeeld.

## Deep learning

Het verschil tussen deep learning en machine learning is het soort data dat we gebruiken als invoer. Wanneer die invoer niet langer in tabelvorm staat maar een foto is, moeten we overstappen naar deep learning. Het grote verschil is het aantal parameters waarop het model moet trainen: onze studenten hebben een twintigtal vakken in het eerste jaar. De foto boven deze tekst daarentegen is 1170x480 pixels groot. Elk van die pixels heeft een RGB-waarde, dus hebben we het over 561.600 pixels die elk 16.581.375 verschillende waardes kunnen hebben.

Op dat moment werkt een klassiek machine learning model niet meer en moeten we een neuraal netwerk gebruiken. Het zijn deze neurale netwerken die nu het nieuws halen onder namen als Chat-GPT, Bing-AI, Stable diffusion, ...

## Inhoud van de cursus

We beginnen deze cursus met een korte geschiedenisles over Artificial Intelligence. Er worden een aantal programmeervoorbeelden gegeven waar je thuis verder mee kan spelen, maar het is niet de focus van de cursus.

Daarna duiken we die in Machine Learning. We gebruiken de titanic-dataset, wat een beetje de hello-world dataset is voor machine learning.

* We maken eerst een random forecaster. Dat is een erg slecht model, maar het zorgt ervoor dat we alle stappen al eens doorlopen (data inlezen, model trainen, getraind model exporteren, een streamlit-web app maken waarin we ze hosten).
* Daarna gebruiken we PyCaret om het model te verbeteren. PyCaret is een library die het hele machine learning proces automatiseert. Het traint een hele hoop modellen en geeft dan aan welk van die modellen het beste zou zijn voor onze data. Er komt ook een model uit dat we terug naar onze web app uitrollen.
* De volgende stap is dat we zelf een model maken. Dit geeft ons een beter inzicht in de verschillende stappen die PyCaret van ons overnam waardoor we het proces beter begrijpen.
* Tenslotte grijpen we in op onze data. Kunnen wij met ons gezond verstand bepaalde ingrepen doen op de data die ervoor zorgen dat het model er meer van kan maken, bijvoorbeeld door missende data bij op te vullen of rijen met duidelijk foute data te verwijderen. Hiermee gaan we in het domein van de data science.

Op de volgende dag doen we het hele proces nog eens opnieuw, maar dan met tijdsgerelateerde data.

## Werking

De cursus is erg hands-on. Dit heeft voor- en nadelen. Voordeel is dat je zelf code hebt gemaakt die werkt en een model hebt gebruikt in een praktische setting. Het nadeel is dat het een doe-cursus wordt: je moet echt zelf aan de slag. Dat maakt het geheel minder geschikt voor cursisten met een beperkte achtergrond in programmeren.

## Hardware

Tijdens deze opleiding werk je op je eigen laptop: vergeet deze dus zeker niet mee te brengen. Heb je geen laptop: geen probleem: er staan ook een aantal vaste PC’s in het opleidingslokaal. Geef het wel even aan bij je inschrijving.

Als software gebruiken we Python en Jupyter notebooks in Visual Studio Code. De installatie hiervan brengen we tijdens de cursus in orde.
