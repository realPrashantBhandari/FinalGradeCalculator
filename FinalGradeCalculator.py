import os
import PySimpleGUI as sg 

sg.theme('DarkGrey1') 

class Gui:
    def __init__(self):
        
        self.layout = [
                        [
                           sg.Text('Assignments (Optional)',justification='center',size=(20,1)),
                           sg.Text('Score',justification='center',size=(5,1)),
                           sg.Text(' Total',justification='center',size=(5,1)),
                           sg.Text('Weight %',justification='center',size=(7,1)),
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', focus=True, key = "ASG0"),
                           sg.Input(size=(6,1),justification='center', key = "S0"),
                           sg.Input(size=(6,1),justification='center', key = "T0"),
                           sg.Input(size=(7,1),justification='center', key = "W0"), 
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG1"),
                           sg.Input(size=(6,1),justification='center', key = "S1"),
                           sg.Input(size=(6,1),justification='center', key = "T1"),
                           sg.Input(size=(7,1),justification='center', key = "W1"), 
                        ],                    
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG2"),
                           sg.Input(size=(6,1),justification='center', key = "S2"),
                           sg.Input(size=(6,1),justification='center', key = "T2"),
                           sg.Input(size=(7,1),justification='center', key = "W2"), 
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG3"),
                           sg.Input(size=(6,1),justification='center', key = "S3"),
                           sg.Input(size=(6,1),justification='center', key = "T3"),
                           sg.Input(size=(7,1),justification='center', key = "W3"), 
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG4"),
                           sg.Input(size=(6,1),justification='center', key = "S4"),
                           sg.Input(size=(6,1),justification='center', key = "T4"),
                           sg.Input(size=(7,1),justification='center', key = "W4"), 
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG5"),
                           sg.Input(size=(6,1),justification='center', key = "S5"),
                           sg.Input(size=(6,1),justification='center', key = "T5"),
                           sg.Input(size=(7,1),justification='center', key = "W5"), 
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG6"),
                           sg.Input(size=(6,1),justification='center', key = "S6"),
                           sg.Input(size=(6,1),justification='center', key = "T6"),
                           sg.Input(size=(7,1),justification='center', key = "W6"), 
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG7"),
                           sg.Input(size=(6,1),justification='center', key = "S7"),
                           sg.Input(size=(6,1),justification='center', key = "T7"),
                           sg.Input(size=(7,1),justification='center', key = "W7"), 
                        ],
                        [
                           sg.Input(size=(23,1),justification='center', key = "ASG8"),
                           sg.Input(size=(6,1),justification='center', key = "S8"),
                           sg.Input(size=(6,1),justification='center', key = "T8"),
                           sg.Input(size=(7,1),justification='center', key = "W8"), 
                        ],
                        [
                           sg.Text("Finals Weight",size=(15,1),justification='center'),
                           sg.Input(size=(10,1),justification='center', key = "FW"), 
                        ],
                        
                        [
                            sg.Text('Expected Final Grade',size=(15,1),justification='center'),
                            sg.Input(size=(10,1),justification='center', key = "FG"),
                            sg.Button('Calculate',size=(10,1), key = "GO", bind_return_key=True),
                        ],
                        [
                            sg.Output(size=(45,5), key='OUTPUT',echo_stdout_stderr = True)
                        ]

                    ]
        
        # Create the window
        self.window = sg.Window('Final Grade Calculator',margins=(10,10)).Layout(self.layout)

