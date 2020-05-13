
print("#####################################")
print("#    Creation d'un dictionnaire     #")
print("#####################################\n")


print('dev1 = {"ip":"10.3.21.5", "version":"A.01.01",  "username":"user1","password":"pw1"}','\n')

dev1 = {"ip":"10.3.21.5", "version":"A.01.01",  "username":"user1","password":"pw1"}

print("affichage de la valeur correspondant à la clef 'ip'")
print(dev1['ip'])

print("\najout d'une clef et sa valeur")
dev1['OS']='NXOS'

print(dev1)

print("\nModification de la valeur correspondant à la clef'version")
dev1['version']='a.02'

print(dev1)

print("\nSuppression de la clef 'OS'")
del dev1['OS']

print(dev1)

print("\nRecherche d'une clef, si elle existe on l'affiche")
if 'ip' in dev1:
    print(dev1['ip'])
