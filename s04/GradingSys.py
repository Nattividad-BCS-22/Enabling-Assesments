class Grading:

    def __init__(self, Name, Q1, Q2, Q3, Fe, CPa, Remark, GridOne, GridTwo, GridThree, Row):
        self.Name = Name
        self.Q1 = Q1
        self.Q2 = Q2
        self.Q3 = Q3
        self.Fe = Fe
        self.CPa = CPa
        self.Remark = Remark
        self.GridOne = GridOne
        self.GridTwo = GridTwo
        self.GridThree = GridThree

        self.GridThree.append(Row)

    def askGrade(self):
        # Intialize input

        self.Name = input("Please Enter your name\n")
        self.GridOne.append(self.Name)

        self.Q1 = int(input("Enter your Quiz 1 score.\n"))
        self.GridOne.append(self.Q1)

        self.Q2 = int(input("Enter your Quiz 2 score.\n"))
        self.GridOne.append(self.Q2)

        self.Q3 = int(input("Enter your Quiz 3 score.\n"))
        self.GridOne.append(self.Q3)

        self.Fe = int(input("Enter your Final Exam score.\n"))
        self.GridOne.append(self.Fe)

        self.CPa = int(input("Enter your Class Participation score.\n"))
        self.GridOne.append(self.CPa)


        newq = self.GridOne[1] + self.GridOne[2] + self.GridOne[3] / 3
        newFe = self.GridOne[5] * 0.40
        newCp = self.GridOne[4] * 0.5

        final = newq + newFe + newCp
        Roundoff = "{:.2f}".format(final)
        self.GridOne.append(Roundoff)

        if final < 75:
            self.Remark = "Failed"
        else:
            self.Remark = "Passed"
        self.GridOne.append(self.Remark)


        self.GridTwo = self.GridOne.copy()

        self.GridThree.append(self.GridTwo)


        Grading.askAgain(self)



    def askAgain(self):
        # ask Again
        usercho = input("Would you like to input grade again? y/n").lower()

        match usercho:
            case 'y':
                self.GridOne.clear(), Grading.askGrade(self)
            case 'n':
                Grading.printGrade(self)
            case _:
                print("Invalid Input (Y/N)"), Grading.askAgain(self)

    def printGrade(self):

        for row in self.GridThree:
            print("{: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15}".format(*row))


GridOne = []
GridTwo = []
GridThree = []
Row = ["Name","Q1","Q2","Q3","CP","Final Exam","Grade","Status"]
Gradings = Grading(None, None, None, None, None, None, None, GridOne, GridTwo, GridThree, Row)
Gradings.askGrade()
