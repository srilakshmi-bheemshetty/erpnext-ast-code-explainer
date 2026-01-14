def explain_functions(functions):
    """
    Convert function names into human-friendly explanations
    """
    explanations = []
    for func in functions:
        explanations.append(f"- `{func}()` handles business logic related to ERP operations.")
    return explanations
