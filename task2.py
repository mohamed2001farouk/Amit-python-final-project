class ExpressionEvaluator:
    def __init__(self, expression):
        self.expression = expression

    def perform_operation(self, num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                raise ValueError("Cannot divide by zero.")

    def evaluate_basic_expression(self, expression):
        numbers = []
        operators = []
        current_number = ''
        
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            elif char in '+-*/':
                if current_number:
                    numbers.append(float(current_number))
                    current_number = ''
                operators.append(char)
        
        if current_number:
            numbers.append(float(current_number))
        
        i = 0
        while i < len(operators):
            if operators[i] == '*' or operators[i] == '/':
                result = self.perform_operation(numbers[i], operators[i], numbers[i + 1])
                numbers[i] = result
                del numbers[i + 1]
                del operators[i]
            else:
                i += 1
        
        i = 0
        while i < len(operators):
            result = self.perform_operation(numbers[i], operators[i], numbers[i + 1])
            numbers[i] = result
            del numbers[i + 1]
            del operators[i]
        
        return numbers[0]

    def evaluate_expression(self):
        expression = self.expression
        while '(' in expression:
            open_index = expression.rfind('(')
            close_index = expression.find(')', open_index)
            if close_index == -1:
                raise ValueError("Mismatched parentheses.")
            
            sub_expression = expression[open_index + 1:close_index]
            sub_result = self.evaluate_basic_expression(sub_expression)
            
            expression = expression[:open_index] + str(sub_result) + expression[close_index + 1:]
        
        return self.evaluate_basic_expression(expression)

user_input = input("Enter a mathematical expression containing numbers, operators, and parentheses: ")
evaluator = ExpressionEvaluator(user_input)

try:
    result = evaluator.evaluate_expression()
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
