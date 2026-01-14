from module_reader import find_module_file
from ast_parser import analyze_functions

def explain_function(func):
    name = func["name"]
    args = func["args"]
    return_type = func["return_type"]

    inputs = args if args else ["None"]

    if name.startswith("validate"):
        action = "Validates business rules before saving or submitting the document."
        result = "Raises an error if validation fails."
    elif name.startswith("get_"):
        action = "Fetches or computes data related to the document."
        result = f"Returns: {return_type}"
    elif name.startswith("make_"):
        action = "Creates a related document or accounting entry."
        result = f"Returns: {return_type}"
    elif name.startswith("update_"):
        action = "Updates related records or fields."
        result = "Updates database records."
    else:
        action = "Handles internal ERPNext business logic."
        result = f"Returns: {return_type}"

    return {
        "name": name,
        "inputs": inputs,
        "action": action,
        "result": result
    }


def main():
    print("=== ERPNext AST-Based Code Explainer ===\n")

    module_name = input("Enter ERP module file name (example: sales_invoice): ").strip()

    file_path = find_module_file(module_name)
    if not file_path:
        print("❌ Module file not found.")
        return

    print(f"\n📄 File found:\n{file_path}\n")
    functions = analyze_functions(file_path)

    print("🔍 Function Analysis:\n")

    for func in functions[:10]:
        exp = explain_function(func)

        print(f"Function: {exp['name']}")
        print(f"Inputs: {', '.join(exp['inputs'])}")
        print(f"What it does: {exp['action']}")
        print(f"Result: {exp['result']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
