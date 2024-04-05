
#Deck of cards
import random
import sys
deck = [(2, "Clubs"),
          (2, "Spades"),
          (2, "Hearts"),
          (2, "Diamonds"),
          (3, "Clubs"),
          (3, "Spades"),
          (3, "Hearts"),
          (3, "Diamonds"),
          (4, "Clubs"),
          (4, "Spades"),
          (4, "Hearts"),
          (4, "Diamonds"),
          (5, "Clubs"),
          (5, "Spades"),
          (5, "Hearts"),
          (5, "Diamonds"),
          (6, "Clubs"),
          (6, "Spades"),
          (6, "Hearts"),
          (6, "Diamonds"),
          (7, "Clubs"),
          (7, "Spades"),
          (7, "Hearts"),
          (7, "Diamonds"),
          (8, "Clubs"),
          (8, "Spades"),
          (8, "Hearts"),
          (8, "Diamonds"),
          (9, "Clubs"),
          (9, "Spades"),
          (9, "Hearts"),
          (9, "Diamonds"),
          (10, "Clubs"),
          (10, "Spades"),
          (10, "Hearts"),
          (10, "Diamonds"),
          ("J", "Clubs"),
          ("J", "Spades"),
          ("J", "Hearts"),
          ("J", "Diamonds"),
          ("Q", "Clubs"),
          ("Q", "Spades"),
          ("Q", "Hearts"),
          ("Q", "Diamonds"),
          ("K", "Clubs"),
          ("K", "Spades"),
          ("K", "Hearts"),
          ("K", "Diamonds"),
          ("A", "Clubs"),
          ("A", "Spades"),
          ("A", "Hearts"),
          ("A", "Diamonds"),
          ]

#Hand cards
hand1 = random.choice(deck)
deck.remove(hand1)
hand2 = random.choice(deck)
deck.remove(hand2)

#Opponent hand cards
opponent1 = random.choice(deck)
deck.remove(opponent1)
opponent2 = random.choice(deck)
deck.remove(opponent2)

#Printing out player cards
print(f"\nYour hand contains a {hand1[0]} of {hand1[1]} and a {hand2[0]} of {hand2[1]}.")

#Pot

pot = 0

#Bet/Check/Fold pre-flop


question = input("\nWould you like to bet, check, or fold (B, C, F): ")
if question == "B" or question == "b":
    bet = int(input("\nHow much would you like to bet?: $" ))
    pot = pot + bet
elif question == "C" or question == "c":
    pass
elif question == "F" or question == "f":
    print("\nYou have folded your hand, game over.")
    sys.exit()
else:
    print("\nYou have not entered B, C or F.")
    sys.exit()

#Table cards

table1 = random.choice(deck)
deck.remove(table1)
table2 = random.choice(deck)
deck.remove(table2)
table3 = random.choice(deck)
deck.remove(table3)
table4 = random.choice(deck)
deck.remove(table4)
table5 = random.choice(deck) 
deck.remove(table5)

#Flop

print(f"\nThe table contains a {table1[0]} of {table1[1]}, a {table2[0]} of {table2[1]} and a {table3[0]} of {table3[1]}")

question = input("\nWould you like to bet, check, or fold (B, C, F): ")
if question == "B" or question == "b":
    bet = int(input("\nHow much would you like to bet?: $" ))
    pot = pot + bet
elif question == "C" or question == "c":
    pass
elif question == "F" or question == "f":
    print("\nYou have folded your hand, game over.")
    sys.exit()
else:
    print("\nYou have not entered B, C or F.")
    sys.exit()

#Turn

print(f"The table now contains a {table1[0]} of {table1[1]}, a {table2[0]} of {table2[1]}, a {table3[0]} of {table3[1]} and a {table4[0]} of {table4[1]}")

question = input("\nWould you like to bet, check, or fold (B, C, F): ")
if question == "B" or question == "b":
    bet = int(input("\nHow much would you like to bet?: $"))
    pot = pot + bet
