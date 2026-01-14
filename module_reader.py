import os

# Path to erpnext/erpnext directory
BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

def find_module_file(module_name):
    """
    Resolves:
    - DocTypes (sales_invoice, account, etc.)
    - Module folders (accounts, stock, selling)
    """

    # 1️⃣ Try to resolve as DocType
    for root, dirs, files in os.walk(BASE_PATH):
        if module_name in dirs:
            candidate = os.path.join(root, module_name, f"{module_name}.py")
            if os.path.exists(candidate):
                return candidate

    # 2️⃣ Try to resolve as module folder (accounts, stock, etc.)
    module_folder = os.path.join(BASE_PATH, module_name)

    if os.path.isdir(module_folder):
        # Priority order
        preferred_files = [
            "utils.py",
            "accounts_controller.py",
            "__init__.py"
        ]

        for file_name in preferred_files:
            candidate = os.path.join(module_folder, file_name)
            if os.path.exists(candidate):
                return candidate

    return None
