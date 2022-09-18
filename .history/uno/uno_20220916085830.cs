//MOVE THIS INTO .NET AT HOMEs
using System;
using System.Collections.Generic;

class card
{
	private string[] color = {"", ""};
	private string[] number = {"", ""};
	public void addcolor(string[] newcolor, string[] newnumber)
	{
		color = newcolor;
		number = newnumber;
	}
}

class player
{
	private List<card> deck;
	public player()
	{
		
	}
}

class cardvalues
{
	public static string[, ] colors = {{"red", "yellow", "green", "blue", "red", "yellow", "green", "blue", "wild"}, {"purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "wild"}};
	public static string[, ] numbers = {{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "reverse", "skip"}};
	public static string[, ] wilds = {{"wild", "+4", "rotate decks"}};
	public static int[, ] pointsnumbers = {{1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 20, 25}};
}

class gamelogic
{
	List<card> deck = new List<card>();
	int startingcardnumber;
	List<player> players;
	
	public gamelogic()
	{
		for (int i = 0; i < cardvalues.colors[0, 0].Length; i++) { for (int j = 0; j < 2; j++) { for (int x = j; x < 12; x++) { deck.Add(new card()); string[] newcolors = new string[]{cardvalues.colors[0, i], ""}; string[] newnumbers = {cardvalues.numbers[0, x], ""}; deck[deck.Count - 1].addcolor(newcolors, newnumbers); } } }
		foreach (player pl in players) {for (int i = 0; i < 10; i++) {Random rnd = new Random(); card addcard = deck[rnd.Next(deck.Count)];}}
	}
}

class main
{
	public static void Main(string[] args)
	{
		gamelogic game = new gamelogic();
		Console.WriteLine("reeee");
	}
}


