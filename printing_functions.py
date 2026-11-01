# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """Menyimulasikan pencetakan desain hingga tidak ada yang tersisa,
    lalu memindahkannya ke list completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang telah selesai dicetak."""
    print("\nModel berikut telah dicetak:")
    for completed_model in completed_models:
        print(completed_model)