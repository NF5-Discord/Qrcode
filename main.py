from pystyle import Colors, Colorate, Center, System, Anime, Write
import pyqrcode
import io

qrcodeascii = """
  #####                                     
 #     # #####   ####   ####  #####  ###### 
 #     # #    # #    # #    # #    # #      
 #     # #    # #      #    # #    # #####  
 #   # # #####  #      #    # #    # #      
 #    #  #   #  #    # #    # #    # #      
  #### # #    #  ####   ####  #####  ###### 
                                            
"""

def init():
 System.Clear()
 System.Title("Qrcode")
 System.Size(200, 50)
 Anime.Fade(text=Center.Center(qrcodeascii), color=Colors.white_to_green, mode=Colorate.Vertical, enter=True)

 
def main():
 System.Clear() 
 print('\n'*2)
 print(Colorate.Diagonal(Colors.white_to_green, Center.XCenter(qrcodeascii)))
 print('\n'*3)


 mode = Write.Input("Veuillez indiquer un lien pour créer un QRCODE ->", Colors.white_to_green, interval=0.005)

 url = pyqrcode.create(mode)

 url.png("qrcode.png", scale=10)
 buffer = io.BytesIO()
 url.png(buffer)
 
 if mode.strip():
   Write.Input("Fini!", Colors.white_to_green, interval=0.005)


 if not mode.strip():
  Colorate.Error("Lien invalide.")
 return

 print()
 

if __name__ == '__main__':
    init()
    while True:
       main()