class GradeCalculator:
    def __init__(self):
        self.expectedFinalGrade = ''
        self.currentGrade = 0
        self.expectedFinalGrade = 0
        self.finalWeight = 0
        self.requiredFinalGrade = 0

    def checkValues(self,values):
        FLAG = False

        weightCheckList = []
        totalWeightCheck = 0

        if values['FG']=='' or len(values['FG']) and values['FG'][-1] not in ('0123456789'):
            print('Error >> Please Enter Expected Final Grade')
            FLAG = True
            
        if values['FW']=='' or len(values['FW']) and values["FW"][-1] not in ('0123456789'):
            print('Error >> Please Enter Final Weight')
            FLAG = True

        for x in range (9):
            tempASG= 'ASG'+ str(x)
            tempS = 'S'+ str(x)
            tempT = 'T' + str(x)
            tempW = 'W' + str(x)

            currentWeight = 0
            if values[tempW] != '':
                currentWeight = int(values[tempW])
            else:
                currentWeight=0
            
            weightCheckList.append(currentWeight)
            
            if len(values[tempS]) and values[tempS][-1] not in ('0123456789'):
                print('Error >> Please Re-Enter Valid Score')
                FLAG = True
            
            if len(values[tempT]) and values[tempT][-1] not in ('0123456789'):
                print('Error >> Please Re-Enter Valid Total Score')
                FLAG = True

            if len(values[tempW]) and values[tempW][-1] not in ('0123456789'):
                print('Error >> Please Re-Enter Valid Weight')
                FLAG = True
            
            if values[tempS] !='':
                if values[tempT] != '':
                    if int(values[tempS]) > int(values[tempT]):
                        print('Error >> Error Score greater than Total')
                        FLAG = True
                else:
                    print('Error >> Please enter all 3 values for Assignment {} '.format(x+1))
                    FLAG = True
            
            if values[tempS] != ''  and values[tempW] == '':
                print('Error >> Please enter all 3 values for Assignment {} '.format(x+1))
                FLAG = True

            if values[tempS] == '' and values[tempW] != '':
                print('Error >> Please enter all 3 values for Assignment {} '.format(x+1))
                FLAG = True
        
        totalWeightCheck = sum(weightCheckList) + int(values['FW'])
        if (totalWeightCheck != 100):
            print('Error >> Sum of weights is not equal to 100')
            FLAG = True

        return FLAG

    def calculateCurrentGrade(self,values):
        gradeList=[]
        weightList = []
        gradeFlag = False
        for x in range (9):

            tempS = 'S'+ str(x)
            tempT = 'T' + str(x)
            tempW = 'W' + str(x)
            currentScore = 0
            currentTotal = 0
            currentWeight = 0

            if values[tempS] != '':
                currentScore = int(values[tempS])
            else:
                currentScore=0

            if values[tempT] != '':
                currentTotal = int(values[tempT])
            else:
                currentTotal=1

            if values[tempW] != '':
                currentWeight = int(values[tempW])
            else:
                currentWeight=0

            tempGrade=int(((currentScore/currentTotal)*100)*currentWeight)
            if tempGrade != 0:
                gradeList.append(tempGrade)
                weightList.append(currentWeight)
            
        try:
            self.currentGrade = sum(gradeList)/sum(weightList)
            print("Your Current Grade is: {:,.2f}" .format(self.currentGrade))
            gradeFlag = False
        except:
            print("Error >> Please enter Valid Values")
            gradeFlag = True
        
        return gradeFlag

        
    def finalGradeCalculator(self,values):
        self.expectedFinalGrade = int(values['FG'])/100
        self.finalWeight = int(values['FW'])/100

        self.requiredFinalGrade = ((self.expectedFinalGrade - (1-self.finalWeight)*(self.currentGrade/100))/self.finalWeight)*100
        print("To get {:,.2f} % in classs," .format(self.expectedFinalGrade * 100))
        print("You need {:,.2f} % in the finals" .format(self.requiredFinalGrade))


def main():
    g=Gui()
    gc = GradeCalculator()
    

    while True:
        event, values = g.window.Read()
        checkValuesFlag = True
        cheackGradeFlag = True

        if event is None:
            break

        if event == 'GO':
            g.window['OUTPUT'].Update('')
            checkValuesFlag = gc.checkValues(values)
            if checkValuesFlag == False:
                cheackGradeFlag = gc.calculateCurrentGrade(values)
                if (cheackGradeFlag == False):
                    gc.finalGradeCalculator(values)


if __name__ == '__main__':
    print('Starting program...')
    main()