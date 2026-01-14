import ast

def infer_return_type(node):
    """Infer return type from AST return expression"""
    if isinstance(node, ast.Return) and node.value:
        val = node.value

        if isinstance(val, ast.Compare):
            return "Boolean"

        if isinstance(val, ast.Constant):
            if isinstance(val.value, bool):
                return "Boolean"
            if isinstance(val.value, (int, float)):
                return "Numeric"

        if isinstance(val, ast.BinOp):
            return "Numeric"

        if isinstance(val, ast.Call):
            return "Function result / Object"

        if isinstance(val, ast.List):
            return "List"

        if isinstance(val, ast.Dict):
            return "Dictionary"

        return "Computed value"

    return "No return (side-effect only)"


def analyze_functions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            args = [arg.arg for arg in node.args.args]

            return_type = "No return (side-effect only)"
            for n in ast.walk(node):
                if isinstance(n, ast.Return):
                    return_type = infer_return_type(n)
                    break

            functions.append({
                "name": node.name,
                "args": args,
                "return_type": return_type
            })

    return functions
