# Minesweeper-bot

Bot to play and win minesweeper as often as possible

# How it works? 
I will not share the code because it might be used as cheat in minesweepers communities
Instead, i will share video and explain how it works. 

So, the first what the program does is reading pixels and checking the colors of them, then it saves the data in dictionaries and lists, I used many storing variables for making the processing the data easier. One notification thing is that at the beginning the program marks every single block as bomb, that’s because the block and empty area have the same color, because of it I need to make it different. Luckily a block with flag does have another color, but unfortunately it has the same color as number seven, fortunately this number doesn’t appear often so there is no need to care about it.  
And the flag is useless because I can store the data of where bombs are in the script. 
The other thing that you probably noticed is that there are no numbers but just colors, this is because the numbers have different shape and there would be more programming for making it work with numbers, the side that I made the program for has possibility for changing the displaying output of the grid. 
So, after the program knows what it looks like it can start processing 

At the beginning or when there is no clue of where empty spaces can be the program clicks completely random and it can choose every block except of the blocks it knows is 100% bomb. 
But when it is possible to know where bombs are first it chooses the first prosses of finding bombs which is “if the number is equal to amount of block around, mark all those blocks as bombs” and  then “if number of a block is equally to the number of know bombs around click on blocks that are not bombs” with just these three arguments the script can win around 1 game of 50 and if speed is sets at high level it can get better scores then the best players in the world get
But this is a game of luck, this program will win as often as it is possible and for to do that it needs to have at least one more argument which is: 
