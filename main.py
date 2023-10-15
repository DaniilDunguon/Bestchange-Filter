from bs4 import BeautifulSoup
import requests
from time import sleep

class Structur():
        def __init__(self):
                self.head = {"Accept": "*/*",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
                print("""██████╗░███████╗███╗░░██╗  ██████╗░██████╗░░░░
██╔══██╗██╔════╝████╗░██║  ██╔══██╗██╔══██╗░░░
██║░░██║█████╗░░██╔██╗██║  ██████╔╝██████╔╝░░░
██║░░██║██╔══╝░░██║╚████║  ██╔═══╝░██╔══██╗░░░
██████╔╝███████╗██║░╚███║  ██║░░░░░██║░░██║██╗""")
                sleep(0.5)
                self.url = str(input("\nWrite url for parsing (only best change): "))
                self.url = requests.get(self.url, headers=self.head)
                self.criterier_from = int(input("from what price are you willing to buy currency? :"))
                self.criterier_until = int(input("until what price are you willing to buy currency?: "))
        def checking_file_content(self):
                with open("Main.txt", "r", encoding="UTF-8") as f:
                        line = f.readline()
                if line == "":
                        pass
                else:
                        with open("Main.txt", "w", encoding="UTF-8") as file:
                                file.write("")
        def Get_vars(self):

                self.page = BeautifulSoup(self.url.content, features="html.parser")

                self.item_state = self.page.findAll(class_="rwr pos")
                self.item_outer = self.page.findAll(class_="ca")
                self.item_count = self.page.findAll(class_="fs")
                self.item_count_from = self.page.findAll(class_="fm1")

        def load_Main_file(self):
                with open("Main.txt", "a", encoding="UTF-8") as f:
                        for i in range(0, len(self.item_count_from)):
                                b = list(self.item_count_from[i])[0][3:]
                                b = str(b).replace(" ", "")
                                if int(b) < self.criterier_until and int(b) > self.criterier_from:
                                        f.write(f"{self.item_outer[i].text} - {self.item_count[i].text[0:11]},            от {b} рублей; отзывы: {self.item_state[i].text}+\n")
                print("The file has been filled")
                sleep(5)


if __name__ == "__main__":
        Class = Structur()
        Class.checking_file_content()
        Class.Get_vars()
        Class.load_Main_file()

