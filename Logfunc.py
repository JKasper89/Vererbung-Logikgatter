# -*- coding: utf8 -*-
__version__ = '2.1'                                         # Versionsinformationen
__author__ = 'Jan Kasper(jan.kasper@students.tbs1.de)'

from abc import ABC, abstractmethod

class LogFunc(ABC):                                         # Beginn der Klassendefinition
    """
    This is the parent class for logic gate classes.
    """
    def __init__(self, numberOfInputs = 2):                 # Definition der Attribute
        """
        Create a logic Gate with given numberOfInputs. By default 2 Inputs are selected.
        Inputs and Output get the boolean value False.
        :param numberOfInputs:
        """
        self.__Inputs = [False for i in range(numberOfInputs)]
        self.__Output = False
        self.__Name = type(self)._name_
        self.execute()

    # Definition der Getter und Setter
    def __get_Inputs(self):
        return self.__Inputs

    def __set_Inputs(self,value):
        isinstance(value,list)
        self.__Inputs = value

    def __get_Output(self):
        return self.__Output

    def _set_Output(self,value):
        isinstance(value,bool)
        self.__Output = value

    def __get_Name(self):
        return self.__Name

    def __set_Name(self,value):
        isinstance(value,str)
        self.__Name = value

    # Definition der Properties
    Inputs = property(__get_Inputs,__set_Inputs)
    Output = property(__get_Output,None)
    Name = property(__get_Name,__set_Name)

    @abstractmethod
    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        pass

    def __str__(self):                                      # Ausformlierung der Stringumwandlung
        """
        Conerts the status of the logical gate to a string.
        :return: string of the gate status
        """
        cwidth = 60
        line = ''.ljust(cwidth, '#')
        format_str = "## {{0:10}}: {{1:{0}}} ##".format(cwidth-18)
        temp = line
        temp += "\n" + format_str.format("Name", self.Name)
        temp += "\n" + format_str.format("Type", type(self).__name__)
        temp += "\n" + format_str.format("Input0", str(self.Inputs))
        temp += "\n" + format_str.format("Output", str(self.Output))
        temp += "\n" + line
        return temp

    def show(self):                                         # Bildschirmausgabe der Stringumwandlung
        """
        Shows the value of each property of the class and the class name
        :return: None
        """
        print(self.__str__())
        
class ORGate(LogFunc):                                      # Definition des OR Gates
    _name_ = "OrGate"
    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Set the Output to False when all Inputs are False.
        :return: None
        """
        if self.Inputs.count(True) == 0:
            self._set_Output(False)
        else:
            self._set_Output(True)
            
class ANDGate(LogFunc):                                     # Definition des AND Gates
    _name_ = "AndGate"
    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Set the Output to True when all Inputs are True
        :return: None
        """
        if self.Inputs.count(False) == 0:
            self._set_Output(True)
        else:
            self._set_Output(False)

class XORGate(LogFunc):                                    # Definition des XOR Gates
    _name_ = "XOrGate"
    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Set the Output to True when exactly one Input is True.
        :return: None
        """
        if self.Inputs.count(True) == 1:
            self._set_Output(True)
        else:
            self._set_Output(False)

class NANDGate(LogFunc):                                    # Definition des NAND Gates
    _name_ = "NandGate"
    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Set the Output to False when all Inputs are True.
        :return: None
        """
        self._set_Output(True)
        if self.Inputs.count(False) == 0:
            self._set_Output(False)
        else:
            self._set_Output(True)

if __name__ == "__main__":
    a = [True, False, False, True]
    OR = ORGate()
    OR.show()
    OR.Inputs=a
    OR.execute()
    OR.show()
    AND = ANDGate()
    AND.show()
    AND.Inputs=a
    AND.execute()
    AND.show()