elif question == "C" or question == "c":
    pass
elif question == "F" or question == "f":
    print("\nYou have folded your hand, game over.")
    sys.exit()
else:
    print("\nYou have not entered B, C or F.")
    sys.exit()

#River

print(f"The table now contains a {table1[0]} of {table1[1]}, a {table2[0]} of {table2[1]}, a {table3[0]} of {table3[1]}, a {table4[0]} of {table4[1]} and a {table5[0]} of {table5[1]}")

question = input("\nWould you like to bet, check, or fold (B, C, F): ")
if question == "B" or question == "b":
    bet = int(input("\nHow much would you like to bet?: $"))
    pot = pot + bet
elif question == "C" or question == "c":
    pass
elif question == "F" or question == "f":
    print("\nYou have folded your hand, game over.")
    sys.exit()
else:
    print("\nYou have not entered B, C or F.")
    sys.exit()

pot = pot * 2

#Opponent hand reveal

print(f"\nYour opponent has a {opponent1[0]} of {opponent1[1]} and a {opponent2[0]} of {opponent2[1]}\n")


#finding winner
#Sorting hand + deck
sortingdeck = [(2, "Clubs"),
          (2, "Spades"),
          (2, "Hearts"),
          (2, "Diamonds"),
          (3, "Clubs"),
          (3, "Spades"),
          (3, "Hearts"),
          (3, "Diamonds"),
          (4, "Clubs"),
          (4, "Spades"),
          (4, "Hearts"),
          (4, "Diamonds"),
          (5, "Clubs"),
          (5, "Spades"),
          (5, "Hearts"),
          (5, "Diamonds"),
          (6, "Clubs"),
          (6, "Spades"),
          (6, "Hearts"),
          (6, "Diamonds"),
          (7, "Clubs"),
          (7, "Spades"),
          (7, "Hearts"),
          (7, "Diamonds"),
          (8, "Clubs"),
          (8, "Spades"),
          (8, "Hearts"),
          (8, "Diamonds"),
          (9, "Clubs"),
          (9, "Spades"),
          (9, "Hearts"),
          (9, "Diamonds"),
          (10, "Clubs"),
          (10, "Spades"),
          (10, "Hearts"),
          (10, "Diamonds"),
          ("J", "Clubs"),
          ("J", "Spades"),
          ("J", "Hearts"),
          ("J", "Diamonds"),
          ("Q", "Clubs"),
          ("Q", "Spades"),
          ("Q", "Hearts"),
          ("Q", "Diamonds"),
          ("K", "Clubs"),
          ("K", "Spades"),
          ("K", "Hearts"),
          ("K", "Diamonds"),
          ("A", "Clubs"),
          ("A", "Spades"),
          ("A", "Hearts"),
          ("A", "Diamonds"),
          ]

hand = [(hand1[0], hand1[1]),
        (hand2[0], hand2[1]),
        (table1[0], table1[1]),
        (table2[0], table2[1]),
        (table3[0], table3[1]),
        (table4[0], table4[1]),
        (table5[0], table5[1])]

hand = sorted(hand, key = sortingdeck.index)

opponenthand = [(opponent1[0], opponent1[1]),
                (opponent2[0], opponent2[1]),
                (table1[0], table1[1]),
                (table2[0], table2[1]),
                (table3[0], table3[1]),
                (table4[0], table4[1]),
                (table5[0], table5[1])]

opponenthand = sorted(opponenthand, key = sortingdeck.index)


#hands
#royal flush

royal_flush_clubs = [(10, "Clubs"),
                     ("J", "Clubs"),
                     ("Q", "Clubs"),
                     ("K", "Clubs"),
                     ("A", "Clubs"),
]

royal_flush_spades = [(10, "Spades"),
                     ("J", "Spades"),
                     ("Q", "Spades"),
                     ("K", "Spades"),
                     ("A", "Spades"),
]

