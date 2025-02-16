import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json


def main():
    app()

def is_valid_currency_code(code, valid_codes):
    return code in valid_codes

def format_price(price_str):
    return float(price_str.replace(",", ""))

def get_data(fr,to):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={fr}&To={to}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}  

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        to_price=soup.find("div", class_="sc-98b4ec47-0 jnAVFH").get_text()
        title=str(soup.find("h1").get_text()).split("- ")[1]
        
        return {
            "price" : to_price,
            "title" : title
        }


    else : 
        return {"message" : "Fail to fetch data"}
        


def app():
    code=[]
    currency=[]
    country=[]
    with open('country.json') as file:
        countries=json.load(file)
    for i in range(len(countries)):
        code.append(countries[i]["code"])
        currency.append(countries[i]["currency"])
        country.append(countries[i]["country"])
    root = tk.Tk()
    root.title("Image Viewer")
    root.title("Convertor")
    root.grid_columnconfigure(0, minsize=20)
    root.grid_rowconfigure(0, minsize=20)
    root.grid_columnconfigure(6, minsize=20) 
    root.grid_rowconfigure(5, minsize=20)  

    def update_convert_button():
        if button_from.cget("text") != "From" and button_to.cget("text") != "To":
            btn_convert.config(state=tk.NORMAL)
        else:
            btn_convert.config(state=tk.DISABLED)
        
    def open_from_country_window():
        button_from.config(state=tk.DISABLED)
            
        country_window = tk.Toplevel(root)
        country_window.title("Selecy a country")

        
        search_label = tk.Label(country_window, text="Search a country:")
        search_label.pack(pady=5)

        country_combobox = ttk.Combobox(country_window, values=code, state="normal", width=30)
        country_combobox.pack(pady=5)

        def select_country():
            
            selected_country = country_combobox.get()
            if selected_country in code :
                button_from.config(text=f"{selected_country}")
                country_window.destroy()
                button_from.config(state=tk.NORMAL) 
                update_convert_button() 
            elif selected_country in country :
                button_from.config(text=f"{code[country.index(selected_country)]}")
                country_window.destroy()
                button_from.config(state=tk.NORMAL) 
                update_convert_button()  
            elif selected_country in currency:
                button_from.config(text=f"{code[currency.index(selected_country)]}")
                country_window.destroy()
                button_from.config(state=tk.NORMAL)  
                update_convert_button() 
            else:
                messagebox.showerror("Erreur", "Ce pays n'est pas dans la liste.")

        select_button = tk.Button(country_window, text="Select", command=select_country)
        select_button.pack(pady=10)

        country_window.protocol("WM_DELETE_WINDOW", lambda: (country_window.destroy(), button_from.config(state=tk.NORMAL)))

    def open_to_country_window():
        button_to.config(state=tk.DISABLED)
            
        country_window = tk.Toplevel(root)
        country_window.title("Select a country")

        search_label = tk.Label(country_window, text="Search a country:")
        search_label.pack(pady=5)

        country_combobox = ttk.Combobox(country_window, values=code, state="normal", width=30)
        country_combobox.pack(pady=5)

        def select_country():
            
            selected_country = country_combobox.get()
            if selected_country in code :
                button_to.config(text=f"{selected_country}")
                country_window.destroy()
                button_to.config(state=tk.NORMAL)
                update_convert_button() 
            elif selected_country in country :
                button_to.config(text=f"{code[country.index(selected_country)]}")
                country_window.destroy()
                button_to.config(state=tk.NORMAL)  
                update_convert_button() 
            elif selected_country in currency:
                button_to.config(text=f"{code[currency.index(selected_country)]}")
                country_window.destroy()
                button_to.config(state=tk.NORMAL)  
                update_convert_button() 
            else:
                messagebox.showerror("Error", "This country isn't in the list")
            

        select_button = tk.Button(country_window, text="Select", command=select_country)
        select_button.pack(pady=10)
        country_window.protocol("WM_DELETE_WINDOW", lambda: (country_window.destroy(), button_to.config(state=tk.NORMAL)))
        

    button_from = tk.Button(root, width=10, height=1, text="From", command=open_from_country_window)
    button_from.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    button_to = tk.Button(root, width=10, height=1, text="To", command=open_to_country_window)
    button_to.grid(row=2, column=3, columnspan=2, sticky="ew", padx=10, pady=5)

    
    def convert_click():
        from_value = button_from.cget("text").strip()
        to_value = button_to.cget("text").strip()

        if not is_valid_currency_code(from_value, code) or not is_valid_currency_code(to_value, code):
            messagebox.showerror("Erreur", "Code devise invalide !")
            return

        data = get_data(from_value, to_value)

        if "price" not in data:
            messagebox.showerror("Erreur", "Échec de la récupération des données.")
            return

        price_splited = data["price"].split(" ")
        real_price = 1 / format_price(price_splited[3])

        title = tk.Label(root, text=data["title"]).grid(row=1, column=1, columnspan=4)
        quantities = [1, 5, 10, 25, 50]

        for index, i in enumerate(quantities):
            tk.Label(root, text=f"{i} {price_splited[4]}").grid(row=6 + index, column=0, columnspan=2)
            tk.Label(root, text=f"{round(real_price * i, 3)} {price_splited[1]}").grid(row=6 + index, column=4, columnspan=2)

    root.grid_rowconfigure(12, minsize=20)
        
    btn_convert = tk.Button(root, text="Convert", command=convert_click, state=tk.DISABLED)
    btn_convert.grid(row=4, column=1, columnspan=5, sticky="ew", padx=10, pady=10)
    root.mainloop()


        
        


if __name__ == "__main__":

    main()
    