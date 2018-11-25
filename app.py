from parsebook import Book
import numpy as np
# from bookNBC import bookNBC


AK = Book("Anna-Karenin.txt", genre="LOVE")
TSAF = Book("'Tween-Snow-and-Fire.txt", genre="LOVE")
EMMA = Book("Emma.txt", genre="LOVE")
HHH = Book("Healing-Her-Heart.txt", genre="LOVE")
TROTN = Book("The-Return-of-The-Native.txt", genre="LOVE")
SMIL= Book("'Smiles'.txt", genre="LOVE")
AFL = Book("All-For-Love.txt", genre="LOVE")
DQ = Book("Don-Quixote.txt", genre="LOVE")
FTW = Book("Fast-as-the-Wind.txt", genre="LOVE")
MAA = Book("Mademoiselle-At-Arms.txt", genre="LOVE")
TC = Book("Taking-Chances.txt", genre="LOVE")
TAI = Book("The-Age-of-Innocence.txt", genre="LOVE")
TU = Book("The-Unveiling.txt", genre="LOVE")
ACC = Book("A-Cathedral-Courtship.txt", genre="LOVE")
AMM = Book("A-Mad-Marriage.txt", genre="LOVE")
ARWAV = Book("A-Room-With-A-View.txt", genre="LOVE")
AOTI = Book("Anne-of-the-Island.txt", genre="LOVE")
DLL = Book("Daddy-Long-Legs.txt", genre="LOVE")
IVAN = Book("Ivanhoe.txt", genre="LOVE")
JG = Book("Jennie-Gerhardt.txt", genre="LOVE")
MP = Book("Mansfield-Park.txt", genre="LOVE")
NAD = Book("Night-and-Day.txt", genre="LOVE")
NAS = Book("North-and-South.txt", genre="LOVE")
NDDP = Book("Notre-Dame-de-Paris.txt", genre="LOVE")
SAS = Book("Sense-and-Sensibility.txt", genre="LOVE")

AC = Book("alyssascottterra.txt", genre="LOVE")
ALMBF = Book("alyzailovemybestfrienduhoh.txt", genre="LOVE")
ADCL = Book("asrai-devin-convenient-love.txt", genre="LOVE")
BMMI = Book("breaamatchmadeinheaven.txt", genre="LOVE")
DSLA = Book("demisugarmylittleaddiction.txt", genre="LOVE")
EWMN = Book("emilywaltonmiseryismyname.txt", genre="LOVE")
EZS = Book("emilyzimmermanshift.txt", genre="LOVE")
EZBG = Book("ezbadgirl.txt", genre="LOVE")
FPIM = Book("fearless-pinoy-i-039-m-in-love-with-my-best-friend-complete.txt", genre="LOVE")
FPCB = Book("fearlesspinoycomplicatedbutp.txt", genre="LOVE")
KADMC = Book("k-armstrong-driving-me-crazy.txt", genre="LOVE")
KWWSE = Book("katy-wormald-when-summer-ends.txt", genre="LOVE")
LSSF = Book("lissie-sales-she-fell-for-the-boy-next-door.txt", genre="LOVE")
LABT = Book("lucky-97-a-beautiful-terrible-love.txt", genre="LOVE")
MFIT = Book("marline-falling-in-the-snow.txt", genre="LOVE")
MCMS = Book("marycollinsmysister039skee.txt", genre="LOVE")
MCFW = Book("missy-changed-for-who.txt", genre="LOVE")
NAACL = Book("nidhi-agrawal-a-cute-love-story.txt", genre="LOVE")
RGFI = Book("repgreecefuninthesun.txt", genre="LOVE")
SLLT = Book("soccerluv4-letters-to-a-nobody.txt", genre="LOVE")
SLT = Book("soccerluv4-transparent.txt", genre="LOVE")
VBML = Book("victoria-benson-masked-love.txt", genre="LOVE")
WWBT = Book("werewolfsbitetoo-my-mate-what.txt", genre="LOVE")

