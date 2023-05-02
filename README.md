# Minesweeper-bot

Bot to play and win minesweeper

### How it works? 

The first what the program does is read pixels and check their colors, and then it saves the data in dictionaries and lists. I used many storing variables to make processing the data easier. The remarkable thing is that at the beginning, the program marks every single block as a bomb. That’s because the block and empty area have the same color. Because of it I need to make it different. Luckily a block with a flag does have another color, but unfortunately, it has the same color as the number seven, fortunately, this number doesn’t appear often, so there is no need to care about it.  
And the flag is useless because I can store the data of where bombs are in the script. 
The other thing you probably noticed is that there are no numbers but just colors. This is because the numbers have different shapes and there would be more programming for making it work with numbers. The website that I made the program for has the possibility of changing the displaying output of the grid. I changed it to dots. 
So, after the program knows what it looks like, it can start processing. 

At the beginning or when there is no clue of where empty spaces can be, the program clicks completely random, and it can choose every block except the blocks it knows is 100% bomb. 

But when it is possible to know where bombs are first, it chooses the first process of finding bombs which is “if the number is equal to the amount of blocks around, mark all those blocks as bombs” and then “if the number of a block is equal to the number of know bombs around click on blocks that are not bombs” with just these two arguments the script can win around 1 game of 50 and if speed is set at high it can get better scores then the best players in the world get.

But this is a game of luck. This program will win as often as it is possible. To do that, it needs to have at least one more argument, which is hard to figure out and much harder to implement because it ultimately needs to use data from every single block on the grid, it sounds weird, and it is weird, and a very hard problem, which I didn't solve because I began to have headaches while working on it, but one day I will solve it.

The video: https://www.youtube.com/watch?v=IiAZ37mdCd8
