HeroName = input('Nome do heroi: ')
HeroXP = int(input('Quanto XP seu heroi tem? '))

HeroClass = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Grandmaster', 'Challenger']

if(HeroXP <= 600):
    print(HeroName + ' é classe ' + HeroClass[0])
elif(HeroXP >= 601 and HeroXP <= 1300):
    print(HeroName + ' é classe ' + HeroClass[1])
elif(HeroXP >= 1301 and HeroXP <= 2200):
    print(HeroName + ' é classe ' + HeroClass[2])
elif(HeroXP >= 2201 and HeroXP <= 3600):
    print(HeroName + ' é classe ' + HeroClass[3])
elif(HeroXP >= 3601 and HeroXP <= 5200):
    print(HeroName + ' é classe ' + HeroClass[4])
elif(HeroXP >= 5201 and HeroXP <= 7200):
    print(HeroName + ' é classe ' + HeroClass[5])
elif(HeroXP >= 7201 and HeroXP <= 8500):
    print(HeroName + ' é classe ' + HeroClass[6])
elif(HeroXP >= 8501 and HeroXP <= 9500):
    print(HeroName + ' é classe ' + HeroClass[7])
else:
    print(HeroName + ' é classe ' + HeroClass[8])
