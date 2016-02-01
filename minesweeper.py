from field import Field

class MineSweeper:
    def __init__(self, definition):
        self.fields = []
        lines = str.split(definition, '\n')
        field_rows = 0
        field_header = True

        # retrieving the fields
        for line in lines:
            if field_header:
                field_rows = int(str.split(str(line), ' ')[0])
                current_field_line = 0
                field_init = ''
                field_header = False
            else:
                field_init += line
                current_field_line += 1
                if current_field_line == field_rows:
                    self.fields.append(Field(field_init))
                    field_header = True
                else:
                    field_init += '\n'

    def resolve(self):
        output = ''
        number = 1
        for field in self.fields:
            output += "Field #" + str(number) + ":\n"
            output += field.resolve()
            number += 1
            if number <= len(self.fields):
                output += '\n\n'
        return output
