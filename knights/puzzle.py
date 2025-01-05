from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(And(AKnight, AKnave), AKnave),
    Not(And(And(AKnight, AKnave), AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)), 
    Or(And(AKnave, BKnave), AKnave),
    Not(And(And(AKnave, BKnave), AKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)), 
    Or(And(AKnight, BKnight), AKnave),
    Not(And(And(AKnight, BKnight), AKnave)),
    Or(And(AKnave, BKnight), BKnave),
    Not(And(And(AKnave, BKnight), BKnave)),
    Or(AKnave,BKnave),
    Not(And(AKnave, BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),  
    Not(And(AKnight, AKnave)), # A can be Knight or Knave
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)), # B can be Knight or Knave
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)), # C can be Knight or Knave
    Or(AKnight, CKnave),
    Not(And(AKnight, CKnave)), # A is Knight or C is Knave (lying)
    Or(BKnave, CKnave),
    Not(And(BKnave, CKnave)), # C is Knave or B is Knave (lying)
    Or(BKnave, AKnave),
    Not(And(BKnave, AKnave)),
    Or(And(AKnight, AKnave), AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
