import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json


def main():
    app()

def get_data(fr,to):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={fr}&To={to}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}  

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        from_image=soup.find("img", alt=fr.lower())
        to_image=soup.find("img", alt=to.lower())
        to_price=soup.find("div", class_="sc-98b4ec47-0 jnAVFH").get_text()
        title=str(soup.find("h1").get_text()).split("- ")[1]
        
        return {
            "from_image": "https://www.xe.com"+from_image['src'],
            "to_image" : "https://www.xe.com"+to_image['src'],
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
    print(countries)
    print(code)
    print(currency)
    print(country)
    root = tk.Tk()
    root.title("Image Viewer")
    root.title("Convertor")
    root.grid_columnconfigure(0, minsize=20)
    root.grid_rowconfigure(0, minsize=20)
    root.grid_columnconfigure(6, minsize=20) 
    root.grid_rowconfigure(5, minsize=20)  

    def open_from_country_window():
        # Désactiver le bouton principal
        button_from.config(state=tk.DISABLED)
            
        # Créer une nouvelle fenêtre
        country_window = tk.Toplevel(root)
        country_window.title("Sélectionner un pays")

        # Label
        search_label = tk.Label(country_window, text="Rechercher un pays:")
        search_label.pack(pady=5)

        # Combobox avec autocomplétion
        country_combobox = ttk.Combobox(country_window, values=code, state="normal", width=30)
        country_combobox.pack(pady=5)

        # Bouton pour valider la sélection
        def select_country():
            
            selected_country = country_combobox.get()
            if selected_country in code :
                button_from.config(text=f"{selected_country}")
                country_window.destroy()
                button_from.config(state=tk.NORMAL)  # Réactiver le bouton de la fenêtre principale
            elif selected_country in country :
                button_from.config(text=f"{code[country.index(selected_country)]}")
                country_window.destroy()
                button_from.config(state=tk.NORMAL)  
            elif selected_country in currency:
                button_from.config(text=f"{code[currency.index(selected_country)]}")
                country_window.destroy()
                button_from.config(state=tk.NORMAL)  
            else:
                messagebox.showerror("Erreur", "Ce pays n'est pas dans la liste.")

        select_button = tk.Button(country_window, text="Select", command=select_country)
        select_button.pack(pady=10)

        # Fermer la fenêtre lorsque l'utilisateur ferme la fenêtre secondaire
        country_window.protocol("WM_DELETE_WINDOW", lambda: (country_window.destroy(), button_from.config(state=tk.NORMAL)))

    def open_to_country_window():
        # Désactiver le bouton principal
        button_to.config(state=tk.DISABLED)
            
        # Créer une nouvelle fenêtre
        country_window = tk.Toplevel(root)
        country_window.title("Sélectionner un pays")

        # Label
        search_label = tk.Label(country_window, text="Rechercher un pays:")
        search_label.pack(pady=5)

        # Combobox avec autocomplétion
        country_combobox = ttk.Combobox(country_window, values=code, state="normal", width=30)
        country_combobox.pack(pady=5)

        # Bouton pour valider la sélection
        def select_country():
            
            selected_country = country_combobox.get()
            if selected_country in code :
                button_to.config(text=f"{selected_country}")
                country_window.destroy()
                button_to.config(state=tk.NORMAL)  # Réactiver le bouton de la fenêtre principale
            elif selected_country in country :
                button_to.config(text=f"{code[country.index(selected_country)]}")
                country_window.destroy()
                button_to.config(state=tk.NORMAL)  
            elif selected_country in currency:
                button_to.config(text=f"{code[currency.index(selected_country)]}")
                country_window.destroy()
                button_to.config(state=tk.NORMAL)  
            else:
                messagebox.showerror("Erreur", "Ce pays n'est pas dans la liste.")

        select_button = tk.Button(country_window, text="Select", command=select_country)
        select_button.pack(pady=10)

        # Fermer la fenêtre lorsque l'utilisateur ferme la fenêtre secondaire
        country_window.protocol("WM_DELETE_WINDOW", lambda: (country_window.destroy(), button_to.config(state=tk.NORMAL)))

    button_from = tk.Button(width=7,height=1,text="From",command=open_from_country_window)
    button_from.grid(row=2,column=2)


    button_to=tk.Button(text="To",command=open_to_country_window ,width=7,height=1)
    button_to.grid(row=2,column=4)
    
    def convert_click():
        for widget in root.winfo_children():
            if isinstance(widget, tk.Label):  # Vérifie si c'est un Label
                widget.config(text="")  # Efface le texte du label
        from_value=button_from.cget("text").strip()
        to_value=button_to.cget("text").strip()
        data=get_data(from_value,to_value)
        price_splited=data["price"].split(" ")
        real_price=1/float(data["price"].split(" ")[3])
        title=tk.Label(root,text=data["title"]).grid(row=1,column=1,columnspan=4)
        # display the values from 1 to 5  
        for i in range(1,6):
            tk.Label(root,text=f"{i} {price_splited[4]}").grid(row=6+i,column=1,columnspan=2) 
            tk.Label(root,text=f"{round(real_price*i,3)} {price_splited[1]}").grid(row=6+i,column=4,columnspan=2)
        root.grid_rowconfigure(12, minsize=20) 
        
        """ or
        #display the values from 1 to 50 (1,5,10,25,50)
            price1=tk.Label(root,text=f"{1} {price_splited[4]} = {real_price} {price_splited[1]}").grid(row=3,column=1,columnspan=4)
            price5=tk.Label(root,text=f"{5} {price_splited[4]} = {real_price*5} {price_splited[1]}").grid(row=4,column=1,columnspan=4)
            price10=tk.Label(root,text=f"{10} {price_splited[4]} = {real_price*10} {price_splited[1]}").grid(row=5,column=1,columnspan=4)
            price25=tk.Label(root,text=f"{25} {price_splited[4]} = {real_price*25} {price_splited[1]}").grid(row=6,column=1,columnspan=4)
            price50=tk.Label(root,text=f"{50} {price_splited[4]} = {real_price*50} {price_splited[1]}").grid(row=7,column=1,columnspan=4)
        
    data = [
    ["Nom", "Âge", "Ville"],
    ["Alice", "25", "Paris"],
    ["Bob", "30", "Lyon"],
    ["Charlie", "22", "Marseille"]
]
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            label = tk.Label(root, text=cell, borderwidth=1, relief="solid", padx=10, pady=5)
            label.grid(row=i, column=j, sticky="nsew")

    # Ajuster la taille des colonnes
    for j in range(len(data[0])):
        root.grid_columnconfigure(j, weight=1)
    """
    btn_convert=tk.Button(root,text="Convert",command=convert_click).grid(row=4,column=1,columnspan=4)
    root.mainloop()


        
        


if __name__ == "__main__":

    main()
    