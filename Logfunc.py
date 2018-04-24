# -*- coding: utf8 -*-
__version__ = '1.0'                                         # Versionsinformationen
__author__ = 'Jan Kasper(jan.kasper@students.tbs1.de)'

class LogFunc:                                               # Beginn der Klassendefinition
    """
    This class calculates the logical OR function.
    """
    def __init__(self):                                     # Definition der Attribute
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "YaGate"

    def __get_Input0(self):                                 # Definition der Getter und Setter
        return self.__Input0
    def __set_Input0(self,value):
        isinstance(value,bool)
        self.__Input0 = value
    def __get_Input1(self):
        return self.__Input1
    def __set_Input1(self,value):
        isinstance(value,bool)
        self.__Input1 = value
    def _get_Output(self):
        return self.__Output
    def _set_Output(self,value):
        isinstance(value,bool)
        self.__Output = value
    def __get_Name(self):
        return self.__Name
    def __set_Name(self,value):
        isinstance(value,str)
        self.__Name = value
        
    Input0 = property(__get_Input0,__set_Input0)            # Definition der Properties
    Input1 = property(__get_Input1,__set_Input1)
    Output = property(_get_Output,None)
    Name = property(__get_Name,__set_Name)

    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        self.__set_Output(False)
        if self.Input0 == True:
            self.__set_Output(True)
        elif self.Input1 == True:
            self.__set_Output(True)

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
        temp += "\n" + format_str.format("Input0", str(self.Input0))
        temp += "\n" + format_str.format("Input1", str(self.Input1))
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
    def __init__(self):
        LogFunc.__init__(self)           
    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        self._set_Output(False)
        if self.Input0 == True:
            self._set_Output(True)
        elif self.Input1 == True:
            self._set_Output(True)
            
class ANDGate(LogFunc):                                     # Definition des AND Gates
    def __init__(self):
        LogFunc.__init__(self)
    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        self._set_Output(False)
        if True == self.Input0:
            if True == self.Input1:
                self._set_Output(True)

class XNORGate(LogFunc):                                    # Definition des XOR Gates

    def __init__(self):
        LogFunc.__init__(self)

    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        self._set_Output(False)
        if self.Input0 == self.Input1:
            self._set_Output(True)

class NANDGate(LogFunc):                                    # Definition des NAND Gates
     
    def __init__(self):
        LogFunc.__init__(self)

    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        self._set_Output(True)
        if True == self.Input0:
            if True == self.Input1:
                self._set_Output(False)   

if __name__ == "__main__":

    OR = ORGate()
    OR.execute()
    
    OR.show()
    
    OR.Input1=True
    
    OR.show()

    OR.execute()

    OR.show()
    AND = ANDGate()
    AND.execute()
    AND.show()
    AND.Input0 = True
    AND.Input1 = True
    AND.execute()
    AND.show()
