# Readme opdracht 2 API van Lucas De Greef

## Informatie over het gekozen onderwerp
  >In deze opdracht hebt ik als thema gekozen dat mensen hun voornaam en achternaam konden ingeven samen met hun beroepen en hun geslacht.
  >De achternamen van deze personen worden gehased zodat alles prive blift.
  >Hier konden ze hun werkgever ingeven. Zonder toesteming te hoeven vragen van de werkgever werden deze namen ge hashed.
  >Ook werd er hier gevraagd in welke stad de werkgever zich bevindt.
  >
  >Als de personen een aanpasssing wouden doen vb. van beroep veranderen konden ze dit ook maken 
  >en als dit indien nodig is, hun geslacht aanpassen.
  >Ook kunnen de mensen als ze het echt willen hun gegevens totaal verwijderen o.a. hun naam en hun info.
  >
* ### links
  * #### hosted API op Oketo
    * [Oketo endpoint Lucas De Greef](https://system-service-lucasdegreef.cloud.okteto.net)

## Screenshots
>Screenshot eerste post toevoegen van personen met voornaam en achternaam. Stuurt voornaam met id terug
>
>![Persoon in data base krijgen eerste post](https://user-images.githubusercontent.com/82623056/211028353-96237943-e0a1-4209-ac8a-d4af441c592d.png)
>
>Screenshot tweede post personen in database beroepen toewijzen met hun geslacht
>
>![persoon beroep toewijzen](https://user-images.githubusercontent.com/82623056/211037776-f8a4061b-76d3-4aa7-9c4b-166d543aaf8e.png)
>
>Screenshot derde post van werkgever door geven en stad van de werkgever. werkgever wordt gehased en stad word terug 
>gestuurd samen met de ID
>
>![post invoeren van werk gever en stad](https://user-images.githubusercontent.com/82623056/211031924-e5eba604-6f43-43df-8474-df35282edf6b.png)
>
>Screenshot eerste get waar alle namen van personen en hun werk met hun geslacht worden weergegeven
>
>![alle personen](https://user-images.githubusercontent.com/82623056/211035385-8915f932-99d2-422c-8eb4-708a055c4472.png)
>
>Screenshot tweede get waar individueel zijn gegevens worden opgevraagd
>
>![persoon apart](https://user-images.githubusercontent.com/82623056/211037894-ce35668d-0284-46ab-8bcd-25698e78e5b3.png)
>

>Screenshot derde get waar alle beroepen met de personen hun geslacht worden weergegeven
>
>![alle beroepen](https://user-images.githubusercontent.com/82623056/211038637-65bdf386-3781-4ad5-a16e-d5caa7b8e291.png)
>

>Screenshot van het resultaat van de put. deze update de beroepen het geslacht van de persoon.
>
>![update beroep](https://user-images.githubusercontent.com/82623056/211039546-c8d2ba74-fa9f-4880-be28-2f67f7ccbee0.png)
>
>Resulutaat
>
>![resultaat put](https://user-images.githubusercontent.com/82623056/211039749-808e502a-c8a3-4bf8-9365-d43c00801bef.png)
>

>Screenshot Delete. Deze delete zorgt er voor dat de persoon wordt verwijderd samen met de info van deze persoon.
>En geeft een json terug dat het een succes was
>
>![Delete persoon ](https://user-images.githubusercontent.com/82623056/211040264-ac7e86dd-6931-4f6b-832d-3797feef3c40.png)
>
>Resultaat van de delete
>
>![resulaat persoon delete](https://user-images.githubusercontent.com/82623056/211040630-eee122c4-7c14-46f8-ad8c-cff0590f3c11.png)
>
>Screenshot van database met hased werkgever en stad
>
>![database hased werkgever en stad](https://user-images.githubusercontent.com/82623056/210453554-67cd38f2-7ab9-4b3f-9c31-f05cb8a95ac9.png)
>
>Screenshot van database na delete persoon.
>
>![database na delete van persoon](https://user-images.githubusercontent.com/82623056/210453631-d93a5216-3817-47ed-afd3-53f85fe50448.png)
>
>Screenshot van database beroepen met een update en een verwijderde kolom
>
>![database van beroepen met update en een verwijderd](https://user-images.githubusercontent.com/82623056/210453772-dcea9a93-9463-4554-b575-5a80deca29f6.png)
>
>Screenshot Pytest fucnties
>
>![fucnties foto 1 pytest](https://user-images.githubusercontent.com/82623056/210456626-988880db-eca2-4acc-9536-3725fdeadb3d.png)
>
>![Pytest tweede foto functies](https://user-images.githubusercontent.com/82623056/210456706-1732872d-6379-4a33-b1e2-26fd420cacf4.png)


>Screenshot resultaat pytest
>
>![Resultaat pytest](https://user-images.githubusercontent.com/82623056/210456835-b3698469-31fd-4c0d-8e75-1ad4c14177ec.png)
>

>Screenshot openAPI docs
>
>![screencapture-system-service-lucasdegreef-cloud-okteto-net-docs-2023-01-03-21_52_04 (1)](https://user-images.githubusercontent.com/82623056/210449263-9c038b9a-f8d7-40e9-bbf3-c6a535716963.png)