royal_flush_hearts = [(10, "Hearts"),
                     ("J", "Hearts"),
                     ("Q", "Hearts"),
                     ("K", "Hearts"),
                     ("A", "Hearts"),
]

royal_flush_diamonds = [(10, "Diamonds"),
                     ("J", "Diamonds"),
                     ("Q", "Diamonds"),
                     ("K", "Diamonds"),
                     ("A", "Diamonds"),
]

top5 = hand[2:7]

royal_flush = False

if top5 == royal_flush_clubs or top5 == royal_flush_spades or top5 == royal_flush_hearts or top5 == royal_flush_diamonds:
    royal_flush = True
    

opponenttop5 = opponenthand[2:7]

opponentroyal_flush = False

if opponenttop5 == royal_flush_clubs or opponenttop5 == royal_flush_spades or opponenttop5 == royal_flush_hearts or opponenttop5 == royal_flush_diamonds:
    opponentroyal_flush = True

#straight

x = hand[0:5]
y = hand[1:6]
z = hand[2:7]
x1 = [x[0][0], x[1][0], x[2][0], x[3][0], x[4][0]]
y1 = [y[0][0], y[1][0], y[2][0], y[3][0], y[4][0]]
z1 = [z[0][0], z[1][0], z[2][0], z[3][0], z[4][0]]



straightdeck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

straight = False

p = -1
c = 0
while p < 8:
    p += 1
    c = p+5
    if x1 == straightdeck[p:c] or y1 == straightdeck[p:c] or z1 == straightdeck[p:c]:
        straight = True

#opponent straight
        
opponentx = opponenthand[0:5]
opponenty = opponenthand[1:6]
opponentz = opponenthand[2:7]
opponentx1 = [opponentx[0][0], opponentx[1][0], opponentx[2][0], opponentx[3][0], opponentx[4][0]]
opponenty1 = [opponenty[0][0], opponenty[1][0], opponenty[2][0], opponenty[3][0], opponenty[4][0]]
opponentz1 = [opponentz[0][0], opponentz[1][0], opponentz[2][0], opponentz[3][0], opponentz[4][0]]

opponentstraight = False

opponentp = -1
opponentc = 0
while p < 8:
    opponentp += 1
    opponentc = opponentp+5
    if x1 == straightdeck[opponentp:opponentc] or y1 == straightdeck[opponentp:opponentc] or z1 == straightdeck[opponentp:opponentc]:
        opponentstraight = True

#Flush

x2 = [x[0:4][1]]
y2 = [y[0:4][1]]
z2 = [z[0:4][1]]
#x2 = [x[0][1], x[1][1], x[2][1], x[3][1], x[4][1]]
#y2 = [y[0][1], y[1][1], y[2][1], y[3][1], y[4][1]]
#z2 = [z[0][1], z[1][1], z[2][1], z[3][1], z[4][1]]


sortingsuit = [(2, "Clubs"),
               (3, "Clubs"),
               (4, "Clubs"),
               (5, "Clubs"),
               (6, "Clubs"),
               (7, "Clubs"),
               (8, "Clubs"),
               (9, "Clubs"),
               (10, "Clubs"),
               ("J", "Clubs"),
               ("Q", "Clubs"),
               ("K", "Clubs"),
               ("A", "Clubs"),
               (2, "Spades"),
               (3, "Spades"),
               (4, "Spades"),
               (5, "Spades"),
               (6, "Spades"),
               (7, "Spades"),
               (8, "Spades"),
               (9, "Spades"),
               (10, "Spades"),
               ("J", "Spades"),
               ("Q", "Spades"),
               ("K", "Spades"),
               ("A", "Spades"),
               (2, "Hearts"),
               (3, "Hearts"),
               (4, "Hearts"),
               (5, "Hearts"),
               (6, "Hearts"),
               (7, "Hearts"),
               (8, "Hearts"),
               (9, "Hearts"),
               (10, "Hearts"),
               ("J", "Hearts"),
               ("Q", "Hearts"),
               ("K", "Hearts"),
               ("A", "Hearts"),
               (2, "Diamonds"),
               (3, "Diamonds"),
               (4, "Diamonds"),
               (5, "Diamonds"),
               (6, "Diamonds"),
               (7, "Diamonds"),
               (8, "Diamonds"),
               (9, "Diamonds"),
               (10, "Diamonds"),
               ("J", "Diamonds"),
               ("Q", "Diamonds"),
               ("K", "Diamonds"),
               ("A", "Diamonds"),
]
suits7 = sorted(hand, key = sortingsuit.index)

