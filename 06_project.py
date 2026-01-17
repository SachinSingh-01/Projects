'''Voting System Simulation (Moderate)
What to build
Candidates list
Users vote once
Show final results
Concepts used
Dictionary for candidates and votes
Set to track voters
if-else for duplicate voting
Loop for voting process
Functions for vote and result display'''
dic={}
voter=set()
candidate={
    "Ram": 0,
    "Shyam": 0,
    "Geeta": 0
}
def vote():
    vid=int(input("Enter you ID:"))
    if vid in voter:
        print("You already voted")
    else:
        name=input("Enter name to vote:")
        if name in candidate:
            voter.add(vid)
            candidate[name] += 1
def show_result():
    for name,vote in candidate.items():
        print(name,vote)
while True:
    choose=int(input("Enter your choice (1-3):"))
    match choose:
        case 1: 
            vote()
        case 2:
            show_result() 
        case 3:
            break