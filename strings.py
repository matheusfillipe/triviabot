# -*- coding: utf-8 -*-
import config

EN = "en"
RO = "ro"
COLOR = "color"

DEFAULT_COLOR = "13,06"
# First number is foreground, second is background
##############################
# COLOR CODES
##############################
# 00 	White
# 01 	Black
# 02 	Navy
# 03 	Green
# 04 	Red
# 05 	Maroon
# 06 	Purple
# 07 	Orange
# 08 	Yellow
# 09 	Light Green
# 10 	Teal
# 11 	Cyan
# 12 	Royal blue
# 13 	Magenta
# 14 	Gray
# 15 	Light Gray
##############################


class Text:
    NEXT = {EN: "Next question:", RO: "Următoarea întrebare:", COLOR: "08,06"}
    CLUE = {EN: "Clue: {}", RO: "Indiciu: {}", COLOR: "02,00"}
    QUESTION = {EN: "Question:", RO: "Întrebare:", COLOR: "08,01"}
    QUESTION_COLOR = {EN: "{}", COLOR: "08,01"}
    BLUE_COLOR = {EN: "{}", COLOR: "12,01"}
    GIVE_CLUE = {EN: "Clue: {}", RO: "Indiciu: {}", COLOR: "02,00"}
    NO_ONE_GOT = {
        EN: "No one got it. The answer was: {}",
        RO: "Aşadar, nimeni nu a ştiut-o. Răspunsul era: {}",
        COLOR: "09,01",
    }
    WELCOME = {EN: "Welcome to {}!", RO: "Bun-venit la {}!", COLOR: "08,01"}
    HAVE_AN_ADMIN = {
        EN: "Have an admin start the game when you are ready.",
        RO: "Ca un admin să pornească jocul când toată lumea e gata.",
        COLOR: "08,01",
    }
    HAVE_HELP = {
        EN: "For how to use this bot, just say !help or",
        RO: "Ca să vedeţi instrucţiunile, tastaţi !help sau",
        COLOR: "00,01",
    }
    HELP = {EN: "{} help."}
    RESPOND_ON_CHANNEL = {
        EN: "I'm sorry, answers must be given in the game channel.",
        RO: "Îmi pare rău dar trebuie să dai răspunsurile pe canalul jocului.",
        COLOR: "08,01",
    }
    USER_GOT_IT = {EN: "{} GOT IT!", RO: "{} A ŞTIUT-O!", COLOR: "09,01"}
    THE_ANSWER_WAS = {
        EN: "If there was any doubt, the correct answer was: {}",
        RO: "Dacă cumva aveaţi dubii, răspunsul corect era: {}",
        COLOR: "00,01",
    }
    POINT_ADDED = {
        EN: "{} point has been added to your score!",
        RO: "{} punct a fost adăugat la scorul tău!",
        COLOR: "04,01",
    }
    POINTS_ADDED = {
        EN: "{} points have been added to your score!",
        RO: "{} puncte au fost adăugate la scorul tău!",
        COLOR: "04,01",
    }
    BELONG = {
        EN: "I'm {}'s trivia bot.",
        RO: "Sunt bot-ul trivia al lui {}.",
        COLOR: "08,01",
    }
    COMMANDS = {
        EN: "Commands: score, standings, repeat, help, next, source",
        RO: "Comenzi pentru jucători: score, standings, repeat, help, next, source",
        COLOR: "08,01",
    }
    ADMIN_CMDS = {
        EN: "Admin commands: die, set <user> <score>, start, stop, save, skip, freeze, unfreeze",
        RO: "Comenzi pentru admini: die, set <user> <score>, start, stop, save, skip, audio, text, freeze, unfreeze",
        COLOR: "08,01",
    }
    NOT_ALLOWED = {
        EN: "{}: You don't tell me what to do.",
        RO: "{}: să nu-mi spui tu mie ce să fac.",
        COLOR: "08,07",
    }
    LOOKS_ODLY = {
        EN: "{} looks at {} oddly.",
        RO: "{} trivia nu poate procesa ceea ce {} vrea.",
        COLOR: "09,01",
    }
    NOT_PLAYING = {
        EN: "We aren't playing right now.",
        RO: "Chiar chiar acuşi nu ne jucăm.",
        COLOR: "08,01",
    }
    ALREADY_VOTED = {
        EN: "You already voted, {}, give someone else a chance to hate this question",
        RO: "Bre {}, matale deja ai votat, ar trebui să voteze altcineva.",
        COLOR: "09,01",
    }
    YOU_VOTED = {
        EN: "{}, you have voted. {} more votes needed to skip.",
        RO: "{}, ai votat pentru a sări peste întrebarea curentă. Totuşi e nevoie să mai voteze încă {}",
        COLOR: "09,01",
    }
    THANKS = {
        EN: "Much obliged for playing trivia!",
        RO: "Mulţumesc că joci trivia!",
        COLOR: "08,01",
    }
    RANKINGS = {EN: "Current rankings were:", RO: "Clasamentul actual:", COLOR: "09,01"}
    AUDIO_ON = {
        EN: f"Channel is on Audio mode. Listen to the stream at: {config.AUDIO_URL}",
        RO: f"Canalul este pe modul Audio. Ascultați fluxul de la: {config.AUDIO_URL}",
        COLOR: "08,01",
    }
    AUDIO_OFF = {
        EN: "Channel is on Text mode",
        RO: "Canalul este pe modul Text",
        COLOR: "08,01",
    }
    SEE_YOU = {
        EN: "Scores have been saved, and see you next game!",
        RO: "Punctajele au fost salvate, ne vedem la următorul joc!",
        COLOR: "08,01",
    }
    SCORE = {
        EN: "Your current score is: {}",
        RO: "Punctajul tău actual este: {}",
        COLOR: "08,01",
    }
    IDKU = {
        EN: "You aren't in my database.",
        RO: "Matale nu eşti în baza de date.",
        COLOR: "08,01",
    }
    SKIPPED_THE_ANSWER_WAS = {
        EN: "Question has been skipped. The answer was: {}",
        RO: "Păi am sărit peste această întrebare. Răspunsul era: {}",
        COLOR: "09,01",
    }
    STANDINGS = {
        EN: "The current trivia standings are: ",
        RO: "Acesta este clasamentul curent:",
        COLOR: "08,01",
    }
    TIMMING = {
        EN: "{} has given the answer in {}.{} seconds.",
        RO: "{} a dat răspunsul corect în {}.{} secunde.",
        COLOR: "09,01",
    }
    RANKING = {
        EN: "{} has now {} points and is the {}th in the ranking after {}.",
        RO: "{} are acum {} puncte şi este al {}-lea în clasament după {}.",
        COLOR: "13,01",
    }
    NUMBER_ONE = {
        EN: "{} now has {} and is number one in the rankings.",
        RO: "{} are acum {} şi este pe locul întâi în clasament.",
        COLOR: "13,01",
    }
    RANK_OFF = {
        EN: "Rank was turned off.",
        RO: "Clasamentul nu este disponibil chiar acum.",
        COLOR: "11,01",
    }
    RANK_ON = {
        EN: "Rank was turned on.",
        RO: "Puteţi da comanda ca să vedeţi clasamentul.",
        COLOR: "11,01",
    }
    MAX_POINT_ANNOUNCE = {
        EN: "Points taken now by dead last player: {}",
        RO: "Puncte luate de către ultimul jucător din clasament: {}",
        COLOR: "12,01",
    }
    FREEZE = {
        EN: "{} is punished by not being allowed to accumulate points in the ranking: all their correct answers will be ignored.",
        RO: "{} este pedepsit cu retragerea sa temporară de pe ranking: vor fi ignorate toate răspunsurile sale corecte.",
        COLOR: "07,01",
    }
    UNFREEZE = {
        EN: "{} has just been readmitted in the ranking: their penalty has been lifted. Welcome back!",
        RO: "{} a fost readmis în joc: pedeapsa a fost ridicată. Bine-ai-venit înapoi!",
        COLOR: "11,01",
    }
    ON_FROST_WIN = {
        EN: "{}, your account is frozen right now, as a punishment these points are NOT going to your score!",
        RO: "{}, contul tău este îngheţat acum, ca pedeapsă aceste puncte NU o să urce în scorul tău!",
        COLOR: "08,04",
    }
    ON_ADMIN_OP_JOIN = {
        EN: "{} has just joined the channel and gets ircop status!",
        RO: "{} a intrat în canalul trivia şi primeşte op!",
        COLOR: "07,01",
    }
    ON_RANK_MODE_REWARD = {
        EN: "{} is an outstanding trivia player and therefore gets +{} status!",
        RO: "{} este un jucător de trivia desăvârşit şi din această cauză primeşte +{}!",
        COLOR: "11,01",
    }
    ON_STREAK_MODE_REWARD = {
        EN: "{} gets status +{} for their outstanding series of correct answers in a row!",
        RO: "{} primeşte +{} pentru excelenta serie de răspunsuri corecte la rând!",
        COLOR: "11,01",
    }


def genTrans(lang):
    t = Text()
    for k in dir(t):
        if not k.startswith("_"):
            o = getattr(Text, k)
            cc = "{}{}".format("\003", o[COLOR] if COLOR in o else DEFAULT_COLOR)
            if lang in o:
                setattr(t, k, "{}{}".format(cc, o[lang]))
            else:
                setattr(t, k, "{}{}".format(cc, o[EN]))

    return t
