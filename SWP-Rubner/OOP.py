from enum import Enum

class Gender(Enum):
    Male = 0
    Female = 1

class Person:

    def __init__(self, fname, lname, birthday, gender):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.gender = gender

    def name(self):
        return self.fname + ' ' + self.lname

    def str(self):
        return f'Name: {self.name()}\nBirthday: {self.birthday}\nGender: {self.gender}'

class Mitarbeiter(Person):
    def __init__(self, fname, lname, birthday, gender, firma, since, salary):
        super().__init__(fname,lname, birthday, gender)
        self.firma = firma
        self.since = since
        self.salary = salary


    def __str__(self):
        return super().str() + f'Firma: {self.firma}\nArbeitet dort seit: {self.since}\nGehalt:{self.salary}'



class Gruppenleiter(Mitarbeiter):
    def __init__(self, fname, lname, birthday, gender, firma, since, salary):
        super().__init__( fname, lname, birthday, gender, firma, since, salary)

    def str(self):
        return super().str()


class Abteilung():
    def __init__(self, name, gruppenleiter):
        self.name = name
        self.gruppenleiter = []
        self.gruppenleiter.append(gruppenleiter)
        self.mitarbeiter = []

    def __str__(self):
        return f'Abteilung: {self.name}\nAnzahl Gruppenleiter: {len(self.gruppenleiter)}'

class Firma():

    def __init__(self, firmenname, sitz, branche):
        self.firmenname = firmenname
        self.sitz = sitz
        self.branche = branche
        self.abteilungen = []

    def __str__(self):
        return f'Firma: {self.firmenname}; Sitz in: {self.sitz}; Branche: {self.branche}'


    #def getAbtl(self):
     #   return len(abteilungen)

    def addMitarbeiter(self, mitarbeiter):
        self.mitarbeiterList.append(mitarbeiter)

    def addGruppenleiter(self, gruppenleiter):
        self.gruppenleiterList = self.gruppenleiterList + gruppenleiter
        return self.gruppenleiterList

    def anzMitarbeiter(self):
        anz = 0
        for a in self.abteilungen:
            anz += len(a.mitarbeiter)
        return anz


    def anzAbteilungen(self):
        return len(self.abteilungen)


    def anzGruppenleiter(self):
        anz = 0
        for a in self.abteilungen:
            anz += len(a.gruppenleiter)
        return anz

    def getHighestAbteilung(self):
        high = self.abteilungen[0]
        for a in self.abteilungen:
            if len(high.mitarbeiter) < len(a.mitarbeiter):
                high = a
        return high

    def menWoman(self):
        anzMen = 0
        anzWoman = 0
        for a in self.abteilungen:
            for m in a.mitarbeiter:
                if m.gender == Gender.Male:
                    anzMen +=1
                else:
                    anzWoman+=1
            for g in a.gruppenleiter:
                if g.gender == Gender.Male:
                    anzMen +=1
                else:
                    anzWoman+=1
        gesamt = anzWoman + anzMen
        percMen = anzMen / gesamt * 100
        percWoman = anzWoman /gesamt * 100
        return {'men' : str(percMen) + ' %', 'woman': str(percWoman) + ' %'}

if __name__ == '__main__':
    #Die Erstellung der Firma
    f1 = Firma('ABD', 'Kufstein', 'Monitorwerbung')

    #Die Erstellung der Mitarbeiter und Gruppenleiter

    m1 = Mitarbeiter('Max', 'Mustermann', '2004-01-01', Gender.Male, f1, 2020, 1500)
    m2 = Mitarbeiter('Max', 'Mustermann', '2004-01-01', Gender.Male, f1, 2020, 1500)
    m3 = Mitarbeiter('Max', 'Mustermann', '2004-01-01', Gender.Male, f1, 2020, 1500)
    m4 = Mitarbeiter('Lena', 'Mülle', '2004-01-01', Gender.Female, f1, 2020, 1500)
    m5 = Mitarbeiter('Alena', 'Allios', '2004-01-01', Gender.Female, f1, 2020, 1500)
    g1 = Gruppenleiter('Herbert', 'Schuster','2004-01-01', Gender.Male, f1, 2020, 1500)
    g2 = Gruppenleiter('Franzi', 'Schuster', '2004-01-01', Gender.Female, f1, 2020, 1500)

    #Die Abteilungen werden erstellt mit den Gruppenleitern
    a1 = Abteilung('IT', g1)
    a2 = Abteilung('Buchhaltung', g2)

    #Mitarbeiter werden den Abteilungen hinzugefügt
    a1.mitarbeiter.append(m1)
    a1.mitarbeiter.append(m4)
    a1.mitarbeiter.append(m2)
    a2.mitarbeiter.append(m5)
    a2.mitarbeiter.append(m3)#

    #Abteilungen werden zur Firma hinzugefügt
    f1.abteilungen.append(a1)
    f1.abteilungen.append(a2)
    #print(a1)
    #print(m1)
    print(f'Anzahl Gruppenleiter gesamt: {f1.anzGruppenleiter()}')
    print(f'Anzahl Mitarbeiter gesamt: {f1.anzMitarbeiter()}')
    print(f'Anzahl Abteilungen gesamt: {f1.anzAbteilungen()}')
    print(f'Größte Abteilung {f1.getHighestAbteilung().name}')
    print(f'Prozenanteil der Männer und Frauen in der ganzen Firma: {f1.menWoman()}')


