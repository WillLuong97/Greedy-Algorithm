#649. Dota2 Senate
'''
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right:
A senator can make another senator lose all his rights in this and all the following rounds.

Announce the victory:
If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.
 
Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:

Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights any more since his right has been banned. 
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
 

Example 2:

Input: "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
Note:

The length of the given string will in the range [1, 10,000].
'''
#Algorithm: 
'''
If there is a chance to ban the opponent, do it (greedy). Repeat this process until only R or D left in senate.
To ban someone, we start up 2 counters
ban_d: chances to ban D
ban_r: chances to bna R
You may wonder, what if someone want to ban person before him?
If we travel back, that will cause extra time and mess things up
But don't worries, if opponent is before you, it will get banned next round. e.g.
Round 0: RRDDDD
Round 1: RRXXDD first 2 Ds were banned by first 2 Rs, but last 2 D can still have 2 chances to ban R
Round 2: XXXXDD since we hold 2 chances to ban R, they will be banned at this round, so they won't have chance to ban D again.
banned: A list to check if current person is banned, if True skip this person
s: A set to check if everyone in the senate are same side

'''
#Function to provide the solution to the problem
def predictPartyVictory(senate: str) -> str:
    #base case: 
    if not senate: 
        return []

    #an array to check if the current party in the game is banned or not, 
    #if the person is in the this array, then we will skip the person
    banned = [False] * len(senate)
    #a set to check if every one in the current senate are on the same side
    friendlies = set()  #we will determine the winner by determining which side is the last to main i
    ban_d = 0 #chances to ban D
    ban_r = 0 #chances to ban R
    while len(friendlies) != 1:
        friendlies = set()  #a new set is created after each new round
        #loop through the senate array and check the player
        for index, player in enumerate(senate):
            #check if a player has been banned before or not: 
            if banned[index]: continue
            #if the current player is R, we will check on whether or not it can be banned o
            if player == 'R':
                #can it be banned or not: 
                if ban_r > 0:
                    ban_r -= 1
                    banned[index] = True
                else: 
                    ban_d += 1
                    friendlies.add('R')

            else: 
                #can it be banned or not: 
                if ban_d > 0:
                    ban_d -= 1
                    banned[index] = True

                else: 
                    ban_r += 1  #increase the chance to ban the opposing force
                    friendlies.add('D')

    return "Radiant" if friendlies.pop() == "R" else "Dire"

#Time complexity: O(n) where n is the length of the array
#Space complexity: O(1)





#Main function:
def main():
    print("TESTING Dota 2 Senate....")
    test_input_01 = "RD"
    test_input_02 = "RDD"
    print(predictPartyVictory(test_input_01))
    print(predictPartyVictory(test_input_02))
    print('END OF TESTING...')
main()