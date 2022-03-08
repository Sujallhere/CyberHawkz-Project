print(''' ________  ___  ___        ___  ________  ___          
|\   ____\|\  \|\  \      |\  \|\   __  \|\  \         
\ \  \___|\ \  \\\  \     \ \  \ \  \|\  \ \  \        
 \ \_____  \ \  \\\  \  __ \ \  \ \   __  \ \  \       
  \|____|\  \ \  \\\  \|\  \\_\  \ \  \ \  \ \  \____  
    ____\_\  \ \_______\ \________\ \__\ \__\ \_______\
 
 ''')


with open("website.log.txt","r") as f:
                              lines=f.readlines()
                              with open("output.txt", "wt") as nf:
                                   for line in lines:
                                              line=line.split(" ")
                                              nf.write("Ip \t Datetime \t time zone \n request type \t path \t http protocol \t status code \t packet size \t user agent ")
                                              nf.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(str(line[0]).replace(' " ',' '),line[3],line[5],line[6],line[7],line[8],line[9],line[11]))

