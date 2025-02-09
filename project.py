import requests
from bs4 import BeautifulSoup
import tkinter as tk
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
    root = tk.Tk()
    root.title("Image Viewer")
    root.geometry("400x400")
    root.title("Devise Convertor")

    input_from = tk.Text(width=7,height=1)
    input_from.grid(row=1,column=1)
    input_to=tk.Text(width=7,height=1)
    input_to.grid(row=1,column=2)
    def convert_click():
        from_value=input_from.get("1.0",tk.END).strip()
        to_value=input_to.get("1.0",tk.END).strip()
        data=get_data(from_value,to_value)
        price_splited=data["price"].split(" ")
        real_price=1/float(data["price"].split(" ")[3])
        price=tk.Label(root,text=f"1 {price_splited[4]} = {real_price} {price_splited[1]}").grid(row=0,column=0,columnspan=4)


    btn_convert=tk.Button(root,text="Convert",command=convert_click).grid(row=3,column=0,columnspan=4)
    root.mainloop()


        
        


if __name__ == "__main__":
    main()
    