//MOVE THIS INTO .NET AT HOMEs
using System;
using System.Collections.Generic;

class card
{
    private string[] color = {"", ""};
    private string[] number = {"", ""};

    public void addcolor(string[] newcolor, string[] newnumber){
        color = newcolor;
        number = newnumber;
    }
}

class player : card {
    private card[] deck;

    public player() {}

}

class cardvalues{
    public string[,] colors = {{"red", "yellow", "green", "blue", "red", "yellow", "green", "blue", "wild"}, {"purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "wild"}};
    public string[,] numbers = {{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "reverse", "skip"}};
    public string[,] wilds = {{"wild", "+4", "rotate decks"}};
    public int[,] pointsnumbers = {{1,2,3,4,5,6,7,8,9,12,20,25}};
}

class gamelogic {

    List<card> deck = new List<card>();
    int startingcardnumber;
    
    public gamelogic() {
        for (int i = 0; i < cardvalues.colors[0].count; i++) {for (int j = 0; j < 2; j++) {for (int x = j; x < cardvalues.numbers.count; x++) {deck.Add(new card()); string[] newcolors = new string[] {cardvalues.colors[0,i], ""}; string[] newnumbers = string[] {cardvalues.numbers[0, j], ""}; stringdeck[deck.Count - 1].addcolor(newcolors, newcolros)}}}
    }

    
}