clubs = ["Clubs", "Clubs", "Clubs", "Clubs", "Clubs"]
spades = ["Spades", "Spades", "Spades", "Spades", "Spades"]
hearts = ["Hearts", "Hearts", "Hearts", "Hearts", "Hearts"]
diamonds = ["Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds"]

x3 = suits7[0:5]
y3 = suits7[1:6]
z3 = suits7[2:7]

x2 = [x3[0][1], x3[1][1], x3[2][1], x3[3][1], x3[4][1]]
y2 = [y3[0][1], y3[1][1], y3[2][1], y3[3][1], y3[4][1]]
z2 = [z3[0][1], z3[1][1], z3[2][1], z3[3][1], z3[4][1]]

flush = False

if x2 == clubs or x2 == spades or x2 == hearts or x2 == diamonds:
    flush = True


#opponent flush

opponentx2 = [opponentx[0:4][1]]
opponenty2 = [opponenty[0:4][1]]
opponentz2 = [opponentz[0:4][1]]

opponentsuits7 = sorted(opponenthand, key = sortingsuit.index)

opponentx3 = opponentsuits7[0:5]
opponenty3 = opponentsuits7[1:6]
opponentz3 = opponentsuits7[2:7]

opponentx2 = [opponentx3[0][1], opponentx3[1][1], opponentx3[2][1], opponentx3[3][1], opponentx3[4][1]]
opponenty2 = [opponenty3[0][1], opponenty3[1][1], opponenty3[2][1], opponenty3[3][1], opponenty3[4][1]]
opponentz2 = [opponentz3[0][1], opponentz3[1][1], opponentz3[2][1], opponentz3[3][1], opponentz3[4][1]]

opponentflush = False

if opponentx2 == clubs or opponentx2 == spades or opponentx2 == hearts or opponentx2 == diamonds:
    opponentflush = True

#four of a kind 
four_of_a_kind = [(2, 2, 2, 2),
                  (3, 3, 3, 3),
                  (4, 4, 4, 4),
                  (5, 5, 5, 5),
                  (6, 6, 6, 6),
                  (7, 7, 7, 7),
                  (8, 8, 8, 8),
                  (9, 9, 9, 9),
                  (10, 10, 10, 10),
                  ("J", "J", "J", "J"),
                  ("Q", "Q", "Q", "Q"),
                  ("K", "K", "K", "K"),
                  ("A", "A", "A", "A"),
]


w = hand[0:4]
k = hand[1:5]
r = hand[2:6]
q = hand[3:7]
w1 = [((w[0][0]), (w[1][0]), (w[2][0]), (w[3][0]))]
k1 = [((k[0][0]), (k[1][0]), (k[2][0]), (k[3][0]))]
r1 = [((r[0][0]), (r[1][0]), (r[2][0]), (r[3][0]))]
q1 = [((q[0][0]), (q[1][0]), (q[2][0]), (q[3][0]))]

fourofakind = False

j = -1
l = 0
while j < 8:
    j += 1
    l = j+1
    if w1 == four_of_a_kind[j:l] or k1 == four_of_a_kind[j:l] or r1 == four_of_a_kind[j:l] or q1 == four_of_a_kind[j:l]:
        fourofakind = True


