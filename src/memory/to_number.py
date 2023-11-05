class ParsingException(Exception):
    pass

def toNumber(value):
    try:
        parsed_value = int(value)
    except:
        try:
            if value.replace('.', '', 1).isdigit():
                parsed_value = float(value)
            else:
                raise ParsingException("What the fuck is wrong with you?")
        except:
            raise ParsingException("What the fuck is wrong with you? (2)")

    
    return parsed_value