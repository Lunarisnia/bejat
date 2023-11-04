from grammar.BejatParser import BejatParser


class Variable:
    global_variable_map = {}

    def declareVariable(self, key: str, data_type: str, value: str, ttype: type):
        # 1. Check if the var already exist (DONE)
        # 2. Check if the type is the correct data type (DONE)
        # 3. Check if its a variable (DONE)
        # 4. Assign the var or reject (DONE)
        # 5. Check if its a function
        parsed_value = None
        if key in self.global_variable_map:
            print(f"{key} kan udah dibikin bang. sehat?")
            exit(1)

        if ttype == BejatParser.AtomContext:
            if data_type == "nomor":
                try:
                    parsed_value = int(value)
                except ValueError:
                    if value.replace('.', '', 1).isdigit():
                        parsed_value = float(value)
                    else:
                        print("what the fuck is wrong with you?")
                        exit(1)
            elif data_type == "bulen":
                parsed_value = True if value == "bener" else False
            elif data_type == "tulisan":
                parsed_value = value
            else:
                print('hah???')
                exit(1)
        elif ttype == BejatParser.IDENTIFIER:
            if value in self.global_variable_map:
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
        # elif ttype == BejatParser.
        self.global_variable_map[key] = parsed_value


variable_notekeeper = Variable()