TGOH = Book("aaditya-shah-the-gates-of-hell.txt", genre="HORROR")
ARC = Book("aaron-redfern-crawl.txt", genre="HORROR")
AAEG = Book("arfa-alim-arfa-alim-evils-ghosts-most-of-horror.txt", genre="HORROR")
ANM = Book("art-nightshade-the-masters-of-horror.txt", genre="HORROR")
TD = Book("c-b-cooper-the-daughter.txt", genre="HORROR")
VAUT = Book("c-e-vance-among-us-they-come.txt", genre="HORROR")
DPZA = Book("dasha-prazak-zickert-abandoned-by-disney.txt", genre="HORROR")
HVTB = Book("hima-vemula-the-boy-in-the-striped-pajamas.txt", genre="HORROR")
ISHS = Book("ice-sukene-horror-stories.txt", genre="HORROR")
EJ = Book("jess-e-w-eyeless-jack.txt", genre="HORROR")
SS = Book("jess-ew-suicide-squidward.txt", genre="HORROR")
TK = Book("jessjc3-jane-the-killer.txt", genre="HORROR")
CGSP = Book("mary-claire-garcia-secret-pet.txt", genre="HORROR")
MPW = Book("mary-perkins-what-039-s-the-worst-that-could-happen.txt", genre="HORROR")
ASH = Book("michael-cannata-a-surgeon-039-s-hands.txt", genre="HORROR")
TTU = Book("michael-cannata-the-thing-under-the-bed.txt", genre="HORROR")
BEDT = Book("michael-whitehouse-bedtime.txt", genre="HORROR")
FGV = Book("michael-whitehouse-forgotten-valentine.txt", genre="HORROR")
OAH = Book("michael-whitehouse-on-a-hill.txt", genre="HORROR")
MBS = Book("mileena-blazonis-slenderman.txt", genre="HORROR")
MCO = Book("min-chan-the-otaku-alice-in-wonderhell.txt", genre="HORROR")
PPV = Book("petter-prene-vacation.txt", genre="HORROR")
RNB = Book("rebeca-night-blinded.txt", genre="HORROR")
SHHT = Book("stephanie95-stephanie-horton-heed-thy-parents-warnings.txt", genre="HORROR")


words = ["love","anticipation","thing"]



lovebooks = [AK, TSAF, EMMA, HHH, TROTN, SMIL, AFL, DQ, FTW, MAA, TC, TAI, TU, ACC, AMM, ARWAV, AOTI, DLL, IVAN, JG, MP, NAD, NAS, NDDP, SAS, AC, ALMBF, ADCL, BMMI, DSLA, EWMN, EZS, EZBG, FPIM, FPCB, KADMC, KWWSE, LSSF, LABT, MFIT, MCMS, MCFW, NAACL, RGFI, SLLT, SLT, VBML, WWBT]
horrorbooks = [TGOH, ARC, AAEG, ANM, TD, VAUT, DPZA, HVTB, ISHS, EJ, SS, TK, CGSP, MPW, ASH, TTU, BEDT, FGV, OAH, MBS, MCO, PPV, RNB, SHHT]




lovevalues = Book.get_counts(lovebooks, words)
np_lovevalues = np.asarray(lovevalues)

#adds the class label
np_lovevalues = np.hstack((np_lovevalues,np.zeros((len(lovebooks),1))))

#saves to file
np.savetxt("Data/wordfreqs.csv", np_lovevalues, delimiter=",", fmt='%1.2f')



horrorvalues = Book.get_counts(horrorbooks, words)
np_horrorvalues = np.asarray(horrorvalues)

#adds the class label
np_horrorvalues = np.hstack((np_horrorvalues,np.ones((len(horrorbooks),1))))

#appends the horror values to the file
file = open("Data/wordfreqs.csv","a")
np.savetxt(file, np_horrorvalues, delimiter=",", fmt='%1.2f')







loveratios = Book.get_ratios(lovebooks, words)
np_loveratios = np.asarray(loveratios)

#adds the class label
np_loveratios = np.hstack((np_loveratios,np.zeros((len(lovebooks),1))))

#saves to file
np.savetxt("Data/wordratios.csv", np_loveratios, delimiter=",", fmt='%1.2f')




horrorratios = Book.get_ratios(horrorbooks, words)
np_horrorratios = np.asarray(horrorratios)

#adds the class label
np_horrorratios = np.hstack((np_horrorratios,np.ones((len(horrorbooks),1))))

#appends the horror values to the file
file = open("Data/wordratios.csv","a")
np.savetxt(file, np_horrorratios, delimiter=",", fmt='%1.2f')





# thingyy = AK.get_freq_dist(10)
# np.savetxt("Data/freqdist.csv", thingyy, delimiter=",", fmt='%s')
# freqfile = open("Data/freqdist.csv","a")


# freq_dist_list = np.empty(shape=[10,10])
# print(freq_dist_list)
word_freq_list = np.empty((1,10))
for book in lovebooks:
	word_list = book.get_freq_dist(10)
	word_list = np.asarray([word_list])
	# word_list = np.transpose(word_list)
	word_freq_list = np.concatenate((word_freq_list,word_list))

	print(word_list)
	print(word_freq_list)
	
	# freq_dist_list = np.concatenate((freq_dist_list,word_list))
	np.savetxt("Data/freqdist.csv", word_freq_list, delimiter=",", fmt='%s')









