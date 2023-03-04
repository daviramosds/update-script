from os import system, remove

system('sudo apt update | grep -A 1 "Err:" > update-err.log')

f = open('update-err.log', 'r')
content = f.read()
content = content.split('Err:')
for err in content:
    ppa = err.split('404')
    if (len(ppa) >= 2):
        ppa_data = ppa[0].split('/')
        ppa_or = ppa_data[5].split(' ')
        ppa_name = f'{ppa_data[3]}-{ppa_or[0]}-{ppa_data[4]}-{ppa_or[1]}.list'
        try:
            remove(f'/etc/apt/sources.list.d/{ppa_name}')
        except:
            print('err')

system('sudo apt upgrade -y')
system('sudo apt autoremove -y')
system('sudo apt clean -y')
system('sudo apt autoclean -y')