#opponent four of a kind
        
opponentw = opponenthand[0:4]
opponentk = opponenthand[1:5]
opponentr = opponenthand[2:6]
opponentq = opponenthand[3:7]
opponentw1 = [((opponentw[0][0]), (opponentw[1][0]), (opponentw[2][0]), (opponentw[3][0]))]
opponentk1 = [((opponentk[0][0]), (opponentk[1][0]), (opponentk[2][0]), (opponentk[3][0]))]
opponentr1 = [((opponentr[0][0]), (opponentr[1][0]), (opponentr[2][0]), (opponentr[3][0]))]
opponentq1 = [((opponentq[0][0]), (opponentq[1][0]), (opponentq[2][0]), (opponentq[3][0]))]

opponentfourofakind = False

opponentj = -1
opponentl = 0
while opponentj < 8:
    opponentj += 1
    opponentl = opponentj+1
    if opponentw1 == four_of_a_kind[opponentj:opponentl] or opponentk1 == four_of_a_kind[opponentj:opponentl] or opponentr1 == four_of_a_kind[opponentj:opponentl] or opponentq1 == four_of_a_kind[opponentj:opponentl]:
        opponentfourofakind = True


#Three of a kind
three_of_a_kind = [(2, 2, 2),
                  (3, 3, 3),
                  (4, 4, 4),
                  (5, 5, 5),
                  (6, 6, 6),
                  (7, 7, 7),
                  (8, 8, 8),
                  (9, 9, 9),
                  (10, 10, 10),
                  ("J", "J", "J"),
                  ("Q", "Q", "Q"),
                  ("K", "K", "K"),
                  ("A", "A", "A"),
]


w = hand[0:3]
k = hand[1:4]
r = hand[2:5]
q = hand[3:6]
i = hand[4:7]
w1 = [((w[0][0]), (w[1][0]), (w[2][0]))]
k1 = [((k[0][0]), (k[1][0]), (k[2][0]))]
r1 = [((r[0][0]), (r[1][0]), (r[2][0]))]
q1 = [((q[0][0]), (q[1][0]), (q[2][0]))]
i1 = [((i[0][0]), (i[1][0]), (i[2][0]))]

threeofakind = False

j = -1
l = 0
while j < 8:
    j += 1
    l = j+1
    if w1 == three_of_a_kind[j:l] or k1 == three_of_a_kind[j:l] or r1 == three_of_a_kind[j:l] or q1 == three_of_a_kind[j:l] or i1 == three_of_a_kind[j:l]:
        threeofakind = True

#Opponent three of a kind

opponentw = opponenthand[0:3]
opponentk = opponenthand[1:4]
opponentr = opponenthand[2:5]
opponentq = opponenthand[3:6]
opponenti = opponenthand[4:7]
opponentw1 = [((opponentw[0][0]), (opponentw[1][0]), (opponentw[2][0]))]
opponentk1 = [((opponentk[0][0]), (opponentk[1][0]), (opponentk[2][0]))]
opponentr1 = [((opponentr[0][0]), (opponentr[1][0]), (opponentr[2][0]))]
opponentq1 = [((opponentq[0][0]), (opponentq[1][0]), (opponentq[2][0]))]
opponenti1 = [((opponenti[0][0]), (opponenti[1][0]), (opponenti[2][0]))]

opponentthreeofakind = False

opponentj = -1
opponentl = 0
while opponentj < 8:
    opponentj += 1
    opponentl = opponentj+1
    if opponentw1 == three_of_a_kind[opponentj:opponentl] or opponentk1 == three_of_a_kind[opponentj:opponentl] or opponentr1 == three_of_a_kind[opponentj:opponentl] or opponentq1 == three_of_a_kind[opponentj:opponentl] or opponenti1 == three_of_a_kind[opponentj:opponentl]:
        opponentthreeofakind = True

