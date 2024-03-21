import tkinter as tk
from tkinter import ttk
import requests
import webbrowser

# Hardcoded main categories
main_categories = {
    "Culture": "Culture",
    "Geography": "Geography",
    "Health": "Health",
    "History": "History",
    "Science": "Science",
}

def get_random_wikipedia_article_in_category(category):
    """Fetches a random Wikipedia article URL in the given category."""
    # Note: This is a simplified example. You might need to adjust the API request
    # to better filter articles by categories.
    endpoint = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,  # Main namespace only
        "rnlimit": 1,  # One random article
        # Example additional parameter to specify category (this part is pseudo-code)
        # "category": category  # This is not a real parameter, see note below
    }
    response = requests.get(endpoint, params=parameters)
    data = response.json()
    article_title = data['query']['random'][0]['title']
    article_url = f"https://en.wikipedia.org/wiki/{article_title.replace(' ', '_')}"
    return article_title, article_url

def on_category_select(event):
    """Handles category selection."""
    selected_category = category_combobox.get()
    print(f"Selected category: {selected_category}")  # For debugging
    # Fetch and open a random article in the selected category
    title, url = get_random_wikipedia_article_in_category(selected_category)
    webbrowser.open(url)

# GUI setup
root = tk.Tk()
root.title("Wikipedia Category Browser")

tk.Label(root, text="Select a Category:").pack()

# Combobox for selecting a category
category_combobox = ttk.Combobox(root, values=list(main_categories.values()))
category_combobox.pack()
category_combobox.bind('<<ComboboxSelected>>', on_category_select)

root.mainloop()
