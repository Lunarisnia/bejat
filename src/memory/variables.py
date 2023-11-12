from grammar.BejatParser import BejatParser


class Variable:
    global_variable_map = {}

    def getVariable(self, key: str):
        if key in self.global_variable_map:
            return self.global_variable_map[key]
        else:
            return None
    
    def updateValue(self, key: str, value):
        if self.getVariable(key) != None:
            self.global_variable_map[key] = value
        else:
            print(f"{key} belom dibuat bambang")

    def declareVariable(self, key: str, data_type: str, value, ttype: type):
        parsed_value = None
        if key in self.global_variable_map:
            print(f"{key} kan udah dibikin bang. sehat?")
            exit(1)

        if ttype == BejatParser.AtomContext or ttype == BejatParser.ExpressionContext or ttype == BejatParser.CallFunctionContext:
            value_type = type(value)
            if data_type == "nomor" and (value_type == float or value_type == int):
                parsed_value = value
            elif data_type == "bulen" and value_type == bool:
                parsed_value = value
            elif data_type == "tulisan" and value_type == str:
                parsed_value = value
            else:
                print(f'Salah type lah itu bambang, emg {value} itu {data_type}?')
                exit(1)
        elif ttype == BejatParser.IdentifierContext:
            if self.getVariable(value) != None:
                value_type = type(self.global_variable_map[value])
                if (value_type == float or value_type == int) and data_type == "nomor":
                    parsed_value = self.global_variable_map[value]
                elif value_type == bool and data_type == "bulen":
                    parsed_value = self.global_variable_map[value]
                elif value_type == str and data_type == "tulisan":
                    parsed_value = self.global_variable_map[value]
                else:
                    print(f"yang bener lah. emang {key} typenya {data_type}?")
                    exit(1)
            else:
                print(f"{value} belom dibikin tolol")
                exit(1)
        self.global_variable_map[key] = parsed_value


variable_notekeeper = Variable()