#pairs
    
pair = [(2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        ("J", "J"),
        ("Q", "Q"),
        ("K", "K"),
        ("A", "A"),
]


w = hand[0:2]
k = hand[1:3]
r = hand[2:4]
q = hand[3:5]
i = hand[4:6]
p = hand[5:7]
w1 = [(w[0][0], w[1][0])]
k1 = [(k[0][0], k[1][0])]
r1 = [(r[0][0], r[1][0])]
q1 = [(q[0][0], q[1][0])]
i1 = [(i[0][0], i[1][0])]
p1 = [(p[0][0], p[1][0])]

j = -1
l = 0

pairs = 0
while j < 8:
    j += 1
    l = j+1
    if w1 == pair[j:l]:
        pairs = pairs + 1
    if k1 == pair[j:l]:
        pairs = pairs + 1
    if r1 == pair[j:l]:
        pairs = pairs + 1
    if q1 == pair[j:l]:
        pairs = pairs + 1
    if i1 == pair[j:l]:
        pairs = pairs + 1
    if p1 == pair[j:l]:
        pairs = pairs + 1
    else:
        pass


#Opponent pair
    
opponentw = opponenthand[0:2]
opponentk = opponenthand[1:3]
opponentr = opponenthand[2:4]
opponentq = opponenthand[3:5]
opponenti = opponenthand[4:6]
opponentp = opponenthand[5:7]
opponentw1 = [(opponentw[0][0], opponentw[1][0])]
opponentk1 = [(opponentk[0][0], opponentk[1][0])]
opponentr1 = [(opponentr[0][0], opponentr[1][0])]
opponentq1 = [(opponentq[0][0], opponentq[1][0])]
opponenti1 = [(opponenti[0][0], opponenti[1][0])]
opponentp1 = [(opponentp[0][0], opponentp[1][0])]

opponentj = -1
opponentl = 0

opponentpairs = 0
while opponentj < 8:
    opponentj += 1
    opponentl = opponentj+1
    if opponentw1 == pair[opponentj:opponentl]:
        opponentpairs = opponentpairs + 1
    if opponentk1 == pair[opponentj:opponentl]:
        opponentpairs = opponentpairs + 1
    if opponentr1 == pair[opponentj:opponentl]:
        opponentpairs = opponentpairs + 1
    if opponentq1 == pair[opponentj:opponentl]:
        opponentpairs = opponentpairs + 1
    if opponenti1 == pair[opponentj:opponentl]:
        opponentpairs = opponentpairs + 1
    if opponentp1 == pair[opponentj:opponentl]:
        opponentpairs = opponentpairs + 1
    else:
        pass

#One pair two pair
if pairs == 1:
    one_pair = True
else:
    one_pair = False

if pairs >= 2:
    two_pair = True
else:
    two_pair = False

#Opponent one pair two pair
    
if opponentpairs == 1:
    opponentone_pair = True
else:
    opponentone_pair = False

if opponentpairs >= 2:
    opponenttwo_pair = True
else:
    opponenttwo_pair = False



#Full house
fullhouse = False
if pairs > 2 and threeofakind == True:
    fullhouse = True
else:
    pass

#opponent full house
opponentfullhouse = False
if opponentpairs > 2 and opponentthreeofakind == True:
    opponentfullhouse = True
else:
    pass

#Straight flush 

straightflush = False

if flush == True and straight == True:
    straightflush = True
else:
    pass

#opponent straight flush

opponentstraightflush = False

if opponentflush == True and opponentstraight == True:
    opponentstraightflush = True
else:
    pass

#High card
highcard = False

if royal_flush == False and straightflush == False and fourofakind == False and fullhouse == False and flush == False and straight == False and threeofakind == False and two_pair == False and one_pair == False:
    highcard = True

#opponent high card

opponenthighcard = False

if opponentroyal_flush == False and opponentstraightflush == False and opponentfourofakind == False and opponentfullhouse == False and opponentflush == False and opponentstraight == False and opponentthreeofakind == False and opponenttwo_pair == False and opponentone_pair == False:
    opponenthighcard = True

#Best hand


RF = 10
SF = 9
FOK = 8
FH = 7
F = 6
S = 5
TOK = 4
TP = 3
OP = 2
HC = 1

if royal_flush == True:
    royal_flush = RF
if straightflush == True:
    straightflush = SF
if fourofakind == True:
    fourofakind = FOK
if fullhouse == True:
    fullhouse = FH
if flush == True:
    flush = F
if straight == True:
    straight = S
if threeofakind == True:
    threeofakind = TOK
if two_pair == True:
    two_pair = TP
if one_pair == True:
    one_pair = OP
if highcard == True:
    highcard = HC



if royal_flush == RF:
    print("You scored a royal flush!\n")
elif straightflush == SF:
    print("You scored a straight flush!\n")
elif fourofakind == FOK:
    print("You scored a four of a kind!\n")
elif fullhouse == FH:
    print("You scored a full house!\n")
elif flush == F:
    print("You scored a flush!\n")
elif straight == S:
    print("You scored a straight!\n")
elif threeofakind == TOK:
    print("You scored a three of a kind!\n")
elif two_pair == TP:
    print("You scored a two pair!\n")
elif one_pair == OP:
    print("You scored a one pair!\n")
elif highcard == HC:
    print("You scored a high card!\n")


#opponent

if opponentroyal_flush == True:
    opponentroyal_flush = RF
if opponentstraightflush == True:
    opponentstraightflush = SF
if opponentfourofakind == True:
    opponentfourofakind = FOK
if opponentfullhouse == True:
    opponentfullhouse = FH
if opponentflush == True:
    opponentflush = F
if opponentstraight == True:
    opponentstraight = S
if opponentthreeofakind == True:
    opponentthreeofakind = TOK
if opponenttwo_pair == True:
    opponenttwo_pair = TP
if opponentone_pair == True:
    opponentone_pair = OP
if opponenthighcard == True:
    opponenthighcard = HC

if opponentroyal_flush == RF:
    print("Your opponent has scored a royal flush.")
elif opponentstraightflush == SF:
    print("Your opponent has scored a straight flush.")
elif opponentfourofakind == FOK:
    print("Your opponent has scored a four of a kind.")
elif opponentfullhouse == FH:
    print("Your opponent has scored a full house.")
elif opponentflush == F:
    print("Your opponent has scored a flush.")
elif opponentstraight == S:
    print("Your opponent has scored a straight.")
elif opponentthreeofakind == TOK:
    print("Your opponent has scored a three of a kind.")
elif opponenttwo_pair == TP:
    print("Your opponent has scored a two pair.")
elif opponentone_pair == OP:
    print("Your opponent has scored a one pair.")
elif opponenthighcard == HC:
    print("Your opponent has scored a high card.")

#playerscore
score = [royal_flush,straightflush,fourofakind,fullhouse,flush,straight,threeofakind,two_pair,one_pair,highcard]


winsort = [10,9,8,7,6,5,4,3,2,1,False]

score = sorted(score, key = winsort.index)

value = score[0]

#opponent score
opponentscore = [opponentroyal_flush,opponentstraightflush,opponentfourofakind,opponentfullhouse,opponentflush,opponentstraight,opponentthreeofakind,opponenttwo_pair,opponentone_pair,opponenthighcard]

opponentscore = sorted(opponentscore, key = winsort.index)

opponentvalue = opponentscore[0]

#print out winner
if value > opponentvalue:
    print("\nYou win!")
    print(f"\nYou have earned ${pot}!")
if value == opponentvalue:
    print("\nYou have the same hand. (Work in progress)")
if value < opponentvalue:
    print("\nYou lose.")
